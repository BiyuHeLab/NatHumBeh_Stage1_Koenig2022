# import time
import os
import sys
import shutil
import re
import shlex
import subprocess

# import configparser

import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))
logger.setLevel(logging.DEBUG)


def run_command(scommand, capture_output=False):
    logger.debug("About to run:\n{}".format(scommand))
    sargs = shlex.split(scommand)
    if capture_output:
        process_results = subprocess.run(sargs, stdout=subprocess.PIPE)
    else:
        process_results = subprocess.run(sargs)
    if process_results.returncode:
        raise RuntimeError("Received non-zero return code: {}".format(process_results))
    return process_results


workingDir = os.getcwd()
with open(os.path.join(workingDir, "directories.ini"), "r") as directories_file:
    directories = directories_file.read()
PD_dir = re.search('PD_dir="(.*)"', directories).group(1)
# Injest directories.ini
structuarlDir = os.path.abspath(PD_dir)
template = os.path.join(workingDir, "design_template_main.fsf")
toProcess = os.path.join(workingDir, "to_process_main.txt")
RAWFILEROOT = "BIYUJADEHE"
STRUCTURALFILENAME = "final_structural"

# Set path to structural ref
with open(template, "r") as file:
    fsfTemplate = file.read()
fsfTemplate = re.sub(
    r'(set highres_files\(1\) ").*"',
    r"\1" + os.path.join(structuarlDir, STRUCTURALFILENAME) + '"',
    fsfTemplate,
)
with open(template, "w") as file:
    file.write(fsfTemplate)

with open(toProcess, "r") as inputs:
    for inputFilename in inputs:
        # Grab the ID number of current input
        cur_nifii = inputFilename[0:2]
        logger.info("Starting block {}".format(cur_nifii))
        block_dir = os.path.join(workingDir, "run" + cur_nifii)
        os.makedirs(block_dir, exist_ok=True)

        # Create block specific fsf file
        block_design_path = os.path.join(block_dir, "block" + cur_nifii + "_design.fsf")
        shutil.copy(template, block_design_path)
        with open(block_design_path, "r") as file:
            block_design = file.read()
        # Update input file
        input_file_root = os.path.join(workingDir, cur_nifii)
        block_design = re.sub(
            r'(set feat_files\(1\) ").*"', r"\1" + input_file_root + r'"', block_design
        )
        # Update output directory
        block_design = re.sub(
            r'(set fmri\(outputdir\) ").*"',
            r"\1" + os.path.join(block_dir, cur_nifii + "-preprocess.feat") + r'"',
            block_design,
        )
        # Update slice timings file
        block_design = re.sub(
            r'(set fmri\(st_file\) ").*"',
            r"\1" + os.path.join(block_dir, "slicetimes.txt") + r'"',
            block_design,
        )
        # Update volume count
        cresult = run_command(
            "sh getNumVolume.sh " + input_file_root + ".nii.gz", capture_output=True
        )
        num_volume = int(cresult.stdout)
        block_design = re.sub(
            r"(set fmri\(npts\) ).*", r"\g<1>" + str(num_volume), block_design
        )
        # Update TR duration
        cresult = run_command(
            "sh getTRDuration.sh " + input_file_root + ".nii.gz", capture_output=True
        )
        TR_duration = float(cresult.stdout)
        block_design = re.sub(
            r"(set fmri\(tr\) ).*", r"\g<1>{:.6f}".format(TR_duration), block_design
        )
        with open(block_design_path, "w") as file:
            file.write(block_design)

        # Create slice timings file
        scommand = (
            "sh makeSlicetimings.sh"
            + (" ../../RawMRIData/TEMP2A_P6_TC/*" + RAWFILEROOT + ".00" + cur_nifii + ".0*.IMA")
            + (" " + block_dir + "/slicetimes.txt")
            + " {}".format(num_volume)
        )
        results = run_command(scommand)

        # run FEAT
        os.chdir(block_dir)
        scommand = 'feat "' + block_design_path + '"'
        results = run_command(scommand)
        os.chdir(workingDir)

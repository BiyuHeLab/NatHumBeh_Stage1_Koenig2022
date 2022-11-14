"""Run batches of fsl GLM analysis.

Raises:
    RuntimeError: Failing shell commands.

"""
import argparse
import logging
import os
import shlex
import subprocess
import sys

from pandas import read_csv

logger = logging.getLogger(__name__)
streamhdlr = logging.StreamHandler(stream=sys.stdout)
streamhdlr.setLevel(logging.INFO)
logger.addHandler(streamhdlr)
logger.setLevel(logging.DEBUG)


def run_command(scommand, capture_output=False):
    """Run a command with the shell.

    Arguments:
        scommand {str} -- Command to be executed.

    Keyword Arguments:
        capture_output {bool} -- Allow the output from the command to be accessed via the
            .stdout attribute on the returned CompletedProcess. (default: {False})

    Raises:
        RuntimeError: Raised if the command returns a non-zero return code.

    Returns:
        subprocess.CompletedProcess -- Result of subprocess.run.

    """
    logger.info("About to run:\n{}".format(scommand))
    sargs = shlex.split(scommand)
    if capture_output:
        process_results = subprocess.run(sargs, stdout=subprocess.PIPE)
    else:
        process_results = subprocess.run(sargs)
    if process_results.returncode:
        logger.error("Received non-zero return code: {}".format(process_results))
        raise RuntimeError("Received non-zero return code: {}".format(process_results))
    return process_results


def get_FileHandler(log_fname, debug_filelogging=True, overwrite=False):
    """Set up logging to a log file on disk.

    Args:
        log_fname (str): File path at which to create the log file.
        debug_filelogging (bool, optional): If True(default), emit maximal messages to
            log. When False, emits one step down, omitting many large log records mostly
            used for debugging.
        overwrite (bool, optional): Determines whether to overwrite any preexisting log
            file. Default False.

    Returns:
        logging.FileHandler: The set up handler.

    """
    logfile_handler = logging.FileHandler(log_fname, mode="w" if overwrite else "a")
    logfile_handler.setLevel(logging.DEBUG if debug_filelogging else logging.INFO)
    logfile_format = logging.Formatter(
        "%(asctime)s - %(levelname)s@%(name)s: %(message)s"
    )
    logfile_handler.setFormatter(logfile_format)
    return logfile_handler


def fill_in_template(template, params):
    """Fill in template placeholders according to params.

    Arguments:
        template {str} -- Template string.
        params {dict} -- Dict requires a key matching each template string placeholder
            variable name. Corresponding values will be inserted.

    Returns:
        str -- Populated template string.

    """
    return template.format(**params)


def session_GLM(workingDir, inputFolders):
    """Run initial session GLMs using fsl's FEAT.

    Arguments:
        workingDir {str} -- Path to directory containing template fsf files.
        inputFolders {[str]} -- List of paths to the runs to process.
    """
    logger.addHandler(get_FileHandler(os.path.join(workingDir, "GLM.log")))
    with open(os.path.join(workingDir, "GLM1_template.fsf"), "r") as file:
        GLM1Template = file.read()
        logger.debug(f"Read GLM1Template from {file.name}.")

    for runDir in inputFolders:
        # Grab the ID number of current input
        curRun = runDir[-2:]
        logger.info("Starting run {}".format(curRun))
        # Get details on current block
        #curRep = blockReps[blockReps["runNum"] == int(curRun)]

        # Set parameters
        params = {}
        params["input_feat_file"] = os.path.join(runDir, curRun + "-preprocess.feat","denoised_data.nii.gz")
        logger.debug(f'input_feat_file = {params["input_feat_file"]}')
        # Update volume count
        cresult = run_command(
            "sh getNumVolume.sh " + params["input_feat_file"],
            capture_output=True,
        )
        params["numVolumes"] = int(cresult.stdout)
        logger.debug(f'numVolumes = {params["numVolumes"]}')
        # Update TR duration
        #cresult = run_command(
        #    "sh getTRDuration.sh " + params["input_feat_file"] + ".nii.gz",
        #    capture_output=True,
        #)
        #params["TR_duration"] = float(cresult.stdout)
        #logger.debug(f'TR_duration = {params["TR_duration"]}')
        # Set EV paths
        EVPrefix = "EVfiles/GLM1_run" + curRun + "_"
        params["image0WMplusPath"] = os.path.join(workingDir, EVPrefix + "image0_WMplus.txt")
        logger.debug(f'image0WMplusPath = {params["image0WMplusPath"]}')
        params["image0WMminusPath"] = os.path.join(workingDir, EVPrefix + "image0_WMminus.txt")
        logger.debug(f'image0WMminusPath = {params["image0WMminusPath"]}')
        params["image1WMplusPath"] = os.path.join(workingDir, EVPrefix + "image1_WMplus.txt")
        logger.debug(f'image1WMplusPath = {params["image1WMplusPath"]}')
        params["image1WMminusPath"] = os.path.join(workingDir, EVPrefix + "image1_WMminus.txt")
        logger.debug(f'image1WMminusPath = {params["image1WMminusPath"]}')
        params["image2WMplusPath"] = os.path.join(workingDir, EVPrefix + "image2_WMplus.txt")
        logger.debug(f'image2WMplusPath = {params["image2WMplusPath"]}')
        params["image2WMminusPath"] = os.path.join(workingDir, EVPrefix + "image2_WMminus.txt")
        logger.debug(f'image2WMminusPath = {params["image2WMminusPath"]}')
        params["image3WMplusPath"] = os.path.join(workingDir, EVPrefix + "image3_WMplus.txt")
        logger.debug(f'image3WMplusPath = {params["image3WMplusPath"]}')
        params["image3WMminusPath"] = os.path.join(workingDir, EVPrefix + "image3_WMminus.txt")
        logger.debug(f'image3WMminusPath = {params["image3WMminusPath"]}')
        params["image4WMplusPath"] = os.path.join(workingDir, EVPrefix + "image4_WMplus.txt")
        logger.debug(f'image4WMplusPath = {params["image4WMplusPath"]}')
        params["image4WMminusPath"] = os.path.join(workingDir, EVPrefix + "image4_WMminus.txt")
        logger.debug(f'image4WMminusPath = {params["image4WMminusPath"]}')
        params["image5WMplusPath"] = os.path.join(workingDir, EVPrefix + "image5_WMplus.txt")
        logger.debug(f'image5WMplusPath = {params["image5WMplusPath"]}')
        params["image5WMminusPath"] = os.path.join(workingDir, EVPrefix + "image5_WMminus.txt")
        logger.debug(f'image5WMminusPath = {params["image5WMminusPath"]}')
        params["image6WMplusPath"] = os.path.join(workingDir, EVPrefix + "image6_WMplus.txt")
        logger.debug(f'image6WMplusPath = {params["image6WMplusPath"]}')
        params["image6WMminusPath"] = os.path.join(workingDir, EVPrefix + "image6_WMminus.txt")
        logger.debug(f'image6WMminusPath = {params["image6WMminusPath"]}')
        params["image7WMplusPath"] = os.path.join(workingDir, EVPrefix + "image7_WMplus.txt")
        logger.debug(f'image7WMplusPath = {params["image7WMplusPath"]}')
        params["image7WMminusPath"] = os.path.join(workingDir, EVPrefix + "image7_WMminus.txt")
        logger.debug(f'image7WMminusPath = {params["image7WMminusPath"]}')
        params["image8WMplusPath"] = os.path.join(workingDir, EVPrefix + "image8_WMplus.txt")
        logger.debug(f'image8WMplusPath = {params["image8WMplusPath"]}')
        params["image8WMminusPath"] = os.path.join(workingDir, EVPrefix + "image8_WMminus.txt")
        logger.debug(f'image8WMminusPath = {params["image8WMminusPath"]}')
        params["image9WMplusPath"] = os.path.join(workingDir, EVPrefix + "image9_WMplus.txt")
        logger.debug(f'image9WMplusPath = {params["image9WMplusPath"]}')
        params["image9WMminusPath"] = os.path.join(workingDir, EVPrefix + "image9_WMminus.txt")
        logger.debug(f'image9WMminusPath = {params["image9WMminusPath"]}')
        params["norespPath"] = os.path.join(workingDir, EVPrefix + "noresponses.txt")
        logger.debug(f'norespPath = {params["norespPath"]}')
        params["testarraypostcuePath"] = os.path.join(workingDir, EVPrefix + "testarraypostcue.txt")
        logger.debug(f'testarraypostcuePath = {params["testarraypostcuePath"]}')
        params["testarrayretrocuePath"] = os.path.join(workingDir, EVPrefix + "testarrayretrocue.txt")
        logger.debug(f'testarrayretrocuePath = {params["testarrayretrocuePath"]}')
        params["memoryarrayretrocuePath"] = os.path.join(workingDir, EVPrefix + "memoryarrayretrocue.txt")
        logger.debug(f'memoryarrayretrocuePath = {params["memoryarrayretrocuePath"]}')

        # Create block specific fsf file
        blockGLMfsf = fill_in_template(GLM1Template, params)
        blockGLMPath = os.path.join(runDir, "block" + curRun + "_GLM1.fsf")
        with open(blockGLMPath, "w") as file:
            file.write(blockGLMfsf)

        # run FEAT
        curDir = os.getcwd()
        os.chdir(runDir)
        scommand = 'feat "' + blockGLMPath + '"'
        results = run_command(scommand,capture_output=True)
        #logger.debug(f"feat CLI run results: {results}")
        os.chdir(curDir)

def session_GLM_CLI(args):
    workingDir = os.path.abspath(os.path.expanduser(args.workingDir))
    # Use to_process.txt to define input run folders
    toProcess = os.path.join(workingDir, "to_process_main.txt")
    inputFolders = []
    with open(toProcess, "r") as inputs:
        for inputFilename in inputs:
            # Grab the ID number of current input
            cur_nifii = inputFilename[0:2]
            inputFolders += [os.path.join(workingDir, "run" + cur_nifii)]
    session_GLM(workingDir, inputFolders)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    sessionParser = subparsers.add_parser("session")
    sessionParser.set_defaults(func=session_GLM_CLI)
    sessionParser.add_argument(
        "--workingDir",
        default=".",
        help="Working directory containing template fsf files",
    )

    args = parser.parse_args()
    logger.debug(f"Parsed: {args}")
    args.func(args)

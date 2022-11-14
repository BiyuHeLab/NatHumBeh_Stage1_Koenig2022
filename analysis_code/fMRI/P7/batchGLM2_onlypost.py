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
    logger.addHandler(get_FileHandler(os.path.join(workingDir, "GLM2.log")))
    with open(os.path.join(workingDir, "GLM2_template_onlypost.fsf"), "r") as file:
        GLM2Template = file.read()
        logger.debug(f"Read GLM2Template from {file.name}.")

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
        EVPrefix = "EVfiles/GLM2_run" + curRun + "_"
        params["missing05Path"] = os.path.join(workingDir, EVPrefix + "missing05_onlypost.txt")
        logger.debug(f'missing05Path = {params["missing05Path"]}')
        params["missing06Path"] = os.path.join(workingDir, EVPrefix + "missing06_onlypost.txt")
        logger.debug(f'missing06Path = {params["missing06Path"]}')
        params["missing07Path"] = os.path.join(workingDir, EVPrefix + "missing07_onlypost.txt")
        logger.debug(f'missing07Path = {params["missing07Path"]}')
        params["missing08Path"] = os.path.join(workingDir, EVPrefix + "missing08_onlypost.txt")
        logger.debug(f'missing08Path = {params["missing08Path"]}')
        params["missing09Path"] = os.path.join(workingDir, EVPrefix + "missing09_onlypost.txt")
        logger.debug(f'missing09Path = {params["missing09Path"]}')
        params["missing15Path"] = os.path.join(workingDir, EVPrefix + "missing15_onlypost.txt")
        logger.debug(f'missing15Path = {params["missing15Path"]}')
        params["missing16Path"] = os.path.join(workingDir, EVPrefix + "missing16_onlypost.txt")
        logger.debug(f'missing16Path = {params["missing16Path"]}')
        params["missing17Path"] = os.path.join(workingDir, EVPrefix + "missing17_onlypost.txt")
        logger.debug(f'missing17Path = {params["missing17Path"]}')
        params["missing18Path"] = os.path.join(workingDir, EVPrefix + "missing18_onlypost.txt")
        logger.debug(f'missing18Path = {params["missing18Path"]}')
        params["missing19Path"] = os.path.join(workingDir, EVPrefix + "missing19_onlypost.txt")
        logger.debug(f'missing19Path = {params["missing19Path"]}')
        params["missing25Path"] = os.path.join(workingDir, EVPrefix + "missing25_onlypost.txt")
        logger.debug(f'missing25Path = {params["missing25Path"]}')
        params["missing26Path"] = os.path.join(workingDir, EVPrefix + "missing26_onlypost.txt")
        logger.debug(f'missing26Path = {params["missing26Path"]}')
        params["missing27Path"] = os.path.join(workingDir, EVPrefix + "missing27_onlypost.txt")
        logger.debug(f'missing27Path = {params["missing27Path"]}')
        params["missing28Path"] = os.path.join(workingDir, EVPrefix + "missing28_onlypost.txt")
        logger.debug(f'missing28Path = {params["missing28Path"]}')
        params["missing29Path"] = os.path.join(workingDir, EVPrefix + "missing29_onlypost.txt")
        logger.debug(f'missing29Path = {params["missing29Path"]}')
        params["missing35Path"] = os.path.join(workingDir, EVPrefix + "missing35_onlypost.txt")
        logger.debug(f'missing35Path = {params["missing35Path"]}')
        params["missing36Path"] = os.path.join(workingDir, EVPrefix + "missing36_onlypost.txt")
        logger.debug(f'missing36Path = {params["missing36Path"]}')
        params["missing37Path"] = os.path.join(workingDir, EVPrefix + "missing37_onlypost.txt")
        logger.debug(f'missing37Path = {params["missing37Path"]}')
        params["missing38Path"] = os.path.join(workingDir, EVPrefix + "missing38_onlypost.txt")
        logger.debug(f'missing38Path = {params["missing38Path"]}')
        params["missing39Path"] = os.path.join(workingDir, EVPrefix + "missing39_onlypost.txt")
        logger.debug(f'missing39Path = {params["missing39Path"]}')
        params["missing45Path"] = os.path.join(workingDir, EVPrefix + "missing45_onlypost.txt")
        logger.debug(f'missing45Path = {params["missing45Path"]}')
        params["missing46Path"] = os.path.join(workingDir, EVPrefix + "missing46_onlypost.txt")
        logger.debug(f'missing46Path = {params["missing46Path"]}')
        params["missing47Path"] = os.path.join(workingDir, EVPrefix + "missing47_onlypost.txt")
        logger.debug(f'missing47Path = {params["missing47Path"]}')
        params["missing48Path"] = os.path.join(workingDir, EVPrefix + "missing48_onlypost.txt")
        logger.debug(f'missing48Path = {params["missing48Path"]}')
        params["missing49Path"] = os.path.join(workingDir, EVPrefix + "missing49_onlypost.txt")
        logger.debug(f'missing49Path = {params["missing49Path"]}')
        params["testarraypostcuePath"] = os.path.join(workingDir, EVPrefix + "testarraypostcue.txt")
        logger.debug(f'testarraypostcuePath = {params["testarraypostcuePath"]}')
        params["testarrayretrocuePath"] = os.path.join(workingDir, EVPrefix + "testarrayretrocue.txt")
        logger.debug(f'testarrayretrocuePath = {params["testarrayretrocuePath"]}')
        params["memoryarrayretrocuePath"] = os.path.join(workingDir, EVPrefix + "memoryarrayretrocue.txt")
        logger.debug(f'memoryarrayretrocuePath = {params["memoryarrayretrocuePath"]}')

        # Create block specific fsf file
        blockGLMfsf = fill_in_template(GLM2Template, params)
        blockGLMPath = os.path.join(runDir, "block" + curRun + "_GLM2onlypost.fsf")
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

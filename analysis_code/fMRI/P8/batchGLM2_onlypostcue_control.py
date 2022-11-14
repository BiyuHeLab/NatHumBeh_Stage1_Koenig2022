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
    with open(os.path.join(workingDir, "GLM2_template_onlypostcue_control.fsf"), "r") as file:
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
        params["missing05CorrPath"] = os.path.join(workingDir, EVPrefix + "missing05_onlypostcorr.txt")
        logger.debug(f'missing05CorrPath = {params["missing05CorrPath"]}')
        params["missing06CorrPath"] = os.path.join(workingDir, EVPrefix + "missing06_onlypostcorr.txt")
        logger.debug(f'missing06CorrPath = {params["missing06CorrPath"]}')
        params["missing07CorrPath"] = os.path.join(workingDir, EVPrefix + "missing07_onlypostcorr.txt")
        logger.debug(f'missing07CorrPath = {params["missing07CorrPath"]}')
        params["missing08CorrPath"] = os.path.join(workingDir, EVPrefix + "missing08_onlypostcorr.txt")
        logger.debug(f'missing08CorrPath = {params["missing08CorrPath"]}')
        params["missing09CorrPath"] = os.path.join(workingDir, EVPrefix + "missing09_onlypostcorr.txt")
        logger.debug(f'missing09CorrPath = {params["missing09CorrPath"]}')
        params["missing15CorrPath"] = os.path.join(workingDir, EVPrefix + "missing15_onlypostcorr.txt")
        logger.debug(f'missing15CorrPath = {params["missing15CorrPath"]}')
        params["missing16CorrPath"] = os.path.join(workingDir, EVPrefix + "missing16_onlypostcorr.txt")
        logger.debug(f'missing16CorrPath = {params["missing16CorrPath"]}')
        params["missing17CorrPath"] = os.path.join(workingDir, EVPrefix + "missing17_onlypostcorr.txt")
        logger.debug(f'missing17CorrPath = {params["missing17CorrPath"]}')
        params["missing18CorrPath"] = os.path.join(workingDir, EVPrefix + "missing18_onlypostcorr.txt")
        logger.debug(f'missing18CorrPath = {params["missing18CorrPath"]}')
        params["missing19CorrPath"] = os.path.join(workingDir, EVPrefix + "missing19_onlypostcorr.txt")
        logger.debug(f'missing19CorrPath = {params["missing19CorrPath"]}')
        params["missing25CorrPath"] = os.path.join(workingDir, EVPrefix + "missing25_onlypostcorr.txt")
        logger.debug(f'missing25CorrPath = {params["missing25CorrPath"]}')
        params["missing26CorrPath"] = os.path.join(workingDir, EVPrefix + "missing26_onlypostcorr.txt")
        logger.debug(f'missing26CorrPath = {params["missing26CorrPath"]}')
        params["missing27CorrPath"] = os.path.join(workingDir, EVPrefix + "missing27_onlypostcorr.txt")
        logger.debug(f'missing27CorrPath = {params["missing27CorrPath"]}')
        params["missing28CorrPath"] = os.path.join(workingDir, EVPrefix + "missing28_onlypostcorr.txt")
        logger.debug(f'missing28CorrPath = {params["missing28CorrPath"]}')
        params["missing29CorrPath"] = os.path.join(workingDir, EVPrefix + "missing29_onlypostcorr.txt")
        logger.debug(f'missing29CorrPath = {params["missing29CorrPath"]}')
        params["missing35CorrPath"] = os.path.join(workingDir, EVPrefix + "missing35_onlypostcorr.txt")
        logger.debug(f'missing35CorrPath = {params["missing35CorrPath"]}')
        params["missing36CorrPath"] = os.path.join(workingDir, EVPrefix + "missing36_onlypostcorr.txt")
        logger.debug(f'missing36CorrPath = {params["missing36CorrPath"]}')
        params["missing37CorrPath"] = os.path.join(workingDir, EVPrefix + "missing37_onlypostcorr.txt")
        logger.debug(f'missing37CorrPath = {params["missing37CorrPath"]}')
        params["missing38CorrPath"] = os.path.join(workingDir, EVPrefix + "missing38_onlypostcorr.txt")
        logger.debug(f'missing38CorrPath = {params["missing38CorrPath"]}')
        params["missing39CorrPath"] = os.path.join(workingDir, EVPrefix + "missing39_onlypostcorr.txt")
        logger.debug(f'missing39CorrPath = {params["missing39CorrPath"]}')
        params["missing45CorrPath"] = os.path.join(workingDir, EVPrefix + "missing45_onlypostcorr.txt")
        logger.debug(f'missing45CorrPath = {params["missing45CorrPath"]}')
        params["missing46CorrPath"] = os.path.join(workingDir, EVPrefix + "missing46_onlypostcorr.txt")
        logger.debug(f'missing46CorrPath = {params["missing46CorrPath"]}')
        params["missing47CorrPath"] = os.path.join(workingDir, EVPrefix + "missing47_onlypostcorr.txt")
        logger.debug(f'missing47CorrPath = {params["missing47CorrPath"]}')
        params["missing48CorrPath"] = os.path.join(workingDir, EVPrefix + "missing48_onlypostcorr.txt")
        logger.debug(f'missing48CorrPath = {params["missing48CorrPath"]}')
        params["missing49CorrPath"] = os.path.join(workingDir, EVPrefix + "missing49_onlypostcorr.txt")
        logger.debug(f'missing49CorrPath = {params["missing49CorrPath"]}')
        params["testarraypostcuePath"] = os.path.join(workingDir, EVPrefix + "testarraypostcue.txt")
        logger.debug(f'testarraypostcuePath = {params["testarraypostcuePath"]}')
        params["testarrayretrocuePath"] = os.path.join(workingDir, EVPrefix + "testarrayretrocue.txt")
        logger.debug(f'testarrayretrocuePath = {params["testarrayretrocuePath"]}')
        params["memoryarrayretrocuePath"] = os.path.join(workingDir, EVPrefix + "memoryarrayretrocue.txt")
        logger.debug(f'memoryarrayretrocuePath = {params["memoryarrayretrocuePath"]}')
        params["missing05IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing05_onlypostincorr.txt")
        logger.debug(f'missing05IncorrPath = {params["missing05IncorrPath"]}')
        params["missing06IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing06_onlypostincorr.txt")
        logger.debug(f'missing06IncorrPath = {params["missing06IncorrPath"]}')
        params["missing07IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing07_onlypostincorr.txt")
        logger.debug(f'missing07IncorrPath = {params["missing07IncorrPath"]}')
        params["missing08IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing08_onlypostincorr.txt")
        logger.debug(f'missing08IncorrPath = {params["missing08IncorrPath"]}')
        params["missing09IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing09_onlypostincorr.txt")
        logger.debug(f'missing09IncorrPath = {params["missing09IncorrPath"]}')
        params["missing15IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing15_onlypostincorr.txt")
        logger.debug(f'missing15IncorrPath = {params["missing15IncorrPath"]}')
        params["missing16IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing16_onlypostincorr.txt")
        logger.debug(f'missing16IncorrPath = {params["missing16IncorrPath"]}')
        params["missing17IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing17_onlypostincorr.txt")
        logger.debug(f'missing17IncorrPath = {params["missing17IncorrPath"]}')
        params["missing18IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing18_onlypostincorr.txt")
        logger.debug(f'missing18IncorrPath = {params["missing18IncorrPath"]}')
        params["missing19IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing19_onlypostincorr.txt")
        logger.debug(f'missing19IncorrPath = {params["missing19IncorrPath"]}')
        params["missing25IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing25_onlypostincorr.txt")
        logger.debug(f'missing25IncorrPath = {params["missing25IncorrPath"]}')
        params["missing26IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing26_onlypostincorr.txt")
        logger.debug(f'missing26IncorrPath = {params["missing26IncorrPath"]}')
        params["missing27IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing27_onlypostincorr.txt")
        logger.debug(f'missing27IncorrPath = {params["missing27IncorrPath"]}')
        params["missing28IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing28_onlypostincorr.txt")
        logger.debug(f'missing28IncorrPath = {params["missing28IncorrPath"]}')
        params["missing29IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing29_onlypostincorr.txt")
        logger.debug(f'missing29IncorrPath = {params["missing29IncorrPath"]}')
        params["missing35IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing35_onlypostincorr.txt")
        logger.debug(f'missing35IncorrPath = {params["missing35IncorrPath"]}')
        params["missing36IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing36_onlypostincorr.txt")
        logger.debug(f'missing36IncorrPath = {params["missing36IncorrPath"]}')
        params["missing37IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing37_onlypostincorr.txt")
        logger.debug(f'missing37IncorrPath = {params["missing37IncorrPath"]}')
        params["missing38IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing38_onlypostincorr.txt")
        logger.debug(f'missing38IncorrPath = {params["missing38IncorrPath"]}')
        params["missing39IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing39_onlypostincorr.txt")
        logger.debug(f'missing39IncorrPath = {params["missing39IncorrPath"]}')
        params["missing45IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing45_onlypostincorr.txt")
        logger.debug(f'missing45IncorrPath = {params["missing45IncorrPath"]}')
        params["missing46IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing46_onlypostincorr.txt")
        logger.debug(f'missing46IncorrPath = {params["missing46IncorrPath"]}')
        params["missing47IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing47_onlypostincorr.txt")
        logger.debug(f'missing47IncorrPath = {params["missing47IncorrPath"]}')
        params["missing48IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing48_onlypostincorr.txt")
        logger.debug(f'missing48IncorrPath = {params["missing48IncorrPath"]}')
        params["missing49IncorrPath"] = os.path.join(workingDir, EVPrefix + "missing49_onlypostincorr.txt")
        logger.debug(f'missing49IncorrPath = {params["missing49IncorrPath"]}')

        # Create block specific fsf file
        blockGLMfsf = fill_in_template(GLM2Template, params)
        blockGLMPath = os.path.join(runDir, "block" + curRun + "_GLM2onlypost_control.fsf")
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

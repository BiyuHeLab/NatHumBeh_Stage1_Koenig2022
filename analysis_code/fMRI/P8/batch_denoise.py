#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 13:24:54 2022

@author: koenil04
"""

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
    curDir = os.getcwd()
    for runDir in inputFolders:
        # Grab the ID number of current input
        curRun = runDir[-2:]
        logger.info("Starting run {}".format(curRun))
        os.chdir(os.path.join(runDir, curRun + "-preprocess.feat"))
        with open(os.path.join(runDir, curRun + "-preprocess.feat","filtered_func_data.ica","reject_ica.txt"), "r") as file:
                reject_components = file.readlines()
        reject_which = reject_components[-1][1:-2]
        
        # Output denoise file by rejecting noisy components
        cresult = run_command(
            "fsl_regfilt -i filtered_func_data -o denoised_data -d filtered_func_data.ica/melodic_mix -f '" + reject_which + "'",
            capture_output=True,
        )
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

#!/bin/sh
### Extract number of volumes from nifii
# Inputs:
#   $1: Path to source .nii.gz file. Bash wildcard characters ok.
fslinfo $1 | grep -w pixdim4 | awk '{print $2}'

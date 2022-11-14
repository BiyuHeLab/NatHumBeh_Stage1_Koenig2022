#!/bin/sh
### Create slicetimings file from an IMA file
# Inputs:
#   $1: Path to source IMA file. Bash wildcard characters ok. Should end .IMA
#   $2: Path to desired destination file, including filename.
#   $3: Number of slices (dim3 from fslinfo). NOTE: Actual number of slices, do not add one.
numSlices=$(($3 + 1))
strings $1 | grep -B $numSlices AutoInlineImage | head -$numSlices | while read line; do awk {'print $line / 1500 - 0.5'}; done > $2

# This will not actually run, but is a guide for how the correction was done
# Many individual lines will run, but I don't guarantee that the loop and logic
# syntax are correct.
# Also possible some variable handling is not bash syntax correct.
runs=run*/
cd ${run[0]}
for run in runs
do
    cd ../$run
    runNum=${run: -2}
    # Grab the number lines for an example EV
    EVs=*EV.txt
    EVlength=wc -l ${EV[0]}  # This wont work, needs to be run thru awk or something
    fMRIlength=fslinfo ${runNum}-preprocess.feat/filtered_func_data.nii.gz | grep ^dim4
    if $EVlength < $fMRIlength
        mv ${runNum}-preprocess.feat/filtered_func_data.nii.gz ${runNum}-preprocess.feat/filtered_func_data-orig.nii.gz
        fslroi ${runNum}-preprocess.feat/filtered_func_data-orig.nii.gz ${runNum}-preprocess.feat/filtered_func_data.nii.gz 0 $EVlength
    fi
    if $EVlength < $fMRIlength
        for EV in EVs
        do
            mv $EV ${EV}.BAK
            head -n $fMRIlength ${EV}.BAK > $EV
        done
    fi
done

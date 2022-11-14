## align GLM cope betas to subject highres

# Parameters
subjects="P6 P7 P8"
data_dir="~PATH_TO_DATA_DIR"
ROIs="dlpfc evc loci locs mpfc ofc sfc tof vlpfc"

for subj in $subjects; do
    flirt -in ${subj}/T1_brain -ref standard_brain_rois/standard -omat ${subj}/rois/highres2standard.mat
    fnirt --in=${subj}/T1_brain --aff=${subj}/rois/highres2standard.mat --cout=${subj}/rois/highres2standard_warp --ref=standard_brain_rois/standard --config=T1_2_MNI152_2mm
    invwarp -w ${subj}/rois/highres2standard_warp -r ${subj}/T1_brain -o ${subj}/rois/standard2highres_warp
    for roi in $ROIs; do
    echo "processing subject $subj data, roi $roi"
    applywarp -i standard_brain_rois/${roi} -r ${subj}/T1_brain -w ${subj}/rois/standard2highres_warp -o ${subj}/rois/${roi}_nonbinnonthr_1mm
    flirt -in ${subj}/rois/${roi}_nonbinnonthr_1mm -ref ${subj}/T1_brain -out ${subj}/rois/${roi}_nonbinnonthr_2mm -applyisoxfm 2
    fslmaths ${subj}/rois/${roi}_nonbinnonthr_2mm -thr 0.5 -bin ${subj}/rois/${roi}
    gunzip ${subj}/rois/${roi}.nii.gz
    done
done

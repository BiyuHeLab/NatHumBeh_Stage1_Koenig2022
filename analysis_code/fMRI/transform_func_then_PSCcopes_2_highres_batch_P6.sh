## align GLM cope betas to subject highres

# Parameters
subjects="P6"
data_dir="/isilon/LFMI/VMdrive/Lua/Temp2A/Temp2A_fMRI_pilot/proc_data/"
copesLoc="1 2 3 4 5 6 7 8 9 10"
runsLoc="run05 run06 run07 run08 run09"
copesMain1="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
copesMain2="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25"
runsMain="run10 run11 run12 run13 run14 run15 run16 run19 run20 run21 run22 run23 run24 run25 run26"

for subj in $subjects; do
    echo "processing subject $subj data"
    subj_dir=$data_dir/$subj
    cd $subj_dir
    for block in $runsLoc; do
        echo "processing block $block"
        mkdir -p ${block}/GLMloc.feat/reg/
        fslmaths T1_brain highres
        fslmaths T1 highres_head
        epi_reg --epi=${block}/GLMloc.feat/example_func --t1=highres_head --t1brain=highres --out=${block}/GLMloc.feat/reg/example_func2highres
        for cope in $copesLoc; do
            flirt -in ${block}/GLMloc.feat/stats/cope${cope}_PSC -ref highres -init ${block}/GLMloc.feat/reg/example_func2highres.mat -out ${block}/GLMloc.feat/stats/cope${cope}_PSC_2highres -applyisoxfm 2
            gunzip ${block}/GLMloc.feat/stats/cope${cope}_PSC_2highres.nii.gz
        done
        echo "finished converting run $block 2highres"
    done
    for block in $runsMain; do
        echo "processing block $block"
        mkdir -p ${block}/GLM1.feat/reg/
        epi_reg --epi=${block}/GLM1.feat/example_func --t1=highres_head --t1brain=highres --out=${block}/GLM1.feat/reg/example_func2highres
        for cope in $copesMain1; do
            flirt -in ${block}/GLM1.feat/stats/cope${cope}_PSC.nii.gz -ref highres.nii.gz -init ${block}/GLM1.feat/reg/example_func2highres.mat -out ${block}/GLM1.feat/stats/cope${cope}_PSC_2highres.nii.gz -applyisoxfm 2
            gunzip ${block}/GLM1.feat/stats/cope${cope}_PSC_2highres.nii.gz
       done
       for cope in $copesMain2; do
            flirt -in ${block}/GLM2.feat/stats/cope${cope}_PSC.nii.gz -ref highres.nii.gz -init ${block}/GLM1.feat/reg/example_func2highres.mat -out ${block}/GLM2.feat/stats/cope${cope}_PSC_2highres.nii.gz -applyisoxfm 2
            gunzip ${block}/GLM2.feat/stats/cope${cope}_PSC_2highres.nii.gz
        done
        echo "finished converting $block 2highres"
    done
    cd ${data_dir}
done

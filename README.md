# readme file for NatHumBeh_Stage1_Koenig2022

Pre-processing
- In each subject folder, batchFEAT_main.py runs the pre-processing steps for all runs in 'to_process_main.txt'
- make event files for GLMs using makeEVS.R
- after pre-processing, reject noisy ICA components by marking them in 'reject_ICA.txt' in each run folder
- run batch_denoise.py, this takes noisy compoenents from 'reject_ICA.txt' and creates denoised_data.nii for each run

GLMs
- batch_GLM1.py, batch_GLM2_onlypost.py, batch_GLM2_onlypostcue_control.py for each subject.
- Prepare ROIs for each subject: transforms_ROIs.sh
- After GLMs are finished, convert beta estimates to percent signal change with batch_convert_to_pct_signal_change.py for GLM1 and GLM2 and batch_convert_to_pct_signal_change_GLM2_control.py for GLM2_control
- Align percent signal change beta estimates to T1 using transform_func_then_PSCcopes_2_highres_batch_SUBJ.sh for each subject

MVPA
- Run decoding using Temp2A_callMVPA_betas_maintask.m and Temp2A_callMVPA_betas_maintask_GLM2control.m
- Plot results using MakeFigs_accuracy.py

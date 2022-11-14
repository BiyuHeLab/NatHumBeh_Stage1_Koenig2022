#Script to analyze piloting data for Templeton Exp 2A fMRI pilot

setwd("~PATH_TO_DATA_FOLDER")
subs = c("P6","P7","P8")
same="6"
diff="7"
allimages = seq(0,9)

for (sub in 1:length(subs)) {
  #Read in the data with the subject number in its file name
  subject_code = subs[sub]

  if (sub == 1){
    part1 = read.csv("./Main Task/behav_data/P6_TC_templeton_exp2A_fMRI_SD67_2022_Jan_13_1119.csv")[-c(1:3,501),-c(2:27,32:99)]
    part2 = read.csv("./Main Task/behav_data/P6_TC_2_templeton_exp2A_fMRI_SD67_2022_Jan_13_1249.csv")[-c(1:3),-c(2:27,32:99)]
    behavdat = rbind(part1,part2)
    rm(part1,part2)
    part1 = read.table("./Main Task/behav_data/P6_TC_templeton_exp2A_fMRI_SD67_2022_Jan_13_1119.log",sep="\t",fill=T)
    mainTaskStart = which(part1$V3 == "static_instruction_33: autoDraw = True")
    part1 = part1[-(1:mainTaskStart),]
    part2 = read.table("./Main Task/behav_data/P6_TC_2_templeton_exp2A_fMRI_SD67_2022_Jan_13_1249.log",sep="\t",fill=T)
    mainTaskStart = which(part2$V3 == "static_instruction_33: autoDraw = True")
    part2 = part2[-(1:mainTaskStart),]
    logdat = rbind(part1,part2)
    rm(part1,part2)
    maintaskruns = c("10","11","12","13","14","15","16","19","20","21","22","23","24","25","26")
  } else if (sub ==2) {
    behavdat = read.csv(dir('./Main Task/behav_data', full.names=T, pattern=paste0("^",as.character(subject_code)))[1])[-c(1:3),-c(2:27,32:99)]
    logdat = read.table("./Main Task/behav_data/P7_HM_templeton_exp2A_fMRI_SD67_2022_Jan_14_1108.log",sep='\t',fill=T)
    mainTaskStart = which(logdat$V3 == "static_instruction_33: autoDraw = True")
    logdat = logdat[-(1:mainTaskStart),]
    maintaskruns = c("09","10","11","12","13","14","15","16","17","18","19","20","21","22","23")
  } else {
    behavdat = read.csv(dir('./Main Task/behav_data', full.names=T, pattern=paste0("^",as.character(subject_code)))[1])[-c(1:9),-c(2:27,32:99)]
    logdat = read.table("./Main Task/behav_data/P8_SC_templeton_exp2A_fMRI_SD67_2022_Jan_25_1937.log",sep="\t",fill=T)
    mainTaskStart = which(logdat$V3 == "static_instruction_33: autoDraw = True")
    logdat = logdat[-(1:mainTaskStart),]
    maintaskruns = c("11","12","13","14","15","16","17","18","19","20","21","22","23","24","25")
  }
  
  start_times_memoryarray = round(behavdat$array_image_1h.started*10)/10
  start_times_testarray = round(behavdat$array_image_1j.started*10)/10
  memory_retint_duration = rep(0.5,length(start_times_testarray))
  test_response_duration = round(behavdat$sd_resp_real.rt*10)/10
  starts_durations = cbind(start_times_memoryarray,start_times_testarray,memory_retint_duration,test_response_duration)
  colnames(starts_durations) = c("start_memory","start_test","duration_postmemory","duration_posttest")
  
  #Log accuracy for each trial
  behavdat[which((behavdat$change_or_no_real==0)&(behavdat$sd_resp_real.keys==same)),"accuracy"] = 1
  behavdat[which((behavdat$change_or_no_real==1)&(behavdat$sd_resp_real.keys==diff)),"accuracy"] = 1
  behavdat[which((behavdat$change_or_no_real==0)&(behavdat$sd_resp_real.keys==diff)),"accuracy"] = 0
  behavdat[which((behavdat$change_or_no_real==1)&(behavdat$sd_resp_real.keys==same)),"accuracy"] = 0
 
  #Log which image was cued and which images are missing from memory array
  missing_imgs = array(NA,c(nrow(behavdat),2))
  for (i in 1:nrow(behavdat)){
    images_in_memory_array = behavdat[i,14:21]
    if (!is.na(behavdat[i,"cue_location_real"])){
      behavdat[i,"image_cued"] = images_in_memory_array[behavdat[i,"cue_location_real"]+1]
    } else {
      behavdat[i,"image_cued"] = NA
    }
    if (!is.na(images_in_memory_array[1])){
      missing_imgs[i,] = allimages[!allimages %in% images_in_memory_array]
    }
  }
  
  #Log which trials had no response
  behavdat[which(behavdat$sd_resp_real.keys == "None"),"response"] = 0
  behavdat[which(behavdat$sd_resp_real.keys != "None"),"response"] = 1
  
  n_block = 15
  n_trial = 50
  TR_length = 1.5
  
  for (block in 1:n_block){
    blockdat = behavdat[((block-1)*n_trial + 1):((block-1)*n_trial + n_trial),]
    starts_durations_block = as.data.frame(starts_durations[((block-1)*n_trial + 1):((block-1)*n_trial + n_trial),])
    starts_durations_block[,2] = starts_durations_block[,2] - starts_durations_block[1,1] #make all start times relative to the start of the run
    starts_durations_block[,1] = starts_durations_block[,1] - starts_durations_block[1,1] #make all start times relative to the start of the run
    blockdat = blockdat[,c("retro_0_post_1_real","accuracy","image_cued","response")]
    
    ### FOR GLM #1 ###
    # Need two regressors for each image (total of 10), all WM+ trials (retro_0_post_1_real = 1, accuracy = 1, response = 1) and all WM- trials (retro_0_post_1_real = 1, accuracy = 0, response = 1)
    # = Total of 20 regressors
    # + 1 regressor for onset of test array in all post-cue trials with a response
    # + 1 regressor for onset of memory array in no-response trials
    
    #Test-array regressor
    allpostcue = which(blockdat$retro_0_post_1_real == 1)
    reg_test = cbind(starts_durations_block$start_test,starts_durations_block$duration_posttest) 
    reg_test = cbind(reg_test,0)
    reg_test[allpostcue,3] = 1
   # write.table(round(reg_test,2),paste0("./proc_data/",subs[sub],"/EVfiles/GLM1_run",maintaskruns[block],"_testarraypostcue.txt"),col.names = F,row.names = F)
    
    allretrocue = which(blockdat$retro_0_post_1_real == 0)
    reg_test_r = cbind(starts_durations_block$start_test,starts_durations_block$duration_posttest) 
    reg_test_r = cbind(reg_test_r,0)
    reg_test_r[allretrocue,3] = 1
    write.table(round(reg_test_r,2),paste0("./proc_data/",subs[sub],"/EVfiles/GLM1_run",maintaskruns[block],"_testarrayretrocue.txt"),col.names = F,row.names = F)
    
    reg_mem_r = cbind(starts_durations_block$start_memory,starts_durations_block$duration_postmemory)
    reg_mem_r = cbind(reg_mem_r,0)
    reg_mem_r[allretrocue,3] = 1
   # write.table(round(reg_mem_r,2),paste0("./proc_data/",subs[sub],"/EVfiles/GLM1_run",maintaskruns[block],"_memoryarrayretrocue.txt"),col.names = F,row.names = F)
    
    #No-response regressor
    no_resp_trials = which(blockdat$response == 0)
    reg_noresp = cbind(starts_durations_block$start_memory,starts_durations_block$duration_postmemory)
    reg_noresp = cbind(reg_noresp,0)
    reg_noresp[no_resp_trials] = 1
   # write.table(round(reg_noresp,2),paste0("./proc_data/",subs[sub],"/EVfiles/GLM1_run",maintaskruns[block],"_noresponses.txt"),col.names = F,row.names = F)
    
    for (image in 0:9){
      regWMplus = cbind(starts_durations_block$start_memory,starts_durations_block$duration_postmemory) #WM+ trials
      regWMplus = cbind(regWMplus,0)
      regWMminus = cbind(starts_durations_block$start_memory,starts_durations_block$duration_postmemory) #WM- trials
      regWMminus = cbind(regWMminus,0)
      
      WM_plus = which((blockdat$retro_0_post_1_real == 1) & (blockdat$accuracy == 1) & (blockdat$response == 1) & (blockdat$image_cued == image))
      WM_minus = which((blockdat$retro_0_post_1_real == 1) & (blockdat$accuracy == 0) & (blockdat$response == 1) & (blockdat$image_cued == image))
      
      regWMplus[WM_plus,3] = 1
      regWMminus[WM_minus,3] = 1
      
    #  write.table(round(regWMplus,2),paste0("./proc_data/",subs[sub],"/EVfiles/GLM1_run",maintaskruns[block],"_image",image,"_WMplus.txt"),col.names = F,row.names = F)
     # write.table(round(regWMminus,2),paste0("./proc_data/",subs[sub],"/EVfiles/GLM1_run",maintaskruns[block],"_image",image,"_WMminus.txt"),col.names = F,row.names = F)
    }
    
    ### FOR GLM#2 ###
    # Need one regressor for each unique pair of missing images (total of 45 2-element sets from 10 total images)
    # 1 regressor for onset of test array in post-cue trials
    all_sets = expand.grid(c(0,1,2,3,4),c(5,6,7,8,9)) #This describes all the unique pairs of missing images
    missing_imgs_block = missing_imgs[((block-1)*n_trial + 1):((block-1)*n_trial + n_trial),]
    missing_imgs_block = missing_imgs_block[allpostcue,] #only post cue trials
    for (combo in 1:nrow(all_sets)){
      regressor = cbind(starts_durations_block$start_memory,starts_durations_block$duration_postmemory)
      regressor = regressor[allpostcue,]
      indices_combo = which((missing_imgs_block[,1] == all_sets[combo,1]) & (missing_imgs_block[,2] == all_sets[combo,2]))
      regressor = cbind(regressor,0)
      regressor[indices_combo,3] = 1
      write.table(round(regressor,2),paste0("./proc_data/",subs[sub],"/EVfiles/GLM2_run",maintaskruns[block],"_missing",all_sets[combo,1],all_sets[combo,2],"_onlypost.txt"),col.names = F,row.names = F)
    }
    
    #Onset of test array in post-cue trials
    write.table(round(reg_test,2),paste0("./proc_data/",subs[sub],"/EVfiles/GLM2_run",maintaskruns[block],"_testarraypostcue.txt"),col.names = F,row.names = F)
    write.table(round(reg_test_r,2),paste0("./proc_data/",subs[sub],"/EVfiles/GLM2_run",maintaskruns[block],"_testarrayretrocue.txt"),col.names = F,row.names = F)
    write.table(round(reg_mem_r,2),paste0("./proc_data/",subs[sub],"/EVfiles/GLM2_run",maintaskruns[block],"_memoryarrayretrocue.txt"),col.names = F,row.names = F)
  }
}

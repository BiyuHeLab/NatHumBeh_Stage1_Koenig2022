% calls MVPA using The Decoding Toolbox, on GLM outputs from HLTP fMRI task
% make edits to below parameters for a particular decoding analysis
% finally calls HLTP_runDecoding.m, which in turn calls TDT functions

allsubs = {'P6','P7','P8'};
rois = {'sfc','ofc','mpfc','vlpfc','dlpfc','loci','locs','evc','tof'};
data_dir = 'isilon/LFMI/VMdrive/Lua/Temp2A/Temp2A_fMRI_pilot/proc_data/'; % PATH TO MAIN DATA DIRECTORY
%cd(data_dir);
class1imgs = [1:2:20]; % PE numbers to use
class2imgs = {[1:5],[6:10],[11:15],[16:20],[21:25],[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24],[5,10,15,20,25]};
decodingDir = '../toolboxes/decoding_toolbox_v3.991';
addpath(decodingDir)
nImages = 10;
nROIs = length(rois);
    
for sub = 1:length(allsubs)%:length(allsubs)
    %% REQUIRED PARAMETERS
    subdir = [allsubs{sub} '/']; % PATH TO SUBJECT'S DATA DIRECTORY
    resultsdir = [subdir 'mvpa/roi_betas_WMplus_maintaskdata/'];
    betasdir1 = 'GLM1.feat'; % .feat directory to pull COPEs from
    betasdir2 = 'GLM2_onlypost.feat';
    anatROIFolder = [subdir 'rois/'];

    %% INITIALIZE
    clear cfg
    
    for iImage = 0:9 %Run decoding for each ROI and each image separately, then average results across images within each ROI\
        for iROI = 1:nROIs
            ROIname = rois{iROI};
            disp(['Currently on image ', num2str(iImage), ', ROI #', num2str(iROI)]);
        
            cfg = decoding_defaults;
            analdir = [subdir, '/mvpa'];
            ThisResultsDir = fullfile(resultsdir, ['image' num2str(iImage)], ROIname);
            if ~exist(ThisResultsDir,'dir'); mkdir(ThisResultsDir); end
            cfg.analdir = analdir;
            cfg.subdir = subdir;
            cfg.results.dir = ThisResultsDir;
            fid = fopen([allsubs{sub} '/goodblocks_main.txt']);
            goodblocks = textscan(fid, '%s', 'delimiter', '\n');
            cfg.goodblocks = str2num(cell2mat(goodblocks{1}));

            % if decoding on beta images, set the following parameters
            cfg.beta_suffix = '_PSC_2highres.nii'; % suffix of beta images to use
            cfg.results.output = {'balanced_accuracy', 'decision_values', 'predicted_labels', 'confusion_matrix'}; % default is accuracy_minus_chance
            cfg.results.overwrite = 1;
            
            %roi/searchlight parameters
            cfg.analysis = 'ROI'; % wholebrain, ROI, or searchlight

            % searchlight parameters, use only if performing searchlight analysis
            %cfg.searchlight.unit = 'voxels'; % voxels or mm
            %cfg.searchlight.radius = 3; % 3 voxel radius = 6mm
            %cfg.files.mask = [subdir, '/proc_data/anat/divt1pd_brain_2mm_mask.nii'];

            % roi parameters, use only if performing ROI analysis
            % roifiles variable needs to contain paths to each ROI mask
            roifile = [subdir, 'rois/', ROIname '.nii'];
            cfg.files.mask = roifile;
            cfg.results.write = 2; % only write .mat, not .nii
            % scaling, default is none
            cfg.scale.method = 'min0max1'; % scales data such that minimum = 0, maximum = 1
            cfg.scale.estimation = 'separate'; % 

            imgs = {};
            labels = [];
            chunks = [];
            for blk = cfg.goodblocks'
                if blk<10
                    blockdir = [cfg.subdir, 'run0', num2str(blk)];
                else
                    blockdir = [cfg.subdir, 'run', num2str(blk)];
                end
                glmdir1 = [blockdir, '/', betasdir1 , '/stats/'];
                glmdir2 = [blockdir, '/', betasdir2 , '/stats/'];
                class1images = class1imgs(iImage+1);
                class2images = class2imgs{iImage+1};

                % sort inputs
                class1_beta = [glmdir1 'cope' num2str(class1images) cfg.beta_suffix];
                imgs = [imgs; class1_beta];
                chunks = [chunks; blk];
                labels = [labels; 1];

                for cls = 1:length(class2images)
                    class2_beta = [glmdir2 'cope' num2str(class2images(cls)) cfg.beta_suffix];
                    imgs = [imgs; class2_beta];
                    chunks = [chunks; blk];
                    labels = [labels; -1];
                end
            end
            cfg.files.name = imgs;
            cfg.files.label = labels;
            cfg.files.chunk = chunks;

            cfg.design = make_design_cv(cfg);
            cfg.design.unbalanced_data = 'ok';
            cfg.plot_design=0;
            cfg.software = 'SPM12';
            cfg.plot_selected_voxels  = 0; % 0: no plotting, 1: every step, 2: every second step, 100: every hundredth step...
            cfg.plot_design=0;% This is by default set to 1, but if you repeat the same design again and again, it can get annoying...
            [results, cfg, passed_data] = decoding(cfg);
            save([cfg.results.dir, '/passed_data.mat'], 'passed_data'); %change to reflect which image
        end
    end
end

%% Permutation test
for sub=1:length(allsubs)
    for iROI = 1:nROIs
        for iImage = 0:9
            combine=0;
            ROIname = rois{iROI};
            ThisResultsDir = fullfile(allsubs{sub}, 'mvpa', 'roi_betas_WMplus_maintaskdata', ['image' num2str(iImage)], ROIname);
            n_perms = 100;
            cfg_file = [ThisResultsDir, '/res_cfg.mat'];
            output = {'balanced_accuracy','confusion_matrix'};
            Temp2A_run_permutation(ThisResultsDir, output, combine);
        end
    end
end

%% Average decoding accuracies across images within each ROI for each subject
average_balanced_accuracy = zeros(length(allsubs),nImages,nROIs);
for sub=1:length(allsubs)
    for iImage = 0:9 %Run decoding for each ROI and each image separately, then average results across images within each ROI\
        for iROI = 1:nROIs
           balanced_acc = load([allsubs{sub}, '/', 'mvpa/roi_betas_WMplus_maintaskdata/image', num2str(iImage), '/', rois{iROI}, '/res_balanced_accuracy.mat']);
           average_balanced_accuracy(sub,iImage+1,iROI) = balanced_acc.results.balanced_accuracy.output;
        end
    end
end

mean_accuracy_persub_perroi = squeeze(mean(average_balanced_accuracy,2));

%% Assess results of permutation
% Take 5000 balanced accuracies per subject per ROI
nReps = 5000;
nullDistribAll = zeros(5000,nROIs,3);
pvalues = zeros(3,nROIs);
permchance = zeros(3,nROIs);
for sub = 1:3
    for iROI = 1:nROIs
        ROIname = rois{iROI};
        parfor i = 1:nReps
            randselection = randsample(100,10);
            randomsamples = zeros(10,1);
            for iImage = 0:9    
                accuracy = load([allsubs{sub} '/mvpa/roi_betas_WMplus_maintaskdata/image' num2str(iImage) '/' ROIname '/perm/perm' num2str(randselection(iImage+1),'%04.f') '_balanced_accuracy.mat']);
                randomsamples(iImage+1,1) = accuracy.results.balanced_accuracy.output;
            end
            nullDistribAll(i,iROI,sub) = mean([randomsamples]);
        end
        pvalues(sub,iROI) = sum(nullDistribAll(:,iROI,sub) >= mean_accuracy_persub_perroi(sub,iROI)) / nReps;
        permchance(sub,iROI) = median(nullDistribAll(:,iROI,sub));
    end
end

results = struct('mean',{mean_accuracy_persub_perroi},'pvalues',{pvalues},'permchance',{permchance});
save('results_mvpa/balacc_beta_main_all9.mat','results');

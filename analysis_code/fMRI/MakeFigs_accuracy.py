#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 13 14:58:57 2022

@author: koenil04
"""
from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from matplotlib.lines import Line2D
from matplotlib.colors import ListedColormap
import os
from statsmodels.stats import multitest

os.chdir('/isilon/LFMI/VMdrive/Lua/Temp2A/Temp2A_fMRI_pilot/proc_data/results_mvpa/SubsP6-8_SmallVisAngle')

def plot_bar(betas, pvalues, permchance, sub, title, savename):
    fig_width = 7  # width in inches
    fig_height = 4.2  # height in inches
    fig_size =  [fig_width,fig_height]
    params = {    
              'axes.spines.right': False,
              'axes.spines.top': False,
              
              'figure.figsize': fig_size,
              
              'ytick.major.size' : 8,      # major tick size in points
              'xtick.major.size' : 8,    # major tick size in points
                  
              'lines.markersize': 6.0,
              # font size
              'axes.labelsize': 18,
              'axes.titlesize': 18,     
              'xtick.labelsize': 15,
              'ytick.labelsize': 15,
              'font.size': 15,
    
              # linewidth
              'axes.linewidth' : 1.3,
              'patch.linewidth': 1.3,
              
              'ytick.major.width': 1.3,
              'xtick.major.width': 1.3,
              'savefig.dpi' : 800
              }
    rcParams.update(params)
    rcParams['font.sans-serif'] = 'Helvetica'
    
    colors = [np.array([118, 106, 218]) / 255.,#([255, 221, 140]) / 255., 
              np.array([122, 184, 99]) / 255.,#([164, 210, 255]) / 255.,  
              np.array([255, 99, 71]) / 255.,
              np.array([186, 85, 211]) / 255.]
    
    roi_names = np.array(['sfc','ofc','mpfc','vlpfc','dlpfc','loci','locs','evc','tof'])
    n_roi = len(roi_names)
    xa = 1+np.arange(n_roi)
    y = betas[sub]
    ps = pvalues[sub,:]
    classes = ['p > 0.05','p < 0.05','p < 0.01','p < 0.001']
    colorlist = ListedColormap(colors)
    
    markers = np.array(["o"]*n_roi)
    cols = np.array([0]*n_roi)
    labels = np.array([classes[0]]*n_roi)
    for m in range(len(ps)):
        if (ps[m] < 0.05) & (ps[m] >= 0.01):
            markers[m] = '*'
            cols[m] = 1
            labels[m] = classes[1]
        elif (ps[m] < 0.01) & (ps[m] >= 0.001):
            markers[m] = 'P'
            cols[m] = 2
            labels[m] = classes[2]
        elif ps[m] < 0.001:
            markers[m] = 'd'
            cols[m] = 3
            labels[m] = classes[3]
            
    allcols = np.zeros((len(ps),3))
    for i in range(len(allcols)):
        allcols[i,:] = colors[cols[i]]
        
    #FDR test
    sig_after_fdr_frontal = multitest.fdrcorrection(ps[:5])[0]
    sig_after_fdr_visual = multitest.fdrcorrection(ps[5:])[0]
    sig_after_fdr = np.concatenate((sig_after_fdr_frontal,sig_after_fdr_visual))
    
    fig, ax = plt.subplots(1, 1, figsize = (5, 3.5))
    
    fakescatter = plt.scatter(xa,y,c=[0,1,2,3,0,0,0,0,0],cmap=colorlist,s=1)
    plt.scatter(xa, y, c=allcols, linewidth = 0.1,marker = 'o',edgecolors = 'None')
    plt.plot(xa[sig_after_fdr], y[sig_after_fdr]+0.2,'^', mfc = 'none', color=colors[0], ms = 10, mew = 1, zorder = 2)
    
    plt.xlim([0, n_roi+2]); #plt.ylim([-2., 2.]);
    plt.ylim([45,67])
    for n in range(1, n_roi+1):
        ax.axvline(n, -1, n_roi, ls = ':', color = 'k', alpha = .5, zorder = 0)
    ax.spines['left'].set_position(('outward', 10))
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_visible( False)
    plt.hlines(50, 1, n_roi, ls = '--')
    for k in range(len(permchance[sub,:])):
        plt.hlines(permchance[sub,k], k+1-0.3, k+1+0.3, ls = '-', color='orange')
    
    ax.tick_params(bottom = False)
    plt.xticks(1+np.arange(n_roi), roi_names, rotation = 'vertical')
    plt.ylabel('balanced accuracy')
    
    for i, tic in enumerate(plt.gca().get_xticklabels()):
        if i > 9: tic.set_color(np.array([204., 102., 0.])/255) 
        else: tic.set_color(np.array([0., 26., 204.])/255) 
    #plt.suptitle('subject ' + str(sub+1) + '\n' + title)
    handles = fakescatter.legend_elements()[0]  
    labels = labels
    line = Line2D([0], [0], color='orange', ls='-')
    handles.extend([line])
    #labels.extend(['perm. chance'])
    #plt.legend(handles=handles, labels=classes, loc='center left', bbox_to_anchor=(0.85, 0.5))
    plt.tight_layout()
    plt.show()
    fig.savefig(savename + '_sub' + str(sub+1) + '_notitles.png',dpi=800, transparent=True)


inputFiles = ['balacc_beta_main_all9.mat','balacc_beta_main_GLM2control.mat','balacc_beta_loc_all9.mat']
titles = ['main task cross-validation (betas)','main task cross-validation (betas)\nmissing imgs from post-cue correct','localizer cross-validation (betas)']
outNames = ['balacc_beta_main_all9ROIs','balacc_beta_main_GLM2control','balacc_beta_loc_all9']
nSubs = 3

for sub in range(nSubs):
    for i, inputFile in enumerate(inputFiles):
        print(i)
        print(inputFile)
        if inputFile == 'balacc_beta_loc_all13.mat':
            results = loadmat(inputFile)['newresults']
            betas = results[0,0][0][:,[0,1,2,3,4,11,12,10,9]]
            pvalues = results[0,0][1][:,[0,1,2,3,4,11,12,10,9]]
            permchance = results[0,0][2][:,[0,1,2,3,4,11,12,10,9]]
        else: 
            results = loadmat(inputFile)['results']
            betas = results[0,0][0]
            pvalues = results[0,0][1]
            permchance = results[0,0][2]
        
        plot_bar(betas, pvalues, permchance, sub, titles[i], outNames[i])
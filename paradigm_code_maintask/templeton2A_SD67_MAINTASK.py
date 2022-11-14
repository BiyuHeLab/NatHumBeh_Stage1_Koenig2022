#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on December 13, 2021, at 14:23
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'templeton_exp2A_fMRI_SD67'  # from the Builder filename that created this script
expInfo = {'participant': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\koenil04\\OneDrive - NYU Langone Health\\Temp2A_fMRI_pilot_V4\\templeton2A_SD67_MAINTASK.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
welcome = visual.TextStim(win=win, name='welcome',
    text='Welcome to the experiment!\n\n\nPress any key to continue.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
intro_continue = keyboard.Keyboard()

# Initialize components for Routine "instruction_1"
instruction_1Clock = core.Clock()
static_instruction = visual.TextStim(win=win, name='static_instruction',
    text='As a reminder: on each trial of the experiment you will see two groups of pictures, first one group and then the other a while later. \n\nYour task will involve reporting whether the pictures shown in the first group are the same as the pictures shown in the second group.',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
static_key1 = keyboard.Keyboard()
static_instruction_2 = visual.TextStim(win=win, name='static_instruction_2',
    text='Press any key to continue and  see an example of how these groups of pictures look.',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instruction_2"
instruction_2Clock = core.Clock()
static_instruction_3 = visual.TextStim(win=win, name='static_instruction_3',
    text='The pictures you’ll see will always be arranged in a circle like this. But the specific pictures shown may differ; this is only an example.',
    font='Arial',
    units='norm', pos=(0, 0.75), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
static_key1_2 = keyboard.Keyboard()
static_instruction_4 = visual.TextStim(win=win, name='static_instruction_4',
    text='Please press any key for more instructions.',
    font='Arial',
    units='norm', pos=(0, -0.75), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
array_image_1 = visual.ImageStim(
    win=win,
    name='array_image_1', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
array_image_2 = visual.ImageStim(
    win=win,
    name='array_image_2', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
array_image_3 = visual.ImageStim(
    win=win,
    name='array_image_3', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
array_image_4 = visual.ImageStim(
    win=win,
    name='array_image_4', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
array_image_5 = visual.ImageStim(
    win=win,
    name='array_image_5', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-8.0)
array_image_6 = visual.ImageStim(
    win=win,
    name='array_image_6', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-9.0)
array_image_7 = visual.ImageStim(
    win=win,
    name='array_image_7', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-10.0)
array_image_8 = visual.ImageStim(
    win=win,
    name='array_image_8', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-11.0)
polygon_17 = visual.Polygon(
    win=win, name='polygon_17',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)

# Initialize components for Routine "instruction_3"
instruction_3Clock = core.Clock()
static_instruction_15 = visual.TextStim(win=win, name='static_instruction_15',
    text='During each trial the first group of pictures will be shown only briefly, like the flash you just saw. After that no pictures will be on the screen for a while.',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
static_key1_6 = keyboard.Keyboard()
static_instruction_16 = visual.TextStim(win=win, name='static_instruction_16',
    text='Please press any key for more instructions.',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
array_image_1b = visual.ImageStim(
    win=win,
    name='array_image_1b', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
array_image_2b = visual.ImageStim(
    win=win,
    name='array_image_2b', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
array_image_3b = visual.ImageStim(
    win=win,
    name='array_image_3b', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
array_image_4b = visual.ImageStim(
    win=win,
    name='array_image_4b', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
array_image_5b = visual.ImageStim(
    win=win,
    name='array_image_5b', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-8.0)
array_image_6b = visual.ImageStim(
    win=win,
    name='array_image_6b', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-9.0)
array_image_7b = visual.ImageStim(
    win=win,
    name='array_image_7b', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-10.0)
array_image_8b = visual.ImageStim(
    win=win,
    name='array_image_8b', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-11.0)
polygon_18 = visual.Polygon(
    win=win, name='polygon_18',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)

# Initialize components for Routine "instruction_4"
instruction_4Clock = core.Clock()
static_instruction_17 = visual.TextStim(win=win, name='static_instruction_17',
    text='After that pause you will see the second group of pictures. This second group will stay on the screen for as long as you want, as shown here.',
    font='Arial',
    units='norm', pos=(0, 0.75), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
static_key1_7 = keyboard.Keyboard()
static_instruction_18 = visual.TextStim(win=win, name='static_instruction_18',
    text='Please press any key for more instructions.',
    font='Arial',
    units='norm', pos=(0, -0.75), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
array_image_1c = visual.ImageStim(
    win=win,
    name='array_image_1c', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
array_image_2c = visual.ImageStim(
    win=win,
    name='array_image_2c', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
array_image_3c = visual.ImageStim(
    win=win,
    name='array_image_3c', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
array_image_4c = visual.ImageStim(
    win=win,
    name='array_image_4c', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
array_image_5c = visual.ImageStim(
    win=win,
    name='array_image_5c', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-8.0)
array_image_6c = visual.ImageStim(
    win=win,
    name='array_image_6c', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-9.0)
array_image_7c = visual.ImageStim(
    win=win,
    name='array_image_7c', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-10.0)
array_image_8c = visual.ImageStim(
    win=win,
    name='array_image_8c', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-11.0)
polygon_19 = visual.Polygon(
    win=win, name='polygon_19',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)

# Initialize components for Routine "instructions_4to5"
instructions_4to5Clock = core.Clock()
static_instruction_25 = visual.TextStim(win=win, name='static_instruction_25',
    text='Your task will always be the same:\n\nTo indicate whether, at one particular spot along the circle of pictures, the same picture was shown both times.\n\nIn other words, you will indicate whether the two groups of pictures both had the same picture in one particular location.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
static_key1_11 = keyboard.Keyboard()
static_instruction_26 = visual.TextStim(win=win, name='static_instruction_26',
    text='Please press any key for more instructions.',
    font='Arial',
    units='norm', pos=(0, -0.75), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instruction_5"
instruction_5Clock = core.Clock()
static_instruction_19 = visual.TextStim(win=win, name='static_instruction_19',
    text='To let you know which spot along the circle you should be reporting about, there will be a red dotted line pointing to one of the eight spots, as shown here.\n\nSo in this example your task would be to identify whether the image to the right and slightly up stayed the same between the two groups of pictures or not, because the red dotted line is pointing to the right and slightly upward.',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
static_key1_8 = keyboard.Keyboard()
static_instruction_20 = visual.TextStim(win=win, name='static_instruction_20',
    text='Please press any key for more instructions.',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
polygon_20 = visual.Polygon(
    win=win, name='polygon_20',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
pointer_dot_0 = visual.Polygon(
    win=win, name='pointer_dot_0',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
pointer_dot_1 = visual.Polygon(
    win=win, name='pointer_dot_1',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
pointer_dot_2 = visual.Polygon(
    win=win, name='pointer_dot_2',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)

# Initialize components for Routine "instruction_6"
instruction_6Clock = core.Clock()
static_instruction_27 = visual.TextStim(win=win, name='static_instruction_27',
    text='You will find that different trials will differ in details: the duration of the pause between the first and second group of pictures may vary, and the moment at which you see the red dotted line may vary, too.\n\nBut your task will always be the same: did the two groups of pictures both have the same picture at the location indicated by red dotted line, or not?',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
static_key1_12 = keyboard.Keyboard()
static_instruction_28 = visual.TextStim(win=win, name='static_instruction_28',
    text='Please press any key to see more instructions.',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
polygon_24 = visual.Polygon(
    win=win, name='polygon_24',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "instruction_67"
instruction_67Clock = core.Clock()
static_instruction_37 = visual.TextStim(win=win, name='static_instruction_37',
    text='To indicate your response you’ll use your right hand; press the left button with your index finger if the two groups of pictures both had the same picture at the location indicated by the red dotted line, or press the right button with your middle finger if two different pictures were shown at that location. See the image below:',
    font='Arial',
    units='norm', pos=(0, 0.8), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
static_key1_17 = keyboard.Keyboard()
static_instruction_38 = visual.TextStim(win=win, name='static_instruction_38',
    text='You will not be explicitly prompted when to give your response: you can simply press one of the two response keys as soon as you’ve seen both groups of pictures as well as the red dotted line indicating the location.\n\nPlease press any key to see more instructions.',
    font='Arial',
    units='norm', pos=(0, -0.7), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
SD_image = visual.ImageStim(
    win=win,
    name='SD_image', 
    image='RH_buttonbox_V1.jpg', mask=None,
    ori=0, pos=(0, 0), size=(0.4, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instruction_67b"
instruction_67bClock = core.Clock()
static_instruction_39 = visual.TextStim(win=win, name='static_instruction_39',
    text='You will find that some trials are easy, yet that on other trials you have no idea and have to guess. That’s okay: immediately after each Same/Different response you get a chance to indicate how sure you were of that response.',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
static_key1_18 = keyboard.Keyboard()
static_instruction_40 = visual.TextStim(win=win, name='static_instruction_40',
    text='Please press any key to see more instructions.',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
polygon_37 = visual.Polygon(
    win=win, name='polygon_37',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "instruction_7"
instruction_7Clock = core.Clock()
static_instruction_31 = visual.TextStim(win=win, name='static_instruction_31',
    text='We will start with a few practice trials so that you can see for yourself.\n\nBefore starting the practice trials: here’s one final instruction. During the trials you will see a black dot at the screen center, just like the one you see there now. It is important to keep your eyes directed at that black dot during the trials. So no looking around while a trial is ongoing.',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
static_key1_14 = keyboard.Keyboard()
static_instruction_32 = visual.TextStim(win=win, name='static_instruction_32',
    text='Please press any key to begin the practice trials.',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
polygon_29 = visual.Polygon(
    win=win, name='polygon_29',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "load_practice_trials"
load_practice_trialsClock = core.Clock()
practice_trial_load_number=0
practice_trial_image_list = []
retro_0_post_1_practice = []
mem_display_to_cue_times_practice = []
change_0_1_practice = []

# Initialize components for Routine "get_ready_practice"
get_ready_practiceClock = core.Clock()
static_instruction_29 = visual.TextStim(win=win, name='static_instruction_29',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
static_key1_13 = keyboard.Keyboard()
static_instruction_30 = visual.TextStim(win=win, name='static_instruction_30',
    text='Please press any key to start.',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
polygon_25 = visual.Polygon(
    win=win, name='polygon_25',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "blank_at_trial_start"
blank_at_trial_startClock = core.Clock()
polygon_39 = visual.Polygon(
    win=win, name='polygon_39',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "practice_mem_display"
practice_mem_displayClock = core.Clock()
array_image_1d = visual.ImageStim(
    win=win,
    name='array_image_1d', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
array_image_2d = visual.ImageStim(
    win=win,
    name='array_image_2d', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
array_image_3d = visual.ImageStim(
    win=win,
    name='array_image_3d', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
array_image_4d = visual.ImageStim(
    win=win,
    name='array_image_4d', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
array_image_5d = visual.ImageStim(
    win=win,
    name='array_image_5d', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
array_image_6d = visual.ImageStim(
    win=win,
    name='array_image_6d', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
array_image_7d = visual.ImageStim(
    win=win,
    name='array_image_7d', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
array_image_8d = visual.ImageStim(
    win=win,
    name='array_image_8d', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-8.0)
polygon_26 = visual.Polygon(
    win=win, name='polygon_26',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)

# Initialize components for Routine "retention_cue_and_test_intval_practice_2"
retention_cue_and_test_intval_practice_2Clock = core.Clock()
polygon_28 = visual.Polygon(
    win=win, name='polygon_28',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
array_image_1f = visual.ImageStim(
    win=win,
    name='array_image_1f', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
array_image_2f = visual.ImageStim(
    win=win,
    name='array_image_2f', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
array_image_3f = visual.ImageStim(
    win=win,
    name='array_image_3f', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
array_image_4f = visual.ImageStim(
    win=win,
    name='array_image_4f', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
array_image_5f = visual.ImageStim(
    win=win,
    name='array_image_5f', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
array_image_6f = visual.ImageStim(
    win=win,
    name='array_image_6f', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
array_image_7f = visual.ImageStim(
    win=win,
    name='array_image_7f', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-8.0)
array_image_8f = visual.ImageStim(
    win=win,
    name='array_image_8f', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-9.0)
pointer_dot_0b = visual.Polygon(
    win=win, name='pointer_dot_0b',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
pointer_dot_1b = visual.Polygon(
    win=win, name='pointer_dot_1b',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
pointer_dot_2b = visual.Polygon(
    win=win, name='pointer_dot_2b',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
sd_practice_resp = keyboard.Keyboard()

# Initialize components for Routine "confidence_rating_practice"
confidence_rating_practiceClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='default text',
    font='Arial',
    units='norm', pos=(0, .65), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
conf_practice_resp = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='LH_buttonbox.JPG', mask=None,
    ori=0, pos=(0, -0.1), size=(0.35, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instruction_8"
instruction_8Clock = core.Clock()
static_instruction_33 = visual.TextStim(win=win, name='static_instruction_33',
    text='default text',
    font='Arial',
    units='norm', pos=(0, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
subj_ready = keyboard.Keyboard()
static_instruction_34 = visual.TextStim(win=win, name='static_instruction_34',
    text='default text',
    font='Arial',
    units='norm', pos=(0, -0.5), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
polygon_31 = visual.Polygon(
    win=win, name='polygon_31',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
experimenter_ready = keyboard.Keyboard()
sub_ready = visual.TextStim(win=win, name='sub_ready',
    text='Standy by...',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "load_real_trials"
load_real_trialsClock = core.Clock()
trial_load_number=0
real_trial_image_list = []
retro_0_post_1_real = []
change_0_1_real = []
cued_locations_real = []
retint_s = []
#-------

# Initialize components for Routine "TR_sync"
TR_syncClock = core.Clock()
wait_for_TR = keyboard.Keyboard()
polygon_2 = visual.Polygon(
    win=win, name='polygon_2',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "real_mem_display"
real_mem_displayClock = core.Clock()
array_image_1h = visual.ImageStim(
    win=win,
    name='array_image_1h', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
array_image_2h = visual.ImageStim(
    win=win,
    name='array_image_2h', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
array_image_3h = visual.ImageStim(
    win=win,
    name='array_image_3h', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
array_image_4h = visual.ImageStim(
    win=win,
    name='array_image_4h', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
array_image_5h = visual.ImageStim(
    win=win,
    name='array_image_5h', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
array_image_6h = visual.ImageStim(
    win=win,
    name='array_image_6h', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
array_image_7h = visual.ImageStim(
    win=win,
    name='array_image_7h', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
array_image_8h = visual.ImageStim(
    win=win,
    name='array_image_8h', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-8.0)
polygon_33 = visual.Polygon(
    win=win, name='polygon_33',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)

# Initialize components for Routine "retention_cue_and_test_intval_real"
retention_cue_and_test_intval_realClock = core.Clock()
polygon_34 = visual.Polygon(
    win=win, name='polygon_34',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
expClock = core.Clock()
array_image_1j = visual.ImageStim(
    win=win,
    name='array_image_1j', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
array_image_2j = visual.ImageStim(
    win=win,
    name='array_image_2j', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
array_image_3j = visual.ImageStim(
    win=win,
    name='array_image_3j', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)
array_image_4j = visual.ImageStim(
    win=win,
    name='array_image_4j', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)
array_image_5j = visual.ImageStim(
    win=win,
    name='array_image_5j', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-6.0)
array_image_6j = visual.ImageStim(
    win=win,
    name='array_image_6j', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-7.0)
array_image_7j = visual.ImageStim(
    win=win,
    name='array_image_7j', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-8.0)
array_image_8j = visual.ImageStim(
    win=win,
    name='array_image_8j', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-9.0)
pointer_dot_0c = visual.Polygon(
    win=win, name='pointer_dot_0c',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
pointer_dot_1c = visual.Polygon(
    win=win, name='pointer_dot_1c',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
pointer_dot_2c = visual.Polygon(
    win=win, name='pointer_dot_2c',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
sd_resp_real = keyboard.Keyboard()

# Initialize components for Routine "confidence_rating_real_2"
confidence_rating_real_2Clock = core.Clock()
conf_real_resp = keyboard.Keyboard()

# Initialize components for Routine "fixation_minimum"
fixation_minimumClock = core.Clock()
polygon = visual.Polygon(
    win=win, name='polygon',units='pix', 
    edges=20, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "break_between_runs"
break_between_runsClock = core.Clock()
break_text='doh!' #if this comes up we forgot to update the msg!
break_text_presentation = visual.TextStim(win=win, name='break_text_presentation',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
resp_subj_ready = keyboard.Keyboard()
resp_experimenter_ready = keyboard.Keyboard()
subject_ready_text = visual.TextStim(win=win, name='subject_ready_text',
    text='Stand by...',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
finish = visual.TextStim(win=win, name='finish',
    text='You’re done with the task!\n\nThank you for your participation.',
    font='Arial',
    units='norm', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intro"-------
continueRoutine = True
# update component parameters for each repeat
from numpy.random import random, shuffle
from numpy import tan, mod

timer  = core.Clock()
x_scale = 50
y_scale = 50
dist_cm = 60

trials_per_block = 50
num_real_blocks = 15
num_real_trials = trials_per_block*num_real_blocks
real_trial_index = 0

blank_trial_start_dur_s=0.8
mem_display_duration_s=0.5
mem_display_to_cue_time_s=2.0           #NB. test display can precede cue.

cue_duration_s=0.5
retention_duration_s=0.8                #blank period following cue in retro-cue trials, before test display appears

#----training related-----
max_num_training_trials=300
consecutive_retro_correct_required=8  #we're starting at the shortest delay (i.e. mem_display_to_cue_times_s[0]) and then we do some more training at a longer one (mem_display_to_cue_times_s[1])
repeat_intructions_every=15
mem_display_to_cue_times_training_s=[0.75,2.6]
short_block_done = 0
trials_long_perblock = 50
#-------------------------

num_images_per_display=8
image_index_list_for_shuffling=list(range(0,num_images_per_display))

num_images_available=10
num_practice_trials=0

rand_val_for_image_selection=int(round(random()*19.))

permutation_data_file_string_practice='limited_permutations.xlsx'

image_side_dva=2.0
image_eccentr_dva=4.5

outline_side_relative_to_image_eccentricity=2.5
pointer_length_relative_to_image_eccentricity=.25

x_y_gains_per_angle=[[0.3826834323650898, 0.9238795325112867], [0.9238795325112867, 0.38268343236508984],
                    [0.9238795325112867, -0.3826834323650897], [0.38268343236508984, -0.9238795325112867],
                    [-0.3826834323650892, -0.923879532511287], [-0.9238795325112868, -0.3826834323650895], 
                    [-0.9238795325112866, 0.38268343236509], [-0.38268343236508956, 0.9238795325112868]]

dot_diam_dva=.2

max_height_accepted_cm=203.5
min_height_accepted_cm=141.5

height_offset_desktop_cm=37.42             #for curve of natural distance vs. height
height_slope_desktop_cm_per_cm=0.1349

height_offset_laptop_cm=-18.48
height_slope_laptop_cm_per_cm=0.4119

blindspot_entry_offset_cm=11.42             #for curve of natural distance vs. blind spot entry point
blind_spot_entry_slope_cm_per_cm=3.569

max_distance_accepted_laptop_cm=81.0        #min and max based on what was not excluded as outlier in earlier data
min_distance_accepted_laptop_cm=22.0

max_distance_accepted_desktop_cm=90.0
min_distance_accepted_desktop_cm=29.0

showDevice=1;
showHeight=1;

all_pic_names = ['bow.png','clown.png','car.png','book.png','bed.png','moon.png','strawberry.png','lemon.png','sun.png','flag.png']
all_pic_names_training=['accordion.png','celery.png','anchor.png','football_helmet.png',
'arm.png','ax.png','bike.png','corn.png','cat.png','chair.png']

TR_length = 1.5
max_response_time = 5*TR_length
min_iti = 0.5
max_duration_sd = max_response_time - min_iti

scannerTRbutton = 'equal'
responseButtons = ['0','1''2','3','4','5','6','7','8','9']
experimenterReadyButton = 'minus'
intro_continue.keys = []
intro_continue.rt = []
_intro_continue_allKeys = []
# keep track of which components have finished
IntroComponents = [welcome, intro_continue]
for thisComponent in IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro"-------
while continueRoutine:
    # get current time
    t = IntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome* updates
    if welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome.frameNStart = frameN  # exact frame index
        welcome.tStart = t  # local t and not account for scr refresh
        welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome, 'tStartRefresh')  # time at next scr refresh
        welcome.setAutoDraw(True)
    
    # *intro_continue* updates
    waitOnFlip = False
    if intro_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_continue.frameNStart = frameN  # exact frame index
        intro_continue.tStart = t  # local t and not account for scr refresh
        intro_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_continue, 'tStartRefresh')  # time at next scr refresh
        intro_continue.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_continue.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_continue.status == STARTED and not waitOnFlip:
        theseKeys = intro_continue.getKeys(keyList=None, waitRelease=False)
        _intro_continue_allKeys.extend(theseKeys)
        if len(_intro_continue_allKeys):
            intro_continue.keys = _intro_continue_allKeys[-1].name  # just the last key pressed
            intro_continue.rt = _intro_continue_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome.started', welcome.tStartRefresh)
thisExp.addData('welcome.stopped', welcome.tStopRefresh)
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction_1"-------
continueRoutine = True
# update component parameters for each repeat
static_key1.keys = []
static_key1.rt = []
_static_key1_allKeys = []
# keep track of which components have finished
instruction_1Components = [static_instruction, static_key1, static_instruction_2]
for thisComponent in instruction_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_1"-------
while continueRoutine:
    # get current time
    t = instruction_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *static_instruction* updates
    if static_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction.frameNStart = frameN  # exact frame index
        static_instruction.tStart = t  # local t and not account for scr refresh
        static_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction, 'tStartRefresh')  # time at next scr refresh
        static_instruction.setAutoDraw(True)
    
    # *static_key1* updates
    waitOnFlip = False
    if static_key1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_key1.frameNStart = frameN  # exact frame index
        static_key1.tStart = t  # local t and not account for scr refresh
        static_key1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_key1, 'tStartRefresh')  # time at next scr refresh
        static_key1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(static_key1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(static_key1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if static_key1.status == STARTED and not waitOnFlip:
        theseKeys = static_key1.getKeys(keyList=None, waitRelease=False)
        _static_key1_allKeys.extend(theseKeys)
        if len(_static_key1_allKeys):
            static_key1.keys = _static_key1_allKeys[-1].name  # just the last key pressed
            static_key1.rt = _static_key1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *static_instruction_2* updates
    if static_instruction_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_2.frameNStart = frameN  # exact frame index
        static_instruction_2.tStart = t  # local t and not account for scr refresh
        static_instruction_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_2, 'tStartRefresh')  # time at next scr refresh
        static_instruction_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_1"-------
for thisComponent in instruction_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction_2"-------
continueRoutine = True
# update component parameters for each repeat
distance_cm = dist_cm

image_eccentr_cm = tan(3.14159*image_eccentr_dva/180.) * distance_cm
image_side_cm = 2. * tan(0.5*3.14159*image_side_dva/180.) * distance_cm

random_pic_names=all_pic_names_training[:]
shuffle(random_pic_names)
pic_1_name=random_pic_names[0]
array_image_1.setImage(pic_1_name, False)
array_image_1.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale), False)
array_image_1.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

pic_2_name=random_pic_names[1]
array_image_2.setImage(pic_2_name, False)
array_image_2.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale), False)
array_image_2.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

pic_3_name=random_pic_names[2]
array_image_3.setImage(pic_3_name, False)
array_image_3.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale), False)
array_image_3.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

pic_4_name=random_pic_names[3]
array_image_4.setImage(pic_4_name, False)
array_image_4.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale), False)
array_image_4.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

pic_5_name=random_pic_names[4]
array_image_5.setImage(pic_5_name, False)
array_image_5.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale), False)
array_image_5.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

pic_6_name=random_pic_names[5]
array_image_6.setImage(pic_6_name, False)
array_image_6.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale), False)
array_image_6.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

pic_7_name=random_pic_names[6]
array_image_7.setImage(pic_7_name, False)
array_image_7.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[6][1]*image_eccentr_cm*y_scale), False)
array_image_7.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

pic_8_name=random_pic_names[7]
array_image_8.setImage(pic_8_name, False)
array_image_8.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale), False)
array_image_8.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
static_key1_2.keys = []
static_key1_2.rt = []
_static_key1_2_allKeys = []
array_image_1.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale))
array_image_1.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_1.setImage(pic_1_name)
array_image_2.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale))
array_image_2.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_2.setImage(pic_2_name)
array_image_3.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale))
array_image_3.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_3.setImage(pic_3_name)
array_image_4.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale))
array_image_4.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_4.setImage(pic_4_name)
array_image_5.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale))
array_image_5.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_5.setImage(pic_5_name)
array_image_6.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale))
array_image_6.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_6.setImage(pic_6_name)
array_image_7.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[6][1]*image_eccentr_cm*y_scale))
array_image_7.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_7.setImage(pic_7_name)
array_image_8.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale))
array_image_8.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_8.setImage(pic_8_name)
polygon_17.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
# keep track of which components have finished
instruction_2Components = [static_instruction_3, static_key1_2, static_instruction_4, array_image_1, array_image_2, array_image_3, array_image_4, array_image_5, array_image_6, array_image_7, array_image_8, polygon_17]
for thisComponent in instruction_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_2"-------
while continueRoutine:
    # get current time
    t = instruction_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *static_instruction_3* updates
    if static_instruction_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_3.frameNStart = frameN  # exact frame index
        static_instruction_3.tStart = t  # local t and not account for scr refresh
        static_instruction_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_3, 'tStartRefresh')  # time at next scr refresh
        static_instruction_3.setAutoDraw(True)
    
    # *static_key1_2* updates
    waitOnFlip = False
    if static_key1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_key1_2.frameNStart = frameN  # exact frame index
        static_key1_2.tStart = t  # local t and not account for scr refresh
        static_key1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_key1_2, 'tStartRefresh')  # time at next scr refresh
        static_key1_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(static_key1_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(static_key1_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if static_key1_2.status == STARTED and not waitOnFlip:
        theseKeys = static_key1_2.getKeys(keyList=None, waitRelease=False)
        _static_key1_2_allKeys.extend(theseKeys)
        if len(_static_key1_2_allKeys):
            static_key1_2.keys = _static_key1_2_allKeys[-1].name  # just the last key pressed
            static_key1_2.rt = _static_key1_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *static_instruction_4* updates
    if static_instruction_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_4.frameNStart = frameN  # exact frame index
        static_instruction_4.tStart = t  # local t and not account for scr refresh
        static_instruction_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_4, 'tStartRefresh')  # time at next scr refresh
        static_instruction_4.setAutoDraw(True)
    
    # *array_image_1* updates
    if array_image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        array_image_1.frameNStart = frameN  # exact frame index
        array_image_1.tStart = t  # local t and not account for scr refresh
        array_image_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_1, 'tStartRefresh')  # time at next scr refresh
        array_image_1.setAutoDraw(True)
    
    # *array_image_2* updates
    if array_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        array_image_2.frameNStart = frameN  # exact frame index
        array_image_2.tStart = t  # local t and not account for scr refresh
        array_image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_2, 'tStartRefresh')  # time at next scr refresh
        array_image_2.setAutoDraw(True)
    
    # *array_image_3* updates
    if array_image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        array_image_3.frameNStart = frameN  # exact frame index
        array_image_3.tStart = t  # local t and not account for scr refresh
        array_image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_3, 'tStartRefresh')  # time at next scr refresh
        array_image_3.setAutoDraw(True)
    
    # *array_image_4* updates
    if array_image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        array_image_4.frameNStart = frameN  # exact frame index
        array_image_4.tStart = t  # local t and not account for scr refresh
        array_image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_4, 'tStartRefresh')  # time at next scr refresh
        array_image_4.setAutoDraw(True)
    
    # *array_image_5* updates
    if array_image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        array_image_5.frameNStart = frameN  # exact frame index
        array_image_5.tStart = t  # local t and not account for scr refresh
        array_image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_5, 'tStartRefresh')  # time at next scr refresh
        array_image_5.setAutoDraw(True)
    
    # *array_image_6* updates
    if array_image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        array_image_6.frameNStart = frameN  # exact frame index
        array_image_6.tStart = t  # local t and not account for scr refresh
        array_image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_6, 'tStartRefresh')  # time at next scr refresh
        array_image_6.setAutoDraw(True)
    
    # *array_image_7* updates
    if array_image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        array_image_7.frameNStart = frameN  # exact frame index
        array_image_7.tStart = t  # local t and not account for scr refresh
        array_image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_7, 'tStartRefresh')  # time at next scr refresh
        array_image_7.setAutoDraw(True)
    
    # *array_image_8* updates
    if array_image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        array_image_8.frameNStart = frameN  # exact frame index
        array_image_8.tStart = t  # local t and not account for scr refresh
        array_image_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_8, 'tStartRefresh')  # time at next scr refresh
        array_image_8.setAutoDraw(True)
    
    # *polygon_17* updates
    if polygon_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_17.frameNStart = frameN  # exact frame index
        polygon_17.tStart = t  # local t and not account for scr refresh
        polygon_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_17, 'tStartRefresh')  # time at next scr refresh
        polygon_17.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_2"-------
for thisComponent in instruction_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction_3"-------
continueRoutine = True
# update component parameters for each repeat
array_image_1b.setImage(pic_1_name, False)
array_image_1b.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale), False)
array_image_1b.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_2b.setImage(pic_2_name, False)
array_image_2b.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale), False)
array_image_2b.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_3b.setImage(pic_3_name, False)
array_image_3b.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale), False)
array_image_3b.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_4b.setImage(pic_4_name, False)
array_image_4b.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale), False)
array_image_4b.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_5b.setImage(pic_5_name, False)
array_image_5b.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale), False)
array_image_5b.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_6b.setImage(pic_6_name, False)
array_image_6b.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale), False)
array_image_6b.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_7b.setImage(pic_7_name, False)
array_image_7b.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[6][1]*image_eccentr_cm*y_scale), False)
array_image_7b.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_8b.setImage(pic_8_name, False)
array_image_8b.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale), False)
array_image_8b.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
static_key1_6.keys = []
static_key1_6.rt = []
_static_key1_6_allKeys = []
array_image_1b.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale))
array_image_1b.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_1b.setImage(pic_1_name)
array_image_2b.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale))
array_image_2b.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_2b.setImage(pic_2_name)
array_image_3b.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale))
array_image_3b.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_3b.setImage(pic_3_name)
array_image_4b.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale))
array_image_4b.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_4b.setImage(pic_4_name)
array_image_5b.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale))
array_image_5b.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_5b.setImage(pic_5_name)
array_image_6b.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale))
array_image_6b.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_6b.setImage(pic_6_name)
array_image_7b.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[6][1]*image_eccentr_cm*y_scale))
array_image_7b.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_7b.setImage(pic_7_name)
array_image_8b.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale))
array_image_8b.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_8b.setImage(pic_8_name)
polygon_18.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
# keep track of which components have finished
instruction_3Components = [static_instruction_15, static_key1_6, static_instruction_16, array_image_1b, array_image_2b, array_image_3b, array_image_4b, array_image_5b, array_image_6b, array_image_7b, array_image_8b, polygon_18]
for thisComponent in instruction_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_3"-------
while continueRoutine:
    # get current time
    t = instruction_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *static_instruction_15* updates
    if static_instruction_15.status == NOT_STARTED and tThisFlip >= 1.-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_15.frameNStart = frameN  # exact frame index
        static_instruction_15.tStart = t  # local t and not account for scr refresh
        static_instruction_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_15, 'tStartRefresh')  # time at next scr refresh
        static_instruction_15.setAutoDraw(True)
    
    # *static_key1_6* updates
    waitOnFlip = False
    if static_key1_6.status == NOT_STARTED and tThisFlip >= 1.-frameTolerance:
        # keep track of start time/frame for later
        static_key1_6.frameNStart = frameN  # exact frame index
        static_key1_6.tStart = t  # local t and not account for scr refresh
        static_key1_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_key1_6, 'tStartRefresh')  # time at next scr refresh
        static_key1_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(static_key1_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(static_key1_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if static_key1_6.status == STARTED and not waitOnFlip:
        theseKeys = static_key1_6.getKeys(keyList=None, waitRelease=False)
        _static_key1_6_allKeys.extend(theseKeys)
        if len(_static_key1_6_allKeys):
            static_key1_6.keys = _static_key1_6_allKeys[-1].name  # just the last key pressed
            static_key1_6.rt = _static_key1_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *static_instruction_16* updates
    if static_instruction_16.status == NOT_STARTED and tThisFlip >= 1.-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_16.frameNStart = frameN  # exact frame index
        static_instruction_16.tStart = t  # local t and not account for scr refresh
        static_instruction_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_16, 'tStartRefresh')  # time at next scr refresh
        static_instruction_16.setAutoDraw(True)
    
    # *array_image_1b* updates
    if array_image_1b.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        # keep track of start time/frame for later
        array_image_1b.frameNStart = frameN  # exact frame index
        array_image_1b.tStart = t  # local t and not account for scr refresh
        array_image_1b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_1b, 'tStartRefresh')  # time at next scr refresh
        array_image_1b.setAutoDraw(True)
    if array_image_1b.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > array_image_1b.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            array_image_1b.tStop = t  # not accounting for scr refresh
            array_image_1b.frameNStop = frameN  # exact frame index
            win.timeOnFlip(array_image_1b, 'tStopRefresh')  # time at next scr refresh
            array_image_1b.setAutoDraw(False)
    
    # *array_image_2b* updates
    if array_image_2b.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        # keep track of start time/frame for later
        array_image_2b.frameNStart = frameN  # exact frame index
        array_image_2b.tStart = t  # local t and not account for scr refresh
        array_image_2b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_2b, 'tStartRefresh')  # time at next scr refresh
        array_image_2b.setAutoDraw(True)
    if array_image_2b.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > array_image_2b.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            array_image_2b.tStop = t  # not accounting for scr refresh
            array_image_2b.frameNStop = frameN  # exact frame index
            win.timeOnFlip(array_image_2b, 'tStopRefresh')  # time at next scr refresh
            array_image_2b.setAutoDraw(False)
    
    # *array_image_3b* updates
    if array_image_3b.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        # keep track of start time/frame for later
        array_image_3b.frameNStart = frameN  # exact frame index
        array_image_3b.tStart = t  # local t and not account for scr refresh
        array_image_3b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_3b, 'tStartRefresh')  # time at next scr refresh
        array_image_3b.setAutoDraw(True)
    if array_image_3b.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > array_image_3b.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            array_image_3b.tStop = t  # not accounting for scr refresh
            array_image_3b.frameNStop = frameN  # exact frame index
            win.timeOnFlip(array_image_3b, 'tStopRefresh')  # time at next scr refresh
            array_image_3b.setAutoDraw(False)
    
    # *array_image_4b* updates
    if array_image_4b.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        # keep track of start time/frame for later
        array_image_4b.frameNStart = frameN  # exact frame index
        array_image_4b.tStart = t  # local t and not account for scr refresh
        array_image_4b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_4b, 'tStartRefresh')  # time at next scr refresh
        array_image_4b.setAutoDraw(True)
    if array_image_4b.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > array_image_4b.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            array_image_4b.tStop = t  # not accounting for scr refresh
            array_image_4b.frameNStop = frameN  # exact frame index
            win.timeOnFlip(array_image_4b, 'tStopRefresh')  # time at next scr refresh
            array_image_4b.setAutoDraw(False)
    
    # *array_image_5b* updates
    if array_image_5b.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        # keep track of start time/frame for later
        array_image_5b.frameNStart = frameN  # exact frame index
        array_image_5b.tStart = t  # local t and not account for scr refresh
        array_image_5b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_5b, 'tStartRefresh')  # time at next scr refresh
        array_image_5b.setAutoDraw(True)
    if array_image_5b.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > array_image_5b.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            array_image_5b.tStop = t  # not accounting for scr refresh
            array_image_5b.frameNStop = frameN  # exact frame index
            win.timeOnFlip(array_image_5b, 'tStopRefresh')  # time at next scr refresh
            array_image_5b.setAutoDraw(False)
    
    # *array_image_6b* updates
    if array_image_6b.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        # keep track of start time/frame for later
        array_image_6b.frameNStart = frameN  # exact frame index
        array_image_6b.tStart = t  # local t and not account for scr refresh
        array_image_6b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_6b, 'tStartRefresh')  # time at next scr refresh
        array_image_6b.setAutoDraw(True)
    if array_image_6b.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > array_image_6b.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            array_image_6b.tStop = t  # not accounting for scr refresh
            array_image_6b.frameNStop = frameN  # exact frame index
            win.timeOnFlip(array_image_6b, 'tStopRefresh')  # time at next scr refresh
            array_image_6b.setAutoDraw(False)
    
    # *array_image_7b* updates
    if array_image_7b.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        # keep track of start time/frame for later
        array_image_7b.frameNStart = frameN  # exact frame index
        array_image_7b.tStart = t  # local t and not account for scr refresh
        array_image_7b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_7b, 'tStartRefresh')  # time at next scr refresh
        array_image_7b.setAutoDraw(True)
    if array_image_7b.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > array_image_7b.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            array_image_7b.tStop = t  # not accounting for scr refresh
            array_image_7b.frameNStop = frameN  # exact frame index
            win.timeOnFlip(array_image_7b, 'tStopRefresh')  # time at next scr refresh
            array_image_7b.setAutoDraw(False)
    
    # *array_image_8b* updates
    if array_image_8b.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        # keep track of start time/frame for later
        array_image_8b.frameNStart = frameN  # exact frame index
        array_image_8b.tStart = t  # local t and not account for scr refresh
        array_image_8b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_8b, 'tStartRefresh')  # time at next scr refresh
        array_image_8b.setAutoDraw(True)
    if array_image_8b.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > array_image_8b.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            array_image_8b.tStop = t  # not accounting for scr refresh
            array_image_8b.frameNStop = frameN  # exact frame index
            win.timeOnFlip(array_image_8b, 'tStopRefresh')  # time at next scr refresh
            array_image_8b.setAutoDraw(False)
    
    # *polygon_18* updates
    if polygon_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_18.frameNStart = frameN  # exact frame index
        polygon_18.tStart = t  # local t and not account for scr refresh
        polygon_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_18, 'tStartRefresh')  # time at next scr refresh
        polygon_18.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_3"-------
for thisComponent in instruction_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction_4"-------
continueRoutine = True
# update component parameters for each repeat
array_image_1c.setImage(pic_1_name, False)
array_image_1c.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale), False)
array_image_1c.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_2c.setImage(pic_2_name, False)
array_image_2c.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale), False)
array_image_2c.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_3c.setImage(pic_3_name, False)
array_image_3c.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale), False)
array_image_3c.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_4c.setImage(pic_4_name, False)
array_image_4c.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale), False)
array_image_4c.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_5c.setImage(pic_5_name, False)
array_image_5c.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale), False)
array_image_5c.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_6c.setImage(pic_6_name, False)
array_image_6c.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale), False)
array_image_6c.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_7c.setImage(pic_7_name, False)
array_image_7c.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale), False)
array_image_7c.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

array_image_8c.setImage(pic_8_name, False)
array_image_8c.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale), False)
array_image_8c.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)

static_key1_7.keys = []
static_key1_7.rt = []
_static_key1_7_allKeys = []
array_image_1c.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale))
array_image_1c.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_1c.setImage(pic_1_name)
array_image_2c.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale))
array_image_2c.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_2c.setImage(pic_2_name)
array_image_3c.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale))
array_image_3c.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_3c.setImage(pic_3_name)
array_image_4c.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale))
array_image_4c.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_4c.setImage(pic_4_name)
array_image_5c.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale))
array_image_5c.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_5c.setImage(pic_5_name)
array_image_6c.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale))
array_image_6c.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_6c.setImage(pic_6_name)
array_image_7c.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[6][1]*image_eccentr_cm*y_scale))
array_image_7c.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_7c.setImage(pic_7_name)
array_image_8c.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale))
array_image_8c.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
array_image_8c.setImage(pic_8_name)
polygon_19.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
# keep track of which components have finished
instruction_4Components = [static_instruction_17, static_key1_7, static_instruction_18, array_image_1c, array_image_2c, array_image_3c, array_image_4c, array_image_5c, array_image_6c, array_image_7c, array_image_8c, polygon_19]
for thisComponent in instruction_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_4"-------
while continueRoutine:
    # get current time
    t = instruction_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *static_instruction_17* updates
    if static_instruction_17.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_17.frameNStart = frameN  # exact frame index
        static_instruction_17.tStart = t  # local t and not account for scr refresh
        static_instruction_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_17, 'tStartRefresh')  # time at next scr refresh
        static_instruction_17.setAutoDraw(True)
    
    # *static_key1_7* updates
    waitOnFlip = False
    if static_key1_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        static_key1_7.frameNStart = frameN  # exact frame index
        static_key1_7.tStart = t  # local t and not account for scr refresh
        static_key1_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_key1_7, 'tStartRefresh')  # time at next scr refresh
        static_key1_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(static_key1_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(static_key1_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if static_key1_7.status == STARTED and not waitOnFlip:
        theseKeys = static_key1_7.getKeys(keyList=None, waitRelease=False)
        _static_key1_7_allKeys.extend(theseKeys)
        if len(_static_key1_7_allKeys):
            static_key1_7.keys = _static_key1_7_allKeys[-1].name  # just the last key pressed
            static_key1_7.rt = _static_key1_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *static_instruction_18* updates
    if static_instruction_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_18.frameNStart = frameN  # exact frame index
        static_instruction_18.tStart = t  # local t and not account for scr refresh
        static_instruction_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_18, 'tStartRefresh')  # time at next scr refresh
        static_instruction_18.setAutoDraw(True)
    
    # *array_image_1c* updates
    if array_image_1c.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        array_image_1c.frameNStart = frameN  # exact frame index
        array_image_1c.tStart = t  # local t and not account for scr refresh
        array_image_1c.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_1c, 'tStartRefresh')  # time at next scr refresh
        array_image_1c.setAutoDraw(True)
    
    # *array_image_2c* updates
    if array_image_2c.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        array_image_2c.frameNStart = frameN  # exact frame index
        array_image_2c.tStart = t  # local t and not account for scr refresh
        array_image_2c.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_2c, 'tStartRefresh')  # time at next scr refresh
        array_image_2c.setAutoDraw(True)
    
    # *array_image_3c* updates
    if array_image_3c.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        array_image_3c.frameNStart = frameN  # exact frame index
        array_image_3c.tStart = t  # local t and not account for scr refresh
        array_image_3c.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_3c, 'tStartRefresh')  # time at next scr refresh
        array_image_3c.setAutoDraw(True)
    
    # *array_image_4c* updates
    if array_image_4c.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        array_image_4c.frameNStart = frameN  # exact frame index
        array_image_4c.tStart = t  # local t and not account for scr refresh
        array_image_4c.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_4c, 'tStartRefresh')  # time at next scr refresh
        array_image_4c.setAutoDraw(True)
    
    # *array_image_5c* updates
    if array_image_5c.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        array_image_5c.frameNStart = frameN  # exact frame index
        array_image_5c.tStart = t  # local t and not account for scr refresh
        array_image_5c.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_5c, 'tStartRefresh')  # time at next scr refresh
        array_image_5c.setAutoDraw(True)
    
    # *array_image_6c* updates
    if array_image_6c.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        array_image_6c.frameNStart = frameN  # exact frame index
        array_image_6c.tStart = t  # local t and not account for scr refresh
        array_image_6c.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_6c, 'tStartRefresh')  # time at next scr refresh
        array_image_6c.setAutoDraw(True)
    
    # *array_image_7c* updates
    if array_image_7c.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        array_image_7c.frameNStart = frameN  # exact frame index
        array_image_7c.tStart = t  # local t and not account for scr refresh
        array_image_7c.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_7c, 'tStartRefresh')  # time at next scr refresh
        array_image_7c.setAutoDraw(True)
    
    # *array_image_8c* updates
    if array_image_8c.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        array_image_8c.frameNStart = frameN  # exact frame index
        array_image_8c.tStart = t  # local t and not account for scr refresh
        array_image_8c.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(array_image_8c, 'tStartRefresh')  # time at next scr refresh
        array_image_8c.setAutoDraw(True)
    
    # *polygon_19* updates
    if polygon_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_19.frameNStart = frameN  # exact frame index
        polygon_19.tStart = t  # local t and not account for scr refresh
        polygon_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_19, 'tStartRefresh')  # time at next scr refresh
        polygon_19.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_4"-------
for thisComponent in instruction_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions_4to5"-------
continueRoutine = True
# update component parameters for each repeat
static_key1_11.keys = []
static_key1_11.rt = []
_static_key1_11_allKeys = []
# keep track of which components have finished
instructions_4to5Components = [static_instruction_25, static_key1_11, static_instruction_26]
for thisComponent in instructions_4to5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_4to5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_4to5"-------
while continueRoutine:
    # get current time
    t = instructions_4to5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_4to5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *static_instruction_25* updates
    if static_instruction_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_25.frameNStart = frameN  # exact frame index
        static_instruction_25.tStart = t  # local t and not account for scr refresh
        static_instruction_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_25, 'tStartRefresh')  # time at next scr refresh
        static_instruction_25.setAutoDraw(True)
    
    # *static_key1_11* updates
    waitOnFlip = False
    if static_key1_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_key1_11.frameNStart = frameN  # exact frame index
        static_key1_11.tStart = t  # local t and not account for scr refresh
        static_key1_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_key1_11, 'tStartRefresh')  # time at next scr refresh
        static_key1_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(static_key1_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(static_key1_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if static_key1_11.status == STARTED and not waitOnFlip:
        theseKeys = static_key1_11.getKeys(keyList=None, waitRelease=False)
        _static_key1_11_allKeys.extend(theseKeys)
        if len(_static_key1_11_allKeys):
            static_key1_11.keys = _static_key1_11_allKeys[-1].name  # just the last key pressed
            static_key1_11.rt = _static_key1_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *static_instruction_26* updates
    if static_instruction_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_26.frameNStart = frameN  # exact frame index
        static_instruction_26.tStart = t  # local t and not account for scr refresh
        static_instruction_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_26, 'tStartRefresh')  # time at next scr refresh
        static_instruction_26.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_4to5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_4to5"-------
for thisComponent in instructions_4to5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions_4to5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction_5"-------
continueRoutine = True
# update component parameters for each repeat
static_key1_8.keys = []
static_key1_8.rt = []
_static_key1_8_allKeys = []
polygon_20.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
pointer_dot_0.setPos((x_y_gains_per_angle[1][0]*pointer_length_relative_to_image_eccentricity*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*pointer_length_relative_to_image_eccentricity*image_eccentr_cm*y_scale))
pointer_dot_0.setSize((dot_diam_dva*x_scale/2., dot_diam_dva*y_scale/2.))
pointer_dot_1.setPos((x_y_gains_per_angle[1][0]*pointer_length_relative_to_image_eccentricity*image_eccentr_cm*x_scale*.66667, x_y_gains_per_angle[1][1]*pointer_length_relative_to_image_eccentricity*image_eccentr_cm*y_scale*.66667))
pointer_dot_1.setSize((dot_diam_dva*x_scale/2., dot_diam_dva*y_scale/2.))
pointer_dot_2.setPos((x_y_gains_per_angle[1][0]*pointer_length_relative_to_image_eccentricity*image_eccentr_cm*x_scale*.33333, x_y_gains_per_angle[1][1]*pointer_length_relative_to_image_eccentricity*image_eccentr_cm*y_scale*.33333))
pointer_dot_2.setSize((dot_diam_dva*x_scale/2., dot_diam_dva*y_scale/2.))
# keep track of which components have finished
instruction_5Components = [static_instruction_19, static_key1_8, static_instruction_20, polygon_20, pointer_dot_0, pointer_dot_1, pointer_dot_2]
for thisComponent in instruction_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_5"-------
while continueRoutine:
    # get current time
    t = instruction_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *static_instruction_19* updates
    if static_instruction_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_19.frameNStart = frameN  # exact frame index
        static_instruction_19.tStart = t  # local t and not account for scr refresh
        static_instruction_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_19, 'tStartRefresh')  # time at next scr refresh
        static_instruction_19.setAutoDraw(True)
    
    # *static_key1_8* updates
    waitOnFlip = False
    if static_key1_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_key1_8.frameNStart = frameN  # exact frame index
        static_key1_8.tStart = t  # local t and not account for scr refresh
        static_key1_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_key1_8, 'tStartRefresh')  # time at next scr refresh
        static_key1_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(static_key1_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(static_key1_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if static_key1_8.status == STARTED and not waitOnFlip:
        theseKeys = static_key1_8.getKeys(keyList=None, waitRelease=False)
        _static_key1_8_allKeys.extend(theseKeys)
        if len(_static_key1_8_allKeys):
            static_key1_8.keys = _static_key1_8_allKeys[-1].name  # just the last key pressed
            static_key1_8.rt = _static_key1_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *static_instruction_20* updates
    if static_instruction_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_20.frameNStart = frameN  # exact frame index
        static_instruction_20.tStart = t  # local t and not account for scr refresh
        static_instruction_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_20, 'tStartRefresh')  # time at next scr refresh
        static_instruction_20.setAutoDraw(True)
    
    # *polygon_20* updates
    if polygon_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_20.frameNStart = frameN  # exact frame index
        polygon_20.tStart = t  # local t and not account for scr refresh
        polygon_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_20, 'tStartRefresh')  # time at next scr refresh
        polygon_20.setAutoDraw(True)
    
    # *pointer_dot_0* updates
    if pointer_dot_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pointer_dot_0.frameNStart = frameN  # exact frame index
        pointer_dot_0.tStart = t  # local t and not account for scr refresh
        pointer_dot_0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pointer_dot_0, 'tStartRefresh')  # time at next scr refresh
        pointer_dot_0.setAutoDraw(True)
    
    # *pointer_dot_1* updates
    if pointer_dot_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pointer_dot_1.frameNStart = frameN  # exact frame index
        pointer_dot_1.tStart = t  # local t and not account for scr refresh
        pointer_dot_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pointer_dot_1, 'tStartRefresh')  # time at next scr refresh
        pointer_dot_1.setAutoDraw(True)
    
    # *pointer_dot_2* updates
    if pointer_dot_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pointer_dot_2.frameNStart = frameN  # exact frame index
        pointer_dot_2.tStart = t  # local t and not account for scr refresh
        pointer_dot_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pointer_dot_2, 'tStartRefresh')  # time at next scr refresh
        pointer_dot_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_5"-------
for thisComponent in instruction_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('pointer_dot_0.started', pointer_dot_0.tStartRefresh)
thisExp.addData('pointer_dot_0.stopped', pointer_dot_0.tStopRefresh)
thisExp.addData('pointer_dot_1.started', pointer_dot_1.tStartRefresh)
thisExp.addData('pointer_dot_1.stopped', pointer_dot_1.tStopRefresh)
thisExp.addData('pointer_dot_2.started', pointer_dot_2.tStartRefresh)
thisExp.addData('pointer_dot_2.stopped', pointer_dot_2.tStopRefresh)
# the Routine "instruction_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction_6"-------
continueRoutine = True
# update component parameters for each repeat
static_key1_12.keys = []
static_key1_12.rt = []
_static_key1_12_allKeys = []
polygon_24.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
# keep track of which components have finished
instruction_6Components = [static_instruction_27, static_key1_12, static_instruction_28, polygon_24]
for thisComponent in instruction_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_6"-------
while continueRoutine:
    # get current time
    t = instruction_6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *static_instruction_27* updates
    if static_instruction_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_27.frameNStart = frameN  # exact frame index
        static_instruction_27.tStart = t  # local t and not account for scr refresh
        static_instruction_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_27, 'tStartRefresh')  # time at next scr refresh
        static_instruction_27.setAutoDraw(True)
    
    # *static_key1_12* updates
    waitOnFlip = False
    if static_key1_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_key1_12.frameNStart = frameN  # exact frame index
        static_key1_12.tStart = t  # local t and not account for scr refresh
        static_key1_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_key1_12, 'tStartRefresh')  # time at next scr refresh
        static_key1_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(static_key1_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(static_key1_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if static_key1_12.status == STARTED and not waitOnFlip:
        theseKeys = static_key1_12.getKeys(keyList=None, waitRelease=False)
        _static_key1_12_allKeys.extend(theseKeys)
        if len(_static_key1_12_allKeys):
            static_key1_12.keys = _static_key1_12_allKeys[-1].name  # just the last key pressed
            static_key1_12.rt = _static_key1_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *static_instruction_28* updates
    if static_instruction_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_28.frameNStart = frameN  # exact frame index
        static_instruction_28.tStart = t  # local t and not account for scr refresh
        static_instruction_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_28, 'tStartRefresh')  # time at next scr refresh
        static_instruction_28.setAutoDraw(True)
    
    # *polygon_24* updates
    if polygon_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_24.frameNStart = frameN  # exact frame index
        polygon_24.tStart = t  # local t and not account for scr refresh
        polygon_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_24, 'tStartRefresh')  # time at next scr refresh
        polygon_24.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_6"-------
for thisComponent in instruction_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction_67"-------
continueRoutine = True
# update component parameters for each repeat
static_key1_17.keys = []
static_key1_17.rt = []
_static_key1_17_allKeys = []
# keep track of which components have finished
instruction_67Components = [static_instruction_37, static_key1_17, static_instruction_38, SD_image]
for thisComponent in instruction_67Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_67Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_67"-------
while continueRoutine:
    # get current time
    t = instruction_67Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_67Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *static_instruction_37* updates
    if static_instruction_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_37.frameNStart = frameN  # exact frame index
        static_instruction_37.tStart = t  # local t and not account for scr refresh
        static_instruction_37.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_37, 'tStartRefresh')  # time at next scr refresh
        static_instruction_37.setAutoDraw(True)
    
    # *static_key1_17* updates
    waitOnFlip = False
    if static_key1_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_key1_17.frameNStart = frameN  # exact frame index
        static_key1_17.tStart = t  # local t and not account for scr refresh
        static_key1_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_key1_17, 'tStartRefresh')  # time at next scr refresh
        static_key1_17.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(static_key1_17.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(static_key1_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if static_key1_17.status == STARTED and not waitOnFlip:
        theseKeys = static_key1_17.getKeys(keyList=None, waitRelease=False)
        _static_key1_17_allKeys.extend(theseKeys)
        if len(_static_key1_17_allKeys):
            static_key1_17.keys = _static_key1_17_allKeys[-1].name  # just the last key pressed
            static_key1_17.rt = _static_key1_17_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *static_instruction_38* updates
    if static_instruction_38.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_38.frameNStart = frameN  # exact frame index
        static_instruction_38.tStart = t  # local t and not account for scr refresh
        static_instruction_38.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_38, 'tStartRefresh')  # time at next scr refresh
        static_instruction_38.setAutoDraw(True)
    
    # *SD_image* updates
    if SD_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SD_image.frameNStart = frameN  # exact frame index
        SD_image.tStart = t  # local t and not account for scr refresh
        SD_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SD_image, 'tStartRefresh')  # time at next scr refresh
        SD_image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_67Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_67"-------
for thisComponent in instruction_67Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('SD_image.started', SD_image.tStartRefresh)
thisExp.addData('SD_image.stopped', SD_image.tStopRefresh)
# the Routine "instruction_67" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction_67b"-------
continueRoutine = True
# update component parameters for each repeat
static_key1_18.keys = []
static_key1_18.rt = []
_static_key1_18_allKeys = []
polygon_37.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
# keep track of which components have finished
instruction_67bComponents = [static_instruction_39, static_key1_18, static_instruction_40, polygon_37]
for thisComponent in instruction_67bComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_67bClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_67b"-------
while continueRoutine:
    # get current time
    t = instruction_67bClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_67bClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *static_instruction_39* updates
    if static_instruction_39.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_39.frameNStart = frameN  # exact frame index
        static_instruction_39.tStart = t  # local t and not account for scr refresh
        static_instruction_39.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_39, 'tStartRefresh')  # time at next scr refresh
        static_instruction_39.setAutoDraw(True)
    
    # *static_key1_18* updates
    waitOnFlip = False
    if static_key1_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_key1_18.frameNStart = frameN  # exact frame index
        static_key1_18.tStart = t  # local t and not account for scr refresh
        static_key1_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_key1_18, 'tStartRefresh')  # time at next scr refresh
        static_key1_18.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(static_key1_18.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(static_key1_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if static_key1_18.status == STARTED and not waitOnFlip:
        theseKeys = static_key1_18.getKeys(keyList=None, waitRelease=False)
        _static_key1_18_allKeys.extend(theseKeys)
        if len(_static_key1_18_allKeys):
            static_key1_18.keys = _static_key1_18_allKeys[-1].name  # just the last key pressed
            static_key1_18.rt = _static_key1_18_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *static_instruction_40* updates
    if static_instruction_40.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_40.frameNStart = frameN  # exact frame index
        static_instruction_40.tStart = t  # local t and not account for scr refresh
        static_instruction_40.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_40, 'tStartRefresh')  # time at next scr refresh
        static_instruction_40.setAutoDraw(True)
    
    # *polygon_37* updates
    if polygon_37.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_37.frameNStart = frameN  # exact frame index
        polygon_37.tStart = t  # local t and not account for scr refresh
        polygon_37.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_37, 'tStartRefresh')  # time at next scr refresh
        polygon_37.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_67bComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_67b"-------
for thisComponent in instruction_67bComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction_67b" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction_7"-------
continueRoutine = True
# update component parameters for each repeat
static_key1_14.keys = []
static_key1_14.rt = []
_static_key1_14_allKeys = []
polygon_29.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
# keep track of which components have finished
instruction_7Components = [static_instruction_31, static_key1_14, static_instruction_32, polygon_29]
for thisComponent in instruction_7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_7"-------
while continueRoutine:
    # get current time
    t = instruction_7Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_7Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *static_instruction_31* updates
    if static_instruction_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_31.frameNStart = frameN  # exact frame index
        static_instruction_31.tStart = t  # local t and not account for scr refresh
        static_instruction_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_31, 'tStartRefresh')  # time at next scr refresh
        static_instruction_31.setAutoDraw(True)
    
    # *static_key1_14* updates
    waitOnFlip = False
    if static_key1_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_key1_14.frameNStart = frameN  # exact frame index
        static_key1_14.tStart = t  # local t and not account for scr refresh
        static_key1_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_key1_14, 'tStartRefresh')  # time at next scr refresh
        static_key1_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(static_key1_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(static_key1_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if static_key1_14.status == STARTED and not waitOnFlip:
        theseKeys = static_key1_14.getKeys(keyList=None, waitRelease=False)
        _static_key1_14_allKeys.extend(theseKeys)
        if len(_static_key1_14_allKeys):
            static_key1_14.keys = _static_key1_14_allKeys[-1].name  # just the last key pressed
            static_key1_14.rt = _static_key1_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *static_instruction_32* updates
    if static_instruction_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_32.frameNStart = frameN  # exact frame index
        static_instruction_32.tStart = t  # local t and not account for scr refresh
        static_instruction_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_32, 'tStartRefresh')  # time at next scr refresh
        static_instruction_32.setAutoDraw(True)
    
    # *polygon_29* updates
    if polygon_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_29.frameNStart = frameN  # exact frame index
        polygon_29.tStart = t  # local t and not account for scr refresh
        polygon_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_29, 'tStartRefresh')  # time at next scr refresh
        polygon_29.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_7"-------
for thisComponent in instruction_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(permutation_data_file_string_practice),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "load_practice_trials"-------
    continueRoutine = True
    # update component parameters for each repeat
    practice_trial_image_list.append([Used_image_1,Used_image_2,Used_image_3,Used_image_4,Used_image_5,Used_image_6,Used_image_7,Used_image_8,Unused_image_1,Unused_image_2])
    if (practice_trial_load_number+1)<=num_practice_trials/2:
        retro_0_post_1_practice.append(0)
        change_0_1_practice.append(0)
    else:
        retro_0_post_1_practice.append(1)
        change_0_1_practice.append(1)
        
    mem_display_to_cue_times_practice.append(mem_display_to_cue_time_s)
    
    # keep track of which components have finished
    load_practice_trialsComponents = []
    for thisComponent in load_practice_trialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    load_practice_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "load_practice_trials"-------
    while continueRoutine:
        # get current time
        t = load_practice_trialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=load_practice_trialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in load_practice_trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "load_practice_trials"-------
    for thisComponent in load_practice_trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_trial_load_number=practice_trial_load_number+1
    
    if practice_trial_load_number>=num_practice_trials:
        trials_2.finished = True
        
        shuffle(retro_0_post_1_practice)
        shuffle(mem_display_to_cue_times_practice)
        shuffle(change_0_1_practice)
        
        practice_trial_index=0
        confidence_onset_time_s=0.
        confidence_image_onset_time_s=0.
     
    # the Routine "load_practice_trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=num_practice_trials, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "get_ready_practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    if practice_trial_index == 0:
        practice_trial_text = "Get ready for practice trial 1 out of " + str(num_practice_trials)+".\n\nPlease don't forget to keep your eyes on the dot in the middle, and to use your right hand to indicate 'Same' or 'Different' using your index and middle finger, respectively."
    elif practice_trial_index >= num_practice_trials/2.:
        practice_trial_text = "Get ready for practice trial " + str(practice_trial_index+1) + " out of " + str(num_practice_trials)
    else:
        practice_trial_text = "Get ready for practice trial " + str(practice_trial_index+1) + " out of " + str(num_practice_trials)+".\n\nPlease don't forget to keep your eyes on the dot in the middle, and to use your right hand to indicate 'Same' or 'Different' with your index and middle finger, respectively, and then your left hand to indicate your confidence in that choice (ring finger=certain, middle finger=doubt, index finger=guess)."
    
    static_instruction_29.setText(practice_trial_text,False);
    
    
    static_instruction_29.setText(practice_trial_text)
    static_key1_13.keys = []
    static_key1_13.rt = []
    _static_key1_13_allKeys = []
    polygon_25.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
    # keep track of which components have finished
    get_ready_practiceComponents = [static_instruction_29, static_key1_13, static_instruction_30, polygon_25]
    for thisComponent in get_ready_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    get_ready_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "get_ready_practice"-------
    while continueRoutine:
        # get current time
        t = get_ready_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=get_ready_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *static_instruction_29* updates
        if static_instruction_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            static_instruction_29.frameNStart = frameN  # exact frame index
            static_instruction_29.tStart = t  # local t and not account for scr refresh
            static_instruction_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(static_instruction_29, 'tStartRefresh')  # time at next scr refresh
            static_instruction_29.setAutoDraw(True)
        
        # *static_key1_13* updates
        waitOnFlip = False
        if static_key1_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            static_key1_13.frameNStart = frameN  # exact frame index
            static_key1_13.tStart = t  # local t and not account for scr refresh
            static_key1_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(static_key1_13, 'tStartRefresh')  # time at next scr refresh
            static_key1_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(static_key1_13.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(static_key1_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if static_key1_13.status == STARTED and not waitOnFlip:
            theseKeys = static_key1_13.getKeys(keyList=None, waitRelease=False)
            _static_key1_13_allKeys.extend(theseKeys)
            if len(_static_key1_13_allKeys):
                static_key1_13.keys = _static_key1_13_allKeys[-1].name  # just the last key pressed
                static_key1_13.rt = _static_key1_13_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *static_instruction_30* updates
        if static_instruction_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            static_instruction_30.frameNStart = frameN  # exact frame index
            static_instruction_30.tStart = t  # local t and not account for scr refresh
            static_instruction_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(static_instruction_30, 'tStartRefresh')  # time at next scr refresh
            static_instruction_30.setAutoDraw(True)
        
        # *polygon_25* updates
        if polygon_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_25.frameNStart = frameN  # exact frame index
            polygon_25.tStart = t  # local t and not account for scr refresh
            polygon_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_25, 'tStartRefresh')  # time at next scr refresh
            polygon_25.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in get_ready_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "get_ready_practice"-------
    for thisComponent in get_ready_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "get_ready_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank_at_trial_start"-------
    continueRoutine = True
    # update component parameters for each repeat
    polygon_39.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
    # keep track of which components have finished
    blank_at_trial_startComponents = [polygon_39]
    for thisComponent in blank_at_trial_startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blank_at_trial_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank_at_trial_start"-------
    while continueRoutine:
        # get current time
        t = blank_at_trial_startClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blank_at_trial_startClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_39* updates
        if polygon_39.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_39.frameNStart = frameN  # exact frame index
            polygon_39.tStart = t  # local t and not account for scr refresh
            polygon_39.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_39, 'tStartRefresh')  # time at next scr refresh
            polygon_39.setAutoDraw(True)
        if polygon_39.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_39.tStartRefresh + blank_trial_start_dur_s-frameTolerance:
                # keep track of stop time/frame for later
                polygon_39.tStop = t  # not accounting for scr refresh
                polygon_39.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_39, 'tStopRefresh')  # time at next scr refresh
                polygon_39.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank_at_trial_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank_at_trial_start"-------
    for thisComponent in blank_at_trial_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "blank_at_trial_start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practice_mem_display"-------
    continueRoutine = True
    # update component parameters for each repeat
    Image_1=all_pic_names_training[practice_trial_image_list[practice_trial_index][0]]
    array_image_1d.setImage(Image_1, False)
    array_image_1d.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale), False)
    array_image_1d.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_2=all_pic_names_training[practice_trial_image_list[practice_trial_index][1]]
    array_image_2d.setImage(Image_2, False)
    array_image_2d.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale), False)
    array_image_2d.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_3=all_pic_names_training[practice_trial_image_list[practice_trial_index][2]]
    array_image_3d.setImage(Image_3, False)
    array_image_3d.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale), False)
    array_image_3d.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_4=all_pic_names_training[practice_trial_image_list[practice_trial_index][3]]
    array_image_4d.setImage(Image_4, False)
    array_image_4d.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale), False)
    array_image_4d.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_5=all_pic_names_training[practice_trial_image_list[practice_trial_index][4]]
    array_image_5d.setImage(Image_5, False)
    array_image_5d.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale), False)
    array_image_5d.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_6=all_pic_names_training[practice_trial_image_list[practice_trial_index][5]]
    array_image_6d.setImage(Image_6, False)
    array_image_6d.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale), False)
    array_image_6d.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_7=all_pic_names_training[practice_trial_image_list[practice_trial_index][6]]
    array_image_7d.setImage(Image_7, False)
    array_image_7d.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[6][1]*image_eccentr_cm*y_scale), False)
    array_image_7d.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_8=all_pic_names_training[practice_trial_image_list[practice_trial_index][7]]
    array_image_8d.setImage(Image_8, False)
    array_image_8d.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale), False)
    array_image_8d.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    thisExp.addData('memDisplayOnTimePractice',timer.getTime())
    
    #storing variables specifying trial
    for image_index in range(8):
        thisExp.addData('mem_image_'+str(image_index)+'_practice',practice_trial_image_list[practice_trial_index][image_index])
    array_image_1d.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale))
    array_image_1d.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_1d.setImage(Image_1)
    array_image_2d.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale))
    array_image_2d.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_2d.setImage(Image_2)
    array_image_3d.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale))
    array_image_3d.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_3d.setImage(Image_3)
    array_image_4d.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale))
    array_image_4d.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_4d.setImage(Image_4)
    array_image_5d.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale))
    array_image_5d.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_5d.setImage(Image_5)
    array_image_6d.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale))
    array_image_6d.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_6d.setImage(Image_6)
    array_image_7d.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[6][1]*image_eccentr_cm*y_scale))
    array_image_7d.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_7d.setImage(Image_7)
    array_image_8d.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale))
    array_image_8d.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_8d.setImage(Image_8)
    polygon_26.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
    # keep track of which components have finished
    practice_mem_displayComponents = [array_image_1d, array_image_2d, array_image_3d, array_image_4d, array_image_5d, array_image_6d, array_image_7d, array_image_8d, polygon_26]
    for thisComponent in practice_mem_displayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_mem_displayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_mem_display"-------
    while continueRoutine:
        # get current time
        t = practice_mem_displayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_mem_displayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *array_image_1d* updates
        if array_image_1d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            array_image_1d.frameNStart = frameN  # exact frame index
            array_image_1d.tStart = t  # local t and not account for scr refresh
            array_image_1d.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_1d, 'tStartRefresh')  # time at next scr refresh
            array_image_1d.setAutoDraw(True)
        if array_image_1d.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > array_image_1d.tStartRefresh + mem_display_duration_s-frameTolerance:
                # keep track of stop time/frame for later
                array_image_1d.tStop = t  # not accounting for scr refresh
                array_image_1d.frameNStop = frameN  # exact frame index
                win.timeOnFlip(array_image_1d, 'tStopRefresh')  # time at next scr refresh
                array_image_1d.setAutoDraw(False)
        
        # *array_image_2d* updates
        if array_image_2d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            array_image_2d.frameNStart = frameN  # exact frame index
            array_image_2d.tStart = t  # local t and not account for scr refresh
            array_image_2d.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_2d, 'tStartRefresh')  # time at next scr refresh
            array_image_2d.setAutoDraw(True)
        if array_image_2d.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > array_image_2d.tStartRefresh + mem_display_duration_s-frameTolerance:
                # keep track of stop time/frame for later
                array_image_2d.tStop = t  # not accounting for scr refresh
                array_image_2d.frameNStop = frameN  # exact frame index
                win.timeOnFlip(array_image_2d, 'tStopRefresh')  # time at next scr refresh
                array_image_2d.setAutoDraw(False)
        
        # *array_image_3d* updates
        if array_image_3d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            array_image_3d.frameNStart = frameN  # exact frame index
            array_image_3d.tStart = t  # local t and not account for scr refresh
            array_image_3d.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_3d, 'tStartRefresh')  # time at next scr refresh
            array_image_3d.setAutoDraw(True)
        if array_image_3d.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > array_image_3d.tStartRefresh + mem_display_duration_s-frameTolerance:
                # keep track of stop time/frame for later
                array_image_3d.tStop = t  # not accounting for scr refresh
                array_image_3d.frameNStop = frameN  # exact frame index
                win.timeOnFlip(array_image_3d, 'tStopRefresh')  # time at next scr refresh
                array_image_3d.setAutoDraw(False)
        
        # *array_image_4d* updates
        if array_image_4d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            array_image_4d.frameNStart = frameN  # exact frame index
            array_image_4d.tStart = t  # local t and not account for scr refresh
            array_image_4d.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_4d, 'tStartRefresh')  # time at next scr refresh
            array_image_4d.setAutoDraw(True)
        if array_image_4d.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > array_image_4d.tStartRefresh + mem_display_duration_s-frameTolerance:
                # keep track of stop time/frame for later
                array_image_4d.tStop = t  # not accounting for scr refresh
                array_image_4d.frameNStop = frameN  # exact frame index
                win.timeOnFlip(array_image_4d, 'tStopRefresh')  # time at next scr refresh
                array_image_4d.setAutoDraw(False)
        
        # *array_image_5d* updates
        if array_image_5d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            array_image_5d.frameNStart = frameN  # exact frame index
            array_image_5d.tStart = t  # local t and not account for scr refresh
            array_image_5d.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_5d, 'tStartRefresh')  # time at next scr refresh
            array_image_5d.setAutoDraw(True)
        if array_image_5d.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > array_image_5d.tStartRefresh + mem_display_duration_s-frameTolerance:
                # keep track of stop time/frame for later
                array_image_5d.tStop = t  # not accounting for scr refresh
                array_image_5d.frameNStop = frameN  # exact frame index
                win.timeOnFlip(array_image_5d, 'tStopRefresh')  # time at next scr refresh
                array_image_5d.setAutoDraw(False)
        
        # *array_image_6d* updates
        if array_image_6d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            array_image_6d.frameNStart = frameN  # exact frame index
            array_image_6d.tStart = t  # local t and not account for scr refresh
            array_image_6d.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_6d, 'tStartRefresh')  # time at next scr refresh
            array_image_6d.setAutoDraw(True)
        if array_image_6d.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > array_image_6d.tStartRefresh + mem_display_duration_s-frameTolerance:
                # keep track of stop time/frame for later
                array_image_6d.tStop = t  # not accounting for scr refresh
                array_image_6d.frameNStop = frameN  # exact frame index
                win.timeOnFlip(array_image_6d, 'tStopRefresh')  # time at next scr refresh
                array_image_6d.setAutoDraw(False)
        
        # *array_image_7d* updates
        if array_image_7d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            array_image_7d.frameNStart = frameN  # exact frame index
            array_image_7d.tStart = t  # local t and not account for scr refresh
            array_image_7d.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_7d, 'tStartRefresh')  # time at next scr refresh
            array_image_7d.setAutoDraw(True)
        if array_image_7d.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > array_image_7d.tStartRefresh + mem_display_duration_s-frameTolerance:
                # keep track of stop time/frame for later
                array_image_7d.tStop = t  # not accounting for scr refresh
                array_image_7d.frameNStop = frameN  # exact frame index
                win.timeOnFlip(array_image_7d, 'tStopRefresh')  # time at next scr refresh
                array_image_7d.setAutoDraw(False)
        
        # *array_image_8d* updates
        if array_image_8d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            array_image_8d.frameNStart = frameN  # exact frame index
            array_image_8d.tStart = t  # local t and not account for scr refresh
            array_image_8d.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_8d, 'tStartRefresh')  # time at next scr refresh
            array_image_8d.setAutoDraw(True)
        if array_image_8d.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > array_image_8d.tStartRefresh + mem_display_duration_s-frameTolerance:
                # keep track of stop time/frame for later
                array_image_8d.tStop = t  # not accounting for scr refresh
                array_image_8d.frameNStop = frameN  # exact frame index
                win.timeOnFlip(array_image_8d, 'tStopRefresh')  # time at next scr refresh
                array_image_8d.setAutoDraw(False)
        
        # *polygon_26* updates
        if polygon_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_26.frameNStart = frameN  # exact frame index
            polygon_26.tStart = t  # local t and not account for scr refresh
            polygon_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_26, 'tStartRefresh')  # time at next scr refresh
            polygon_26.setAutoDraw(True)
        if polygon_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_26.tStartRefresh + mem_display_duration_s-frameTolerance:
                # keep track of stop time/frame for later
                polygon_26.tStop = t  # not accounting for scr refresh
                polygon_26.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_26, 'tStopRefresh')  # time at next scr refresh
                polygon_26.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_mem_displayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_mem_display"-------
    for thisComponent in practice_mem_displayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    mem_display_to_cue_duration_s=mem_display_to_cue_times_practice[practice_trial_index]
    
    if retro_0_post_1_practice[practice_trial_index]:
        mem_display_to_test_array_duration_s=mem_display_to_cue_duration_s-.1
        routine_duration_s=mem_display_to_cue_duration_s+cue_duration_s
        response_time_s = routine_duration_s - cue_duration_s
    else:
        mem_display_to_test_array_duration_s=mem_display_to_cue_duration_s+cue_duration_s+retention_duration_s
        routine_duration_s=mem_display_to_cue_duration_s+cue_duration_s+retention_duration_s
        response_time_s = routine_duration_s
    
    shuffle(image_index_list_for_shuffling)
    change_from_index_practice=image_index_list_for_shuffling[0]  #create a change_from_index, even when there is no change. So you have somewhere to point the pointer.
    
    image_index_list_in_order=list(range(0,num_images_per_display))
    
    change_or_no_practice=change_0_1_practice[practice_trial_index]
    if change_or_no_practice:
        change_to_index_practice=num_images_per_display
        image_index_list_in_order[change_from_index_practice]=change_to_index_practice
    
    thisExp.addData('retention_interval_practice',mem_display_to_cue_duration_s)
    thisExp.addData('retro_0_post_1_practice',retro_0_post_1_practice[practice_trial_index])
    thisExp.addData('change_or_no_practice',change_or_no_practice)
    thisExp.addData('cue_location_practice',change_from_index_practice)
    
    thisExp.addData('mem_display_to_test_array_duration_s',mem_display_to_test_array_duration_s)
    thisExp.addData('mem_display_to_cue_duration_s',mem_display_to_cue_duration_s)
    thisExp.addData('routine_duration_s',routine_duration_s)
    # the Routine "practice_mem_display" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "retention_cue_and_test_intval_practice_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    Image_1=all_pic_names_training[practice_trial_image_list[practice_trial_index][image_index_list_in_order[0]]]
    array_image_1f.setImage(Image_1, False)
    array_image_1f.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale), False)
    array_image_1f.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_2=all_pic_names_training[practice_trial_image_list[practice_trial_index][image_index_list_in_order[1]]]
    array_image_2f.setImage(Image_2, False)
    array_image_2f.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale), False)
    array_image_2f.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_3=all_pic_names_training[practice_trial_image_list[practice_trial_index][image_index_list_in_order[2]]]
    array_image_3f.setImage(Image_3, False)
    array_image_3f.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale), False)
    array_image_3f.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_4=all_pic_names_training[practice_trial_image_list[practice_trial_index][image_index_list_in_order[3]]]
    array_image_4f.setImage(Image_4, False)
    array_image_4f.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale), False)
    array_image_4f.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_5=all_pic_names_training[practice_trial_image_list[practice_trial_index][image_index_list_in_order[4]]]
    array_image_5f.setImage(Image_5, False)
    array_image_5f.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale), False)
    array_image_5f.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_6=all_pic_names_training[practice_trial_image_list[practice_trial_index][image_index_list_in_order[5]]]
    array_image_6f.setImage(Image_6, False)
    array_image_6f.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale), False)
    array_image_6f.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_7=all_pic_names_training[practice_trial_image_list[practice_trial_index][image_index_list_in_order[6]]]
    array_image_7f.setImage(Image_7, False)
    array_image_7f.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[6][1]*image_eccentr_cm*y_scale), False)
    array_image_7f.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    Image_8=all_pic_names_training[practice_trial_image_list[practice_trial_index][image_index_list_in_order[7]]]
    array_image_8f.setImage(Image_8, False)
    array_image_8f.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale), False)
    array_image_8f.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
    
    x_pointer_0=x_y_gains_per_angle[change_from_index_practice][0]*pointer_length_relative_to_image_eccentricity*image_eccentr_cm*x_scale
    y_pointer_0=x_y_gains_per_angle[change_from_index_practice][1]*pointer_length_relative_to_image_eccentricity*image_eccentr_cm*y_scale
    pointer_dot_0b.setPos((x_pointer_0, y_pointer_0), False)
    
    x_pointer_1=x_pointer_0*.66667
    y_pointer_1=y_pointer_0*.66667
    pointer_dot_1b.setPos((x_pointer_1, y_pointer_1), False)
    
    x_pointer_2=x_pointer_0*.33333
    y_pointer_2=y_pointer_0*.33333
    pointer_dot_2b.setPos((x_pointer_2, y_pointer_2), False)
    
    polygon_28.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
    array_image_1f.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale))
    array_image_1f.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_1f.setImage(Image_1)
    array_image_2f.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale))
    array_image_2f.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_2f.setImage(Image_2)
    array_image_3f.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale))
    array_image_3f.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_3f.setImage(Image_3)
    array_image_4f.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale))
    array_image_4f.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_4f.setImage(Image_4)
    array_image_5f.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale))
    array_image_5f.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_5f.setImage(Image_5)
    array_image_6f.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale))
    array_image_6f.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_6f.setImage(Image_6)
    array_image_7f.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[6][1]*image_eccentr_cm*y_scale))
    array_image_7f.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_7f.setImage(Image_7)
    array_image_8f.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale))
    array_image_8f.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
    array_image_8f.setImage(Image_8)
    pointer_dot_0b.setPos((x_pointer_0,y_pointer_0))
    pointer_dot_0b.setSize((dot_diam_dva*x_scale/2., dot_diam_dva*y_scale/2.))
    pointer_dot_1b.setPos((x_pointer_1,y_pointer_1))
    pointer_dot_1b.setSize((dot_diam_dva*x_scale/2., dot_diam_dva*y_scale/2.))
    pointer_dot_2b.setPos((x_pointer_2,y_pointer_2))
    pointer_dot_2b.setSize((dot_diam_dva*x_scale/2., dot_diam_dva*y_scale/2.))
    sd_practice_resp.keys = []
    sd_practice_resp.rt = []
    _sd_practice_resp_allKeys = []
    # keep track of which components have finished
    retention_cue_and_test_intval_practice_2Components = [polygon_28, array_image_1f, array_image_2f, array_image_3f, array_image_4f, array_image_5f, array_image_6f, array_image_7f, array_image_8f, pointer_dot_0b, pointer_dot_1b, pointer_dot_2b, sd_practice_resp]
    for thisComponent in retention_cue_and_test_intval_practice_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    retention_cue_and_test_intval_practice_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "retention_cue_and_test_intval_practice_2"-------
    while continueRoutine:
        # get current time
        t = retention_cue_and_test_intval_practice_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=retention_cue_and_test_intval_practice_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_28* updates
        if polygon_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_28.frameNStart = frameN  # exact frame index
            polygon_28.tStart = t  # local t and not account for scr refresh
            polygon_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_28, 'tStartRefresh')  # time at next scr refresh
            polygon_28.setAutoDraw(True)
        
        # *array_image_1f* updates
        if array_image_1f.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
            # keep track of start time/frame for later
            array_image_1f.frameNStart = frameN  # exact frame index
            array_image_1f.tStart = t  # local t and not account for scr refresh
            array_image_1f.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_1f, 'tStartRefresh')  # time at next scr refresh
            array_image_1f.setAutoDraw(True)
        
        # *array_image_2f* updates
        if array_image_2f.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
            # keep track of start time/frame for later
            array_image_2f.frameNStart = frameN  # exact frame index
            array_image_2f.tStart = t  # local t and not account for scr refresh
            array_image_2f.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_2f, 'tStartRefresh')  # time at next scr refresh
            array_image_2f.setAutoDraw(True)
        
        # *array_image_3f* updates
        if array_image_3f.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
            # keep track of start time/frame for later
            array_image_3f.frameNStart = frameN  # exact frame index
            array_image_3f.tStart = t  # local t and not account for scr refresh
            array_image_3f.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_3f, 'tStartRefresh')  # time at next scr refresh
            array_image_3f.setAutoDraw(True)
        
        # *array_image_4f* updates
        if array_image_4f.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
            # keep track of start time/frame for later
            array_image_4f.frameNStart = frameN  # exact frame index
            array_image_4f.tStart = t  # local t and not account for scr refresh
            array_image_4f.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_4f, 'tStartRefresh')  # time at next scr refresh
            array_image_4f.setAutoDraw(True)
        
        # *array_image_5f* updates
        if array_image_5f.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
            # keep track of start time/frame for later
            array_image_5f.frameNStart = frameN  # exact frame index
            array_image_5f.tStart = t  # local t and not account for scr refresh
            array_image_5f.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_5f, 'tStartRefresh')  # time at next scr refresh
            array_image_5f.setAutoDraw(True)
        
        # *array_image_6f* updates
        if array_image_6f.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
            # keep track of start time/frame for later
            array_image_6f.frameNStart = frameN  # exact frame index
            array_image_6f.tStart = t  # local t and not account for scr refresh
            array_image_6f.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_6f, 'tStartRefresh')  # time at next scr refresh
            array_image_6f.setAutoDraw(True)
        
        # *array_image_7f* updates
        if array_image_7f.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
            # keep track of start time/frame for later
            array_image_7f.frameNStart = frameN  # exact frame index
            array_image_7f.tStart = t  # local t and not account for scr refresh
            array_image_7f.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_7f, 'tStartRefresh')  # time at next scr refresh
            array_image_7f.setAutoDraw(True)
        
        # *array_image_8f* updates
        if array_image_8f.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
            # keep track of start time/frame for later
            array_image_8f.frameNStart = frameN  # exact frame index
            array_image_8f.tStart = t  # local t and not account for scr refresh
            array_image_8f.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(array_image_8f, 'tStartRefresh')  # time at next scr refresh
            array_image_8f.setAutoDraw(True)
        
        # *pointer_dot_0b* updates
        if pointer_dot_0b.status == NOT_STARTED and tThisFlip >= mem_display_to_cue_duration_s-frameTolerance:
            # keep track of start time/frame for later
            pointer_dot_0b.frameNStart = frameN  # exact frame index
            pointer_dot_0b.tStart = t  # local t and not account for scr refresh
            pointer_dot_0b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pointer_dot_0b, 'tStartRefresh')  # time at next scr refresh
            pointer_dot_0b.setAutoDraw(True)
        if pointer_dot_0b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pointer_dot_0b.tStartRefresh + cue_duration_s-frameTolerance:
                # keep track of stop time/frame for later
                pointer_dot_0b.tStop = t  # not accounting for scr refresh
                pointer_dot_0b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pointer_dot_0b, 'tStopRefresh')  # time at next scr refresh
                pointer_dot_0b.setAutoDraw(False)
        
        # *pointer_dot_1b* updates
        if pointer_dot_1b.status == NOT_STARTED and tThisFlip >= mem_display_to_cue_duration_s-frameTolerance:
            # keep track of start time/frame for later
            pointer_dot_1b.frameNStart = frameN  # exact frame index
            pointer_dot_1b.tStart = t  # local t and not account for scr refresh
            pointer_dot_1b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pointer_dot_1b, 'tStartRefresh')  # time at next scr refresh
            pointer_dot_1b.setAutoDraw(True)
        if pointer_dot_1b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pointer_dot_1b.tStartRefresh + cue_duration_s-frameTolerance:
                # keep track of stop time/frame for later
                pointer_dot_1b.tStop = t  # not accounting for scr refresh
                pointer_dot_1b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pointer_dot_1b, 'tStopRefresh')  # time at next scr refresh
                pointer_dot_1b.setAutoDraw(False)
        
        # *pointer_dot_2b* updates
        if pointer_dot_2b.status == NOT_STARTED and tThisFlip >= mem_display_to_cue_duration_s-frameTolerance:
            # keep track of start time/frame for later
            pointer_dot_2b.frameNStart = frameN  # exact frame index
            pointer_dot_2b.tStart = t  # local t and not account for scr refresh
            pointer_dot_2b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pointer_dot_2b, 'tStartRefresh')  # time at next scr refresh
            pointer_dot_2b.setAutoDraw(True)
        if pointer_dot_2b.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pointer_dot_2b.tStartRefresh + cue_duration_s-frameTolerance:
                # keep track of stop time/frame for later
                pointer_dot_2b.tStop = t  # not accounting for scr refresh
                pointer_dot_2b.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pointer_dot_2b, 'tStopRefresh')  # time at next scr refresh
                pointer_dot_2b.setAutoDraw(False)
        
        # *sd_practice_resp* updates
        waitOnFlip = False
        if sd_practice_resp.status == NOT_STARTED and tThisFlip >= response_time_s-frameTolerance:
            # keep track of start time/frame for later
            sd_practice_resp.frameNStart = frameN  # exact frame index
            sd_practice_resp.tStart = t  # local t and not account for scr refresh
            sd_practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_practice_resp, 'tStartRefresh')  # time at next scr refresh
            sd_practice_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sd_practice_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sd_practice_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sd_practice_resp.status == STARTED and not waitOnFlip:
            theseKeys = sd_practice_resp.getKeys(keyList=['6', '7'], waitRelease=False)
            _sd_practice_resp_allKeys.extend(theseKeys)
            if len(_sd_practice_resp_allKeys):
                sd_practice_resp.keys = _sd_practice_resp_allKeys[-1].name  # just the last key pressed
                sd_practice_resp.rt = _sd_practice_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in retention_cue_and_test_intval_practice_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "retention_cue_and_test_intval_practice_2"-------
    for thisComponent in retention_cue_and_test_intval_practice_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('array_image_1f.started', array_image_1f.tStartRefresh)
    trials.addData('array_image_1f.stopped', array_image_1f.tStopRefresh)
    trials.addData('array_image_2f.started', array_image_2f.tStartRefresh)
    trials.addData('array_image_2f.stopped', array_image_2f.tStopRefresh)
    trials.addData('array_image_3f.started', array_image_3f.tStartRefresh)
    trials.addData('array_image_3f.stopped', array_image_3f.tStopRefresh)
    trials.addData('array_image_4f.started', array_image_4f.tStartRefresh)
    trials.addData('array_image_4f.stopped', array_image_4f.tStopRefresh)
    trials.addData('array_image_5f.started', array_image_5f.tStartRefresh)
    trials.addData('array_image_5f.stopped', array_image_5f.tStopRefresh)
    trials.addData('array_image_6f.started', array_image_6f.tStartRefresh)
    trials.addData('array_image_6f.stopped', array_image_6f.tStopRefresh)
    trials.addData('array_image_7f.started', array_image_7f.tStartRefresh)
    trials.addData('array_image_7f.stopped', array_image_7f.tStopRefresh)
    trials.addData('array_image_8f.started', array_image_8f.tStartRefresh)
    trials.addData('array_image_8f.stopped', array_image_8f.tStopRefresh)
    trials.addData('pointer_dot_0b.started', pointer_dot_0b.tStartRefresh)
    trials.addData('pointer_dot_0b.stopped', pointer_dot_0b.tStopRefresh)
    trials.addData('pointer_dot_1b.started', pointer_dot_1b.tStartRefresh)
    trials.addData('pointer_dot_1b.stopped', pointer_dot_1b.tStopRefresh)
    trials.addData('pointer_dot_2b.started', pointer_dot_2b.tStartRefresh)
    trials.addData('pointer_dot_2b.stopped', pointer_dot_2b.tStopRefresh)
    # check responses
    if sd_practice_resp.keys in ['', [], None]:  # No response was made
        sd_practice_resp.keys = None
    trials.addData('sd_practice_resp.keys',sd_practice_resp.keys)
    if sd_practice_resp.keys != None:  # we had a response
        trials.addData('sd_practice_resp.rt', sd_practice_resp.rt)
    trials.addData('sd_practice_resp.started', sd_practice_resp.tStartRefresh)
    trials.addData('sd_practice_resp.stopped', sd_practice_resp.tStopRefresh)
    # the Routine "retention_cue_and_test_intval_practice_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "confidence_rating_practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    if practice_trial_index==0:
        confidence_reminder_text='Excellent. At this point, right after each Same/Different choice, you’re expected to indicate how confident you are that the choice you just made was correct.\n\nPlease use your left hand and use your ring finger if you are certain, your middle finger if you have some doubt, or your index finger if it was just a guess. See image below and make your response.'
    else:
        confidence_reminder_text='Don\'t forget: after each Same/Different choice, you should indicate how confident you are in the choice you just made.\n\nPlease use your left hand to press either ring finger (I\'m certain), middle finger (I have some doubt), or index finger (it was just a guess.)'
    text_10.setText(confidence_reminder_text,False)
    text_10.setText(confidence_reminder_text)
    conf_practice_resp.keys = []
    conf_practice_resp.rt = []
    _conf_practice_resp_allKeys = []
    # keep track of which components have finished
    confidence_rating_practiceComponents = [text_10, conf_practice_resp, image]
    for thisComponent in confidence_rating_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    confidence_rating_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "confidence_rating_practice"-------
    while continueRoutine:
        # get current time
        t = confidence_rating_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=confidence_rating_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= confidence_onset_time_s-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        
        # *conf_practice_resp* updates
        waitOnFlip = False
        if conf_practice_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            conf_practice_resp.frameNStart = frameN  # exact frame index
            conf_practice_resp.tStart = t  # local t and not account for scr refresh
            conf_practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(conf_practice_resp, 'tStartRefresh')  # time at next scr refresh
            conf_practice_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(conf_practice_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(conf_practice_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if conf_practice_resp.status == STARTED and not waitOnFlip:
            theseKeys = conf_practice_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _conf_practice_resp_allKeys.extend(theseKeys)
            if len(_conf_practice_resp_allKeys):
                conf_practice_resp.keys = _conf_practice_resp_allKeys[-1].name  # just the last key pressed
                conf_practice_resp.rt = _conf_practice_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in confidence_rating_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "confidence_rating_practice"-------
    for thisComponent in confidence_rating_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_trial_index = practice_trial_index + 1
    trials.addData('text_10.started', text_10.tStartRefresh)
    trials.addData('text_10.stopped', text_10.tStopRefresh)
    # check responses
    if conf_practice_resp.keys in ['', [], None]:  # No response was made
        conf_practice_resp.keys = None
    trials.addData('conf_practice_resp.keys',conf_practice_resp.keys)
    if conf_practice_resp.keys != None:  # we had a response
        trials.addData('conf_practice_resp.rt', conf_practice_resp.rt)
    trials.addData('conf_practice_resp.started', conf_practice_resp.tStartRefresh)
    trials.addData('conf_practice_resp.stopped', conf_practice_resp.tStopRefresh)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    # the Routine "confidence_rating_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed num_practice_trials repeats of 'trials'


# ------Prepare to start Routine "instruction_8"-------
continueRoutine = True
# update component parameters for each repeat
real_exp_text = 'Great. It is now time to move on to the real experiment. Your task will be exactly the same as during the practice trials you just completed, except that there will be no reminder texts anymore. Instead, you’ll just see the pictures and the red dotted line, and the experiment will automatically proceed to the next trial as soon as you’ve responded for same/different, and for your confidence.\n\nYou will, however, be given a break screen every ' + str(trials_per_block) + ' trials, to give you a breather.'

real_exp_text_2='There are ' + str(num_real_trials) + ' trials total.\n\nPlease press any key to begin.'
static_instruction_33.setText(real_exp_text)
subj_ready.keys = []
subj_ready.rt = []
_subj_ready_allKeys = []
static_instruction_34.setText(real_exp_text_2)
polygon_31.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
experimenter_ready.keys = []
experimenter_ready.rt = []
_experimenter_ready_allKeys = []
# keep track of which components have finished
instruction_8Components = [static_instruction_33, subj_ready, static_instruction_34, polygon_31, experimenter_ready, sub_ready]
for thisComponent in instruction_8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruction_8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruction_8"-------
while continueRoutine:
    # get current time
    t = instruction_8Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruction_8Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *static_instruction_33* updates
    if static_instruction_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_33.frameNStart = frameN  # exact frame index
        static_instruction_33.tStart = t  # local t and not account for scr refresh
        static_instruction_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_33, 'tStartRefresh')  # time at next scr refresh
        static_instruction_33.setAutoDraw(True)
    if static_instruction_33.status == STARTED:
        if bool(subj_ready.keys):
            # keep track of stop time/frame for later
            static_instruction_33.tStop = t  # not accounting for scr refresh
            static_instruction_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(static_instruction_33, 'tStopRefresh')  # time at next scr refresh
            static_instruction_33.setAutoDraw(False)
    
    # *subj_ready* updates
    waitOnFlip = False
    if subj_ready.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        subj_ready.frameNStart = frameN  # exact frame index
        subj_ready.tStart = t  # local t and not account for scr refresh
        subj_ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(subj_ready, 'tStartRefresh')  # time at next scr refresh
        subj_ready.status = STARTED
        # AllowedKeys looks like a variable named `responseButtons`
        if not type(responseButtons) in [list, tuple, np.ndarray]:
            if not isinstance(responseButtons, str):
                logging.error('AllowedKeys variable `responseButtons` is not string- or list-like.')
                core.quit()
            elif not ',' in responseButtons:
                responseButtons = (responseButtons,)
            else:
                responseButtons = eval(responseButtons)
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(subj_ready.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(subj_ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if subj_ready.status == STARTED:
        if bool(subj_ready.keys):
            # keep track of stop time/frame for later
            subj_ready.tStop = t  # not accounting for scr refresh
            subj_ready.frameNStop = frameN  # exact frame index
            win.timeOnFlip(subj_ready, 'tStopRefresh')  # time at next scr refresh
            subj_ready.status = FINISHED
    if subj_ready.status == STARTED and not waitOnFlip:
        theseKeys = subj_ready.getKeys(keyList=list(responseButtons), waitRelease=False)
        _subj_ready_allKeys.extend(theseKeys)
        if len(_subj_ready_allKeys):
            subj_ready.keys = _subj_ready_allKeys[0].name  # just the first key pressed
            subj_ready.rt = _subj_ready_allKeys[0].rt
    
    # *static_instruction_34* updates
    if static_instruction_34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        static_instruction_34.frameNStart = frameN  # exact frame index
        static_instruction_34.tStart = t  # local t and not account for scr refresh
        static_instruction_34.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(static_instruction_34, 'tStartRefresh')  # time at next scr refresh
        static_instruction_34.setAutoDraw(True)
    if static_instruction_34.status == STARTED:
        if bool(subj_ready.keys):
            # keep track of stop time/frame for later
            static_instruction_34.tStop = t  # not accounting for scr refresh
            static_instruction_34.frameNStop = frameN  # exact frame index
            win.timeOnFlip(static_instruction_34, 'tStopRefresh')  # time at next scr refresh
            static_instruction_34.setAutoDraw(False)
    
    # *polygon_31* updates
    if polygon_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_31.frameNStart = frameN  # exact frame index
        polygon_31.tStart = t  # local t and not account for scr refresh
        polygon_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_31, 'tStartRefresh')  # time at next scr refresh
        polygon_31.setAutoDraw(True)
    if polygon_31.status == STARTED:
        if bool(subj_ready.keys):
            # keep track of stop time/frame for later
            polygon_31.tStop = t  # not accounting for scr refresh
            polygon_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_31, 'tStopRefresh')  # time at next scr refresh
            polygon_31.setAutoDraw(False)
    
    # *experimenter_ready* updates
    waitOnFlip = False
    if experimenter_ready.status == NOT_STARTED and subj_ready.keys:
        # keep track of start time/frame for later
        experimenter_ready.frameNStart = frameN  # exact frame index
        experimenter_ready.tStart = t  # local t and not account for scr refresh
        experimenter_ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experimenter_ready, 'tStartRefresh')  # time at next scr refresh
        experimenter_ready.status = STARTED
        # AllowedKeys looks like a variable named `experimenterReadyButton`
        if not type(experimenterReadyButton) in [list, tuple, np.ndarray]:
            if not isinstance(experimenterReadyButton, str):
                logging.error('AllowedKeys variable `experimenterReadyButton` is not string- or list-like.')
                core.quit()
            elif not ',' in experimenterReadyButton:
                experimenterReadyButton = (experimenterReadyButton,)
            else:
                experimenterReadyButton = eval(experimenterReadyButton)
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(experimenter_ready.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(experimenter_ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if experimenter_ready.status == STARTED:
        if bool(experimenter_ready.keys):
            # keep track of stop time/frame for later
            experimenter_ready.tStop = t  # not accounting for scr refresh
            experimenter_ready.frameNStop = frameN  # exact frame index
            win.timeOnFlip(experimenter_ready, 'tStopRefresh')  # time at next scr refresh
            experimenter_ready.status = FINISHED
    if experimenter_ready.status == STARTED and not waitOnFlip:
        theseKeys = experimenter_ready.getKeys(keyList=list(experimenterReadyButton), waitRelease=False)
        _experimenter_ready_allKeys.extend(theseKeys)
        if len(_experimenter_ready_allKeys):
            experimenter_ready.keys = _experimenter_ready_allKeys[-1].name  # just the last key pressed
            experimenter_ready.rt = _experimenter_ready_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *sub_ready* updates
    if sub_ready.status == NOT_STARTED and subj_ready.keys:
        # keep track of start time/frame for later
        sub_ready.frameNStart = frameN  # exact frame index
        sub_ready.tStart = t  # local t and not account for scr refresh
        sub_ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sub_ready, 'tStartRefresh')  # time at next scr refresh
        sub_ready.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_8"-------
for thisComponent in instruction_8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if subj_ready.keys in ['', [], None]:  # No response was made
    subj_ready.keys = None
thisExp.addData('subj_ready.keys',subj_ready.keys)
if subj_ready.keys != None:  # we had a response
    thisExp.addData('subj_ready.rt', subj_ready.rt)
thisExp.nextEntry()
# check responses
if experimenter_ready.keys in ['', [], None]:  # No response was made
    experimenter_ready.keys = None
thisExp.addData('experimenter_ready.keys',experimenter_ready.keys)
if experimenter_ready.keys != None:  # we had a response
    thisExp.addData('experimenter_ready.rt', experimenter_ready.rt)
thisExp.addData('experimenter_ready.started', experimenter_ready.tStartRefresh)
thisExp.addData('experimenter_ready.stopped', experimenter_ready.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('sub_ready.started', sub_ready.tStartRefresh)
thisExp.addData('sub_ready.stopped', sub_ready.tStopRefresh)
# the Routine "instruction_8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
main_exp_blocks = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('main_exp_condFiles.xlsx'),
    seed=None, name='main_exp_blocks')
thisExp.addLoop(main_exp_blocks)  # add the loop to the experiment
thisMain_exp_block = main_exp_blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMain_exp_block.rgb)
if thisMain_exp_block != None:
    for paramName in thisMain_exp_block:
        exec('{} = thisMain_exp_block[paramName]'.format(paramName))

for thisMain_exp_block in main_exp_blocks:
    currentLoop = main_exp_blocks
    # abbreviate parameter names if possible (e.g. rgb = thisMain_exp_block.rgb)
    if thisMain_exp_block != None:
        for paramName in thisMain_exp_block:
            exec('{} = thisMain_exp_block[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_7 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condFile),
        seed=None, name='trials_7')
    thisExp.addLoop(trials_7)  # add the loop to the experiment
    thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7:
            exec('{} = thisTrial_7[paramName]'.format(paramName))
    
    for thisTrial_7 in trials_7:
        currentLoop = trials_7
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
        if thisTrial_7 != None:
            for paramName in thisTrial_7:
                exec('{} = thisTrial_7[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "load_real_trials"-------
        continueRoutine = True
        # update component parameters for each repeat
        real_trial_image_list.append([Used_image_1,Used_image_2,Used_image_3,Used_image_4,Used_image_5,Used_image_6,Used_image_7,Used_image_8,Unused_image_1,Unused_image_2])
        retro_0_post_1_real.append(Retro_post_0_1)
        change_0_1_real.append(Change_yes_no)
        retint_s.append(Ret_int)
        
        thisExp.addData('DataFile',condFile)
        
        # keep track of which components have finished
        load_real_trialsComponents = []
        for thisComponent in load_real_trialsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        load_real_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "load_real_trials"-------
        while continueRoutine:
            # get current time
            t = load_real_trialsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=load_real_trialsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in load_real_trialsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "load_real_trials"-------
        for thisComponent in load_real_trialsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial_load_number=trial_load_number+1
        
        if trial_load_number>=num_real_trials:
            trials_7.finished = True
            real_trial_index=0
        # the Routine "load_real_trials" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1 repeats of 'trials_7'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_8 = data.TrialHandler(nReps=trials_per_block, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_8')
    thisExp.addLoop(trials_8)  # add the loop to the experiment
    thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8:
            exec('{} = thisTrial_8[paramName]'.format(paramName))
    
    for thisTrial_8 in trials_8:
        currentLoop = trials_8
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
        if thisTrial_8 != None:
            for paramName in thisTrial_8:
                exec('{} = thisTrial_8[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "TR_sync"-------
        continueRoutine = True
        # update component parameters for each repeat
        wait_for_TR.keys = []
        wait_for_TR.rt = []
        _wait_for_TR_allKeys = []
        polygon_2.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
        # keep track of which components have finished
        TR_syncComponents = [wait_for_TR, polygon_2]
        for thisComponent in TR_syncComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TR_syncClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TR_sync"-------
        while continueRoutine:
            # get current time
            t = TR_syncClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TR_syncClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *wait_for_TR* updates
            if wait_for_TR.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                wait_for_TR.frameNStart = frameN  # exact frame index
                wait_for_TR.tStart = t  # local t and not account for scr refresh
                wait_for_TR.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wait_for_TR, 'tStartRefresh')  # time at next scr refresh
                wait_for_TR.status = STARTED
                # AllowedKeys looks like a variable named `scannerTRbutton`
                if not type(scannerTRbutton) in [list, tuple, np.ndarray]:
                    if not isinstance(scannerTRbutton, str):
                        logging.error('AllowedKeys variable `scannerTRbutton` is not string- or list-like.')
                        core.quit()
                    elif not ',' in scannerTRbutton:
                        scannerTRbutton = (scannerTRbutton,)
                    else:
                        scannerTRbutton = eval(scannerTRbutton)
                # keyboard checking is just starting
                wait_for_TR.clock.reset()  # now t=0
                wait_for_TR.clearEvents(eventType='keyboard')
            if wait_for_TR.status == STARTED:
                theseKeys = wait_for_TR.getKeys(keyList=list(scannerTRbutton), waitRelease=False)
                _wait_for_TR_allKeys.extend(theseKeys)
                if len(_wait_for_TR_allKeys):
                    wait_for_TR.keys = _wait_for_TR_allKeys[-1].name  # just the last key pressed
                    wait_for_TR.rt = _wait_for_TR_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *polygon_2* updates
            if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_2.frameNStart = frameN  # exact frame index
                polygon_2.tStart = t  # local t and not account for scr refresh
                polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TR_syncComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TR_sync"-------
        for thisComponent in TR_syncComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if wait_for_TR.keys in ['', [], None]:  # No response was made
            wait_for_TR.keys = None
        trials_8.addData('wait_for_TR.keys',wait_for_TR.keys)
        if wait_for_TR.keys != None:  # we had a response
            trials_8.addData('wait_for_TR.rt', wait_for_TR.rt)
        trials_8.addData('wait_for_TR.started', wait_for_TR.tStart)
        trials_8.addData('wait_for_TR.stopped', wait_for_TR.tStop)
        trials_8.addData('polygon_2.started', polygon_2.tStartRefresh)
        trials_8.addData('polygon_2.stopped', polygon_2.tStopRefresh)
        # the Routine "TR_sync" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "real_mem_display"-------
        continueRoutine = True
        # update component parameters for each repeat
        Image_1=all_pic_names[real_trial_image_list[real_trial_index][0]]
        array_image_1h.setImage(Image_1, False)
        array_image_1h.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale), False)
        array_image_1h.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_2=all_pic_names[real_trial_image_list[real_trial_index][1]]
        array_image_2h.setImage(Image_2, False)
        array_image_2h.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale), False)
        array_image_2h.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_3=all_pic_names[real_trial_image_list[real_trial_index][2]]
        array_image_3h.setImage(Image_3, False)
        array_image_3h.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale), False)
        array_image_3h.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_4=all_pic_names[real_trial_image_list[real_trial_index][3]]
        array_image_4h.setImage(Image_4, False)
        array_image_4h.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale), False)
        array_image_4h.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_5=all_pic_names[real_trial_image_list[real_trial_index][4]]
        array_image_5h.setImage(Image_5, False)
        array_image_5h.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale), False)
        array_image_5h.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_6=all_pic_names[real_trial_image_list[real_trial_index][5]]
        array_image_6h.setImage(Image_6, False)
        array_image_6h.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale), False)
        array_image_6h.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_7=all_pic_names[real_trial_image_list[real_trial_index][6]]
        array_image_7h.setImage(Image_7, False)
        array_image_7h.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[6][1]*image_eccentr_cm*y_scale), False)
        array_image_7h.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_8=all_pic_names[real_trial_image_list[real_trial_index][7]]
        array_image_8h.setImage(Image_8, False)
        array_image_8h.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale), False)
        array_image_8h.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        thisExp.addData('memDisplayOnTime',timer.getTime())
        #storing variables specifying trial
        for image_index in range(8):
            thisExp.addData('mem_image_'+str(image_index)+'_real',real_trial_image_list[real_trial_index][image_index])
        
        array_image_1h.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale))
        array_image_1h.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_1h.setImage(Image_1)
        array_image_2h.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale))
        array_image_2h.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_2h.setImage(Image_2)
        array_image_3h.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale))
        array_image_3h.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_3h.setImage(Image_3)
        array_image_4h.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale))
        array_image_4h.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_4h.setImage(Image_4)
        array_image_5h.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale))
        array_image_5h.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_5h.setImage(Image_5)
        array_image_6h.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale))
        array_image_6h.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_6h.setImage(Image_6)
        array_image_7h.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[6][1]*image_eccentr_cm*y_scale))
        array_image_7h.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_7h.setImage(Image_7)
        array_image_8h.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale))
        array_image_8h.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_8h.setImage(Image_8)
        polygon_33.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
        # keep track of which components have finished
        real_mem_displayComponents = [array_image_1h, array_image_2h, array_image_3h, array_image_4h, array_image_5h, array_image_6h, array_image_7h, array_image_8h, polygon_33]
        for thisComponent in real_mem_displayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        real_mem_displayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "real_mem_display"-------
        while continueRoutine:
            # get current time
            t = real_mem_displayClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=real_mem_displayClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *array_image_1h* updates
            if array_image_1h.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                array_image_1h.frameNStart = frameN  # exact frame index
                array_image_1h.tStart = t  # local t and not account for scr refresh
                array_image_1h.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_1h, 'tStartRefresh')  # time at next scr refresh
                array_image_1h.setAutoDraw(True)
            if array_image_1h.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > array_image_1h.tStartRefresh + mem_display_duration_s-frameTolerance:
                    # keep track of stop time/frame for later
                    array_image_1h.tStop = t  # not accounting for scr refresh
                    array_image_1h.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(array_image_1h, 'tStopRefresh')  # time at next scr refresh
                    array_image_1h.setAutoDraw(False)
            
            # *array_image_2h* updates
            if array_image_2h.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                array_image_2h.frameNStart = frameN  # exact frame index
                array_image_2h.tStart = t  # local t and not account for scr refresh
                array_image_2h.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_2h, 'tStartRefresh')  # time at next scr refresh
                array_image_2h.setAutoDraw(True)
            if array_image_2h.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > array_image_2h.tStartRefresh + mem_display_duration_s-frameTolerance:
                    # keep track of stop time/frame for later
                    array_image_2h.tStop = t  # not accounting for scr refresh
                    array_image_2h.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(array_image_2h, 'tStopRefresh')  # time at next scr refresh
                    array_image_2h.setAutoDraw(False)
            
            # *array_image_3h* updates
            if array_image_3h.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                array_image_3h.frameNStart = frameN  # exact frame index
                array_image_3h.tStart = t  # local t and not account for scr refresh
                array_image_3h.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_3h, 'tStartRefresh')  # time at next scr refresh
                array_image_3h.setAutoDraw(True)
            if array_image_3h.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > array_image_3h.tStartRefresh + mem_display_duration_s-frameTolerance:
                    # keep track of stop time/frame for later
                    array_image_3h.tStop = t  # not accounting for scr refresh
                    array_image_3h.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(array_image_3h, 'tStopRefresh')  # time at next scr refresh
                    array_image_3h.setAutoDraw(False)
            
            # *array_image_4h* updates
            if array_image_4h.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                array_image_4h.frameNStart = frameN  # exact frame index
                array_image_4h.tStart = t  # local t and not account for scr refresh
                array_image_4h.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_4h, 'tStartRefresh')  # time at next scr refresh
                array_image_4h.setAutoDraw(True)
            if array_image_4h.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > array_image_4h.tStartRefresh + mem_display_duration_s-frameTolerance:
                    # keep track of stop time/frame for later
                    array_image_4h.tStop = t  # not accounting for scr refresh
                    array_image_4h.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(array_image_4h, 'tStopRefresh')  # time at next scr refresh
                    array_image_4h.setAutoDraw(False)
            
            # *array_image_5h* updates
            if array_image_5h.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                array_image_5h.frameNStart = frameN  # exact frame index
                array_image_5h.tStart = t  # local t and not account for scr refresh
                array_image_5h.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_5h, 'tStartRefresh')  # time at next scr refresh
                array_image_5h.setAutoDraw(True)
            if array_image_5h.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > array_image_5h.tStartRefresh + mem_display_duration_s-frameTolerance:
                    # keep track of stop time/frame for later
                    array_image_5h.tStop = t  # not accounting for scr refresh
                    array_image_5h.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(array_image_5h, 'tStopRefresh')  # time at next scr refresh
                    array_image_5h.setAutoDraw(False)
            
            # *array_image_6h* updates
            if array_image_6h.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                array_image_6h.frameNStart = frameN  # exact frame index
                array_image_6h.tStart = t  # local t and not account for scr refresh
                array_image_6h.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_6h, 'tStartRefresh')  # time at next scr refresh
                array_image_6h.setAutoDraw(True)
            if array_image_6h.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > array_image_6h.tStartRefresh + mem_display_duration_s-frameTolerance:
                    # keep track of stop time/frame for later
                    array_image_6h.tStop = t  # not accounting for scr refresh
                    array_image_6h.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(array_image_6h, 'tStopRefresh')  # time at next scr refresh
                    array_image_6h.setAutoDraw(False)
            
            # *array_image_7h* updates
            if array_image_7h.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                array_image_7h.frameNStart = frameN  # exact frame index
                array_image_7h.tStart = t  # local t and not account for scr refresh
                array_image_7h.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_7h, 'tStartRefresh')  # time at next scr refresh
                array_image_7h.setAutoDraw(True)
            if array_image_7h.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > array_image_7h.tStartRefresh + mem_display_duration_s-frameTolerance:
                    # keep track of stop time/frame for later
                    array_image_7h.tStop = t  # not accounting for scr refresh
                    array_image_7h.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(array_image_7h, 'tStopRefresh')  # time at next scr refresh
                    array_image_7h.setAutoDraw(False)
            
            # *array_image_8h* updates
            if array_image_8h.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                array_image_8h.frameNStart = frameN  # exact frame index
                array_image_8h.tStart = t  # local t and not account for scr refresh
                array_image_8h.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_8h, 'tStartRefresh')  # time at next scr refresh
                array_image_8h.setAutoDraw(True)
            if array_image_8h.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > array_image_8h.tStartRefresh + mem_display_duration_s-frameTolerance:
                    # keep track of stop time/frame for later
                    array_image_8h.tStop = t  # not accounting for scr refresh
                    array_image_8h.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(array_image_8h, 'tStopRefresh')  # time at next scr refresh
                    array_image_8h.setAutoDraw(False)
            
            # *polygon_33* updates
            if polygon_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_33.frameNStart = frameN  # exact frame index
                polygon_33.tStart = t  # local t and not account for scr refresh
                polygon_33.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_33, 'tStartRefresh')  # time at next scr refresh
                polygon_33.setAutoDraw(True)
            if polygon_33.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_33.tStartRefresh + mem_display_duration_s-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_33.tStop = t  # not accounting for scr refresh
                    polygon_33.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon_33, 'tStopRefresh')  # time at next scr refresh
                    polygon_33.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in real_mem_displayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "real_mem_display"-------
        for thisComponent in real_mem_displayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ret_int = retint_s[real_trial_index]
        mem_display_to_cue_duration_s=ret_int
        
        if retro_0_post_1_real[real_trial_index]:
            mem_display_to_test_array_duration_s=mem_display_to_cue_duration_s-.1
            routine_duration_s=mem_display_to_cue_duration_s+cue_duration_s
            response_time_s = routine_duration_s-cue_duration_s
        else:
            mem_display_to_test_array_duration_s=mem_display_to_cue_duration_s+cue_duration_s+retention_duration_s
            routine_duration_s=mem_display_to_cue_duration_s+cue_duration_s+retention_duration_s
            response_time_s = routine_duration_s
        
        shuffle(image_index_list_for_shuffling)
        change_from_index_real=image_index_list_for_shuffling[0]  #create a change_from_index, even when there is no change. So you have somewhere to point the pointer.
        
        image_index_list_in_order=list(range(0,num_images_per_display))
        
        change_or_no_real=change_0_1_real[real_trial_index]
        if change_or_no_real:
            change_to_index_real=num_images_per_display
            image_index_list_in_order[change_from_index_real]=change_to_index_real
        
        thisExp.addData('retention_interval_real',mem_display_to_cue_duration_s)
        thisExp.addData('retro_0_post_1_real',retro_0_post_1_real[real_trial_index])
        thisExp.addData('change_or_no_real',change_or_no_real)
        thisExp.addData('cue_location_real',change_from_index_real)
        thisExp.addData('ret_int_real',ret_int)
        
        trials_8.addData('array_image_1h.started', array_image_1h.tStartRefresh)
        trials_8.addData('array_image_1h.stopped', array_image_1h.tStopRefresh)
        # the Routine "real_mem_display" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "retention_cue_and_test_intval_real"-------
        continueRoutine = True
        # update component parameters for each repeat
        polygon_34.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
        sd_time_start = expClock.getTime() + response_time_s
        
        Image_1=all_pic_names[real_trial_image_list[real_trial_index][image_index_list_in_order[0]]]
        array_image_1j.setImage(Image_1, False)
        array_image_1j.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale), False)
        array_image_1j.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_2=all_pic_names[real_trial_image_list[real_trial_index][image_index_list_in_order[1]]]
        array_image_2j.setImage(Image_2, False)
        array_image_2j.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale), False)
        array_image_2j.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_3=all_pic_names[real_trial_image_list[real_trial_index][image_index_list_in_order[2]]]
        array_image_3j.setImage(Image_3, False)
        array_image_3j.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale), False)
        array_image_3j.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_4=all_pic_names[real_trial_image_list[real_trial_index][image_index_list_in_order[3]]]
        array_image_4j.setImage(Image_4, False)
        array_image_4j.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale), False)
        array_image_4j.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_5=all_pic_names[real_trial_image_list[real_trial_index][image_index_list_in_order[4]]]
        array_image_5j.setImage(Image_5, False)
        array_image_5j.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale), False)
        array_image_5j.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_6=all_pic_names[real_trial_image_list[real_trial_index][image_index_list_in_order[5]]]
        array_image_6j.setImage(Image_6, False)
        array_image_6j.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale), False)
        array_image_6j.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_7=all_pic_names[real_trial_image_list[real_trial_index][image_index_list_in_order[6]]]
        array_image_7j.setImage(Image_7, False)
        array_image_7j.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[6][1]*image_eccentr_cm*y_scale), False)
        array_image_7j.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        Image_8=all_pic_names[real_trial_image_list[real_trial_index][image_index_list_in_order[7]]]
        array_image_8j.setImage(Image_8, False)
        array_image_8j.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale), False)
        array_image_8j.setSize((image_side_cm*x_scale,image_side_cm*y_scale),False)
        
        x_pointer_0=x_y_gains_per_angle[change_from_index_real][0]*pointer_length_relative_to_image_eccentricity*image_eccentr_cm*x_scale
        y_pointer_0=x_y_gains_per_angle[change_from_index_real][1]*pointer_length_relative_to_image_eccentricity*image_eccentr_cm*y_scale
        pointer_dot_0c.setPos((x_pointer_0, y_pointer_0), False)
        
        x_pointer_1=x_pointer_0*.66667
        y_pointer_1=y_pointer_0*.66667
        pointer_dot_1c.setPos((x_pointer_1, y_pointer_1), False)
        
        x_pointer_2=x_pointer_0*.33333
        y_pointer_2=y_pointer_0*.33333
        pointer_dot_2c.setPos((x_pointer_2, y_pointer_2), False)
        
        array_image_1j.setPos((x_y_gains_per_angle[0][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[0][1]*image_eccentr_cm*y_scale))
        array_image_1j.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_1j.setImage(Image_1)
        array_image_2j.setPos((x_y_gains_per_angle[1][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[1][1]*image_eccentr_cm*y_scale))
        array_image_2j.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_2j.setImage(Image_2)
        array_image_3j.setPos((x_y_gains_per_angle[2][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[2][1]*image_eccentr_cm*y_scale))
        array_image_3j.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_3j.setImage(Image_3)
        array_image_4j.setPos((x_y_gains_per_angle[3][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[3][1]*image_eccentr_cm*y_scale))
        array_image_4j.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_4j.setImage(Image_4)
        array_image_5j.setPos((x_y_gains_per_angle[4][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[4][1]*image_eccentr_cm*y_scale))
        array_image_5j.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_5j.setImage(Image_5)
        array_image_6j.setPos((x_y_gains_per_angle[5][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[5][1]*image_eccentr_cm*y_scale))
        array_image_6j.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_6j.setImage(Image_6)
        array_image_7j.setPos((x_y_gains_per_angle[6][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[6][1]*image_eccentr_cm*y_scale))
        array_image_7j.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_7j.setImage(Image_7)
        array_image_8j.setPos((x_y_gains_per_angle[7][0]*image_eccentr_cm*x_scale, x_y_gains_per_angle[7][1]*image_eccentr_cm*y_scale))
        array_image_8j.setSize((image_side_cm*x_scale,image_side_cm*y_scale))
        array_image_8j.setImage(Image_8)
        pointer_dot_0c.setPos((x_pointer_0,y_pointer_0))
        pointer_dot_0c.setSize((dot_diam_dva*x_scale/2., dot_diam_dva*y_scale/2.))
        pointer_dot_1c.setPos((x_pointer_1,y_pointer_1))
        pointer_dot_1c.setSize((dot_diam_dva*x_scale/2., dot_diam_dva*y_scale/2.))
        pointer_dot_2c.setPos((x_pointer_2,y_pointer_2))
        pointer_dot_2c.setSize((dot_diam_dva*x_scale/2., dot_diam_dva*y_scale/2.))
        sd_resp_real.keys = []
        sd_resp_real.rt = []
        _sd_resp_real_allKeys = []
        # keep track of which components have finished
        retention_cue_and_test_intval_realComponents = [polygon_34, array_image_1j, array_image_2j, array_image_3j, array_image_4j, array_image_5j, array_image_6j, array_image_7j, array_image_8j, pointer_dot_0c, pointer_dot_1c, pointer_dot_2c, sd_resp_real]
        for thisComponent in retention_cue_and_test_intval_realComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        retention_cue_and_test_intval_realClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "retention_cue_and_test_intval_real"-------
        while continueRoutine:
            # get current time
            t = retention_cue_and_test_intval_realClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=retention_cue_and_test_intval_realClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_34* updates
            if polygon_34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_34.frameNStart = frameN  # exact frame index
                polygon_34.tStart = t  # local t and not account for scr refresh
                polygon_34.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_34, 'tStartRefresh')  # time at next scr refresh
                polygon_34.setAutoDraw(True)
            currTime = expClock.getTime()
            
            if currTime >= sd_time_start + max_duration_sd:
                continueRoutine = False
            
            # *array_image_1j* updates
            if array_image_1j.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
                # keep track of start time/frame for later
                array_image_1j.frameNStart = frameN  # exact frame index
                array_image_1j.tStart = t  # local t and not account for scr refresh
                array_image_1j.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_1j, 'tStartRefresh')  # time at next scr refresh
                array_image_1j.setAutoDraw(True)
            
            # *array_image_2j* updates
            if array_image_2j.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
                # keep track of start time/frame for later
                array_image_2j.frameNStart = frameN  # exact frame index
                array_image_2j.tStart = t  # local t and not account for scr refresh
                array_image_2j.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_2j, 'tStartRefresh')  # time at next scr refresh
                array_image_2j.setAutoDraw(True)
            
            # *array_image_3j* updates
            if array_image_3j.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
                # keep track of start time/frame for later
                array_image_3j.frameNStart = frameN  # exact frame index
                array_image_3j.tStart = t  # local t and not account for scr refresh
                array_image_3j.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_3j, 'tStartRefresh')  # time at next scr refresh
                array_image_3j.setAutoDraw(True)
            
            # *array_image_4j* updates
            if array_image_4j.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
                # keep track of start time/frame for later
                array_image_4j.frameNStart = frameN  # exact frame index
                array_image_4j.tStart = t  # local t and not account for scr refresh
                array_image_4j.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_4j, 'tStartRefresh')  # time at next scr refresh
                array_image_4j.setAutoDraw(True)
            
            # *array_image_5j* updates
            if array_image_5j.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
                # keep track of start time/frame for later
                array_image_5j.frameNStart = frameN  # exact frame index
                array_image_5j.tStart = t  # local t and not account for scr refresh
                array_image_5j.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_5j, 'tStartRefresh')  # time at next scr refresh
                array_image_5j.setAutoDraw(True)
            
            # *array_image_6j* updates
            if array_image_6j.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
                # keep track of start time/frame for later
                array_image_6j.frameNStart = frameN  # exact frame index
                array_image_6j.tStart = t  # local t and not account for scr refresh
                array_image_6j.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_6j, 'tStartRefresh')  # time at next scr refresh
                array_image_6j.setAutoDraw(True)
            
            # *array_image_7j* updates
            if array_image_7j.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
                # keep track of start time/frame for later
                array_image_7j.frameNStart = frameN  # exact frame index
                array_image_7j.tStart = t  # local t and not account for scr refresh
                array_image_7j.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_7j, 'tStartRefresh')  # time at next scr refresh
                array_image_7j.setAutoDraw(True)
            
            # *array_image_8j* updates
            if array_image_8j.status == NOT_STARTED and tThisFlip >= mem_display_to_test_array_duration_s-frameTolerance:
                # keep track of start time/frame for later
                array_image_8j.frameNStart = frameN  # exact frame index
                array_image_8j.tStart = t  # local t and not account for scr refresh
                array_image_8j.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(array_image_8j, 'tStartRefresh')  # time at next scr refresh
                array_image_8j.setAutoDraw(True)
            
            # *pointer_dot_0c* updates
            if pointer_dot_0c.status == NOT_STARTED and tThisFlip >= mem_display_to_cue_duration_s-frameTolerance:
                # keep track of start time/frame for later
                pointer_dot_0c.frameNStart = frameN  # exact frame index
                pointer_dot_0c.tStart = t  # local t and not account for scr refresh
                pointer_dot_0c.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pointer_dot_0c, 'tStartRefresh')  # time at next scr refresh
                pointer_dot_0c.setAutoDraw(True)
            if pointer_dot_0c.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pointer_dot_0c.tStartRefresh + cue_duration_s-frameTolerance:
                    # keep track of stop time/frame for later
                    pointer_dot_0c.tStop = t  # not accounting for scr refresh
                    pointer_dot_0c.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(pointer_dot_0c, 'tStopRefresh')  # time at next scr refresh
                    pointer_dot_0c.setAutoDraw(False)
            
            # *pointer_dot_1c* updates
            if pointer_dot_1c.status == NOT_STARTED and tThisFlip >= mem_display_to_cue_duration_s-frameTolerance:
                # keep track of start time/frame for later
                pointer_dot_1c.frameNStart = frameN  # exact frame index
                pointer_dot_1c.tStart = t  # local t and not account for scr refresh
                pointer_dot_1c.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pointer_dot_1c, 'tStartRefresh')  # time at next scr refresh
                pointer_dot_1c.setAutoDraw(True)
            if pointer_dot_1c.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pointer_dot_1c.tStartRefresh + cue_duration_s-frameTolerance:
                    # keep track of stop time/frame for later
                    pointer_dot_1c.tStop = t  # not accounting for scr refresh
                    pointer_dot_1c.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(pointer_dot_1c, 'tStopRefresh')  # time at next scr refresh
                    pointer_dot_1c.setAutoDraw(False)
            
            # *pointer_dot_2c* updates
            if pointer_dot_2c.status == NOT_STARTED and tThisFlip >= mem_display_to_cue_duration_s-frameTolerance:
                # keep track of start time/frame for later
                pointer_dot_2c.frameNStart = frameN  # exact frame index
                pointer_dot_2c.tStart = t  # local t and not account for scr refresh
                pointer_dot_2c.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pointer_dot_2c, 'tStartRefresh')  # time at next scr refresh
                pointer_dot_2c.setAutoDraw(True)
            if pointer_dot_2c.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pointer_dot_2c.tStartRefresh + cue_duration_s-frameTolerance:
                    # keep track of stop time/frame for later
                    pointer_dot_2c.tStop = t  # not accounting for scr refresh
                    pointer_dot_2c.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(pointer_dot_2c, 'tStopRefresh')  # time at next scr refresh
                    pointer_dot_2c.setAutoDraw(False)
            
            # *sd_resp_real* updates
            waitOnFlip = False
            if sd_resp_real.status == NOT_STARTED and tThisFlip >= response_time_s-frameTolerance:
                # keep track of start time/frame for later
                sd_resp_real.frameNStart = frameN  # exact frame index
                sd_resp_real.tStart = t  # local t and not account for scr refresh
                sd_resp_real.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sd_resp_real, 'tStartRefresh')  # time at next scr refresh
                sd_resp_real.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(sd_resp_real.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(sd_resp_real.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if sd_resp_real.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sd_resp_real.tStartRefresh + max_duration_sd-frameTolerance:
                    # keep track of stop time/frame for later
                    sd_resp_real.tStop = t  # not accounting for scr refresh
                    sd_resp_real.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(sd_resp_real, 'tStopRefresh')  # time at next scr refresh
                    sd_resp_real.status = FINISHED
            if sd_resp_real.status == STARTED and not waitOnFlip:
                theseKeys = sd_resp_real.getKeys(keyList=['6', '7'], waitRelease=False)
                _sd_resp_real_allKeys.extend(theseKeys)
                if len(_sd_resp_real_allKeys):
                    sd_resp_real.keys = _sd_resp_real_allKeys[-1].name  # just the last key pressed
                    sd_resp_real.rt = _sd_resp_real_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in retention_cue_and_test_intval_realComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "retention_cue_and_test_intval_real"-------
        for thisComponent in retention_cue_and_test_intval_realComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_8.addData('array_image_1j.started', array_image_1j.tStartRefresh)
        trials_8.addData('array_image_1j.stopped', array_image_1j.tStopRefresh)
        trials_8.addData('array_image_2j.started', array_image_2j.tStartRefresh)
        trials_8.addData('array_image_2j.stopped', array_image_2j.tStopRefresh)
        trials_8.addData('array_image_3j.started', array_image_3j.tStartRefresh)
        trials_8.addData('array_image_3j.stopped', array_image_3j.tStopRefresh)
        trials_8.addData('array_image_4j.started', array_image_4j.tStartRefresh)
        trials_8.addData('array_image_4j.stopped', array_image_4j.tStopRefresh)
        trials_8.addData('array_image_5j.started', array_image_5j.tStartRefresh)
        trials_8.addData('array_image_5j.stopped', array_image_5j.tStopRefresh)
        trials_8.addData('array_image_6j.started', array_image_6j.tStartRefresh)
        trials_8.addData('array_image_6j.stopped', array_image_6j.tStopRefresh)
        trials_8.addData('array_image_7j.started', array_image_7j.tStartRefresh)
        trials_8.addData('array_image_7j.stopped', array_image_7j.tStopRefresh)
        trials_8.addData('array_image_8j.started', array_image_8j.tStartRefresh)
        trials_8.addData('array_image_8j.stopped', array_image_8j.tStopRefresh)
        trials_8.addData('pointer_dot_0c.started', pointer_dot_0c.tStartRefresh)
        trials_8.addData('pointer_dot_0c.stopped', pointer_dot_0c.tStopRefresh)
        trials_8.addData('pointer_dot_1c.started', pointer_dot_1c.tStartRefresh)
        trials_8.addData('pointer_dot_1c.stopped', pointer_dot_1c.tStopRefresh)
        trials_8.addData('pointer_dot_2c.started', pointer_dot_2c.tStartRefresh)
        trials_8.addData('pointer_dot_2c.stopped', pointer_dot_2c.tStopRefresh)
        # check responses
        if sd_resp_real.keys in ['', [], None]:  # No response was made
            sd_resp_real.keys = None
        trials_8.addData('sd_resp_real.keys',sd_resp_real.keys)
        if sd_resp_real.keys != None:  # we had a response
            trials_8.addData('sd_resp_real.rt', sd_resp_real.rt)
        trials_8.addData('sd_resp_real.started', sd_resp_real.tStartRefresh)
        trials_8.addData('sd_resp_real.stopped', sd_resp_real.tStopRefresh)
        # the Routine "retention_cue_and_test_intval_real" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "confidence_rating_real_2"-------
        continueRoutine = True
        # update component parameters for each repeat
        elapsed_response_time = expClock.getTime() - sd_time_start
        
        remaining_response_time = max_response_time - min_iti - elapsed_response_time
        conf_real_resp.keys = []
        conf_real_resp.rt = []
        _conf_real_resp_allKeys = []
        # keep track of which components have finished
        confidence_rating_real_2Components = [conf_real_resp]
        for thisComponent in confidence_rating_real_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        confidence_rating_real_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "confidence_rating_real_2"-------
        while continueRoutine:
            # get current time
            t = confidence_rating_real_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=confidence_rating_real_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *conf_real_resp* updates
            waitOnFlip = False
            if conf_real_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                conf_real_resp.frameNStart = frameN  # exact frame index
                conf_real_resp.tStart = t  # local t and not account for scr refresh
                conf_real_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(conf_real_resp, 'tStartRefresh')  # time at next scr refresh
                conf_real_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(conf_real_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(conf_real_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if conf_real_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > conf_real_resp.tStartRefresh + remaining_response_time-frameTolerance:
                    # keep track of stop time/frame for later
                    conf_real_resp.tStop = t  # not accounting for scr refresh
                    conf_real_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(conf_real_resp, 'tStopRefresh')  # time at next scr refresh
                    conf_real_resp.status = FINISHED
            if conf_real_resp.status == STARTED and not waitOnFlip:
                theseKeys = conf_real_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _conf_real_resp_allKeys.extend(theseKeys)
                if len(_conf_real_resp_allKeys):
                    conf_real_resp.keys = _conf_real_resp_allKeys[-1].name  # just the last key pressed
                    conf_real_resp.rt = _conf_real_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in confidence_rating_real_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "confidence_rating_real_2"-------
        for thisComponent in confidence_rating_real_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('real_trial_index',real_trial_index)
        real_trial_index = real_trial_index + 1
        
        if (real_trial_index>=num_real_trials):
            trials_8.finished = True
        # check responses
        if conf_real_resp.keys in ['', [], None]:  # No response was made
            conf_real_resp.keys = None
        trials_8.addData('conf_real_resp.keys',conf_real_resp.keys)
        if conf_real_resp.keys != None:  # we had a response
            trials_8.addData('conf_real_resp.rt', conf_real_resp.rt)
        trials_8.addData('conf_real_resp.started', conf_real_resp.tStartRefresh)
        trials_8.addData('conf_real_resp.stopped', conf_real_resp.tStopRefresh)
        # the Routine "confidence_rating_real_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "fixation_minimum"-------
        continueRoutine = True
        routineTimer.add(0.480000)
        # update component parameters for each repeat
        polygon.setSize((dot_diam_dva*x_scale, dot_diam_dva*y_scale))
        # keep track of which components have finished
        fixation_minimumComponents = [polygon]
        for thisComponent in fixation_minimumComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixation_minimumClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixation_minimum"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixation_minimumClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixation_minimumClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 0.48-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation_minimumComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation_minimum"-------
        for thisComponent in fixation_minimumComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_8.addData('polygon.started', polygon.tStartRefresh)
        trials_8.addData('polygon.stopped', polygon.tStopRefresh)
        thisExp.nextEntry()
        
    # completed trials_per_block repeats of 'trials_8'
    
    
    # ------Prepare to start Routine "break_between_runs"-------
    continueRoutine = True
    # update component parameters for each repeat
    break_text = 'You finished a block of '+str(trials_per_block)+' trials. In total you have now completed '+str(real_trial_index)+' trials out of '+ str(num_real_trials) + '.\n\nTake a brief break if desired.\n\n Please press any button to continue.'
    break_text_presentation.setText(break_text)
    resp_subj_ready.keys = []
    resp_subj_ready.rt = []
    _resp_subj_ready_allKeys = []
    resp_experimenter_ready.keys = []
    resp_experimenter_ready.rt = []
    _resp_experimenter_ready_allKeys = []
    # keep track of which components have finished
    break_between_runsComponents = [break_text_presentation, resp_subj_ready, resp_experimenter_ready, subject_ready_text]
    for thisComponent in break_between_runsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    break_between_runsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "break_between_runs"-------
    while continueRoutine:
        # get current time
        t = break_between_runsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=break_between_runsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_text_presentation* updates
        if break_text_presentation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_text_presentation.frameNStart = frameN  # exact frame index
            break_text_presentation.tStart = t  # local t and not account for scr refresh
            break_text_presentation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_text_presentation, 'tStartRefresh')  # time at next scr refresh
            break_text_presentation.setAutoDraw(True)
        if break_text_presentation.status == STARTED:
            if bool(resp_subj_ready.keys):
                # keep track of stop time/frame for later
                break_text_presentation.tStop = t  # not accounting for scr refresh
                break_text_presentation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break_text_presentation, 'tStopRefresh')  # time at next scr refresh
                break_text_presentation.setAutoDraw(False)
        
        # *resp_subj_ready* updates
        waitOnFlip = False
        if resp_subj_ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_subj_ready.frameNStart = frameN  # exact frame index
            resp_subj_ready.tStart = t  # local t and not account for scr refresh
            resp_subj_ready.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_subj_ready, 'tStartRefresh')  # time at next scr refresh
            resp_subj_ready.status = STARTED
            # AllowedKeys looks like a variable named `responseButtons`
            if not type(responseButtons) in [list, tuple, np.ndarray]:
                if not isinstance(responseButtons, str):
                    logging.error('AllowedKeys variable `responseButtons` is not string- or list-like.')
                    core.quit()
                elif not ',' in responseButtons:
                    responseButtons = (responseButtons,)
                else:
                    responseButtons = eval(responseButtons)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_subj_ready.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_subj_ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_subj_ready.status == STARTED:
            if bool(resp_subj_ready.keys):
                # keep track of stop time/frame for later
                resp_subj_ready.tStop = t  # not accounting for scr refresh
                resp_subj_ready.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp_subj_ready, 'tStopRefresh')  # time at next scr refresh
                resp_subj_ready.status = FINISHED
        if resp_subj_ready.status == STARTED and not waitOnFlip:
            theseKeys = resp_subj_ready.getKeys(keyList=list(responseButtons), waitRelease=False)
            _resp_subj_ready_allKeys.extend(theseKeys)
            if len(_resp_subj_ready_allKeys):
                resp_subj_ready.keys = _resp_subj_ready_allKeys[0].name  # just the first key pressed
                resp_subj_ready.rt = _resp_subj_ready_allKeys[0].rt
        
        # *resp_experimenter_ready* updates
        waitOnFlip = False
        if resp_experimenter_ready.status == NOT_STARTED and resp_subj_ready.keys:
            # keep track of start time/frame for later
            resp_experimenter_ready.frameNStart = frameN  # exact frame index
            resp_experimenter_ready.tStart = t  # local t and not account for scr refresh
            resp_experimenter_ready.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_experimenter_ready, 'tStartRefresh')  # time at next scr refresh
            resp_experimenter_ready.status = STARTED
            # AllowedKeys looks like a variable named `experimenterReadyButton`
            if not type(experimenterReadyButton) in [list, tuple, np.ndarray]:
                if not isinstance(experimenterReadyButton, str):
                    logging.error('AllowedKeys variable `experimenterReadyButton` is not string- or list-like.')
                    core.quit()
                elif not ',' in experimenterReadyButton:
                    experimenterReadyButton = (experimenterReadyButton,)
                else:
                    experimenterReadyButton = eval(experimenterReadyButton)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_experimenter_ready.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_experimenter_ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_experimenter_ready.status == STARTED:
            if bool(resp_experimenter_ready.keys):
                # keep track of stop time/frame for later
                resp_experimenter_ready.tStop = t  # not accounting for scr refresh
                resp_experimenter_ready.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp_experimenter_ready, 'tStopRefresh')  # time at next scr refresh
                resp_experimenter_ready.status = FINISHED
        if resp_experimenter_ready.status == STARTED and not waitOnFlip:
            theseKeys = resp_experimenter_ready.getKeys(keyList=list(experimenterReadyButton), waitRelease=False)
            _resp_experimenter_ready_allKeys.extend(theseKeys)
            if len(_resp_experimenter_ready_allKeys):
                resp_experimenter_ready.keys = _resp_experimenter_ready_allKeys[-1].name  # just the last key pressed
                resp_experimenter_ready.rt = _resp_experimenter_ready_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *subject_ready_text* updates
        if subject_ready_text.status == NOT_STARTED and resp_subj_ready.keys:
            # keep track of start time/frame for later
            subject_ready_text.frameNStart = frameN  # exact frame index
            subject_ready_text.tStart = t  # local t and not account for scr refresh
            subject_ready_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(subject_ready_text, 'tStartRefresh')  # time at next scr refresh
            subject_ready_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_between_runsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_between_runs"-------
    for thisComponent in break_between_runsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    main_exp_blocks.addData('break_text_presentation.started', break_text_presentation.tStartRefresh)
    main_exp_blocks.addData('break_text_presentation.stopped', break_text_presentation.tStopRefresh)
    # check responses
    if resp_subj_ready.keys in ['', [], None]:  # No response was made
        resp_subj_ready.keys = None
    main_exp_blocks.addData('resp_subj_ready.keys',resp_subj_ready.keys)
    if resp_subj_ready.keys != None:  # we had a response
        main_exp_blocks.addData('resp_subj_ready.rt', resp_subj_ready.rt)
    main_exp_blocks.addData('resp_subj_ready.started', resp_subj_ready.tStartRefresh)
    main_exp_blocks.addData('resp_subj_ready.stopped', resp_subj_ready.tStopRefresh)
    # check responses
    if resp_experimenter_ready.keys in ['', [], None]:  # No response was made
        resp_experimenter_ready.keys = None
    main_exp_blocks.addData('resp_experimenter_ready.keys',resp_experimenter_ready.keys)
    if resp_experimenter_ready.keys != None:  # we had a response
        main_exp_blocks.addData('resp_experimenter_ready.rt', resp_experimenter_ready.rt)
    main_exp_blocks.addData('resp_experimenter_ready.started', resp_experimenter_ready.tStartRefresh)
    main_exp_blocks.addData('resp_experimenter_ready.stopped', resp_experimenter_ready.tStopRefresh)
    main_exp_blocks.addData('subject_ready_text.started', subject_ready_text.tStartRefresh)
    main_exp_blocks.addData('subject_ready_text.stopped', subject_ready_text.tStopRefresh)
    # the Routine "break_between_runs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'main_exp_blocks'


# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(8.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [finish]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finish* updates
    if finish.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finish.frameNStart = frameN  # exact frame index
        finish.tStart = t  # local t and not account for scr refresh
        finish.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish, 'tStartRefresh')  # time at next scr refresh
        finish.setAutoDraw(True)
    if finish.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finish.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            finish.tStop = t  # not accounting for scr refresh
            finish.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finish, 'tStopRefresh')  # time at next scr refresh
            finish.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

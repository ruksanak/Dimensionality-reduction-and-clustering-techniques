#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 00:54:21 2021

@author: ruksanakhan
"""

import os
import pandas as pd
import numpy as np

#os.chdir("/Users/ruksanakhan/Documents/CS 688/Project/CS688_Project_RuksanaKhan_U99048046")

import re

import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import operator
from functools import reduce

#Get the data

df = pd.read_csv("1. pose-output.csv")


for i in df.columns.tolist()[1:]:
    # print(i)
    split_str = [re.split(', |, |/[ |]', x.strip("[]")) for x in df[i].tolist()]

    convert= [[float(t) for t in l] for l in split_str]

    df[i]  = convert
    

#change the value of e
e = 2

df["name"][e]


#Gif Function
def gif(e):
    
    # %matplotlib qt  
    
    fig = plt.figure()
    ax  = fig.add_subplot(111, projection ="3d")
    
    def update(i):
        ax.clear()
        
        ax.plot(
    
            [-df['xX_left_wrist'][e][i], -df['xX_left_elbow'][e][i]], 
            [-df['yY_left_wrist'][e][i], -df['yY_left_elbow'][e][i]], 
            [-df['zZ_left_wrist'][e][i], -df['zZ_left_elbow'][e][i]], marker='o', color='green', linestyle='dashed')
            
        ax.plot(
            
            [-df['xX_left_elbow'][e][i], -df['xX_left_shoulder'][e][i]], 
            [-df['yY_left_elbow'][e][i], -df['yY_left_shoulder'][e][i]], 
            [-df['zZ_left_elbow'][e][i], -df['zZ_left_shoulder'][e][i]], marker='o',color='red', linestyle='dashed' )
        
        ax.plot(
    
            [-df['xX_right_wrist'][e][i], -df['xX_right_elbow'][e][i]], 
            [-df['yY_right_wrist'][e][i], -df['yY_right_elbow'][e][i]], 
            [-df['zZ_right_wrist'][e][i], -df['zZ_right_elbow'][e][i]], marker='o', color='green', linestyle='dashed')
        
        
        ax.plot(
            
            [-df['xX_right_elbow'][e][i], -df['xX_right_shoulder'][e][i]], 
            [-df['yY_right_elbow'][e][i], -df['yY_right_shoulder'][e][i]], 
            [-df['zZ_right_elbow'][e][i], -df['zZ_right_shoulder'][e][i]], marker='o',color='red', linestyle='dashed' )
        
    
        ax.plot(
            
            [-df['xX_left_shoulder'][e][i], -df['xX_right_shoulder'][e][i]], 
            [-df['yY_left_shoulder'][e][i], -df['yY_right_shoulder'][e][i]], 
            [-df['zZ_left_shoulder'][e][i], -df['zZ_right_shoulder'][e][i]], marker='o', color='y', linestyle='dashed' )
     
        ax.plot(
            
            [-df['xX_right_shoulder'][e][i], -df['xX_right_hip'][e][i]], 
            [-df['yY_right_shoulder'][e][i], -df['yY_right_hip'][e][i]], 
            [-df['zZ_right_shoulder'][e][i], -df['zZ_right_hip'][e][i]], marker='o', color='blue', linestyle='dashed' )
                   
    
        ax.plot(
            
            [-df['xX_left_shoulder'][e][i], -df['xX_left_hip'][e][i]], 
            [-df['yY_left_shoulder'][e][i], -df['yY_left_hip'][e][i]], 
            [-df['zZ_left_shoulder'][e][i], -df['zZ_left_hip'][e][i]], marker='o', color='blue', linestyle='dashed' )
    
    
        ax.plot(
            [-df['xX_left_hip'][e][i], -df['xX_right_hip'][e][i]], 
            [-df['yY_left_hip'][e][i], -df['yY_right_hip'][e][i]], 
            [-df['zZ_left_hip'][e][i], -df['zZ_right_hip'][e][i]], marker='o',color='m', linestyle='dashed' )
         
        ax.plot(
            [-df['xX_left_hip'][e][i], -df['xX_left_knee'][e][i]], 
            [-df['yY_left_hip'][e][i], -df['yY_left_knee'][e][i]], 
            [-df['zZ_left_hip'][e][i], -df['zZ_left_knee'][e][i]], marker='o',color='grey', linestyle='dashed' )
    
        ax.plot(
            [-df['xX_left_knee'][e][i], -df['xX_left_ankle'][e][i]], 
            [-df['yY_left_knee'][e][i], -df['yY_left_ankle'][e][i]], 
            [-df['zZ_left_knee'][e][i], -df['zZ_left_ankle'][e][i]], marker='o',color='black', linestyle='dashed' )
    
        ax.plot(
            [-df['xX_right_hip'][e][i], -df['xX_right_knee'][e][i]], 
            [-df['yY_right_hip'][e][i], -df['yY_right_knee'][e][i]], 
            [-df['zZ_right_hip'][e][i], -df['zZ_right_knee'][e][i]], marker='o',color='grey', linestyle='dashed' )
    
        ax.plot(
            [-df['xX_right_knee'][e][i], -df['xX_right_ankle'][e][i]], 
            [-df['yY_right_knee'][e][i], -df['yY_right_ankle'][e][i]], 
            [-df['zZ_right_knee'][e][i], -df['zZ_right_ankle'][e][i]], marker='o',color='black', linestyle='dashed' )
    
    frames = 50
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=100)
    
    
    ani.save(df["name"][e] + '.gif', writer='pillow')
 

    

#Use the gif function and get the gif
gif(0)    


x = df["name"]

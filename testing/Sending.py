import csv
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk,Image 
import Optimized
import numpy as np
from timeit import default_timer as timer
from numba import vectorize
def readcsv(filename):	
    file = open(filename, "r")
    reader = csv.reader(file, delimiter=";")
    rownum = 0	
    a = []

    for row in reader:
        a.append (row)
        rownum += 1

    return a
def seperate(b):
    n=[]
    for i in b:
        for j in i:
            l=j.split(',')
            n.append(l)
    return n
b=readcsv('C:\\Users\\akhil\\Downloads\\chikku\\Dataset\\MainDataSet.csv')
temp=len(b)
Main_File=seperate(b)
Optimized_File=Optimized.n
@vectorize(["float32(float32, float32)"], target='cuda')
def Collect_crops(State1,District1,Season1,Soil1,level):
    lis=[]
    for i in range(0,len(Optimized_File)):
        if(Soil1==Optimized_File[i][0] and level==Optimized_File[i][1] and Season1==Optimized_File[i][2] and State1==Optimized_File[i][3] and (District1 in Optimized_File[i][4] or ' ' in Optimized_File[i][4])):
            lis.append(Optimized_File[i][5])
    return lis
@vectorize(["float32(float32, float32)"], target='cuda')
def Collect_Data(l,State1,District1,Season1,Soil1,level):
    c={}
    if(len(l)>0):
        for i in l:
            #print(i,level)
            years=[]
            production=[]
            for j in range(1,temp):
                if(State1==Main_File[j][0] and District1==Main_File[j][1] and Season1==Main_File[j][3] and i==Main_File[j][4]  and Soil1==Main_File[j][8] and level==Main_File[j][7]):
                    years.append(int(Main_File[j][2]))
                    production.append(int(float(Main_File[j][5])*float(Main_File[j][5])/float(Main_File[j][5])))
            c[i]=[years,production]
        return c
    else:
        return {}
@vectorize(["float32(float32, float32)"], target='cuda')
def Best_Crop(low):
    if(len(low)>0):
        c=list(low.keys())
        f=c[0]
        years=low[c[0]]
        size=len(years[0])
        for i in c:
            t=low[i]
            if(size<len(t[0])):
                f=i
        return {f:low[f]}
    else:
        year=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
        production=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        return {'no crops Found':[year,production]}













        
                
    


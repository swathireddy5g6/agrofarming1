import csv
import math
import threading
import timeit
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
b=readcsv('C:\chikku\chikku\Dataset\\MainDataSet.csv')
#b=readcsv('C:\\Users\\akhil\\Downloads\\chikku\\Dataset\\MainDataSet.csv')
temp=len(b)
print(b[0])
s=seperate(b)
total_entered=0
total_completed=0
l=[]
for i in [0,2,3,4,7,8]:
    li=[]
    for j in range(1,temp):
        if(s[j][i] not in li):
                li.append(s[j][i])
    li.sort()
    l.append(li)
for i in l:
    print(i,'\n')
#print(l[5])

def Calculate(crop,index):
    global total_entered
    global total_completed
    count=0
    size=0
    for i in range(1,len(b)):
        size=size+1
        total_entered=total_entered+1
        if(crop==s[i][index]):
            count=count+1
            total_completed=total_completed+1
    #print(count)
    return count,size
def Crop_Calculation(i,index):
    entropy=0
    for crop in l[i]:
        #print(i)
        temp_crop_count,size=Calculate(crop,index)
        #print(math.log(2,log_value))
        #print(i,temp_crop_count,log_value)
        entropy=entropy+(-(temp_crop_count/size)*(math.log((temp_crop_count/size),2)))
        #print(crop,-(temp_crop_count/size)*(math.log((temp_crop_count/size),2)),entropy)
    #print('Final Entropy is ',entropy)
    return entropy
def Calculate_State(crop,state,crop_index,State_index):
    global total_entered
    global total_completed
    count=0
    size=0
    for i in range(0,len(b)):
        if(state==s[i][State_index]):
            size=size+1
            total_entered=total_entered+1
            if(crop==s[i][crop_index]):
                total_completed=total_completed+1
                #print(crop+' '+state+' founded '+str(count))
                count=count+1
    #print(count)
    return count,size
def State_Entropy(row1,row2,srow1,srow2):
    sno=1
    remain=len(l[row1])-1
    Information=0
    for i in l[row1]:
        Result_Entropy=0
        for crop in l[row2]:
            present,All=Calculate_State(crop,i,srow1,srow2)
            #print(i,crop,present,All)
            if((present==0) or (present==1 and All==1) or (present==All)):
                Entropy=0
            else:
                Entropy=-(present/All)*(math.log((present/All),2))
            Result_Entropy=Result_Entropy+Entropy
        #print('From ',i,' the Entropy ',Result_Entropy)
        Information=Information+(All/len(b)*Result_Entropy)
        #print('Till ',i,'the Overall Information Gained is ',Information)
        print(str(sno)+')'+i+' Calculation Completed Please wait '+str(remain)+' remaining')
        sno=sno+1
        remain=remain-1
    return Information
start=timeit.timeit()
"""Main_Entropy=Crop_Calculation(3,4)
print('Main_Entropy is:',Main_Entropy)
print('\n\n')
print('Calculation for State started:')
Information_States=State_Entropy(0,3,4,0)
print('Information From State: ',Information_States)
Information_Gain_States=Main_Entropy-Information_States
print('Information Gained From State: ',Information_Gain_States)"""
"""
print('\n\n')
print('Calculation for Years started:')
Information_Years=State_Entropy(1,3,4,2)
print('Information From Years: ',Information_Years)
Information_Gain_Years=Main_Entropy-Information_Years
print('Information Gained From Years: ',Information_Gain_Years)"""
"""print('\n\n')
print('Calculation for Season started:')
Information_Season=State_Entropy(2,3,4,3)
print('Information From Season: ',Information_Season)
Information_Gain_Season=Main_Entropy-Information_Season
print('Information Gained From Season: ',Information_Gain_Season)
print('\n\n')
print('Calculation for Water level started:')
Information_Water=State_Entropy(4,3,4,7)
print('Information From Water_Level: ',Information_Water)
Information_Gain_Water=Main_Entropy-Information_Water
print('Information Gained From Level: ',Information_Gain_Water)
print('\n\n')
print('Calculation for Soil started:')
Information_Soil=State_Entropy(5,3,4,8)
print('Information From Soil: ',Information_Soil)
Information_Gain_Soil=Main_Entropy-Information_Soil
print('Information Gained From Soil: ',Information_Gain_Soil)
end=timeit.timeit()
#print(end-start)
print(total_entered,total_completed)
#print('Total comparisions are '+str(comparisions))"""

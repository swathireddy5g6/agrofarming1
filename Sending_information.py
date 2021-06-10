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
import Apply_Regression
import language
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
temp=len(b)
Main_File=seperate(b)
Optimized_File=Optimized.n
def Collect_crops(State1,District1,Season1,Soil1,level):
    lis=[]
    for i in range(0,len(Optimized_File)):
        if(Soil1==Optimized_File[i][0] and level==Optimized_File[i][1] and Season1==Optimized_File[i][2] and State1==Optimized_File[i][3] and (District1 in Optimized_File[i][4] or ' ' in Optimized_File[i][4])):
            lis.append(Optimized_File[i][5])
    return lis
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
def plotGraph(root1,low_year,medium_year,high_year,State1,District1,Season1,Soil1):
    #root1=tk.Tk()
    #root1.title("Display Resulted Crops...")
    label1=Label(root1,text="These are the predicted crops",font=("arial", 22,"bold"),fg="black").place(x=1000,y=200)
    output1 = Text(root1, width=40, height=8,font=('arial',12,'bold'))
    output2 = Text(root1, width=40, height=8,font=('arial',12,'bold'))
    output3 = Text(root1, width=40, height=8,font=('arial',12,'bold'))
    def Generate_Graph():
        i=list(low_year.keys())
        i=i[0]
        x1=low_year[i]
        x1_data1=x1[0]
        y1_data2=x1[1]
        data1 = {'years': x1_data1,
         'production': y1_data2
            }
        df1 = DataFrame(data1,columns=['years','production'])
    
        j=list(medium_year.keys())
        j=j[0]
        x2=medium_year[j]
        x2_data1=x2[0]
        y2_data2=x2[1]
        data2 = {'years': x2_data1,
         'production': y2_data2
            }
        df2 = DataFrame(data2,columns=['years','production'])

        k=list(high_year.keys())
        k=k[0]
        x3=high_year[k]
        x3_data1=x3[0]
        y3_data2=x3[1]
        data3 = {'years': x3_data1,
         'production': y3_data2
            }
        df3 = DataFrame(data3,columns=['years','production'])
        if(i=='no crops Found' and j=='no crops Found' and k=='no crops Found'):
            messagebox.showinfo("Change Value", "Please Change Season We dont have the analasis on specific "+Season1+" Season" )
        else:
    
            root= tk.Tk() 
            root.title("Displaying Graph")
            figure1 = plt.Figure(figsize=(4,4), dpi=100)
            ax1 = figure1.add_subplot(111)
            bar1 = FigureCanvasTkAgg(figure1, root)
            bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df1 = df1[['years','production']].groupby('years').sum()
            df1.plot(kind='bar', legend=True, ax=ax1)
            ax1.set_xlabel(i)
            ax1.set_title(i+' found in low Water')

            figure2 = plt.Figure(figsize=(4,4), dpi=100)
            ax2 = figure2.add_subplot(111)
            bar2 = FigureCanvasTkAgg(figure2, root)
            bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df2 = df2[['years','production']].groupby('years').sum()
            df2.plot(kind='bar', legend=True, ax=ax2)
            ax2.set_xlabel(j)
            ax2.set_title(j+' found in medium Water')

            figure3 = plt.Figure(figsize=(4,4), dpi=100)
            ax3 = figure3.add_subplot(111)
            bar3 = FigureCanvasTkAgg(figure3, root)
            bar3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            df3 = df3[['years','production']].groupby('years').sum()
            df3.plot(kind='bar', legend=True, ax=ax3)
            ax3.set_xlabel(k)
            ax3.set_title(k+' found in high Water')
            Generate_Fertilizers=tk.Button(root,text="GENERATE FERTILIZERS",width=35,height=1,bg='orange',command=Fertilizer).pack()
            Predict=tk.Button(root,text="Predict low water crop for  2020 Year",width=35,height=1,bg='orange',command=Regression_low).pack()
            Predict=tk.Button(root,text="Predict medium water crop for 2020 Year",width=35,height=1,bg='orange',command=Regression_medium).pack()
            Predict=tk.Button(root,text="Predict high water crop for  2020 Year",width=35,height=1,bg='orange',command=Regression_high).pack()
            Quit=tk.Button(root,text="QUIT GRAPH",width=35,height=1,bg='orange',command=root.destroy).pack()
            root.mainloop()
    def Regression_low():
        i=list(low_year.keys())
        i=i[0]
        x1=low_year[i]
        x1_data1=x1[0]
        y1_data2=x1[1]
        if(i=='no crops Found'):
            messagebox.showinfo("Sorry For inconvience", "Sorry no graph for Low Water Hence we cant apply regression" )
        else:
            Apply_Regression.regression(i,x1_data1,y1_data2)
    def Regression_medium():
        j=list(medium_year.keys())
        j=j[0]
        x2=medium_year[j]
        x2_data1=x2[0]
        y2_data2=x2[1]
        if(j=='no crops Found'):
            messagebox.showinfo("Sorry For inconvience", "Sorry no graph for medium Water Hence we cant apply regression" )
        else:
            Apply_Regression.regression(j,x2_data1,y2_data2)
    def Regression_high():
        k=list(high_year.keys())
        k=k[0]
        x3=high_year[k]
        x3_data1=x3[0]
        y3_data2=x3[1]
        if(k=='no crops Found'):
            messagebox.showinfo("Sorry For inconvience", "Sorry no graph for high Water Hence we cant apply regression" )
        else:
            Apply_Regression.regression(k,x3_data1,y3_data2)
        
    def Fertilizer():
        root2=tk.Tk()
        root2.title("Select Language")
        root2.geometry("10000x10000+0+0")
        txt="                                    These are the Fertilizers for the crops                                   "
        heading=Label(root2,text=txt,font=("arial",40,"bold"),fg="steelblue",bg="black").pack()
        #c=Canvas(root2,bg="black",height="10000",width="10000")
        #img=ImageTk.PhotoImage(Image.open("C:\\Users\\Hp\\AppData\\Local\\Programs\\Python\\Python38-32\\akh.jpg"))
        #c.create_image(0,0,anchor=NW,image=img)
        label1=tk.Label(root2,text="Select Language:",font=("arial",22,"bold"),fg="black").place(x=300,y=200)
        Choice='English'
        def choice(selected_item):
                global Choice
                Choice=repr(selected_item.strip())
                Choice=Choice[1:len(Choice)-1]
                print(Choice)
        
        name1=StringVar()
        max_len = 38
        names1 = tk.StringVar()
        choices = ['Default (English)','Telugu','Hindi','English']
        padded_choices = [x+' '*(max_len-len(x)) for x in choices]
        name1= ttk.OptionMenu(root2, names1,'Select Choice', *padded_choices,command=choice).place(x=700,y=210)
        Output1 = Text(root2, width=40, height=20,font=('arial',12,'bold'))
        Output2 = Text(root2, width=40, height=20,font=('arial',12,'bold'))
        Output3 = Text(root2, width=40, height=20,font=('arial',12,'bold'))
        def Produce():
            global Choice
            x=list(low_year.keys())
            y=list(medium_year.keys())
            z=list(high_year.keys())
            try:
                print(Choice)
            except NameError:
                #messagebox.showerror('Choice','You have Not selected any value so the default value\n English is selected')
                Choice='English'
            x=language.convert(x,Choice)
            y=language.convert(y,Choice)
            z=language.convert(z,Choice)
            Output1.insert(END, x+'\n'+'\n')
            Output2.insert(END, y+'\n'+'\n')
            Output3.insert(END, z+'\n'+'\n')
            #Output1.place(x=50,y=300)
            #Output2.place(x=350,y=300)
            #Output3.place(x=650,y=300)
            scrollbar1 = Scrollbar(root2, command=Output1.yview, )
            scrollbar2 = Scrollbar(root2, command=Output2.yview, )
            scrollbar3 = Scrollbar(root2, command=Output3.yview, )
            Output1['yscrollcommand'] = scrollbar1.set
            scrollbar1.place(x=520,y=300, height=386)
            Output1.place(x=150,y=300, height=386)
            
            Output2['yscrollcommand'] = scrollbar2.set
            scrollbar2.place(x=1020,y=305, height=386)
            Output2.place(x=650,y=300, height=386 )
            
            Output3['yscrollcommand'] = scrollbar3.set
            scrollbar3.place(x=1520,y=300, height=386)
            Output3.place(x=1150,y=300, height=386, width=370)
            
        submit=tk.Button(root2,text="RESULT",width=20,height=1,bg='orange',command=Produce).place(x=500,y=700)
        cancel=tk.Button(root2,text="QUIT",width=20,height=1,bg='orange',command=root2.destroy).place(x=700,y=700)
        #c.pack()
        root2.mainloop()
        
    output1.place(x=1000,y=310)
    output2.place(x=1000,y=410)
    output3.place(x=1000,y=510)
    a=list(low_year.keys())
    b=list(medium_year.keys())
    c=list(high_year.keys())
    output1.insert(END, a[0]+' in low water level')
    output2.insert(END, b[0]+' in medium medium level')
    output3.insert(END, c[0]+' in high water level')
    submit=tk.Button(root1,text="GENERATE GRAPH",width=20,height=1,bg='orange',command=Generate_Graph).place(x=1000,y=700)
    fertilizer=tk.Button(root1,text="SHOW FERTILIZER",width=20,height=1,bg='orange',command=Fertilizer).place(x=1200,y=700)
    root1.mainloop()












        
                
    


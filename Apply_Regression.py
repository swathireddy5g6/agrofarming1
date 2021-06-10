import matplotlib.pyplot as plt
import math
print('Ready for Regression')
def regression(title,x,y):
        tem=len(x)
        i=x[tem-1]
        while(i<2020):
                x.append(i)
                mean=sum(y)//len(y)
                print(mean,len(y),i)
                y.append(mean)
                i=i+1
        mean_x=sum(x)//len(x)
        mean_y=sum(y)/len(y)
        print(mean_y,mean_x)
        l=[]
        for i in range(0,len(x)):
                li=[]
                x_xbar=x[i]-mean_x
                y_ybar=y[i]-mean_y
                li.append(x[i])
                li.append(y[i])
                li.append(x_xbar)
                li.append(y_ybar)
                li.append(x_xbar*x_xbar)
                li.append(x_xbar*y_ybar)
                l.append(li)
        print('x,','y,','x_xbar,','y_ybar,','(x-x),','(x_xbar)(y_ybar)')
        for i in l:
                print(i)
        sigmax=0
        sigmay=0
        for i in l:
                sigmax=sigmax+i[4]
                sigmay=sigmay+i[5]
        if(sigmax==0):
                m=sigmay/1
        else:
                m=sigmay/sigmax
        c=mean_y-m*mean_x
        #print('Mean of x:',mean_x,', Mean of y:',mean_y,', Sigma of x:',sigmax,', Sigma of y:',sigmay,', Slope m is:',m,', Constant c:',c)
        plx=[]
        ply=[]
        plx1=[]
        ply1=[]
        for i in x:
                py=m*i+c
                plx.append(i)
                ply.append(py)
        """while(i<2020):
                i=i+1
                py=m*i+c
                plx.append(i)
                ply.append(py)"""
        i=i+1
        py=m*i+c
        plx1.append(i)
        ply1.append(py)
        """for i in range(0,len(plx)):
                print(plx[i],ply[i])"""
        error=0
        for i in range(0,len(plx)):
                #print(ply[i],y[i],ply[i]-y[i])
                error=error+ply[i]-y[i]
        print('predicted value is ',int(ply1[0]))
        print('predicted value lies from',ply1[0]-error//len(x))
        print('to ',ply1[0]+error//len(x))
        print('Error=',error//len(x))
        plt.scatter(x, y,label='actual values')
        plt.plot(plx,ply,label='regression values')
        plt.scatter(plx1,ply1,label='Predicted value')
        plt.xlabel('Years') 
        plt.ylabel('Production Rate') 
        plt.title(title) 
        plt.legend()
        plt.show()
        
        
        



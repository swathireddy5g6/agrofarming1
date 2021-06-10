import csv
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
b=readcsv('C:\\Users\\akhil\\Downloads\\chikku\\Dataset\\Max_Optimized_rule.csv')
temp=len(b)
s=seperate(b)
#print(b[0])
n=[]
for i in s:
    a=[]
    l=[]
    for j in range(4,len(i)-1):
        #print('      ',i[j])
        l.append(i[j])
    a.append(i[0])
    a.append(i[1])
    a.append(i[2])
    a.append(i[3])
    a.append(l)
    a.append(i[len(i)-1])
    n.append(a)
print('Model Learned')
        

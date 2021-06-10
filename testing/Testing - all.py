import Sending
import csv
import math
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
print(b[0])
s=seperate(b)
total_entered=0
total_completed=0
l=[]
"""for i in [8,0,1,3,7,4]:
    li=[]
    for j in range(1,temp):
        if(s[j][i] not in li):
                li.append(s[j][i])
    li.sort()
    l.append(li)
dist={'Andhra Pradesh':['ANANTAPUR', 'CHITTOOR', 'EAST GODAVARI', 'GUNTUR', 'KADAPA', 'KRISHNA',
                                'KURNOOL', 'PRAKASAM', 'SPSR NELLORE', 'SRIKAKULAM', 'VISAKHAPATANAM',
                                'VIZIANAGARAM', 'WEST GODAVARI'],
                      'Andaman and Nicobar Islands':['NICOBARS', 'NORTH AND MIDDLE ANDAMAN', 'SOUTH ANDAMANS'],
                      'Arunachal Pradesh':['ANJAW', 'CHANGLANG', 'DIBANG VALLEY', 'EAST KAMENG', 'EAST SIANG',
                                   'KURUNG KUMEY', 'LOHIT', 'LONGDING', 'LOWER DIBANG VALLEY',
                                   'LOWER SUBANSIRI', 'NAMSAI', 'PAPUM PARE', 'TAWANG', 'TIRAP',
                                   'UPPER SIANG', 'UPPER SUBANSIRI', 'WEST KAMENG', 'WEST SIANG'],
                      'Assam':['BAKSA', 'BARPETA', 'BONGAIGAON', 'CACHAR', 'CHIRANG', 'DARRANG', 'DHEMAJI',
                       'DHUBRI', 'DIBRUGARH', 'DIMA HASAO', 'GOALPARA', 'GOLAGHAT', 'HAILAKANDI',
                       'JORHAT', 'KAMRUP', 'KAMRUP METRO', 'KARBI ANGLONG', 'KARIMGANJ', 'KOKRAJHAR',
                       'LAKHIMPUR', 'MARIGAON', 'NAGAON', 'NALBARI', 'SIVASAGAR', 'SONITPUR', 'TINSUKIA', 'UDALGURI'],
                      'Bihar':['ARARIA', 'ARWAL', 'AURANGABAD', 'BANKA', 'BEGUSARAI', 'BHAGALPUR', 'BHOJPUR'
                       , 'BUXAR', 'DARBHANGA', 'GAYA', 'GOPALGANJ', 'JAMUI', 'JEHANABAD', 'KAIMUR (BHABUA)',
                       'KATIHAR', 'KHAGARIA', 'KISHANGANJ', 'LAKHISARAI', 'MADHEPURA', 'MADHUBANI', 'MUNGER',
                       'MUZAFFARPUR', 'NALANDA', 'NAWADA', 'PASHCHIM CHAMPARAN', 'PATNA', 'PURBI CHAMPARAN',
                       'PURNIA', 'ROHTAS', 'SAHARSA', 'SAMASTIPUR', 'SARAN', 'SHEIKHPURA', 'SHEOHAR', 'SITAMARHI',
                       'SIWAN', 'SUPAUL', 'VAISHALI'],
                      'Chhattisgarh':['BALOD', 'BALODA BAZAR', 'BALRAMPUR', 'BASTAR', 'BEMETARA', 'BIJAPUR', 'BILASPUR',
                              'DANTEWADA', 'DHAMTARI', 'DURG', 'GARIYABAND', 'JANJGIR-CHAMPA', 'JASHPUR', 'KABIRDHAM',
                              'KANKER', 'KONDAGAON', 'KORBA', 'KOREA', 'MAHASAMUND', 'MUNGELI', 'NARAYANPUR', 'RAIGARH',
                              'RAIPUR', 'RAJNANDGAON', 'SUKMA', 'SURAJPUR', 'SURGUJA'],
                      'Dadra and Nagar Haveli':['DADRA AND NAGAR HAVELI'],
                      'Goa':['NORTH GOA', 'SOUTH GOA'],
                      'Gujarat':['AHMADABAD', 'AMRELI', 'ANAND', 'BANAS KANTHA', 'BHARUCH', 'BHAVNAGAR', 'DANG', 'DOHAD',
                                 'GANDHINAGAR', 'JAMNAGAR', 'JUNAGADH', 'KACHCHH', 'KHEDA', 'MAHESANA', 'NARMADA', 'NAVSARI',
                                 'PANCH MAHALS', 'PATAN', 'PORBANDAR', 'RAJKOT', 'SABAR KANTHA', 'SURAT', 'SURENDRANAGAR', 'TAPI',
                                 'VADODARA', 'VALSAD'],
                      'Chandigarh':['CHANDIGARH'],
                      'Haryana':['AMBALA', 'BHIWANI', 'FARIDABAD', 'FATEHABAD', 'GURGAON', 'HISAR', 'JHAJJAR', 'JIND', 'KAITHAL',
                                 'KARNAL', 'KURUKSHETRA', 'MAHENDRAGARH', 'MEWAT', 'PALWAL', 'PANCHKULA', 'PANIPAT', 'REWARI',
                                 'ROHTAK', 'SIRSA', 'SONIPAT', 'YAMUNANAGAR'],
              'Himachal Pradesh':['BILASPUR', 'CHAMBA', 'HAMIRPUR', 'KANGRA', 'KINNAUR', 'KULLU', 'LAHUL AND SPITI',
                                  'MANDI', 'SHIMLA', 'SIRMAUR', 'SOLAN', 'UNA'],
              'Jammu and Kashmir':['ANANTNAG', 'BADGAM', 'BANDIPORA', 'BARAMULLA', 'DODA', 'GANDERBAL', 'JAMMU', 'KARGIL',
                                   'KATHUA', 'KISHTWAR', 'KULGAM', 'KUPWARA', 'LEH LADAKH', 'POONCH', 'PULWAMA', 'RAJAURI',
                                   'RAMBAN', 'REASI', 'SAMBA', 'SHOPIAN', 'SRINAGAR', 'UDHAMPUR'],
              'Jharkhand':['BOKARO', 'CHATRA', 'DEOGHAR', 'DHANBAD', 'DUMKA', 'EAST SINGHBUM', 'GARHWA', 'GIRIDIH', 'GODDA',
                           'GUMLA', 'HAZARIBAGH', 'JAMTARA', 'KHUNTI', 'KODERMA', 'LATEHAR', 'LOHARDAGA', 'PAKUR', 'PALAMU',
                           'RAMGARH', 'RANCHI', 'SAHEBGANJ', 'SARAIKELA KHARSAWAN', 'SIMDEGA', 'WEST SINGHBHUM'],
              'Karnataka':['BAGALKOT', 'BANGALORE RURAL', 'BELGAUM', 'BELLARY', 'BENGALURU URBAN', 'BIDAR', 'BIJAPUR',
                           'CHAMARAJANAGAR', 'CHIKBALLAPUR', 'CHIKMAGALUR', 'CHITRADURGA', 'DAKSHIN KANNAD', 'DAVANGERE',
                           'DHARWAD', 'GADAG', 'GULBARGA', 'HASSAN', 'HAVERI', 'KODAGU', 'KOLAR', 'KOPPAL', 'MANDYA',
                           'MYSORE', 'RAICHUR', 'RAMANAGARA', 'SHIMOGA', 'TUMKUR', 'UDUPI', 'UTTAR KANNAD', 'YADGIR'],
              'Kerala':['ALAPPUZHA', 'ERNAKULAM', 'IDUKKI', 'KANNUR', 'KASARAGOD', 'KOLLAM', 'KOTTAYAM', 'KOZHIKODE',
                        'MALAPPURAM', 'PALAKKAD', 'PATHANAMTHITTA', 'THIRUVANANTHAPURAM', 'THRISSUR', 'WAYANAD'],
              'Madhya Pradesh':['AGAR MALWA', 'ALIRAJPUR', 'ANUPPUR', 'ASHOKNAGAR', 'BALAGHAT', 'BARWANI', 'BETUL',
                                'BHIND', 'BHOPAL', 'BURHANPUR', 'CHHATARPUR', 'CHHINDWARA', 'DAMOH', 'DATIA', 'DEWAS',
                                'DHAR', 'DINDORI', 'GUNA', 'GWALIOR', 'HARDA', 'HOSHANGABAD', 'INDORE', 'JABALPUR',
                                'JHABUA', 'KATNI', 'KHANDWA', 'KHARGONE', 'MANDLA', 'MANDSAUR', 'MORENA', 'NARSINGHPUR',
                                'NEEMUCH', 'PANNA', 'RAISEN', 'RAJGARH', 'RATLAM', 'REWA', 'SAGAR', 'SATNA', 'SEHORE', 'SEONI',
                                'SHAHDOL', 'SHAJAPUR', 'SHEOPUR', 'SHIVPURI', 'SIDHI', 'SINGRAULI', 'TIKAMGARH', 'UJJAIN',
                                'UMARIA', 'VIDISHA'],
              'Maharashtra':['AHMEDNAGAR', 'AKOLA', 'AMRAVATI', 'AURANGABAD', 'BEED', 'BHANDARA', 'BULDHANA', 'CHANDRAPUR',
                             'DHULE', 'GADCHIROLI', 'GONDIA', 'HINGOLI', 'JALGAON', 'JALNA', 'KOLHAPUR', 'LATUR', 'MUMBAI',
                             'NAGPUR', 'NANDED', 'NANDURBAR', 'NASHIK', 'OSMANABAD', 'PALGHAR', 'PARBHANI', 'PUNE', 'RAIGAD',
                             'RATNAGIRI', 'SANGLI', 'SATARA', 'SINDHUDURG', 'SOLAPUR', 'THANE', 'WARDHA', 'WASHIM', 'YAVATMAL'],
              'Manipur':['BISHNUPUR', 'CHANDEL', 'CHURACHANDPUR', 'IMPHAL EAST', 'IMPHAL WEST', 'SENAPATI', 'TAMENGLONG', 'THOUBAL', 'UKHRUL'],
               'Meghalaya':['EAST GARO HILLS', 'EAST JAINTIA HILLS', 'EAST KHASI HILLS', 'NORTH GARO HILLS', 'RI BHOI', 'SOUTH GARO HILLS',
                            'SOUTH WEST GARO HILLS', 'SOUTH WEST KHASI HILLS', 'WEST GARO HILLS', 'WEST JAINTIA HILLS', 'WEST KHASI HILLS'],
                'Mizoram':['EAST GARO HILLS', 'EAST JAINTIA HILLS', 'EAST KHASI HILLS', 'NORTH GARO HILLS', 'RI BHOI', 'SOUTH GARO HILLS',
                           'SOUTH WEST GARO HILLS', 'SOUTH WEST KHASI HILLS', 'WEST GARO HILLS', 'WEST JAINTIA HILLS', 'WEST KHASI HILLS'],
                'Nagaland':['DIMAPUR', 'KIPHIRE', 'KOHIMA', 'LONGLENG', 'MOKOKCHUNG', 'MON', 'PEREN', 'PHEK', 'TUENSANG', 'WOKHA', 'ZUNHEBOTO'],
                'Odisha':['ANUGUL', 'BALANGIR', 'BALESHWAR', 'BARGARH', 'BHADRAK', 'BOUDH', 'CUTTACK', 'DEOGARH', 'DHENKANAL', 'GAJAPATI', 'GANJAM',
                          'JAGATSINGHAPUR', 'JAJAPUR', 'JHARSUGUDA', 'KALAHANDI', 'KANDHAMAL', 'KENDRAPARA', 'KENDUJHAR', 'KHORDHA', 'KORAPUT', 'MALKANGIRI',
                          'MAYURBHANJ', 'NABARANGPUR', 'NAYAGARH', 'NUAPADA', 'PURI', 'RAYAGADA', 'SAMBALPUR', 'SONEPUR', 'SUNDARGARH'],   
              'Puducherry':['KARAIKAL', 'MAHE', 'PONDICHERRY', 'YANAM'],
                'Punjab':['AMRITSAR', 'BARNALA', 'BATHINDA', 'FARIDKOT', 'FATEHGARH SAHIB', 'FAZILKA', 'FIROZEPUR', 'GURDASPUR', 'HOSHIARPUR', 'JALANDHAR',
                          'KAPURTHALA', 'LUDHIANA', 'MANSA', 'MOGA', 'MUKTSAR', 'NAWANSHAHR', 'PATHANKOT', 'PATIALA', 'RUPNAGAR', 'S.A.S NAGAR', 'SANGRUR',
                          'TARN TARAN'],
                   'Rajasthan':['AJMER', 'ALWAR', 'BANSWARA', 'BARAN', 'BARMER', 'BHARATPUR', 'BHILWARA', 'BIKANER', 'BUNDI', 'CHITTORGARH', 'CHURU', 'DAUSA',
                                'DHOLPUR', 'DUNGARPUR', 'GANGANAGAR', 'HANUMANGARH', 'JAIPUR', 'JAISALMER', 'JALORE', 'JHALAWAR', 'JHUNJHUNU', 'JODHPUR', 'KARAULI',
                                'KOTA', 'NAGAUR', 'PALI', 'PRATAPGARH', 'RAJSAMAND', 'SAWAI MADHOPUR', 'SIKAR', 'SIROHI', 'TONK', 'UDAIPUR'],
                      'Sikkim':['EAST DISTRICT', 'NORTH DISTRICT', 'SOUTH DISTRICT', 'WEST DISTRICT'],
                      'Tamil Nadu':['ARIYALUR', 'COIMBATORE', 'CUDDALORE', 'DHARMAPURI', 'DINDIGUL', 'ERODE', 'KANCHIPURAM', 'KANNIYAKUMARI', 'KARUR',
                                    'KRISHNAGIRI', 'MADURAI', 'NAGAPATTINAM', 'NAMAKKAL', 'PERAMBALUR', 'PUDUKKOTTAI', 'RAMANATHAPURAM', 'SALEM', 'SIVAGANGA',
                                    'THANJAVUR', 'THE NILGIRIS', 'THENI', 'THIRUVALLUR', 'THIRUVARUR', 'TIRUCHIRAPPALLI', 'TIRUNELVELI', 'TIRUPPUR', 'TIRUVANNAMALAI',
                                    'TUTICORIN', 'VELLORE', 'VILLUPURAM', 'VIRUDHUNAGAR'],
                      'Telangana':['ADILABAD', 'HYDERABAD', 'KARIMNAGAR', 'KHAMMAM', 'MAHBUBNAGAR', 'MEDAK', 'NALGONDA', 'NIZAMABAD', 'RANGAREDDI', 'WARANGAL'],
                      'Tripura':['DHALAI', 'GOMATI', 'KHOWAI', 'NORTH TRIPURA', 'SEPAHIJALA', 'SOUTH TRIPURA', 'UNAKOTI', 'WEST TRIPURA'],
                      'Uttar Pradesh':['AGRA', 'ALIGARH', 'ALLAHABAD', 'AMBEDKAR NAGAR', 'AMETHI', 'AMROHA', 'AURAIYA', 'AZAMGARH', 'BAGHPAT', 'BAHRAICH', 'BALLIA',
                                       'BALRAMPUR', 'BANDA', 'BARABANKI', 'BAREILLY', 'BASTI', 'BIJNOR', 'BUDAUN', 'BULANDSHAHR', 'CHANDAULI', 'CHITRAKOOT', 'DEORIA',
                                       'ETAH', 'ETAWAH', 'FAIZABAD', 'FARRUKHABAD', 'FATEHPUR', 'FIROZABAD', 'GAUTAM BUDDHA NAGAR', 'GHAZIABAD', 'GHAZIPUR', 'GONDA',
                                       'GORAKHPUR', 'HAMIRPUR', 'HAPUR', 'HARDOI', 'HATHRAS', 'JALAUN', 'JAUNPUR', 'JHANSI', 'KANNAUJ', 'KANPUR DEHAT', 'KANPUR NAGAR',
                                       'KASGANJ', 'KAUSHAMBI', 'KHERI', 'KUSHI NAGAR', 'LALITPUR', 'LUCKNOW', 'MAHARAJGANJ', 'MAHOBA', 'MAINPURI', 'MATHURA', 'MAU',
                                       'MEERUT', 'MIRZAPUR', 'MORADABAD', 'MUZAFFARNAGAR', 'PILIBHIT', 'PRATAPGARH', 'RAE BARELI', 'RAMPUR', 'SAHARANPUR', 'SAMBHAL',
                                       'SANT KABEER NAGAR', 'SANT RAVIDAS NAGAR', 'SHAHJAHANPUR', 'SHAMLI', 'SHRAVASTI', 'SIDDHARTH NAGAR', 'SITAPUR', 'SONBHADRA',
                                      'SULTANPUR', 'UNNAO', 'VARANASI'],
                      'Uttarakhand':['ALMORA', 'BAGESHWAR', 'CHAMOLI', 'CHAMPAWAT', 'DEHRADUN', 'HARIDWAR', 'NAINITAL', 'PAURI GARHWAL', 'PITHORAGARH', 'RUDRA PRAYAG',
                                     'TEHRI GARHWAL', 'UDAM SINGH NAGAR','UTTAR KASHI'],
                      'West Bengal':['24 PARAGANAS NORTH', '24 PARAGANAS SOUTH', 'BANKURA', 'BARDHAMAN', 'BIRBHUM', 'COOCHBEHAR', 'DARJEELING', 'DINAJPUR DAKSHIN',
                                     'DINAJPUR UTTAR','HOOGHLY', 'HOWRAH', 'JALPAIGURI', 'MALDAH', 'MEDINIPUR EAST', 'MEDINIPUR WEST', 'MURSHIDABAD', 'NADIA', 'PURULIA']}
#print(len(l[1]))
rules=[]
norules=[]
file1=open('Rules1.csv','w+')
file2=open('NoRules1.csv','w+')
co=0
cond=[]
for s_soil in ['well drained loam soil']:
    com=len(l[0])-co
    print(com)
    #print(s_state+' Started \n')
    for s_state in l[1]:
        for s_district in dist[s_state]:
            #print(s_soil)
            for s_season in l[3]:
                for s_water in l[4]:
                    for i in range(1,temp):
                        if((s_soil==s[i][8] and s_state==s[i][0] and s_district==s[i][1] and s_season==s[i][3] and s_water==s[i][7]) and [s_soil,s_state,s_district,s_season,s_water,s[i][4]] not in rules):
                            rules.append([s_soil,s_state,s_district,s_season,s_water,s[i][4]])
                            cond.append(([s_soil,s_state,s_district,s_season,s_water]))
                            file1.write(s[i][8]+','+s[i][0]+','+s[i][1]+','+s[i][3]+','+s[i][7]+','+s[i][4]+'\n')
                            print(s_soil,s_state,s_district,s_season,s_water,s[i][4],1)
        
    co=co+1
#print('\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ')
for s_soil in ['well drained loam soil']:
    com=len(l[0])-co
    print(com)
    #print(s_state+' Started \n')
    for s_state in l[1]:
        for s_district in dist[s_state]:
            #print(s_soil)
            for s_season in l[3]:
                for s_water in l[4]:
                    for s_crop in l[5]:
                        if([s_soil,s_state,s_district,s_season,s_water,s_crop] not in rules and [s_soil,s_state,s_district,s_season,s_water,s_crop] not in norules
                           and [s_soil,s_state,s_district,s_season,s_water] not in cond):
                            norules.append([s_soil,s_state,s_district,s_season,s_water,s_crop])
                            cond.append(([s_soil,s_state,s_district,s_season,s_water]))
                            file2.write(s_soil+','+s_state+','+s_district+','+s_season+','+s_water+','+s_crop+'\n')
                            print(s_soil,s_state,s_district,s_season,s_water,s_crop,2)
                        
    co=co+1

file1.close()
file2.close()
"""
"""Rules generation completed now claculating accuracy error rate"""
new=[]
tp=0
no=0
fn=0
file1=open('C://Users//akhil//Downloads//chikku//testing//all//All_TruePositive.csv','w+')
file2=open('C://Users//akhil//Downloads//chikku//testing//all//All_NoValuesTP.csv','w+')
file3=open('C://Users//akhil//Downloads//chikku//testing//all//All_NoCropvaluesFN.csv','w+')
file4=open('C://Users//akhil//Downloads//chikku//testing//all//All_AllValues.csv','w+')
size=int(input("Enter number of rows to be tested:"))
for i in range(1,temp):
    Soil=s[i][8]
    State=s[i][0]
    District=s[i][1]
    Season=s[i][3]
    Water=s[i][7]
    crop=s[i][4]
    #if(i==998+size+1):
        #break
    #if([Soil,State,District,Season,Water,crop] not in new):
    #new.append([Soil,State,District,Season,Water,crop])
    l=Sending.Collect_crops(State,District,Season,Soil,Water)
    #Sending_information.show_crops(l,m,h)
    low_year=Sending.Collect_Data(l,State,District,Season,Soil,Water)
    low_year=Sending.Best_Crop(low_year)
    l=list(low_year.keys())
    l=l[0]
    if(l==crop and l!='no crops Found'):
        tp=tp+1
        print(i,Soil,State,District,Season,Water,crop,l,'yes',1111,tp)
        file4.write(Soil+','+State+','+District+','+Season+','+Water+','+crop+','+l+','+'yes'+'\n')
        file1.write(Soil+','+State+','+District+','+Season+','+Water+','+crop+','+l+','+'yes'+'\n')
    elif(l=='no crops Found'):
        fn=fn+1
        print(i,Soil,State,District,Season,Water,crop,l,'no crops Found',2222,fn)
        file3.write(Soil+','+State+','+District+','+Season+','+Water+','+crop+','+l+','+'no crops Found'+'\n')
        file4.write(Soil+','+State+','+District+','+Season+','+Water+','+crop+','+l+','+'no crops Found'+'\n')
    else:
        tp=tp+1
        print(i,Soil,State,District,Season,Water,crop,l,'no',3333,tp)
        file2.write(Soil+','+State+','+District+','+Season+','+Water+','+crop+','+l+','+'no'+'\n')
        file4.write(Soil+','+State+','+District+','+Season+','+Water+','+crop+','+l+','+'no'+'\n')
file1.close()
file2.close()
file3.close()
b=readcsv('C:\\Users\\akhil\\Downloads\\chikku\\Dataset\\NoRules.csv')
temp=len(b)
print(b[0])
s=seperate(b)
file1=open('C://Users//akhil//Downloads//chikku//testing//all//All_FalsePositive.csv','w+')
file2=open('C://Users//akhil//Downloads//chikku//testing//all//All_TrueNegative.csv','w+')
fp=0
tn=0
for i in range(1,temp):
    Soil=s[i][0]
    State=s[i][1]
    District=s[i][2]
    Season=s[i][3]
    Water=s[i][4]
    crop=s[i][5]
    #if(i==size+1):
        #break
    #if([Soil,State,District,Season,Water,crop] not in new):
    #new.append([Soil,State,District,Season,Water,crop])
    l=Sending.Collect_crops(State,District,Season,Soil,Water)
    #Sending_information.show_crops(l,m,h)
    low_year=Sending.Collect_Data(l,State,District,Season,Soil,Water)
    low_year=Sending.Best_Crop(low_year)
    l=list(low_year.keys())
    l=l[0]
    if(l!='no crops Found'):
        fp=fp+1
        print(i,Soil,State,District,Season,Water,crop,l,'yes',4444,fp)
        file4.write(Soil+','+State+','+District+','+Season+','+Water+','+crop+','+l+','+'FalsePositive'+'Correct'+'\n')
        file1.write(Soil+','+State+','+District+','+Season+','+Water+','+crop+','+l+','+'FalsePositive'+'Correct'+'\n')
    elif(l=='no crops Found'):
        tn=tn+1
        print(i,Soil,State,District,Season,Water,crop,l,'no crops Found',5555,tn)
        file2.write(Soil+','+State+','+District+','+Season+','+Water+','+crop+','+l+','+'TrueNegative'+'\n')
        file4.write(Soil+','+State+','+District+','+Season+','+Water+','+crop+','+l+','+'TrueNegative'+'\n')
file1.close()
file2.close()
file3.close()
file4.close()
print(tp,fn,'\n',fp,tn)
err=(fp+fn)/(tp+fn+fp+tn)
acc=(tp+tn)/(tp+fn+fp+tn)
sn=tp/(tp+fn)
sp=tn/tn+fp
prec=tp/tp+fp
fpr=fp/tn+fp
mcc=(tp*tn)-(fp*fn)/math.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
f_0=(1.25*prec*sn)/(1.25*prec+sn)
f_1=(2*prec*sn)/(prec+sn)
f_2=(5*prec*sn)/(4*prec+sn)
file1=open('C://Users//akhil//Downloads//chikku//testing//all//All_Result.csv','w+')
file1.write('Error rate'+','+str(err)+'\n')
print('Error rate',err)
file1.write('Accuracy'+','+str(acc)+'\n')
print('Accuracy',acc)
file1.write('Sensitivity (or) True Positivity rate (or) Recall'+','+str(sn)+'\n')
print('Sensitivity \nTrue Positivity rate \nRecall',sn)
file1.write('Specificity (or) True Negative rate'+','+str(sp)+'\n')
print('Specificity \nTrue Negative rate',sp)
file1.write('Precision (or) Positive Predicted Value'+','+str(prec)+'\n')
print('Precision \nPositive Predicted Value',prec)
file1.write('False positive rate'+','+str(fpr)+'\n')
print('False positive rate',fpr)
file1.write('Matthews correlation coefficient'+','+str(mcc)+'\n')
print('Matthews correlation coefficient',mcc)
file1.write('F_0.5'+','+str(f_0)+'\n')
print('F_0.5',f_0)
file1.write('F_1'+','+str(f_1)+'\n')
print('F_1',f_1)
file1.write('F_2'+','+str(f_2)+'\n')
print('F_2',f_2)
file1.close()

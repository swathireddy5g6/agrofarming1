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
b=readcsv('C:\\Users\\akhil\\Downloads\\chikku\\Dataset\\MainDataSet.csv')
temp=len(b)
print(b[0])
s=seperate(b)
total_entered=0
total_completed=0
l=[]
for i in [8,0,1,3,7,4]:
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
print(len(l[1]))
rules=[]
norules=[]
co=0
for s_soil in l[0]:
    com=len(l[0])-co
    print(com)
    #print(s_state+' Started \n')
    for s_state in l[1]:
        for s_district in dist[s_state]:
            #print(s_soil)
            for s_season in l[3]:
                for s_water in l[4]:
                    for i in range(1,temp):
                        if(s_soil==s[i][8] and s_state==s[i][0] and s_district==s[i][1] and s_season==s[i][3] and s_water==s[i][7]):
                            rules.append([s_soil,s_state,s_district,s_season,s_water,s[i][4]])
                            print(s_soil,s_state,s_district,s_season,s_water,s[i][4])
for s_soil in l[0]:
    com=len(l[0])-co
    print(com)
    #print(s_state+' Started \n')
    for s_state in l[1]:
        for s_district in dist[s_state]:
            #print(s_soil)
            for s_season in l[3]:
                for s_water in l[4]:
                    for s_crop in l[5]:
                        for i in range(1,temp):
                            if([s_soil,s_state,s_district,s_season,s_water,s_crop] not in rules and [s_soil,s_state,s_district,s_season,s_water,s_crop] not in norules):
                                norules.append(s_soil,s_state,s_district,s_season,s_water,s_crop)
                                print(s_soil,s_state,s_district,s_season,s_water,s_crop)
                        
    co=co+1







                        

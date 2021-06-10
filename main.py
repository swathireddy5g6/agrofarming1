from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import Sending_information

def Interface1():
        root =tk.Tk()
        root.title("Agro Farming Using Machine Learning")
        root.geometry("10000x10000+0+0")
        c=Canvas(root,bg="black",height="10000",width="10000")
        img=ImageTk.PhotoImage(Image.open("C:\chikku\chikku\\akh.jpg"))
        c.create_image(0,0,anchor=NW,image=img)
    

        txt="                                    Welcome To the Engineered Farming                                    "
        heading=Label(root,text=txt,font=("arial",40,"bold"),fg="steelblue",bg="black").pack()


        label1=Label(root,text="Enter soil:",font=("arial", 22,"bold"),fg="black").place(x=300,y=200) #Label === Enter Soil
        l=[]
        Season="'Default Choice'"
        State="'Default Choice'"
        Soil="'Default Choice'"
        District="'Default Choice'"
        Water="'Default Choice'"
        def Soil(selected_item):
                global Soil
                Soil=repr(selected_item.strip())
                print(Soil)
        l=[]
        def District(selected_item):
                global District
                District=repr(selected_item.strip())
                l.append(District)
                print(District)
        def Water(selected_item):
                global Water
                Water=repr(selected_item.strip())
                print(Water)
        def Season(selected_item):
                global Season
                Season=repr(selected_item.strip())
                print(Season)
        def State(selected_item):
                global State
                State=repr(selected_item.strip())
                print(State)
                dist={'Default Choice':['Enter State'],'Andhra Pradesh':['ANANTAPUR', 'CHITTOOR', 'EAST GODAVARI', 'GUNTUR', 'KADAPA', 'KRISHNA',
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
                      'Chandigarh':['CHANDIGARH'],
                      'Goa':['NORTH GOA', 'SOUTH GOA'],
                      'Gujarat':['AHMADABAD', 'AMRELI', 'ANAND', 'BANAS KANTHA', 'BHARUCH', 'BHAVNAGAR', 'DANG', 'DOHAD',
                                 'GANDHINAGAR', 'JAMNAGAR', 'JUNAGADH', 'KACHCHH', 'KHEDA', 'MAHESANA', 'NARMADA', 'NAVSARI',
                                 'PANCH MAHALS', 'PATAN', 'PORBANDAR', 'RAJKOT', 'SABAR KANTHA', 'SURAT', 'SURENDRANAGAR', 'TAPI',
                                 'VADODARA', 'VALSAD'],
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
                                     'DINAJPUR UTTAR','HOOGHLY', 'HOWRAH', 'JALPAIGURI', 'MALDAH', 'MEDINIPUR EAST', 'MEDINIPUR WEST', 'MURSHIDABAD', 'NADIA', 'PURULIA']
              
              
             }
                name3=StringVar()
                max_len = 38
                names3 = tk.StringVar()
                choices3 = dist[State[1:len(State)-1]]
                padded_choices = [x+' '*(max_len-len(x)) for x in choices3]
                name3= ttk.OptionMenu(root, names3, 'Default Choice', *padded_choices,command=District).place(x=700,y=410)
        
                
        
        name1=StringVar()
        max_len = 38
        names1 = tk.StringVar()
        choices = ['Default Choice','alluvial soil', 'black cotton soil', 'black soil', 'clay loam soil', 'dry sandy soil', 'fertile soil',
                   'laterite soil', 'loam soil', 'sandy loam soil', 'sandy soil', 'silt loam soil', 'well drained loam soil']
        padded_choices = [x+' '*(max_len-len(x)) for x in choices]
        name1= ttk.OptionMenu(root, names1,'Select Choice', *padded_choices,command=Soil).place(x=700,y=210)


        label2=Label(root,text="Enter State:",font=("arial",20,"bold"),fg="black").place(x=300,y=300) #Label2 ===Enter Area
        name2=StringVar()
        max_len = 38
        names2 = tk.StringVar()

        choices = ['Default Choice','Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
                   'Chhattisgarh', 'Dadra and Nagar Haveli', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir',
                   'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland',
                   'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                   'Uttarakhand', 'West Bengal']
        padded_choices = [x+' '*(max_len-len(x)) for x in choices]
        name2= ttk.OptionMenu(root, names2, 'Select Choice', *padded_choices,command=State).place(x=700,y=310)
        
        label3=Label(root,text="Enter District:",font=("arial",20,"bold"),fg="black").place(x=300,y=400) #label3 === Enter Water Level
        
        
    
        label4=Label(root,text="Enter Water Level:",font=("arial",20,"bold"),fg="black").place(x=300,y=500) #label3 === Enter Water Level
        name4=StringVar()
        max_len = 38
        names4 = tk.StringVar()
        choices = ['Default Choice','low','medium','high']
        padded_choices = [x+' '*(max_len-len(x)) for x in choices]
        name4= ttk.OptionMenu(root, names4, 'Select Choice', *padded_choices,command=Water).place(x=700,y=510)

        label5=Label(root,text="Enter Season:",font=("arial",20,"bold"),fg="black").place(x=300,y=600) #label3 === Enter Water Level
        name5=StringVar()
        max_len = 38
        names5 = tk.StringVar()
        choices = ['Default Choice','Kharif', 'Whole Year ', 'Autumn', 'Rabi', 'Summer', 'Winter']
        padded_choices = [x+' '*(max_len-len(x)) for x in choices]
        name5= ttk.OptionMenu(root, names5, 'Select Choice', *padded_choices,command=Season).place(x=700,y=610)
        def sub():
                global Soil
                global State
                global District
                global Season
                global Water
                try:
                        if(Soil[1:len(Soil)-1]=='Default Choice'):
                                messagebox.showinfo("Missing Value", "Select Soil")
                except NameError:
                        messagebox.showerror('Missing Soil','Please Select Soil')
                try:
                        if(State[1:len(State)-1]=='Default Choice'):
                                messagebox.showinfo("Missing Value", "Select State")
                except NameError:
                        messagebox.showerror('Missing Soil','Please Select State')
                try:
                        if(District[1:len(District)-1]=='Default Choice' and District[1:len(District)-1]=='Enter State'):
                                messagebox.showinfo("Missing Value", "Select District")
                except NameError:
                        messagebox.showerror('Missing Soil','Please Select District')
                try:
                        if(Season[1:len(Season)-1]=='Default Choice'):
                            messagebox.showinfo("Missing Value", "Select Season")
                except NameError:
                        messagebox.showerror('Missing Soil','Please Select Season')
                try:
                        if(Water[1:len(Water)-1]=='Default Choice'):
                                messagebox.showinfo("Missing Value", "Select Water Level")
                except NameError:
                        messagebox.showerror('Missing Water','Please Select Water')
                else:
                        Soil1=Soil[1:len(Soil)-1]
                        State1=State[1:len(State)-1]
                        District1=District[1:len(District)-1]
                        Season1=Season[1:len(Season)-1]
                        Water1=Water[1:len(Water)-1]
                        print(State1,District1,Season1,Soil1,Water1)
                        l=Sending_information.Collect_crops(State1,District1,Season1,Soil1,'low')
                        m=Sending_information.Collect_crops(State1,District1,Season1,Soil1,'medium')
                        h=Sending_information.Collect_crops(State1,District1,Season1,Soil1,'high')
                        #Sending_information.show_crops(l,m,h)
                        low_year=Sending_information.Collect_Data(l,State1,District1,Season1,Soil1,'low')
                        medium_year=Sending_information.Collect_Data(m,State1,District1,Season1,Soil1,'medium')
                        high_year=Sending_information.Collect_Data(h,State1,District1,Season1,Soil1,'high')
                        low_year=Sending_information.Best_Crop(low_year)
                        medium_year=Sending_information.Best_Crop(medium_year)
                        high_year=Sending_information.Best_Crop(high_year)
                        #print(low_year,medium_year,high_year)
                        Sending_information.plotGraph(root,low_year,medium_year,high_year,State1,District1,Season1,Soil1)
                        
                        
                
        submit=Button(root,text="SUBMIT",width=20,height=1,bg='orange',command=sub).place(x=500,y=700)
        cancel=Button(root,text="QUIT",width=20,height=1,bg='orange',command=root.destroy).place(x=700,y=700)
        

        #out1=Text(root,width=20,height=1,wrap=WORD).place(x=50,y=710)
        #w = Scale(root, from_=0, to=600).place(x=10,y=1000)
        c.pack()
        root.mainloop()
Interface1()


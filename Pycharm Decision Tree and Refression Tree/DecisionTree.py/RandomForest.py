import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('C:\\Users\\akhil\\Downloads\\chikku\\Dataset\\MainDataSet.csv')
df1 = pd.read_csv('C:\\Users\\akhil\\Downloads\\chikku\\Dataset\\MainDataSet.csv')
a='Crop'
last_col=df.pop(a)
df.insert(8,a,last_col)
le_State_Name=LabelEncoder()
le_District_Name=LabelEncoder()
le_Season=LabelEncoder()
le_Water_Level=LabelEncoder()
le_Soil=LabelEncoder()
le_Crop=LabelEncoder()
df['State_Name']=le_State_Name.fit_transform(df['State_Name'])
df['District_Name']=le_District_Name.fit_transform(df['District_Name'])
df['Season']=le_Season.fit_transform(df['Season'])
df['Water_Level']=le_State_Name.fit_transform(df['Water_Level'])
df['Soil']=le_Soil.fit_transform(df['Soil'])
df['Crop']=le_Crop.fit_transform(df['Crop'])
df.pop('Area')
df.pop('Production')
df.pop('Crop_Year')
X=df.iloc[:,:-1] # independent features
Y=df.iloc[:,-1] # dependent features
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
print('Splitted succesfull')
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train,y_train)
model.score(X_train,y_train)
model.predict(X_train)
print('Model build successful')
print('Training Data Score:',model.score(X_train,y_train))
print('Training Data Score:',model.score(X_test,y_test))

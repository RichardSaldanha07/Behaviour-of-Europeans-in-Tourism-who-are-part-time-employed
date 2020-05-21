#Author: Richard Saldanha
#Student id : 18183034
# Cource : Master of Science in Data Analytics
# Batch: A
# Subject: Data Intensive Architecture
# Code: For Cleaning of the datasets.
import pandas as pd
import numpy as np
df1 = pd.read_csv('E:\\DataIntensive\\Project\\Dataset\\mainreasonforparttime.csv')
df1
# Removing Duplicate values from the dataset
df1.drop_duplicates(keep=False,inplace=True)
df1
#Handling of missing values by replacing them with 0
df2 = df1.fillna(0)
df2
#Merging of the two column TIME and GEO to create a unique column country_period for merging of the two datasets 
df2['country_period'] = df2['GEO'].map(str) + '-' + df2['TIME'].map(str)
df2
# Renaming of the column headers according to standard naming conventions for column headers
df2.rename(columns={'TIME':'time',
                    'GEO':'country',
                    'SEX':'gender_Female_and_male',
                    'AGE':'age',
                    'REASON':'reason',
                    'UNIT':'unit',
                    'Value':'value_in_percent',
                    }, 
                 inplace=True)
df3 = df2[['time','country','gender_Female_and_male','age','reason','unit','value_in_percent','country_period']]
df3
# converting the ready dataframe to csv file ready_mainreasonforparttime
df3.to_csv('E:\\DataIntensive\\Project\\Dataset\\ready_mainreasonforparttime.csv')
df4 = pd.read_csv('E:\\DataIntensive\\Project\\Dataset\\participationintourismforpersonalpurposes.csv')
df4
# Removing Duplicate values from the dataset
df4.drop_duplicates(keep=False,inplace=True)
df4
# Replacing the Missing value as indicated in the dataset (":") with NaN
df4['Value'].replace(':', np.nan, inplace= True)
df4
#Handling of missing values by replacing them with 0
df5 = df4.fillna(0)
df5
#Merging of the two column TIME and GEO to create a unique column country_period for merging of the two datasets 
df5['country_period'] = df5['GEO'].map(str) + '-' + df5['TIME'].map(str)
df5
# Renaming of the column headers according to standard naming conventions for column headers
df5.rename(columns={'TIME':'time',
                    'GEO':'country',
                    'UNIT':'unit',
                    'PARTNER':'partner',
                    'Value':'value_in_percent',
                    }, 
                 inplace=True)
df6 = df5[['time','country','unit','partner','value_in_percent','country_period']]
df6
# converting the ready dataframe to csv file ready_participationintourismforpersonalpurpose
df6.to_csv('E:\\DataIntensive\\Project\\Dataset\\ready_participationintourismforpersonalpurpose.csv')

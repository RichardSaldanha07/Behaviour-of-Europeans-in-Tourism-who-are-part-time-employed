#Author: Richard Saldanha
#Student id : 18183034
# Cource : Master of Science in Data Analytics
# Batch: A
# Subject: Data Intensive Architecture
# Code: To find out the Pearson Correaltion Coefficient in Python and carry out Visualization.
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv('D:\\NCI\\practice-labs\\Data Intensive\\AWS\\.ssh\\correlation.csv', header=None)
df1
# Handling of missing values
missing_values = ["0"]
df1 = pd.read_csv('D:\\NCI\\practice-labs\\Data Intensive\\AWS\\.ssh\\correlation.csv',na_values=missing_values, header=None)
df1.columns = ["country_year","total_parttime","total_tourism"]
df1 = df1.dropna(how='any')
df1
# calculating Pearson Coefficient of Correlation
correlation = df1.corr(method="pearson")
correlation
import matplotlib.pyplot as plt
import pandas as pd

# gca stands for 'get current axis'
ax = plt.gca()
plt.xlabel('country_year')
plt.ylabel('Percentage of Population')
df1.plot(kind='line',x='country_year',y='total_parttime',ax=ax, color='red')
df1.plot(kind='line',x='country_year',y='total_tourism',ax=ax, color='green')
plt.show()
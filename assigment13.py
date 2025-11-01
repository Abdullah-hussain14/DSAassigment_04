import pandas as pd
import numpy as np
ImportWarning
# Warning.filterwarning('Ignore')

df = pd.read_csv('Salaries.csv')

df =df[~((df['EmployeeName']== 'Not provided') | (df['JobTitle']=='Not provided'))]
print(df.tail(10))
print(df.shape[0])

df['BasePay'] = df['BasePay'].replace('Not Provided',0)
df['BasePay']= df['BasePay'].astype(float)

df['OvertimePay'] = df['OvertimePay'].replace('Not Provided',0)
df['OvertimePay']= df['OvertimePay'].astype(float)

df['OtherPay'] = df['OtherPay'].replace('Not Provided',0)
df['OtherPay']= df['OtherPay'].astype(float)

df['Benefits'] = df['Benefits'].replace('Not Provided',0)
df['Benefits']= df['Benefits'].astype(float)
# print(df.info())

record = df[df['BasePay']>200000]
print(record[['EmployeeName','BasePay']])

print(df[df.JobTitle.str.contains('MANAGER',case=False)])

retrive =df[['EmployeeName','JobTitle','TotalPay']]
print(retrive)

overtime = df[df['OvertimePay'] == 0]
print(overtime['EmployeeName'].count())

result = df[df['TotalPay']>300000].groupby('JobTitle') ['TotalPay'].sum()
print(result)

result1 = (
    df.groupby('JobTitle', as_index= False)['TotalPayBenefits'].mean().sort_values('TotalPayBenefits',ascending=False).head(5)
    )
print(result1)

df['Benefits']=df['Benefits'].replace(' ',0)

result3 = (
    df.sort_values('TotalPay',ascending=False)
    .groupby('Year',as_index=False)
    .head(1)[['Year','EmployeeName','TotalPay']]
)
print(result3)

result4 = df.groupby('JobTitle')['EmployeeName'].count()
print(result4)
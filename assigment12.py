import pandas as pd
df = pd.read_csv("retail supermarket.csv")
print(df)
#Question 01
record = df[(df['Sales']> 500)&(df['Quantity'])]
print(record)
#Question 02
record2= df[(df['Discount']>0.5)&(df['Profit']<0)]
print(record2)
#Question 03
record3= df[df['Region']== 'East']
print(record3[['Sales','Profit']])
#Question 04
count =df[(df['Segment']== 'Corporate')&(df['Region']== 'Central')].shape[0]# without shape it'll show complete data the total rows and columns
print(count)
#Question 05
count1 =df[(df['Category']== 'Furniture') & (df['Sub-Category']!= 'Chairs')]
print(count1)
#Question 06
count2 =df[(df['Discount']>0.3) & (df['Profit']>0)]
print(count2)
#Question 07
count3 =df[(df['Quantity']> 5) & (df['Category']== 'Technology')]
print(count3[['Profit']])
#Question 08
print(df.iloc[0:5,[0,1,9]])
#Question 09
count4 =df[(df['Sales']> 100) & (df['Quantity']>3)&(df['Segment']=='Home Office')]
print(count4[['Sales','Quantity','Segment']])
#Question 10
df['profit_magin'] = (df['Profit'] / df['Sales'])
profit_margin = df[df['profit_magin']>0.3]
print(profit_margin)


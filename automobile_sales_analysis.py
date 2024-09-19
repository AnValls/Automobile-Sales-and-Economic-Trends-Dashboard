import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('automobile_sales_dataset.csv')

yearly_sales = df.groupby('Year')['Automobile_Sales'].sum()

plt.figure(figsize=(10, 6))
plt.plot(yearly_sales, marker='o')
plt.title('Yearly Automobile Sales Fluctuation')
plt.xlabel('Year')
plt.ylabel('Automobile Sales')
plt.grid(True)
plt.show()


df_recession = df[df['Recession'] == 1] 

plt.figure(figsize=(12, 8)) 
sns.lineplot(x='Year', y='Automobile_Sales', hue='Vehicle_Type', data=df_recession, marker='o')
plt.title('Sales Trends by Vehicle Type During Recession Periods') 
plt.xlabel('Year')  
plt.ylabel('Automobile Sales')  
plt.grid(True)
plt.show()  


plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Automobile_Sales', hue='Vehicle_Type', style='Recession', data=df, markers=True)
plt.title('Sales Trends by Vehicle Type: Recession vs Non-Recession')
plt.xlabel('Year')
plt.ylabel('Automobile Sales')
plt.grid(True)
plt.show()


df_non_recession = df[df['Recession'] == 0]

fig, axes = plt.subplots(2, 1, figsize=(12, 8))

axes[0].plot(df_recession.groupby('Year')['GDP'].mean(), color='r', marker='o')
axes[0].set_title('GDP During Recession Periods')
axes[0].set_ylabel('GDP')

axes[1].plot(df_non_recession.groupby('Year')['GDP'].mean(), color='g', marker='o')
axes[1].set_title('GDP During Non-Recession Periods')
axes[1].set_ylabel('GDP')

plt.tight_layout() 
plt.show()




plt.figure(figsize=(10, 6))
plt.scatter(df['Seasonality_Weight'], df['Automobile_Sales'], s=df['Automobile_Sales']/100, alpha=0.5)
plt.title('Impact of Seasonality on Automobile Sales')
plt.xlabel('Seasonality Weight')
plt.ylabel('Automobile Sales')
plt.show()



plt.figure(figsize=(10, 6))
plt.scatter(df_recession['Price'], df_recession['Automobile_Sales'], alpha=0.5)
plt.title('Price vs Sales Volume During Recessions')
plt.xlabel('Average Vehicle Price')
plt.ylabel('Automobile Sales')
plt.grid(True)
plt.show()




ad_expenditure = df.groupby('Recession')['Advertising_Expenditure'].sum()

plt.figure(figsize=(8, 8))
plt.pie(ad_expenditure, labels=['Non-Recession', 'Recession'], autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightcoral'])
plt.title('Advertising Expenditure: Recession vs Non-Recession')
plt.show()



ad_expenditure_by_type = df_recession.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()

plt.figure(figsize=(8, 8))
plt.pie(ad_expenditure_by_type, labels=ad_expenditure_by_type.index, autopct='%1.1f%%', startangle=90)
plt.title('Advertisement Expenditure by Vehicle Type During Recession')
plt.show()



plt.figure(figsize=(12, 6))
sns.lineplot(x='Unemployment_Rate', y='Automobile_Sales', hue='Vehicle_Type', data=df_recession, marker='o')
plt.title('Effect of Unemployment Rate on Sales by Vehicle Type During Recession')
plt.xlabel('Unemployment Rate')
plt.ylabel('Automobile Sales')
plt.grid(True)
plt.show()



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\ML\cardata.csv')
df.head()
print(df.head())
print(df.tail())
print(df.info())
print(df.nunique())
print(df.nunique()) 
print(df.isnull().sum())
print(df.isnull().sum())
print((df.isnull().sum()/(len(df)))*100)
print((df.isnull().sum()/(len(df)))*100)
print(df.columns)


# 1. Bar Chart - Cars by Fuel Type
df['Fuel_Type'].value_counts().plot(kind='bar')
plt.title('Cars by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Number of Cars')
plt.show()

# 2. Pie Chart - Cars by Transmission
df['Transmission'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Cars by Transmission')
plt.ylabel('')
plt.show()

# 3. Histogram - Selling Price by Fuel Type
df.groupby('Fuel_Type')['Selling_Price'].plot(kind='hist', alpha=0.5, legend=True)

plt.title('Selling Price by Fuel Type')
plt.xlabel('Selling Price')
plt.ylabel('Number of Cars')
plt.show() 

# 4. Scatter Plot - Kms Driven vs Selling Price
plt.scatter(df['Kms_Driven'], df['Selling_Price'])
plt.title('Kms Driven vs Selling Price')
plt.xlabel('Kms Driven')
plt.ylabel('Selling Price')
plt.show()
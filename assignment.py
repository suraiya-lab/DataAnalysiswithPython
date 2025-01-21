import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('Salary_data.csv')
#data.plot(kind='line',x='YearExperience',y='Salary')
#data.plot(kind='line',x='YearsExperience',y='Salary',marker='o',ls='--',color='g',linewidth='3')
plt.plot(data["YearsExperience"],data["Salary"],color='r')
plt.scatter(data["YearsExperience"],data["Salary"],color='g')
#data.plot(kind='hist')
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.title("Experience Vs Salary")
plt.grid(color='r')
#plt.grid(axis='x',color='r')
plt.show( )
print(data)


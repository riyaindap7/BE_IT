#import necessary libraries 
import pandas as pd
import matplotlib.pyplot as plt
#load the csv file 
data=pd.read_csv("C:/Users/RIYA/OneDrive/Desktop/python/employees_new.csv")
print(data)

data.columns
#get the detailed information of all the columns and thier types
data.info()

#extract only first 100 records and apply visualization on it
data = data[0:100]
#create bar chart
x = data["First Name"].astype(str)
y = data["Salary"]
plt.bar(x,y,label="Employee",color = "red")
plt.xlabel("Employee name")
plt.ylabel("Salary")
plt.title("Employee Details")
plt.legend()
plt.show()

#read the file again and print histogram
data=pd.read_csv("C:/Users/RIYA/OneDrive/Desktop/python/employees_new.csv")
y = data["Salary"]
plt.hist(y,bins=100 ,histtype = "bar", rwidth=0.8, color = 'cyan')
plt.grid(axis='y', alpha=0.75)
plt.xlabel("Employee ages")
plt.ylabel("no of employees ")
plt.title("Employee Details")
plt.legend()
plt.show()

#now extract team colums and create pie chart

X = data.groupby("Team").nunique()

#Creating pie chart only for first 10 records of the given file

labels = data.Team[0:10]
#labels
v = data.Salary[0:10]
e= [0] * len(labels)
plt.pie(v,explode=e,labels=labels,autopct='%1.3f%%',shadow=True,startangle=90)
plt.show()

#creating scatter plot, read the file again
data=pd.read_csv("C:/Users/RIYA/OneDrive/Desktop/python/employees_new.csv")
data = data[0:20]
y =data["Bonus %"]
x= data["Team"].astype(str)
plt.scatter(x,y,marker="*")
#plt.scatter(x,y,marker="v",alpha = 0.5)
plt.xticks(rotation=90)
plt.show()

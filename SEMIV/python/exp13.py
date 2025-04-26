"""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd       #also there is opnyxl
df=pd.read_excel("C:\\Users\\RIYA\\OneDrive\\Desktop\\python\\employees_new.xlsx")
#print(df)
#print(df.columns)
#print(df.head(5))
#print(df.tail(2))
#print(df.info())
#print(df.describe())
#print(df.shape)
#print("minimum bonus:")
#min_bonus=(df["Bonus %"].min())
#print(min_bonus)
#print("salary in range>=101004")
#print(df[df.Salary>=101004])
#print(df["Team"].value_counts())
#print(df["Team"].value_counts().sum())
#print(df.isnull())
#print(df.isnull().sum())
#loc=df.iloc[:1:3]
#print(loc)
print(df.loc[:,"Gender":"Salary"])

import matplotlib.pyplot as plt
import numpy as np
labels='cricket','Hockey','Tennis','Football'
v=[40,20,90,80]
e=(0,0,0.1,0)
plt.pie(v,explode=e,labels=labels,autopct='%1.3f%%',shadow=True,startangle=90)
plt.show()"""

import matplotlib.pyplot as plt
import numpy as np
import math
x=np.linspace(0,10,50)
y=np.sin(x)
plt.scatter(x,y,marker="v")
plt.scatter(x,y,marker="v",alpha=0.5)
plt.show()






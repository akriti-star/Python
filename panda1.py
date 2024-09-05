import pandas as pd
import numpy as np
df = pd.DataFrame(data=np.arange(0,20).reshape(5,4),index=["Row1","Row2","Row3","Row4","Row5"],
                  columns=["Column1","Column2","Column3","Column4"])
# print(df)
# print(df[["Column1","Column2"]])
# print(df.loc[["Row1","Row2"]])
print(df.describe)
print(df.iloc[0:,0::3])
#converting into array
print(df.iloc[:,1:].values)
#checking if null value is there
print(df.isnull().sum())
print(df[df<2])
# print(df["Column1"].unique)
print(df["Column1"].value_counts())
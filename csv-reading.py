from io import StringIO
import pandas as pd

# df = pd.read_csv('C:\\Users\\ADMIN\\Downloads\\Orders_Central (2).csv', encoding='ISO-8859-1',usecols=['Row ID','Order ID','Ship Mode'])
# print(df.head())  # This will display the first few rows of the dataframe
# df.to_csv('test.csv',index= False)#This will save the that data as csv file and without indexes
data = ('Col1,Col2,Col3\n'
        'a,b,1\n'
        'x,y,2\n'
        'd,c')
print(StringIO(data))
print(pd.read_csv(StringIO(data)))
# d1=pd.read_csv(StringIO(data),dtype={'Col1':int,'Col2':float})
# print(d1.info())
print(pd.read_csv(StringIO(data),index_col=0))
print(pd.read_csv(StringIO(data),usecols=['Col2','Col3'],index_col=0))


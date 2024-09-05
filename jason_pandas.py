import pandas as pd
import json

# data = {"name": ["Jason", "Michael"], "age": [25, 30]}  # Example dictionary
# json_data = json.dumps(data)  # Convert the dictionary to JSON string

# df = pd.read_json(json_data)
# print(df)
data1 = pd.DataFrame([["a","b"],["c","d"]],index = ["Row1","Row2"],columns= ["Col1","Col2"]
)

print(data1.to_json(orient="index"))
print(data1.to_json(orient='columns'))
print(data1.to_json(orient='records'))
print(data1.to_json(orient='split'))
print(data1.to_json(orient='table'))
schema = {"schema":{"fields":[{"name":"index","type":"string"},{"name":"Col1","type":"string"},{"name":"Col2","type":"string"}],"primaryKey":["index"],"pandas_version":"1.4.0"},"data":[{"index":"Row1","Col1":"a","Col2":"b"},{"index":"Row2","Col1":"c","Col2":"d"}]}
sc = json.dumps(schema)
print(pd.read_json(sc,orient='table'))
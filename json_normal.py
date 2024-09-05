import pandas as pd
from pandas import json_normalize

# Example nested JSON data
data = {
    "students": [
        {
            "name": "Alice",
            "age": 23,
            "courses": [
                {"name": "Mathematics", "grade": "A"},
                {"name": "Physics", "grade": "B+"}
            ],
            "address": {
                "city": "New York",
                "state": "NY"
            }
        },
        {
            "name": "Bob",
            "age": 24,
            "courses": [
                {"name": "Chemistry", "grade": "A-"},
                {"name": "Biology", "grade": "B"}
            ],
            "address": {
                "city": "Los Angeles",
                "state": "CA"
            }
        }
    ]
}

# Normalizing the nested JSON data
df = json_normalize(data['students'], 
                    record_path='courses', 
                    meta=['name', 'age', ['address', 'city'], ['address', 'state']],
                    meta_prefix='student_')

print(df)

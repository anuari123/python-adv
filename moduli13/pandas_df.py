import pandas as pd

data = {
    'Name': ['alice', 'bob', 'john'],
    'Age':[25,30,26],
    'City':['new york','prishtina', 'san francisco']
}
df = pd.DataFrame(data)
print(df)

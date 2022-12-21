import pandas as pd

df=pd.read_csv('combined.csv')
print(df.shape)
a=df.columns.tolist()

print(a.index('open_NVDA'))
print(len(set(a)))
a.insert(0, a[1])
a.pop(2)
print(len(set(a)))
df=df[a]
print(df.shape)
df.to_csv('combined.csv', index=False)
import pandas

# Read the data from the CSV files
data1954 = pandas.read_csv("datasets/economic/Indust_prod_semi_historical.csv")
data1959 = pandas.read_csv("datasets/economic/PCE_historical.csv")
data1984 = pandas.read_csv("datasets/economic/PPI_semi_historical.csv")


# Merge the data
print(data1954.shape, (2022-1954)*12)
print(data1959.shape, (2022-1959)*12)
print(data1984.shape, (2022-1984)*12)

#825-
print(data1954[371:373]) # 825-454 = 371
print(data1959[311:313])  # 765 - 454 = 311
print(data1984[0:2])


data1954=data1954[371:].reset_index(drop=True)
data1959=data1959[311:].reset_index(drop=True)

print(data1954.columns)

data1954=data1954.drop(columns=['level_1'])
data1959=data1959.drop(columns=['level_1'])
data1984=data1984.drop(columns=['level_1'])

final=pandas.merge(data1954,data1959,on="DATE")
final=pandas.merge(final,data1984,on="DATE")
final.rename(columns={"0_x": "IPB53122S", "0_y": "PCE", "0": "PCU33443344"}, inplace=True)
print(final.shape)
print(final.head())

final.to_csv("mergedData/monthlyData.csv", index=False)


#mergedData = pandas.merge(data1954, data1959, on="DATE")
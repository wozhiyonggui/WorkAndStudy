import pandas as pd

path_result_battlepass = r'E:\WorkAndStudy\Python\result-cn\result_battlepass.xlsx'

data = pd.read_excel(path_result_battlepass)
data_freedrop = data['FreeDrop(uint32)']
data_freedrop = data_freedrop.fillna('2')
data_freedrop = [int(i) for i in data_freedrop]

print(data_freedrop)

data_id = data['id(key.uint32)*']
data_id = [int(i) for i in data_id]
print(data_id)

compare = data_freedrop == data_id
print(compare)
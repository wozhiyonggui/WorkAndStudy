import pandas as pd

#操作前先手动全选表格转格式为文本
path_config_battlepass = r'E:\WorkAndStudy\Python\config-cn\battlepass.xlsx'
path_config_drop = r'E:\WorkAndStudy\Python\config-cn\drop.xlsx'
path_result_battlepass = r'E:\WorkAndStudy\Python\result-cn\result_battlepass.xlsx'


a = 100001
b = 100020
bpid = list(range(a, b+1))


data_BPLevel = pd.read_excel(path_config_battlepass, sheet_name='BPLevel')
bplevel = data_BPLevel['Id(key.uint32)*'].isin(bpid)
sheet_BPLevel = data_BPLevel[bplevel]
#免费奖励
sheet1 = sheet_BPLevel.drop(columns=['GotoType(uint32)', 'SeasonId(uint32)*', 'ImportantLevel(uint32)', 'SpecialGift(uint32)', 'FreePicRate(float)', 'PayPicRate(float)', 'Exp(uint32)*', 'Id(key.uint32)*', 'PaidDrop(uint32)', 'PaidBox(uint32)', 'Cost(uint32)', 'PaidReward(array.uint32)'])
dropid_BPLevel_free = sheet1['FreeDrop(uint32)']
dropset_BPLevel_free = [i for i in dropid_BPLevel_free.values if not pd.isna(i)]
dropset_BPLevel_free = [int(i) for i in dropset_BPLevel_free]
data_drop_free = pd.read_excel(path_config_drop, sheet_name='drop')
drop_columns_free = data_drop_free.columns.values
dst_free = pd.DataFrame(columns=drop_columns_free)
for dropid_free in dropset_BPLevel_free:
    oneidx_free = data_drop_free["id(key.uint32)*"] == dropid_free
    oneline_free_ = data_drop_free[oneidx_free].values
    if len(oneline_free_)>0:
        oneline_free = oneline_free_[0]
        dst_free.loc[len(dst_free)] = oneline_free
    else:
        print(dropid_free, '找不到')

sheet2 = dst_free.drop(columns=['limitRepeated(array.string)', 'showId(uint32)', 'dropPackage(array.string)', 'limitExtraDropId(uint32)', 'guaranteeDropList(array.string)', 'guaranteeXRound(array.string)', 'typeId(uint32)*'])

excel_writer = pd.ExcelWriter(path_result_battlepass)
sheet1.to_excel(excel_writer, sheet_name='bplevel', index=False)
sheet2.to_excel(excel_writer, sheet_name='bplevel', index=False, startcol=5)
excel_writer.save()
















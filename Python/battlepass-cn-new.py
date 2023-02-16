import pandas as pd

#a,b是编号
a = 100001
b = 100080

#操作前先手动全选表格转格式为文本
path_config_battlepass = r'E:\WorkAndStudy\Python\config-cn\battlepass.xlsx'
path_config_drop = 'E:\WorkAndStudy\Python\config-cn\drop.xlsx'
path_result_battlepass = r'E:\WorkAndStudy\Python\result-cn\result_battlepass.xlsx'

data_BPLevel = pd.read_excel(path_config_battlepass, sheet_name='BPLevel')
bpid = list(range(a, b+1))
bplevel = data_BPLevel['Id(key.uint32)*'].isin(bpid)

#付费奖励
sheet_BPLevel = data_BPLevel[bplevel]
dropid_BPLevel_paid = sheet_BPLevel['PaidDrop(uint32)']
dropset_BPLevel_paid = [i for i in dropid_BPLevel_paid.values if not pd.isna(i)]
dropset_BPLevel_paid = [int(i) for i in dropset_BPLevel_paid]
data_drop_paid = pd.read_excel(path_config_drop, sheet_name='drop')

drop_columns_paid=data_drop_paid.columns.values
dst_paid = pd.DataFrame(columns=drop_columns_paid)
for dropid_paid in dropset_BPLevel_paid:
    oneidx_paid = data_drop_paid["id(key.uint32)*"] == dropid_paid
    oneline_paid_ = data_drop_paid[oneidx_paid].values
    if len(oneline_paid_)>0:
        oneline_paid = oneline_paid_[0]
        dst_paid.loc[len(dst_paid)] = oneline_paid
    else:
        print(dropid_paid, '找不到')

#免费奖励
sheet_BPLevel = data_BPLevel[bplevel]
dropid_BPLevel_free = sheet_BPLevel['FreeDrop(uint32)']
dropset_BPLevel_free = [i for i in dropid_BPLevel_free.values if not pd.isna(i)]
dropset_BPLevel_free = [int(i) for i in dropset_BPLevel_free]
data_drop_free = pd.read_excel(path_config_drop, sheet_name='drop')

drop_columns_free=data_drop_free.columns.values
dst_free = pd.DataFrame(columns=drop_columns_free)
for dropid_free in dropset_BPLevel_free:
    oneidx_free = data_drop_free["id(key.uint32)*"] == dropid_free
    oneline_free_ = data_drop_free[oneidx_free].values
    if len(oneline_free_)>0:
        oneline_free = oneline_free_[0]
        dst_free.loc[len(dst_free)] = oneline_free
    else:
        print(dropid_free, '找不到')

#打印到新表
excel_writer = pd.ExcelWriter(path_result_battlepass)
data_BPLevel[bplevel].to_excel(excel_writer, sheet_name='XXXXX')
dst_paid.to_excel(excel_writer, sheet_name='drop_paid')
dst_free.to_excel(excel_writer, sheet_name='drop_free')
excel_writer.save()




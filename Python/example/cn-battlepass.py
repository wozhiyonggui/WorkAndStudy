import sys
import pandas as pd
import argparse
 
#命令行解析器对象
parser = argparse.ArgumentParser(description='Demo of argparse') 
#命令行参数
parser.add_argument('--path_config_battlepass', type=str, default=r"D:\pythoncodes\jinyan-params\config-cn\battlepass.xlsx")
parser.add_argument('--path_config_drop', type=str, default=r"D:\pythoncodes\jinyan-params\config-cn\drop.xlsx")
parser.add_argument('--path_result_battlepass', type=str, default=r"D:\pythoncodes\jinyan-params\result-cn\result_battlepass.xlsx")

parser.add_argument('--a', type=int, default=0)
parser.add_argument('--b', type=int, default=0)

#获取参数
args = parser.parse_args()

#操作前先手动全选表格转格式为文本
#修改待测试BP起初ID参数
path_config_battlepass = args.path_config_battlepass
path_config_drop = args.path_config_drop
path_result_battlepass = args.path_result_battlepass
a = args.a
b = args.b

#读取battlepass
bpid = list(range(a, b+1))
data_BPLevel = pd.read_excel(path_config_battlepass, sheet_name='BPLevel')
bplevel = data_BPLevel['Id(key.uint32)*'].isin(bpid)
sheet_BPLevel = data_BPLevel[bplevel]
#免费奖励
sheet1 = sheet_BPLevel.drop(columns=['GotoType(uint32)', 'SeasonId(uint32)*', 'ImportantLevel(uint32)', 'SpecialGift(uint32)', 'FreePicRate(float)', 'PayPicRate(float)',
                                     'Exp(uint32)*', 'Id(key.uint32)*', 'PaidDrop(uint32)', 'PaidBox(uint32)', 'Cost(uint32)', 'PaidReward(array.uint32)'])
dropid_BPLevel_free = sheet1['FreeDrop(uint32)']
dropid_BPLevel_free = dropid_BPLevel_free.fillna(value='1')
dropset_BPLevel_free = [i for i in dropid_BPLevel_free.values] #if not pd.isna(i)]
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
sheet2 = dst_free.drop(columns=['limitRepeated(array.string)', 'showId(uint32)', 'dropPackage(array.string)', 'limitExtraDropId(uint32)', 'guaranteeDropList(array.string)',
                                'guaranteeXRound(array.string)'])

#付费奖励
sheet3 = sheet_BPLevel.drop(columns=['Id(key.uint32)*', 'SeasonId(uint32)*', 'Level(uint32)*', 'Exp(uint32)*', 'FreeDrop(uint32)', 'FreeBox(uint32)', 'Cost(uint32)', 'FreeReward(array.uint32)',
                                     'GotoType(uint32)', 'ImportantLevel(uint32)', 'SpecialGift(uint32)', 'FreePicRate(float)', 'PayPicRate(float)'])
dropid_BPLevel_paid = sheet3['PaidDrop(uint32)']
dropid_BPLevel_paid = dropid_BPLevel_paid.fillna(value='1')
dropset_BPLevel_paid = [i for i in dropid_BPLevel_paid.values if not pd.isna(i)]
dropset_BPLevel_paid = [int(i) for i in dropset_BPLevel_paid]
data_drop_paid = pd.read_excel(path_config_drop, sheet_name='drop')
drop_columns_paid = data_drop_paid.columns.values
dst_paid = pd.DataFrame(columns=drop_columns_paid)
for dropid_paid in dropset_BPLevel_paid:
    oneidx_paid = data_drop_paid["id(key.uint32)*"] == dropid_paid
    oneline_paid_ = data_drop_paid[oneidx_paid].values
    if len(oneline_paid_)>0:
        oneline_paid = oneline_paid_[0]
        dst_paid.loc[len(dst_paid)] = oneline_paid
    else:
        print(dropid_paid, '找不到')
sheet4 = dst_paid.drop(columns=['limitRepeated(array.string)', 'showId(uint32)', 'dropPackage(array.string)', 'limitExtraDropId(uint32)', 'guaranteeDropList(array.string)',
                                'guaranteeXRound(array.string)'])

#将数据写入新表
excel_writer = pd.ExcelWriter(path_result_battlepass)
sheet1.to_excel(excel_writer, sheet_name='bplevel', index=False)
sheet2.to_excel(excel_writer, sheet_name='bplevel', index=False, startcol=5)
sheet3.to_excel(excel_writer, sheet_name='bplevel', index=False, startcol=11)
sheet4.to_excel(excel_writer, sheet_name='bplevel', index=False, startcol=15)
excel_writer.save()
















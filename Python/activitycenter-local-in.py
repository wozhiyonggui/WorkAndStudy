import pandas as pd


#操作脚本前，手动将acttasks,actexchangeitem的对应行全部使用分列转文本

#配置目录
path_config_activitycenter = r'C:\Users\jinyan\PycharmProjects\Python\config\ActivityCenter.xlsx'
path_result_activitycenter = r'C:\Users\jinyan\PycharmProjects\Python\result\result_activitycenter.xlsx'
path_config_drop = r'C:\Users\jinyan\PycharmProjects\Python\config\drop.xlsx'

#输入需要测试的全部活动id
testactid = [219, 220]

#依次通过活动id进行操作
for actid in testactid:
    id = str(actid)
    path = r'C:\Users\jinyan\PycharmProjects\Python\result\a' + str(actid) + '.xlsx'
    #根据actid从子表ActivityCenter中获取需要的数据sheet1
    data1 = pd.read_excel(path_config_activitycenter, sheet_name='ActivityCenter')
    data1_1 = data1['id(key.uint32)*'] == actid
    data1_2 = data1[data1_1]
    sheet1 = data1_2.drop(columns=['FuncId(uint32)', 'ActId(uint32)', 'actvityName(string)', 'Commentary(string)', 'Bg(string)', 'sortType(uint32)*', 'sort(uint32)*', 'actvityType(uint32)*',
                        'TimeResetParams(array.string)', 'ShowTime(string)', 'actvityTag(uint32)', 'redPoint(uint32)', 'redPointParam(string)', 'actSystemName(string)', 'TabSort(uint32)',
                        'ProgressPool(uint32)', 'channnel(array.string)', 'location(array.uint32)', 'ActivityTips(array.string)', 'TipsColor(string)', 'TitleText(string)', 'TitleBorder(string)',
                        'IntroText(string)', 'IntroBorder(string)', 'Button(array.string)', 'isAds(bool)'])
    #获取sheet1中字段taskpool的值
    taskpool1 = sheet1['TaskPool(array.uint32)'].values[0]
    # #获取sheet1中字段exchangepool的值
    # exchangepool1 = sheet1['ExchangePool(array.uint32)'].values[0]
    #
    if type(taskpool1) == int:
        print('任务id： %d' % taskpool1)
        #根据actid从子表TaskPage中获取需要的数据sheet2
        data2 = pd.read_excel(path_config_activitycenter, sheet_name='TaskPage')
        data2_1 = data2['id(key.uint32)*'] == actid
        data2_2 = data2[data2_1]
        sheet2 = data2_2.drop(columns=['IsRand(bool)', 'TabName(string)'])
        #从sheet2中获取taskid的值，并转换成列表
        taskid1 = sheet2['TaskId(array.string)'].values[0].split('|')
        taskid1 = [int(i) for i in taskid1]
        #根据多个taskid从子表ActTasks中获取需要的数据sheet3
        data3 = pd.read_excel(path_config_activitycenter, sheet_name='ActTasks')
        data3_columns = data3.columns.values
        dst1 = pd.DataFrame(columns=data3_columns)
        for taskid in taskid1:
            data_taskid1 = data3['ID(key.uint32)*'] == taskid
            data_taskid2_ = data3[data_taskid1].values
            if len(data_taskid2_)>0:
                data_taskid2 = data_taskid2_[0]
                dst1.loc[len(dst1)] = data_taskid2
        sheet3 = dst1.drop(columns=['SubId(uint32)', 'Describe(string)', 'JumpLink(string)', 'ShareContent(string)', 'TimeLimitParams(array.string)', 'TimeResetParams(array.string)',
                                   'BarStyle(uint32)', 'Commentary(string)'])
        #从sheet3中获取dropid的值，如果是NA则填充1，然后转换成列表，并将列表中的所有数变成int
        dropid1 = sheet3['DropId(uint32)'].fillna(value='1')
        dropid1 = list(dropid1)
        dropid1 = [int(i) for i in dropid1]
        #根据多个dropid从表drop中获取需要的数据sheet4
        data_drop = pd.read_excel(path_config_drop, sheet_name='drop')
        data_drop_columns = data_drop.columns.values
        dst2 = pd.DataFrame(columns=data_drop_columns)
        for dropid in dropid1:
            data_dropid1 = data_drop['id(key.uint32)*'] == dropid
            data_dropid2_ = data_drop[data_dropid1].values
            if len(data_dropid2_)>0:
                data_dropid2 = data_dropid2_[0]
                dst2.loc[len(dst2)] = data_dropid2
        sheet4 = dst2.drop(columns=['limitRepeated(array.string)', 'showId(uint32)', 'dropPackage(array.string)', 'limitExtraDropId(uint32)', 'guaranteeDropList(array.string)',
                                'guaranteeXRound(array.string)'])

        excel_writer = pd.ExcelWriter(path)
        sheet1.to_excel(excel_writer, sheet_name=id, index=False)
        sheet2.to_excel(excel_writer, sheet_name=id, index=False, startrow=4)
        sheet3.to_excel(excel_writer, sheet_name=id, index=False, startrow=8)
        sheet3.to_excel(excel_writer, sheet_name='ActTasks-drop', index=False)
        sheet4.to_excel(excel_writer, sheet_name=id, index=False, startrow=8, startcol=12)
        sheet4.to_excel(excel_writer, sheet_name='ActTasks-drop', index=False, startcol=12)
        excel_writer.save()
    #
    else:
        print('任务组id：%s' % taskpool1)
        #将taskpool的值转变成列表
        taskpool1 = taskpool1.split('|')
        taskpool1 = [int(i) for i in taskpool1]
        #根据多个taskpool从子表TaskPage中获取需要的数据sheet5
        data2 = pd.read_excel(path_config_activitycenter, sheet_name='TaskPage')
        data2_columns = data2.columns.values
        dst3 = pd.DataFrame(columns=data2_columns)
        for taskpoolid in taskpool1:
            data_taskpoolid1 = data2['id(key.uint32)*'] == taskpoolid
            data_taskpoolid2_ = data2[data_taskpoolid1].values
            if len(data_taskpoolid2_)>0:
                data_taskpoolid2 = data_taskpoolid2_[0]
                dst3.loc[len(dst3)] = data_taskpoolid2
        sheet5 = dst3.drop(columns=['IsRand(bool)', 'TabName(string)'])
        # 从sheet5中获取taskid的值，转换成列表并合并。目前该代码版本默认是2个列表合并。
        taskid2_1 = sheet5['TaskId(array.string)'].values[0].split('|')
        taskid2_1 = [int(i) for i in taskid2_1]
        taskid2_2 = sheet5['TaskId(array.string)'].values[1].split('|')
        taskid2_2 = [int(i) for i in taskid2_2]
        taskid2 = taskid2_1 + taskid2_2
        #根据多个taskid从子表ActTasks获取需要的数据sheet6
        data3 = pd.read_excel(path_config_activitycenter, sheet_name='ActTasks')
        data3_columns = data3.columns.values
        dst4 = pd.DataFrame(columns=data3_columns)
        for taskid1 in taskid2:
            data_taskid3 = data3['ID(key.uint32)*'] == taskid1
            data_taskid4_ = data3[data_taskid3].values
            if len(data_taskid4_) > 0:
                data_taskid4 = data_taskid4_[0]
                dst4.loc[len(dst4)] = data_taskid4
        sheet6 = dst4.drop(columns=['SubId(uint32)', 'Describe(string)', 'JumpLink(string)', 'ShareContent(string)', 'TimeLimitParams(array.string)', 'TimeResetParams(array.string)',
                                   'BarStyle(uint32)', 'Commentary(string)'])
        #从sheet6中获取dropid的值，如果是NA则填充1，然后转换成列表，并将列表中的所有数变成int
        dropid2 = sheet6['DropId(uint32)'].fillna(value='1')
        dropid2 = list(dropid2)
        dropid2 = [int(i) for i in dropid2]
        # 根据多个dropid从表drop中获取需要的数据sheet7
        data_drop = pd.read_excel(path_config_drop, sheet_name='drop')
        data_drop_columns = data_drop.columns.values
        dst5 = pd.DataFrame(columns=data_drop_columns)
        for dropid1 in dropid2:
            data_dropid3 = data_drop['id(key.uint32)*'] == dropid1
            data_dropid4_ = data_drop[data_dropid3].values
            if len(data_dropid4_) > 0:
                data_dropid4 = data_dropid4_[0]
                dst5.loc[len(dst5)] = data_dropid4
        sheet7 = dst5.drop(columns=['limitRepeated(array.string)', 'showId(uint32)', 'dropPackage(array.string)',
                                    'limitExtraDropId(uint32)', 'guaranteeDropList(array.string)',
                                    'guaranteeXRound(array.string)'])

        #根据actid读取子表ActExchange的数据sheet8
        data4 = pd.read_excel(path_config_activitycenter, sheet_name='ActExchange')
        data4_1 = data4['Id(key.uint32)'] == actid
        data4_2 = data4[data4_1]
        sheet8 = data4_2.drop(columns=['TabName(string)'])
        #从sheet8中获取itemlist的值，如果值为空则跳过
        itemlist = sheet8['ItemList(array.uint32)'].values
        if len(itemlist) == 0:
            excel_writer2 = pd.ExcelWriter(path)
            sheet1.to_excel(excel_writer2, sheet_name=id, index=False)
            sheet5.to_excel(excel_writer2, sheet_name=id, index=False, startrow=4)
            sheet6.to_excel(excel_writer2, sheet_name=id, index=False, startrow=9)
            sheet6.to_excel(excel_writer2, sheet_name='ActTasks-drop', index=False)
            sheet7.to_excel(excel_writer2, sheet_name=id, index=False, startcol=13, startrow=9)
            sheet7.to_excel(excel_writer2, sheet_name='ActTasks-drop', index=False, startcol=13)
            sheet8.to_excel(excel_writer2, sheet_name=id, index=False, startrow=29)
            excel_writer2.save()

        #从sheet8中获取itemlist的值，如果值不为空，则转变成列表，并且全部变成int
        else:
            itemlist = sheet8['ItemList(array.uint32)'].values[0].split('|')
            itemlist = [int(i) for i in itemlist]
            #根据多个itemlist从子表ActExchangeItem获取需要的数据sheet9
            data5 = pd.read_excel(path_config_activitycenter, sheet_name='ActExchangeItem')
            data5_columns = data5.columns.values
            dst6 = pd.DataFrame(columns=data5_columns)
            for itemlistid in itemlist:
                data5_1 = data5['Id(key.uint32)'] == itemlistid
                data5_2_ = data5[data5_1].values
                if len(data5_2_)>0:
                    data5_2 = data5_2_[0]
                    dst6.loc[len(dst6)] = data5_2
            sheet9 = dst6.drop(columns=['DayLimit(uint32)', 'BarStyle(uint32)', 'Commentary(string)', 'CostMoney(string)'])
            #从sheet9中获取dropid的值，如果是NA则填充1，然后转换成列表，并将列表中的所有数变成int
            dropid3 = sheet9['DropId(uint32)'].fillna(value='1')
            dropid3 = list(dropid3)
            dropid3 = [int(i) for i in dropid3]
            # 根据多个dropid从表drop中获取需要的数据sheet10
            data_drop = pd.read_excel(path_config_drop, sheet_name='drop')
            data_drop_columns = data_drop.columns.values
            dst7 = pd.DataFrame(columns=data_drop_columns)
            for dropid2 in dropid3:
                data_dropid5 = data_drop['id(key.uint32)*'] == dropid2
                data_dropid6_ = data_drop[data_dropid5].values
                if len(data_dropid6_) > 0:
                    data_dropid6 = data_dropid6_[0]
                    dst7.loc[len(dst7)] = data_dropid6
            sheet10 = dst7.drop(columns=['limitRepeated(array.string)', 'showId(uint32)', 'dropPackage(array.string)',
                                        'limitExtraDropId(uint32)', 'guaranteeDropList(array.string)',
                                        'guaranteeXRound(array.string)'])

            #
            excel_writer1 = pd.ExcelWriter(path)
            sheet1.to_excel(excel_writer1, sheet_name=id, index=False)
            sheet5.to_excel(excel_writer1, sheet_name=id, index=False, startrow=4)
            sheet6.to_excel(excel_writer1, sheet_name=id, index=False, startrow=9)
            sheet6.to_excel(excel_writer1, sheet_name='ActTasks-drop', index=False)
            sheet7.to_excel(excel_writer1, sheet_name=id, index=False, startcol=13,startrow=9)
            sheet7.to_excel(excel_writer1, sheet_name='ActTasks-drop', index=False, startcol=13)
            sheet8.to_excel(excel_writer1, sheet_name=id, index=False, startrow=29)
            sheet9.to_excel(excel_writer1, sheet_name=id, index=False, startrow=33)
            sheet9.to_excel(excel_writer1, sheet_name='ActExchangeItem', index=False)
            sheet10.to_excel(excel_writer1, sheet_name=id, index=False, startrow=33, startcol=13)
            sheet10.to_excel(excel_writer1, sheet_name='ActExchangeItem', index=False, startcol=13)
            excel_writer1.save()






















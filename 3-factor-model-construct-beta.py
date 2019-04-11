# -*- coding: utf-8 -*-
"""
@Date: Created on Tue Apr  9 04:25:30 2019
@Author: Haojun Gao
@Description: Fama-French 3-factor model
    构建连接三因子模型和CAPM模型的组合
        构建市值和β值分类的二十五个股票组合
        构建账面市值比和β值分类的二十五个股票组合
"""

import numpy as np
import pandas as pd

def open_excel(path):
    
    excel_ori = pd.read_excel(io=path)
    values = excel_ori.values
    data_df = pd.DataFrame(values)
    
    return data_df


def get_data_Msmv():
    
    # 循环读取25个根据市值和账面市值比的股票组合
    id = str(0)
    xlsx_path = ".\\pf25_data\\pfdata_"+id+".csv"
    data_df = pd.read_csv(xlsx_path)
    print(data_df.shape)
    data_Msmv = data_df
    
    # 根据以上矩阵获取到备选的股票以及相应年份的数据条目
    
    data_year = data_Msmv[[1,8,9]]
    
    data_year.rename(columns={1: "Stkcd", 8: 'year', 9: 'month'}, inplace=True)


    print(data_year)    
    
    
    data_year = data_year.drop_duplicates()
    data_year = data_year.reset_index(drop=True)
    
    return data_year

def get_data_beta(data_Msmv_year):
    
    # 计算每年每只股票的平均β值，并且根据每年的β值的20%-80%进行分类
    
    id = "1"
    csv_path = ".\\beita\\SMONRETBETA_BFDT12__("+id+").csv"
    data_beta = pd.read_csv(csv_path)
    
    data_beta[1] = pd.to_datetime(data_beta[1], format='%Y-%m-%d')
    data_beta[3] = data_beta[1].dt.year
    data_beta[4] = data_beta[1].dt.month
    
    for row in data_beta.iterrows():
        temp = data_Msmv_year[data_Msmv_year[0].isin([row[1][0]])]
        if not temp.empty:   
            print(temp)
    
# =============================================================================
#     print(data_Msmv_year)
#     print(data_beta)
# =============================================================================


if __name__ == '__main__':

    data_Msmv_year = get_data_Msmv()
    #print(data_Msmv_year)
    
    #get_data_beta(data_Msmv_year)
    
    
    
    
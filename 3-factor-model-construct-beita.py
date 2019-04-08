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


if __name__ == '__main__':
    
    

    # 循环读取25个根据市值和账面市值比的股票组合
    i = 0
    data_Msmv = None
    for j in range(5):
        id = str(i)+str(j)
        print(id)
        csv_path = ".\\portfolio_final2\\portfolio_final"+id+".xlsx"
        excel_ori = pd.read_excel(io=csv_path)
        values = excel_ori.values
        data_df = pd.DataFrame(values)
        print(data_df.shape)
        if data_Msmv is None:
            data_Msmv = data_df
        else:
            data_Msmv = pd.concat((data_Msmv,data_df))
            
    # 根据以上矩阵获取到备选的股票以及相应年份的数据条目
    
    
            
    # 计算每年每只股票的平均β值，并且根据每年的β值的20%-80%进行分类
            
    print(data_Msmv.shape)
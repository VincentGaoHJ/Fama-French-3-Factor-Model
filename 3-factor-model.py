# -*- coding: utf-8 -*-
"""
@Date: Created on Tue Apr  9 01:01:00 2019
@Author: Haojun Gao
@Description: Fama-French 3-factor model
    首先直观感受三因子模型的有效性：
        按照市值分成五组，感受市值与收益率关系
        按照账面市值比分成五组，感受账面市值比与收益率关系
        按照市值和账面市值比分成二十五组，感受两个因子与收益率关系
"""

import numpy as np
import pandas as pd


class Portafolio(object):
    """
    创建组合的类
    idnum [组合的代号 00-44(str)]
    num [组合所包含的数据的条目数量(int)]
    rank_Msmv [组合所代表的市值属性大小 0最小，4最大(int)]
    rank_Bktomk [组合所代表的账面市值比属性大小 0最小，4最大(int)]
    Mretwd [平均考虑现金红利再投资的月个股回报率(float)]
    Mretnd [平均不考虑现金红利再投资的月个股回报率(float)]
    Msmvosd [平均月个股流通市值(float)] - 个股的流通股数与月收盘价的乘积
    Msmvttl [平均月个股总市值(float)] - 个股的发行总股数与月收盘价的乘积
    Bktomk [平均账面市值比(float)]

    """

    def __init__(self, idnum, num, rank_Msmv, rank_Bktomk, Msmvosd, Msmvttl, Mretwd, Mretnd, Bktomk):
        self.idnum = idnum
        self.num = num
        self.rank_Msmv = rank_Msmv
        self.rank_Bktomk = rank_Bktomk
        self.Msmvosd = Msmvosd
        self.Msmvttl = Msmvttl
        self.Mretwd = Mretwd
        self.Mretnd = Mretnd
        self.Bktomk = Bktomk


# 创建25个类对象，并且用一个字典进行管理
Portafolio_dict = {}
for i in range(25):
    a = int(i/5)
    b = i % 5
    id = str(a) + str(b)

    csv_path = ".\\portfolio_final2\\portfolio_final"+id+".xlsx"
    excel_ori = pd.read_excel(io=csv_path)
    values = excel_ori.values
    data_df = pd.DataFrame(values)

    temp_idnum = id
    temp_num = data_df.shape[0]
    temp_rank_Msmv = a
    temp_rank_Bktomk = b
    temp_Msmvosd = data_df[2].mean()
    temp_Msmvttl = data_df[3].mean()
    temp_Mretwd = data_df[4].mean()
    temp_Mretnd = data_df[5].mean()
    temp_Bktomk = data_df[8].mean()

    Portafolio_dict[id] = Portafolio(temp_idnum, temp_num, temp_rank_Msmv, temp_rank_Bktomk,
                                     temp_Msmvosd, temp_Msmvttl, temp_Mretwd, temp_Mretnd, temp_Bktomk)


def Msmv_portafolio(Portafolio_dict):
    print("\n根据市值大小输出\n")
    value_rank_Msmv = value_Msmvosd = value_Msmvttl = value_Mretwd = value_Mretnd = 0
    for i in range(5):
        for j in range(5):
            id = str(i) + str(j)
            value_rank_Msmv = Portafolio_dict[id].rank_Msmv
            value_Msmvosd += Portafolio_dict[id].Msmvosd
            value_Msmvttl += Portafolio_dict[id].Msmvttl
            value_Mretwd += Portafolio_dict[id].Mretwd
            value_Mretnd += Portafolio_dict[id].Mretnd
        print(value_rank_Msmv, end="\t")
        print(value_Msmvosd/5, end="\t")
        print(value_Msmvttl/5, end="\t")
        print(value_Mretwd/5, end="\t")
        print(value_Mretnd/5)


def Bktomk_portafolio(Portafolio_dict):
    print("\n根据账面市值比大小输出\n")
    value_rank_Bktomk = value_Bktomk = value_Mretwd = value_Mretnd = 0
    for i in range(5):
        for j in range(5):
            id = str(j) + str(i)
            value_rank_Bktomk = Portafolio_dict[id].rank_Bktomk
            value_Bktomk += Portafolio_dict[id].Bktomk
            value_Mretwd += Portafolio_dict[id].Mretwd
            value_Mretnd += Portafolio_dict[id].Mretnd
        print(value_rank_Bktomk, end="\t")
        print(value_Bktomk/5, end="\t")
        print(value_Mretwd/5, end="\t")
        print(value_Mretnd/5)


# =============================================================================
# # 循环展示25个类对象的所有值
# for i in range(25):
#     a = int(i/5)
#     b = i%5
#     id = str(a) + str(b)
#     print(Portafolio_dict[id].idnum, end="\t")
#     print(Portafolio_dict[id].num, end="\t")
#     print(Portafolio_dict[id].rank_Msmv, end="\t")
#     print(Portafolio_dict[id].rank_Bktomk, end="\t")
#     print(Portafolio_dict[id].Msmvosd, end="\t")
#     print(Portafolio_dict[id].Msmvttl, end="\t")
#     print(Portafolio_dict[id].Mretwd, end="\t")
#     print(Portafolio_dict[id].Mretnd, end="\t")
#     print(Portafolio_dict[id].Bktomk)
# =============================================================================
if __name__ == '__main__':

    Msmv_portafolio(Portafolio_dict)

    Bktomk_portafolio(Portafolio_dict)

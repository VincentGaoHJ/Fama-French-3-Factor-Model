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


def prepare_Portafolio(num):
    """
    读取每一个二十五个以csv文件储存的Portafolio
    :param num: 所需要的数据的年份，如果传入的num为零，则使用所有年份的数据
    :return: 为每一个Portafolio创建一个类对象
    """
    for i in range(25):
        a = int(i / 5)
        b = i % 5

        path = ".\\pf25_data\\pfdata_" + str(i) + ".csv"
        data_df = pd.read_csv(path)

        if num != 0:
            data_df = data_df.loc[data_df["Trdmnt_year"] == num]

        temp_idnum = str(i)
        temp_num = data_df.shape[0]
        temp_rank_Msmv = a
        temp_rank_Bktomk = b
        temp_Msmvosd = data_df["Msmvosd"].mean()
        temp_Msmvttl = data_df["Msmvttl"].mean()
        temp_Mretwd = data_df["Mretwd"].mean()
        temp_Mretnd = data_df["Mretnd"].mean()
        temp_Bktomk = data_df["bemeA"].mean()

        Portafolio_dict[str(i)] = Portafolio(temp_idnum, temp_num, temp_rank_Msmv, temp_rank_Bktomk,
                                             temp_Msmvosd, temp_Msmvttl, temp_Mretwd, temp_Mretnd, temp_Bktomk)

    return Portafolio_dict


def Msmv_portafolio(Portafolio_dict):
    """
    根据市值大小分成五个Portafolio，并且输出他们的信息
    :param Portafolio_dict: 类对象字典
    :return:
    """
    print("\n根据市值大小输出\n")
    for i in range(5):
        value_rank_Msmv = value_Msmvosd = value_Msmvttl = value_Bktomk = value_Mretwd = value_Mretnd = 0
        for j in range(5):
            id = str(i * 5 + j)
            value_rank_Msmv = Portafolio_dict[id].rank_Msmv
            value_Msmvosd += Portafolio_dict[id].Msmvosd
            value_Msmvttl += Portafolio_dict[id].Msmvttl
            value_Bktomk += Portafolio_dict[id].Bktomk
            value_Mretwd += Portafolio_dict[id].Mretwd
            value_Mretnd += Portafolio_dict[id].Mretnd
        print(value_rank_Msmv, end="\t")
        print(value_Msmvosd / 5, end="\t")
        print(value_Msmvttl / 5, end="\t")
        print(value_Bktomk / 5, end="\t")
        print(value_Mretwd / 5, end="\t")
        print(value_Mretnd / 5)


def Bktomk_portafolio(Portafolio_dict):
    """
    根据账面市值比大小分成五个 Portafolio，并且输出他们的信息
    :param Portafolio_dict: 类对象字典
    :return:
    """
    print("\n根据账面市值比大小输出\n")
    for i in range(5):
        value_rank_Bktomk = value_Msmvosd = value_Msmvttl = value_Bktomk = value_Mretwd = value_Mretnd = 0
        for j in range(5):
            id = str(i + j * 5)
            value_rank_Bktomk = Portafolio_dict[id].rank_Bktomk
            value_Msmvosd += Portafolio_dict[id].Msmvosd
            value_Msmvttl += Portafolio_dict[id].Msmvttl
            value_Bktomk += Portafolio_dict[id].Bktomk
            value_Mretwd += Portafolio_dict[id].Mretwd
            value_Mretnd += Portafolio_dict[id].Mretnd
        print(value_rank_Bktomk, end="\t")
        print(value_Msmvosd / 5, end="\t")
        print(value_Msmvttl / 5, end="\t")
        print(value_Bktomk / 5, end="\t")
        print(value_Mretwd / 5, end="\t")
        print(value_Mretnd / 5)


def twentyfive_Mretwd_portafolio(Portafolio_dict):
    """
    根据账面市值比大小和市值分成25个 Portafolio，并且输出他们的Mretwd
    :param Portafolio_dict: 类对象字典
    :return:
    """
    print("\n根据账面市值比与市值大小输出Mretwd\n")
    for i in range(5):
        for j in range(5):
            id = str(i * 5 + j)
            value_Mretwd = Portafolio_dict[id].Mretwd
            print(value_Mretwd, end="\t")
        print(end="\n")


def twentyfive_Mretnd_portafolio(Portafolio_dict):
    """
    根据账面市值比大小和市值分成25个 Portafolio，并且输出他们的Mretnd
    :param Portafolio_dict: 类对象字典
    :return:
    """
    print("\n根据账面市值比与市值大小输出Mretnd\n")
    for i in range(5):
        for j in range(5):
            id = str(i * 5 + j)
            value_Mretnd = Portafolio_dict[id].Mretnd
            print(value_Mretnd, end="\t")
        print(end="\n")


def twentyfive_Bktomk_portafolio(Portafolio_dict):
    """
    根据账面市值比大小和市值分成25个Portafolio，并且输出他们的 Bktomk
    :param Portafolio_dict: 类对象字典
    :return:
    """
    print("\n根据账面市值比与市值大小输出账面市值比Bktomk\n")
    for i in range(5):
        for j in range(5):
            id = str(i * 5 + j)
            value_Bktomk = Portafolio_dict[id].Bktomk
            print(value_Bktomk, end="\t")
        print(end="\n")


def twentyfive_Msmvttl_portafolio(Portafolio_dict):
    """
    根据账面市值比大小和市值分成25个Portafolio，并且输出他们的 Msmvttl
    :param Portafolio_dict: 类对象字典
    :return:
    """
    print("\n根据账面市值比与市值大小输出市值Msmvttl\n")
    for i in range(5):
        for j in range(5):
            id = str(i * 5 + j)
            value_Msmvttl = Portafolio_dict[id].Msmvttl
            print(value_Msmvttl, end="\t")
        print(end="\n")


def twentyfive_Msmvosd_portafolio(Portafolio_dict):
    """
    根据账面市值比大小和市值分成25个Portafolio，并且输出他们的 Msmvosd
    :param Portafolio_dict: 类对象字典
    :return:
    """
    print("\n根据账面市值比与市值大小输出市值Msmvosd\n")
    for i in range(5):
        for j in range(5):
            id = str(i * 5 + j)
            value_Msmvosd = Portafolio_dict[id].Msmvosd
            print(value_Msmvosd, end="\t")
        print(end="\n")


def print_matrix(dictionary):
    """
    根据25个Portafolio输出相关的矩阵
    :param dictionary: 类对象字典
    :return:
    """
    Msmv_portafolio(dictionary)
    Bktomk_portafolio(dictionary)
    twentyfive_Mretwd_portafolio(dictionary)
    twentyfive_Mretnd_portafolio(dictionary)
    twentyfive_Bktomk_portafolio(dictionary)
    twentyfive_Msmvttl_portafolio(dictionary)
    twentyfive_Msmvosd_portafolio(dictionary)


# 创建25个类对象，并且用一个字典进行管理
Portafolio_dict = {}

Portafolio_dict = prepare_Portafolio(0)
print_matrix(Portafolio_dict)

# Portafolio_dict = prepare_Portafolio(2018)
# print_matrix(Portafolio_dict)

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


def get_data_Msmv(Msmv_path):
    data_df = pd.read_csv(Msmv_path)

    # 根据以上矩阵获取到备选的股票以及相应年份的数据条目

    data_year = data_df[["Stkcd", "Msmvosd", 'Msmvttl', 'Mretwd', 'Mretnd', 'bemeA']]

    data_year['Trdmnt_year'] = data_df['Trdmnt_year']
    data_year['Trdmnt_mon'] = data_df['Trdmnt_mon'].map(lambda x: int(x[-2:]))
    data_year = data_year.drop_duplicates()
    data_year = data_year.reset_index(drop=True)

    data_year.rename(columns={'Stkcd': 'StkCd', 'Trdmnt_year': 'Date-year', 'Trdmnt_mon': 'Date-month'}, inplace=True)

    return data_year


def get_data_beta(i):
    id = str(i + 1)
    csv_path = ".\\beta\\SMONRETBETA_BFDT12__(" + id + ").csv"
    data_beta = pd.read_csv(csv_path, encoding='ANSI')

    data_beta.rename(columns={'股票代码_StkCd': 'StkCd', '日期_Date': 'Date', '风险因子_流通市值加权_持有期收益_Beta_TMV_H': 'Beta'},
                     inplace=True)

    data_beta["Date"] = pd.to_datetime(data_beta["Date"], format='%Y-%m-%d')
    data_beta["Date-year"] = data_beta["Date"].dt.year
    data_beta["Date-month"] = data_beta["Date"].dt.month

    data_beta.drop(['Date'], axis=1, inplace=True)

    return data_beta


def add_beta_to_Msmv(data_Msmv, data_beta):
    Msmv_beta = pd.merge(
        data_Msmv[["StkCd", "Date-year", "Date-month", "Msmvosd", 'Msmvttl', 'Mretwd', 'Mretnd', 'bemeA']],
        data_beta[["StkCd", "Date-year", "Date-month", "Beta"]],
        on=["StkCd", "Date-year", "Date-month"])

    return Msmv_beta


def get_full_data(data_Msmv):
    full_data = None
    data_Msmv.insert(0, 'beta', 0)
    for i in range(6):
        data_beta = get_data_beta(i)
        Msmv_beta = add_beta_to_Msmv(data_Msmv, data_beta)
        if full_data is None:
            full_data = Msmv_beta
        else:
            full_data = pd.concat([full_data, Msmv_beta], axis=0, ignore_index=True)

    return full_data


if __name__ == '__main__':

    for i in range(25):

        Msmv_path = ".\\pf25_data\\pfdata_" + str(i) + ".csv"
        file_path = ".\\full_data\\pfdata_beta_" + str(i) + ".csv"

        data_Msmv = get_data_Msmv(Msmv_path)
        full_data = get_full_data(data_Msmv)
        full_data.to_csv(file_path)

        print("[main]成功保存第{}个Portafolio".format(str(i+1)))

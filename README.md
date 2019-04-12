
# Fama French 3-Factor Model

![downloads](https://img.shields.io/github/downloads/atom/atom/total.svg)

## Description

* This is a repo used to verify the validity of the Fama three-factor model.
* The data used is from the Chinese stock market.
* The operation of the data is mainly based on pandas.
* Input and output data is saved in `.csv` format.


## Operation

+ run `3-factor-model.py` to view the basic information about 25 Portafolio (according to the methodology in the paper written by Fama in 1992 & 1993)

+ run `3-factor-model-construct-beta.py` to add the Beta information to the data list of the origin portafolio and save it in a new folder.

+ run `3-factor-model-evaluate-beta.py` to view the full information about 25 Portafolio, observing whether beta plays a role in Fama Three-factor Model.



## Input Format

* **\\pf25_data\\pfdata_0.csv**
```
	Stkcd	Trdmnt	Msmvosd	Msmvttl	Mretwd	Mretnd	Markettype	Trdmnt_year	Trdmnt_mon	bemeA
0	4	2005/7/1	166211.4	335066.97	-0.109375	-0.109375	4	2005	Jul-05	0.506898
1	4	2005/8/1	196621.0	396369.95	0.182957	0.182957	4	2005	Aug-05	0.506898
2	4	2005/9/1	197454.14	398049.48	0.004237	0.004237	4	2005	Sep-05	0.506898
3	4	2005/10/1	186206.75	375375.78	-0.056962	-0.056962	4	2005	Oct-05	0.506898
4	4	2005/11/1	187039.89	377055.31	0.004474	0.004474	4	2005	Nov-05	0.506898
5	4	2005/12/1	172459.95	347663.47	-0.077951	-0.077951	4	2005	Dec-05	0.506898
6	4	2008/1/1	580150.52	745712.95	-0.108434	-0.108434	4	2008	Jan-08	0.415926
7	4	2008/2/1	622616.49	800297.8	0.073198	0.073198	4	2008	Feb-08	0.415926
8	4	2008/3/1	535071.26	687769.04	-0.140609	-0.140609	4	2008	Mar-08	0.415926
9	4	2008/4/1	473658.93	608830.96	-0.114774	-0.114774	4	2008	Apr-08	0.415926
10	4	2008/5/1	451445.96	580278.89	-0.046897	-0.046897	4	2008	May-08	0.415926

```

* **\\beta\\SMONRETBETA_BFDT12__(1).txt**
```
股票代码_StkCd	日期_Date	风险因子_流通市值加权_持有期收益_Beta_TMV_H
1	2005/1/31	0.9075
1	2005/2/28	0.7836
1	2005/3/31	0.8823
1	2005/4/29	0.8277
1	2005/5/31	0.7782
1	2005/6/30	0.7628
1	2005/7/29	0.7914
1	2005/8/31	0.7783
1	2005/9/30	0.8098

```


## Output Format

* **\\full_data\\pfdata_beta_0.csv**
```
	StkCd	Date-year	Date-month	Msmvosd	Msmvttl	Mretwd	Mretnd	bemeA	Beta
0	4	2005	7	166211.4	335066.97	-0.109375	-0.109375	0.506898	1.5095
1	4	2005	8	196621.0	396369.95	0.182957	0.182957	0.506898	1.5595
2	4	2005	9	197454.14	398049.48	0.004237	0.004237	0.506898	1.4627
3	4	2005	10	186206.75	375375.78	-0.056962	-0.056962	0.506898	1.4694
4	4	2005	11	187039.89	377055.31	0.004474	0.004474	0.506898	1.378
5	4	2005	12	172459.95	347663.47	-0.077951	-0.077951	0.506898	1.2646
6	4	2008	1	580150.52	745712.95	-0.108434	-0.108434	0.415926	1.153
7	4	2008	2	622616.49	800297.8	0.073198	0.073198	0.415926	1.1246
8	4	2008	3	535071.26	687769.04	-0.140609	-0.140609	0.415926	0.992
9	4	2008	4	473658.93	608830.96	-0.114774	-0.114774	0.415926	1.1501
10	4	2008	5	451445.96	580278.89	-0.046897	-0.046897	0.415926	1.1479


```

## Data Explanation

> Read more about Gherkin here: idnum [组合的代号 00-44(str)]
> num [组合所包含的数据的条目数量(int)]
> rank_Msmv [组合所代表的市值属性大小 0最小，4最大(int)]
> rank_Bktomk [组合所代表的账面市值比属性大小 0最小，4最大(int)]
> Mretwd [平均考虑现金红利再投资的月个股回报率(float)]
> Mretnd [平均不考虑现金红利再投资的月个股回报率(float)]
> Msmvosd [平均月个股流通市值(float)] - 个股的流通股数与月收盘价的乘积
> Msmvttl [平均月个股总市值(float)] - 个股的发行总股数与月收盘价的乘积
> Bktomk [平均账面市值比(float)]


###### tags: `Readme` `Documentation`

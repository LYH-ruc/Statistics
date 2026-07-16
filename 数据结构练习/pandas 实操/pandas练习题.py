# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:29:16 2026

@author: 95451
"""
import pandas as pd
import seaborn as sns  # 用 seaborn 自带数据集

tips = sns.load_dataset('tips')
print(tips['total_bill'].head(3))
print(tips[['total_bill','sex']].head(3))
print(tips.iloc[0])
print(tips.loc[1])
print(tips.loc[0:3,['total_bill','tip']])
print(tips[tips['tip']>5])
print(tips[(tips['tip']>5) & (tips['size']<4)])
print(tips[tips['sex'].isin(['Male'])])
print(tips[~tips['sex'].isin(['Male'])])
print(tips[(tips['sex'].isin(['Male'])) & (tips['smoker'].isin(['Yes'])) & (tips['size']<5)])
print(tips.loc[tips['size']<5,['sex','day']])
print(tips.query('tip>5 and sex in ["Male"]'))
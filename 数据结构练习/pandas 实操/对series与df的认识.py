# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:25:12 2026

@author: 95451
"""

import pandas as pd
import numpy as np

#series 的创建
s = pd.Series([70,69,89,68,99],
              index = ['zhang','wang','liu','lei','li'],
              name = 'grades')
print(s)
print(s['li'])
print(s.values)

#DataFrame的创建
df = pd.DataFrame({
    'name':['li','wang','lei','liu','zhang'],
    'age':[1,2,3,4,5],
    'height':[177,188,199,166,155],
    'datetime':pd.to_datetime(['2022-3-15','2010-6-28','2014-4-4','2017-7-7','2019-9-9'])
    })
print(df)
print(df.shape)
print(df.dtypes)
print(df.info())
print(df.describe())

s1 = pd.Series([1,2,3],index=['a','b','c'])
s2 = pd.Series([2,3,4],index=['b','c','d'])
print(s1+s2)

#数据的选择：
df['xx'].head()
df['xx'].tail()
df.iloc[0]
df.loc[0]
df.loc[0:3,['xx','xxx']]#三行两列
df[df['xx']]>0#数值型数据的筛选
df[df['xx'].isin(['xxx'])]
df[(df['xx']>0) & (df['xxx'].isin(['xxxx']))]
df.loc[df['xx']<0,['xxx','xxx']]
df.query('xxx>5 and xxx in "xx"')

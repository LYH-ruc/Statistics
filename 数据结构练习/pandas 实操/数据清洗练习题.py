# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:53:18 2026

@author: 95451
"""

import pandas as pd
import numpy as np

# 模拟一份脏数据
df = pd.DataFrame({
    '姓名': ['  Alice', 'Bob', 'CHARLIE', 'David', 'Bob'],   # 重复 + 大小写不一致 + 空格
    '年龄': ['28', '35', '?', '42', '35'],                    # 字符串,有 ?
    '工资': [10000, np.nan, 15000, 20000, np.nan],            # 有 NaN
    '入职日期': ['2022-03-15', '2018/07/01', '2020-09-10', '2015年1月20日', '2018/07/01']
})
print('原始数据:')
print(df)

#第一列姓名：Charlie大小写
df['姓名'] = df['姓名'].str.strip().str.title()
print(df)
df = df.drop_duplicates()
print(df)
#第二列年龄：把问号改成NaN 然后想办法填充一个数字
df['年龄'] = pd.to_numeric(df['年龄'],errors='coerce')
print(df)
df['年龄'] = df['年龄'].fillna(df['年龄'].median())
print(df)
#第三列工资：本身的nan想办法添加一个数
df['工资'] = df['工资'].fillna(df['工资'].mean())
print(df)
#第四列日期：格式统一
df['入职日期'] = df['入职日期'].str.replace('年', '-').str.replace('月', '-').str.replace('日', '')
df['入职日期'] = df['入职日期'].str.replace('/', '-').str.replace('/', '-').str.replace('/', '')
df['入职日期'] = pd.to_datetime(df['入职日期'], errors='coerce')
print(df)
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:09:51 2026

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
#对缺失值的处理：
print(df.isna())
print(df.isna().sum())
print(df.isna().mean())
#激进的处理法：删除
print(df.dropna())
print(df.dropna(how='all'))
print(df.dropna(subset='年龄'))
print(df.dropna(axis=1))
print(df.dropna(thresh=3))
#温和的处理法：填充
print(df.fillna(0))
print(df.fillna(df.mean()))
print(df.fillna(df.medium()))
print(df.fillna(df.sum()))
print(df.fillna(df.mode().iloc[0]))
print(df['年龄'].fillna(df['年龄'].mean()))
#处理重复
df.duplicated()
df.duplicated().sum()
df.drop_duplicated()
df.drop_duplicates(keep='last')
df.drop_duplicates(keep=False)
df.drop_duplicates(subset=['姓名'])
#转数据类型：
df['年龄'] = df['年龄'].astype(int)
df['工资'] = df['工资'].astype(float)
df['是否在职'] = df['是否在职'].astype(bool)
df = df.astype({'年龄': 'int', '工资': 'float'})
df['入职日期'] = pd.to_datetime(df['入职日期'])
df['入职日期'] = pd.to_datetime(df['入职日期'],format='%Y/%M/%D')
df['年龄'] = pd.to_numeric(df['年龄'],errors='corece')
#字符串的处理：
s = pd.Series(['  Alice  ', 'Bob', 'CHARLIE', 'david', None])
s.str.lower()
s.str.upper()
s.str.title()
s.str.capitalize()
s.str.strip()
s.str.lstrip()
s.str.rstrip()
s.str.len()
# 包含/匹配
s.str.contains('a', case=False)   # 不区分大小写,包含 a
s.str.startswith('A')
s.str.endswith('e')

# 替换
s.str.replace('Alice', 'Anne')
s.str.replace(r'\s+', '_', regex=True)   # 正则替换

# 切分
s.str.split(' ')                  # 按空格切,返回 list 的 Series
s.str.split(' ', expand=True)     # expand=True 把 list 展开成多列

# 提取(正则,超强)
s.str.extract(r'(\w+)')

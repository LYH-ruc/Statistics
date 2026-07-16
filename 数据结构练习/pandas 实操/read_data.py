# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:13:40 2026

@author: 95451
"""
import pandas as pd
import os

def read_data(filepath):
    suffix = os.path.splitext(filepath)[-1].lower()

    if suffix == ".csv":
        df = pd.read_csv(filepath)
    elif suffix in [".xlsx", ".xls"]:
        df = pd.read_excel(filepath)
    else:
        raise ValueError(f"不支持的文件格式：{suffix}，仅支持 csv / xlsx / xls")

    print('shape:', df.shape)
    print('columns:', df.columns.tolist())
    print("-" * 40)
    print("前5行：")
    print(df.head())
    print("-" * 40)
    df.info()
    print("-" * 40)
    print(df.describe())
    print("-" * 40)

    for col in df.select_dtypes(include='object').columns:
        print(f"\n【{col}】 取值统计：")
        print(df[col].value_counts())

    return df
    
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd
import k26_som_xdc_to_csv

k26_som_xdc_to_csv.k26_som_xdc_to_csv('Kria_K26_SOM_Rev1.xdc', 'k26-som-xck26-sfvc784-pin.csv')


# ファイルを読み込む
df_som = pd.read_csv("k26-som-connector-pin.csv")
df_dev = pd.read_csv("k26-som-xck26-sfvc784-pin.csv")

# 結合用のキーを生成
df_som['Port Name'] = 'som240_' + df_som['Connector Number'].astype(str) + '_' + df_som['Connector Pin Number'].str.lower()

# 結合
df = df_som.merge(df_dev, on="Port Name", how="left")

# 必要なものを好きな順で並べる
df = df[[
    'Connector Number',
    'Connector Pin Number',
    'Port Name',
    'Device Pin Number',
    'Device Pin Type',
    'Bank',
    'VCCO',
    'Signal Name',
    'Connector Pin Type',
    'Signal Description',
]]

# CSV 出力
df.to_csv('kria-k26-som-pin.csv', index = False)

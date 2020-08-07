
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import QUANTAXIS as QA
from QUANTAXIS.QAData.data_marketvalue import QA_data_marketvalue
from alpha101 import *
import pymongo

b = QA.QA_fetch_stock_block_adv()
stocks = b.get_block('上证50').code
data = QA.QA_fetch_stock_day_adv(stocks, '2018-01-01', '2020-01-01',
                                 collections=pymongo.MongoClient('192.168.114.21').quantaxis.stock_day).to_qfq()
inds = pd.read_csv('data_export_swl2_month.csv', encoding='gbk', index_col=[0])
indx = inds.loc[:, ['2017-01-01']]
indx.index = indx.index.map(QA.QA_util_code_tostr)
indx.index.name = 'code'
close = data.pivot('close')
Open = data.pivot('open')
high = data.pivot('high')
low = data.pivot('low')
volume = data.pivot('volume')
amount = data.pivot('amount')
vwap = amount/(volume*100)
mv = QA_data_marketvalue(data.data)
returns = close.pct_change()
cap = mv.reset_index().pivot(index='date', columns='code', values='mv')
ind = indx.reindex(close.columns)


#print(alpha5(Open, vwap, close))

def split_data(data, un=5):
    data = data.sort_values().dropna()
    step= int(len(data)/un)
    return pd.Series([data.iloc[step*(n-1):step*n].index.tolist() for n in range(1,un+1) ], index=['l{}'.format(n) for n in range(1,un+1)])
def get_all(res, level, timerange=50):
    zres = res.loc[:, level].shift(1)
    y = lambda datex :data.selects(zres.loc[datex], datex, QA.QA_util_get_next_day(datex)).pct_change.loc[QA.QA_util_get_next_day(datex), slice(None)].mean()
    return pd.Series(zres.iloc[1:timerange+1].index.map(y), index= zres.iloc[1:timerange+1].index, name=level).cumsum()
def test_factor(x,layer=5, timerange=50):
    res = x.apply(lambda x:split_data(x, layer), axis=1)
    return pd.concat([get_all(res, i, timerange) for i in ['l{}'.format(n) for n in range(1,layer+1)]],axis=1)

x = alpha101(close, Open, high, low)
pxx = test_factor(x, 10, 60)
pxx.plot(figsize=(20,8))
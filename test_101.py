
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
                                 collections=pymongo.MongoClient('192.168.2.124').quantaxis.stock_day).to_qfq()
inds = pd.read_csv('data_export_swl2_month.csv', encoding='gbk', index_col=[0])
indx = inds.loc[:, ['2017-01-01']]
indx.index = indx.index.map(QA.QA_util_code_tostr)
indx.index.name = 'code'
close = data.pivot('close').bfill().ffill()
Open = data.pivot('open').bfill().ffill()
high = data.pivot('high').bfill().ffill()
low = data.pivot('low').bfill().ffill()
volume = data.pivot('volume').bfill().ffill()
amount = data.pivot('amount').bfill().ffill()
vwap = amount/(volume*100)
mv = QA_data_marketvalue(data.data)
returns = close.pct_change()
cap = mv.reset_index().pivot(index='date', columns='code', values='mv')
ind = indx.reindex(close.columns)


print(alpha5(Open, vwap, close))
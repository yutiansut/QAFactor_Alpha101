# QAFactor_Alpha101
alpha101 的 quantaxis 适配版本

目前只是一个初略的测试

![image.png](http://picx.gulizhu.com/FkVVHHtMnLBUUrs5f-Dp-veTii3S)



网上搜集来的注释

| 因子分类 | 因子     | 公式                                                         | 注释（不完整）           |
| -------- | -------- | ------------------------------------------------------------ | ------------------------ |
| 价格类   | Alpha1   | argmax(power(if(1日涨幅<  0, stdev(1日涨幅，20), 1日涨幅),2),5) | 趋势                     |
|          | Alpha4   | PercentRank(hrank(最低价,  1, 0),9)                          | 反转                     |
|          | Alpha5   | hrankscore(开盘价-MA(日均成交价,10),  0, 0)*hrankscore((收盘价-日均成交价), 0, 0) | 反转                     |
|          | Alpha9   | if(  or(min(1日涨幅,5)>0, max(1日涨幅,5)<0),  delta(后复权收盘价,1), (0-delta(后复权收盘价,1)))/后复权因子 | 反转或者趋势             |
|          | Alpha8   | hrankscore((sum(开盘价,5)*sum(1日涨幅,5)-barref(sum(开盘价,5)*sum(1日涨幅,5),  10)), 0, 0) | 反转                     |
|          | Alpha18  | hrank(stdev(abs(后复权收盘价-后复权开盘价),5)+(收盘价-开盘价)+barcorr(后复权收盘价,  后复权开盘价, 10), 1, 0) | 反转                     |
|          | Alpha19  | sign(0-N日涨幅(7))*hrank(sum(1日涨幅,  250))                 | 长短趋势背离             |
|          | Alpha20  |                                                              | 反转                     |
|          |          | hrankscore((后复权开盘价-barref(后复权开盘价,1))/后复权因子,  0, 0)*hrankscore((后复权开盘价-barref(后复权收盘价,1))/后复权因子, 0,  0)*hrankscore((后复权开盘价-barref(后复权最低价,1))/后复权因子, 0, 0) |                          |
|          | Alpha23  | if(MA(后复权最高价,20)<后复权最高价,  (0-delta(后复权最高价,2)/后复权因子),0) | 20日均线上，短期回归     |
|          | Alpha24  | if((delta(MA(后复权收盘价,100),100)/barref(后复权收盘价,100))>0.05,  (0-delta(后复权收盘价,3)/后复权因子), (min(后复权收盘价, 100)-后复权收盘价)/后复权因子) | 反转                     |
|          | Alpha29  | min(hpercentrank(min(hpercentrank(delta(后复权收盘价,  5)/后复权因子, 0,0),2)),5) + percentrank(barref(0-1日涨幅,6),5) | 反转                     |
|          | Alpha32  | hscale((ma(后复权收盘价,7)-后复权收盘价)/后复权因子,0)+  20*hscale(barcorr(后复权日均成交价,barref(后复权收盘价,5), 230),0) | 反转                     |
|          | Alpha33  | 开盘价/收盘价                                                | 反转                     |
|          | Alpha34  | hrankscore(stdev(1日涨幅,2)/stdev(1日涨幅,5),  0, 0)+ hrankscore(delta(后复权收盘价,1)/后复权因子,0,0) - Countbars(or(当日涨停标记 = 1,  当日跌停标记 =1),5) | 反转                     |
|          | Alpha37  | hrankscore(barcorr(barref(后复权开盘价-后复权收盘价,1),后复权收盘价,200))+  hrankscore((开盘价-收盘价)) | 统计相关性               |
|          | Alpha38  | hrankscore(percentRank(后复权收盘价,10),  0, 0)*hrankscore(收盘价/开盘价, 0, 0) | 反转                     |
|          | Alpha41  | sqrt(最高价*最低价)-日均成交价                               | 反转                     |
|          | Alpha42  | (日均成交价-收盘价)/(日均成交价+收盘价)                      | 反转                     |
|          | Alpha46  | if(  (delta(后复权收盘价,10) - barref(delta(后复权收盘价,10), 10))/后复权因子 > 2.5, 0-1,  if(delta(后复权收盘价,10) - barref(delta(后复权收盘价,10), 10) <0,  1,(0-delta(后复权收盘价,1)/后复权因子))) | 反转                     |
|          | Alpha48  | hDemean(barcorr(delta(后复权收盘价,1),delta(barref(后复权收盘价,1),1),250)*  1日涨幅/(1+1日涨幅), 2)/sum(power(1日涨幅,2),250) | 统计相关性               |
|          | Alpha49  | if(  (delta(后复权收盘价,10) - delta(barref(后复权收盘价,10),10))/后复权因子 +1 <  0,1,0-delta(后复权收盘价,1)/后复权因子) | 反转                     |
|          | Alpha51  | if  ((delta(barref(后复权收盘价,10),10) -delta(后复权收盘价,10))/后复权因子 > 0.5 ,  1, 0-delta(后复权收盘价,1)/后复权因子) |                          |
|          | Alpha53  | 0-delta((2*收盘价-最低价-最高价)/(收盘价-最低价),9)          | 反转                     |
|          | Alpha54  | (收盘价-最低价)*power(开盘价,5)/((最低价-最高价)*power(收盘价,5)) | 反转                     |
|          | Alpha56  | hrankscore(sum(1日涨幅,10)/sum(sum(1日涨幅,2),3),  0, 0)* hrankscore(1日涨幅*总市值, 0, 0) | 反转                     |
|          | Alpha57  | (日均成交价-收盘价)/decayMA(hrankscore(argmax(后复权收盘价,30),  1, 0),2) | 反转                     |
|          | Alpha60  | hscale(hrankscore(argmax(后复权收盘价,10),  1, 0), 0)-2*hscale(hrankscore((2*后复权收盘价-后复权最低价-后复权最高价)/(后复权最高价-后复权最低价)*当日成交量,  1, 0),0) |                          |
|          | Alpha66  | hpercentrank(decayMA(delta(后复权日均成交价,4),7)/后复权因子,  0, 0)+ percentRank(decayMA((日均成交价-最低价)/(开盘价-(最高价+最低价)/2),11),7) | 反转                     |
|          | Alpha73  | 0-Greater(hpercentrank(decayMA(delta(后复权日均成交价,5)/后复权因子,3)),percentRank(decayMA((0-delta(后复权开盘价*0.147155+  后复权最低价*0.852845,2)/(后复权开盘价*0.147155+后复权最低价*0.852845)),3),17)) | 反转                     |
|          | Alpha84  | Power(percentRank(后复权日均成交价-max(后复权日均成交价,15),21),  delta(后复权收盘价,5)/后复权因子) |                          |
|          | Alpha101 | (开盘价-收盘价)/(最高价-最低价+  0.001)                      | 日内反转                 |
| 量价类   | Alpha2   | 0-barcorr(hrank(delta(log(当日成交量),2)),hrank(收盘价/开盘价  - 1),6) | 量价背离                 |
|          | Alpha3   | 0-barcorr(hrank(开盘价,  0, 0),hrank(当日换手率, 0, 0),10)   | 量价背离                 |
|          | Alpha6   | 0-barcorr(后复权开盘价,中性N日换手率(1),10)                  | 量价背离                 |
|          | Alpha7   | if(20日平均成交额<当日成交额,(0-PercentRank(abs(delta(后复权收盘价,7)),60))*sign(delta(后复权收盘价,7)),  -1 ) |                          |
|          | Alpha11  | (hrankscore(max(日均成交价-收盘价,3))+hrankscore(min(日均成交价-收盘价,3)))*  hrankscore(delta(当日换手率,3),0,0) | 反转缩量                 |
|          | Alpha12  | sign(delta(当日换手率,1))*(0-delta(收盘价,1))                | 量价背离                 |
|          | Alpha13  | hrank(covar(hrank(收盘价),  hrank(当日成交量),5), 1, 0)      | 量价背离                 |
|          | Alpha14  | 0-hrankscore(delta(1日涨幅,3))*barcorr(后复权开盘价,当日换手率,10) | 量价背离                 |
|          | Alpha15  | sum(hpercentrank(barcorr(hrank(最高价),  hrank(当日成交量),3), 0, 0),3) | 量价背离                 |
|          | Alpha16  | hrank(covar(hrank(最高价),  hrank(当日成交量),5), 1, 0)      | 量价背离                 |
|          | Alpha17  | hrankscore(percentrank(后复权收盘价,10),  0, 0)*hrankscore(delta(delta(后复权收盘价,1),1)/后复权因子, 0, 0) *  hrankscore(percentrank(当日换手率/20日换手率,5), 0, 0) | 反转缩量                 |
|          |          |                                                              |                          |
|          | Alpha22  | 0-delta(barcorr(后复权最高价,当日成交量,5),5)*hrankscore(stdev(后复权收盘价,20)/后复权收盘价) | 量价背离增加+高波动      |
|          | Alpha25  | hrank((0-1日涨幅)*20日平均成交额*日均成交价*(最高价-收盘价)) | 1日反转加成交活跃， 量价 |
|          | Alpha26  | 0-max(barcorr(percentrank(当日成交量,5),percentrank(后复权最高价,5),5),3) | 量价背离                 |
|          | Alpha28  | 0-barcorr(20日平均成交额,后复权最低价,5)+(最高价+最低价)/2-收盘价 | 背离+反转                |
|          | Alpha30  | (1-hpercentrank((sign(1日涨幅)+sign(barref(1日涨幅,1))+  sign(barref(1日涨幅,2)))) )*ma(当日成交量,5)/ma(当日成交量,20)* (20- Countbars(or(当日涨停标记 =  1, 当日跌停标记 =1),20)) | 反转                     |
|          | Alpha31  | hpercentrank(decayMA(hpercentrank(delta(后复权收盘价,10)/后复权因子,  0, 0),10))+hpercentrank(delta(后复权收盘价,3)/后复权因子, 0,  0)+sign(barcorr(20日平均成交额,后复权最低价,12)) | 反转+量价背离            |
|          | Alpha35  | PercentRank(当日成交量,32)*(1-PercentRank((后复权收盘价+后复权最高价-后复权最低价),16))*(1-PercentRank(1日涨幅,32)) | 量大价低                 |
|          | Alpha36  | 2.21*hrankscore(barcorr(收盘价-开盘价,barref(当日成交量,1),15))  + 0.7*hrankscore(开盘价-收盘价)+ 0.73*hrankscore(percentRank(barref(0-1日涨幅,6),5)) +  hrankscore(abs(barcorr(后复权日均成交价, 20日平均成交额,6))) +  0.6*hrankscore((MA(后复权收盘价,200)-后复权开盘价)/后复权因子*(收盘价-开盘价)) | 趋势                     |
|          |          |                                                              |                          |
|          | Alpha39  | hpercentrank(delta(后复权收盘价,7)/后复权因子*  (1-HPercentRank(decayMA(当日成交量/20日平均成交额,9))),0,0)*(1+hpercentrank(sum(1日涨幅,250),0,0)) | 反转+量价背离            |
|          | Alpha40  | (0-hpercentrank(stdev(后复权最高价,10)))*barcorr(最高价,当日成交量,10) | 低波动+量价背离          |
|          | Alpha43  | percentRank(当日成交量/20日平均成交额,20)*percentRank((0-delta(后复权收盘价,7)/后复权因子),8) | 反转 价跌量涨            |
|          | Alpha44  | 0-barcorr(后复权最高价,hrank(当日成交量),5)                  | 量价背离                 |
|          | Alpha45  | 0-hrank(MA(barref(后复权收盘价,5),20)/后复权因子)*barcorr(收盘价,当日成交量,2)*  hrank(barcorr(sum(后复权收盘价,5),sum(后复权收盘价,20),2)) | 反转+量价背离            |
|          | Alpha47  | hpercentrank(收盘价,0,  0)*当日成交量/20日平均成交额*最高价*hpercentrank(最高价-收盘价)/MA(最高价,5)-hpercentrank(delta(后复权日均成交价,5)/后复权因子) |                          |
|          | Alpha50  | 0-max(hrank(barcorr(hrank(当日成交量),hrank(日均成交价),5)),5) | 量价背离                 |
|          | Alpha52  | (barref(min(后复权最低价,5),5)-min(后复权最低价,5))/后复权因子*hpercentrank((sum(1日涨幅,240)-sum(1日涨幅,20))/220)*percentRank(当日换手率,5) | 量价背离                 |
|          | Alpha55  | 0-barcorr(hrank((后复权收盘价-min(后复权最低价,12))/(max(后复权最高价,12)-min(后复权最低价,  12))), hrank(当日换手率),6) | 量价背离                 |
|          | Alpha58  | 1-percentrank(decayMa(barcorr(hDemean(日均成交价,  1),当日成交量, 4), 8),6) | 量价背离                 |
|          | Alpha59  | 1-percentrank(decayMA(barcorr(hDemean(日均成交价,1),当日成交量,4),16),8) | 量价背离                 |
|          | Alpha63  | hrankscore(decayMA(barcorr((日均成交价*0.318+开盘价*0.682),sum(N日均成交金额(180),  37),14),12)) - hrankscore(decayMA(delta(hDemean(收盘价,1),2),8)) | 短价和长量高相关， 价格  |
|          | Alpha67  | 0-  power(hpercentrank((后复权最高价-min(后复权最高价,2))/后复权因子),hpercentrank(barcorr(hDemean(日均成交价,  1),hDemean(20日平均成交额,2),6))) | 量价背离                 |
|          | Alpha69  | 0-power(hpercentrank(max(delta(hDemean(日均成交价,1),3),  5)),percentRank(barcorr(后复权收盘价*0.490655+后复权日均成交价*0.509345,20日平均成交额,5), 9)) | 量价背离，低价           |
|          | Alpha70  | 0-power(hpercentrank(delta(后复权日均成交价,1)/后复权因子),percentrank(barcorr(hDemean(收盘价,  1),N日均成交金额(50),18),18)) | 量价背离，低价           |
|          | Alpha71  | greater(percentRank(decayMA(barcorr(percentRank(后复权收盘价,3),percentRank(N日均成交金额(180),12),18),4),16),  percentRank(decayMA(power(hpercentrank(最低价 + 开盘价-日均成交价*2),2),16),4)) |                          |
|          | Alpha72  | hrank(decayMA(barcorr((后复权最高价+后复权最低价)/2,  N日均成交金额(40), 9),10))/ hrank(decayMA(barcorr(percentRank(后复权日均成交价,4),  percentRank(当日成交量,19),7), 3)) | 短价和长量高相关， 量价  |
|          | Alpha76  | 0-Greater(hpercentrank(decayMA(delta(后复权日均成交价,1)/后复权因子,12)),  percentRank(decayMA(percentRank(barcorr(hDemean(最低价,1),N日均成交金额(81),  8),20),17),19)) |                          |
|          | Alpha77  | Less(hrank(decayMA((后复权最高价+后复权最低价)/2-后复权日均成交价,20)/后复权因子),  hrank(decayMA(barcorr((后复权最高价+后复权最低价)/2,N日均成交金额(40),3),6))) |                          |
|          | Alpha78  | power(hpercentRank(barcorr(MA(后复权最低价*0.352233+后复权日均成交价*(1-0.352233),20),MA(N日均成交金额(40),20),7)),  hPercentRank(barcorr(hrank(日均成交价),hrank(当日成交量),6))) |                          |
|          | Alpha80  | 0-power(hpercentrank(Sign(delta(hDemean(开盘价*0.868128+最高价*(1-0.868128),  1),4))), percentRank(barcorr(后复权最高价,N日均成交金额(10),5),6)) |                          |
|          | Alpha82  | 0-less(hpercentrank(decayMa(delta(开盘价,1),15)),percentRank(decayma(barcorr(hDemean(当日成交量,1),开盘价,17),  7),13)) |                          |
|          | Alpha83  | hpercentrank(barref((后复权最高价-后复权最低价)/5日复权均价,2))*hPercentRank(当日成交量)/((后复权最高价-后复权最低价)/5日复权均价/(日均成交价-收盘价)) |                          |
|          | Alpha85  | power(hpercentrank(barcorr(后复权最高价*0.876703+后复权收盘价*(1-0.876703),N日均成交金额(30),  10)), hpercentrank(barcorr(percentRank((后复权最高价+后复权最低价)/2,  4),percentrank(当日成交量,10), 7))) |                          |
|          | Alpha87  | 0-greater(hpercentrank(decayma(delta(后复权收盘价*0.369701+后复权日均成交价*(1-0.369701),2)/后复权因子,3)),percentRank(decayma(abs(barcorr(hdemean(N日均成交金额(81),  1), 后复权收盘价,13)),5),14)) |                          |
|          | Alpha88  | less(hPercentRank(decayma((hPercentRank(开盘价)+hPercentRank(最低价)-hPercentRank(最高价)-hPercentRank(收盘价)),  8)),percentRank(decayma(barcorr(percentRank(后复权收盘价,8),  percentRank(N日均成交金额(60),21),8),7),3)) |                          |
|          | Alpha89  | percentRank(decayMA(barcorr(后复权最低价,  N日均成交金额(10), 7), 6),4)- percentRank(decayMA(delta(hdemean(日均成交价,1),3),10),15) |                          |
|          | Alpha90  | 0-power(hpercentrank((后复权收盘价-max(后复权收盘价,5))  / 后复权因子), percentRank(barcorr(hdemean(N日均成交金额(40), 1),后复权最低价,5),3)) | 短价和长量高相关，反转   |
|          | Alpha91  | hpercentrank(decayma(barcorr(后复权日均成交价,N日均成交金额(30),4),3))  - percentRank(decayma(decayma(barcorr(hdemean(收盘价,  1),当日成交量,10),16),4),5) | 短价和长量高相关，量价背 |
|          | Alpha92  | less(percentRank(decayMa(if((最高价+最低价)/2+收盘价<最低价+开盘价,  1, 0),15), 19),  percentRank(decayMA(barcorr(hpercentrank(最低价),hpercentrank(N日均成交金额(30)),8),  7), 7)) |                          |
|          | Alpha93  | percentRank(decayma(barcorr(hdemean(日均成交价,1),N日均成交金额(81),  17),19),8)/hpercentrank(decayma(delta(后复权收盘价*0.524434+后复权日均成交价*10.524434,  3),16)/后复权因子) | 短价和长量高相关，低价格 |
|          | Alpha94  | 0-power(hPercentRank((后复权日均成交价-min(后复权日均成交价,16))/后复权因子),  percentRank(barcorr(percentRank(后复权日均成交价,20), percentRank(N日均成交金额(60),4),18),  3)) | 短价和长量高相关， 反转  |
|          | Alpha96  | 0-greater(percentRank(decayma(barcorr(hpercentrank(日均成交价),hpercentrank(当日成交量),  4), 4), 8), percentRank(decayMA(ArgMax(barcorr(percentRank(后复权收盘价,7),  percentRank(N日均成交金额(60),4), 4),13),14),13)) | 短价和长量高相关，量价背 |
|          | Alpha97  | percentRank(decayMA(percentRank(barcorr(percentRank(后复权最低价,  8), percentRank(N日均成交金额(60),17), 5),19),16), 7) -  hpercentrank(decayMA(delta(hdemean((最低价*0.721001+日均成交价*(1-0.721001)),  1),3),20)) | 短价和长量高相关， 反转  |
|          | Alpha98  | hpercentrank(  decayMA(percentRank(ArgMin(barcorr(hrank(开盘价),hrank(N日均成交金额(15)),21),9),  7),8)) - hpercentrank(decayma(barcorr(后复权日均成交价,sum(5日平均成交额,26),5),7)) |                          |
|          | Alpha100 |                                                              | 短价和长量高相关， 反转, |
|          |          | (hscale(hdemean(barcorr(后复权收盘价,  hPercentRank(N日均成交金额(20)),5)-hpercentrank(argmin(后复权收盘价,30)),2), 0) - |                          |
|          |          | 1.5*hscale(hdemean(hdemean(hpercentrank((收盘价*2  -最低价-最高价)/(最高价-最低价)*当日成交量),2), 2), 0))*(当日成交量/N日均成交金额(20)) |                          |
| 二分类   | Alpha21  | if ((MA(后复权收盘价,8) +  stdev(后复权收盘价,8))< MA(后复权收盘价,2),(0-1), if(MA(后复权收盘价,  2)<(MA(后复权收盘价,8)-stdev(后复权收盘价,8)), 1, if((当日成交量/ 20日平均成交量)< 1), 0, 1)) | 反转                     |
|          | Alpha27  | if(HPercentRank(MA(barcorr(hrank(当日成交量),hrank(日均成交价),6),2))  > 0.5, 0,1) | 量价背离                 |
|          | Alpha61  | if  (hrank((后复权日均成交价/min(后复权日均成交价,16))) < hrank(barcorr(日均成交价,  N日均成交金额(180),18)) , 1, 0) | 量价背离                 |
|          | Alpha62  | if(hrank(barcorr(后复权日均成交价,sum(20日平均成交额,22),10))  < hrank(if (hrank(开盘价)* 2<(hrank((最高价+最低价)/2)+hrank(最高价)), 1, 0), 0,0),  0, 1) |                          |
|          | Alpha64  | if(hrank(barcorr(sum(开盘价*0.178404+最低价*0.821596,13),ma(N日均成交金额(120),13),17))  < hrank(delta((后复权最高价+后复权最低价)/2*0.17840+后复权日均成交价*10.178404,4)/后复权因子),0, 1) | 短价和长量高相关， 价格  |
|          | Alpha65  | if(hrank(barcorr((开盘价*0.00817205+日均成交价*0.99182795),ma(N日均成交金额(60),9),6))  < hrank(后复权开盘价/min(后复权开盘价,14)), 0, 1) | 短价和长量高相关，价格低 |
|          | Alpha68  | if(percentRank(barcorr(hrank(最高价,  0,0),hrank(N日均成交金额(15), 0, 0),9),14) <  hpercentrank(delta(后复权收盘价*0.518371+后复权最低价*0.481629,1)/后复权因子), 0, 1) |                          |
|          | Alpha74  | if(hrank(barcorr(后复权收盘价,MA(N日均成交金额(30),37),15))<  hrank(barcorr(hrank(最高价*0.0261661+日均成交价*0.9738339),hrank(当日成交量),11)), 0, 1) |                          |
|          | Alpha75  | if(hrank(barcorr(日均成交价,当日成交量,4))<hrank(barcorr(hrank(最低价),hrank(N日均成交金额(50)),  12)), 1,0) | 量价关系                 |
|          | Alpha79  | if(hrank(delta(hDemean(收盘价*0.60733+开盘价*(1-0.60733),  1),1),1,0) <  hrank(barcorr(percentRank(后复权日均成交价,4),percentRank(N日均成交金额(150),  9),15),1,0),0,1) |                          |
|          | Alpha86  | if(percentRank(barcorr(后复权收盘价,ma(N日均成交金额(20),15),6),20)  < hpercentrank(收盘价-日均成交价),0,1) |                          |
|          | Alpha81  | if(hrank(Log(product(hpercentrank(barcorr(后复权日均成交价,ma(N日均成交金额(10),  50), 8)),15))) < hrank(barcorr(hrank(日均成交价),hrank(当日成交量),5)), 0, 1) |                          |
|          | Alpha95  | if  (hPercentRank((后复权开盘价-min(后复权开盘价,12))/后复权因子) <  percentRank(hPercentRank(barcorr(ma((后复权最高价+后复权最低价)/2,19),ma(N日均成交金额(40),19),13)),12),  1,0) | 短价和长量高相关， 反转  |
|          | Alpha99  | if  (hpercentrank(barcorr(ma((后复权最高价+后复权最低价)/2,20),ma(N日均成交金额(60),20),9))<  hpercentrank(barcorr(最低价,当日成交量,6)), 0, 1) |                          |


import pandas as pd

   # 移动求和
def ts_sum(se, window=10):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return se.rolling(window).sum()

# 移动平均
def ts_mean(se, window=10):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return se.rolling(window).mean()

# 标准差
def stddev(se, window=10):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return se.rolling(window).std()

# 相关系数
def correlation(se_x, se_y, window=10):
    if not isinstance(se_x, pd.Series):
        se_x = pd.Series(se_x)
    if not isinstance(se_y, pd.Series):
        se_y = pd.Series(se_y)
    return se_x.rolling(window).corr(se_y)

# 协方差
def covariance(se_x, se_y, window=10):
    if not isinstance(se_x, pd.Series):
        se_x = pd.Series(se_x)
    if not isinstance(se_y, pd.Series):
        se_y = pd.Series(se_y)
    return se_x.rolling(window).cov(se_y)

def rolling_rank(se):
    return rankdata(se)[-1]

# 移动排序
def ts_rank(se, window=10):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return se.rolling(window).apply(self.rolling_rank)

def rolling_prod(se):
    return se.prod(se)

def product(se, window=10):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return se.rolling(window).apply(self.rolling_prod)

# 移动窗口最小值
def ts_min(se, window=10):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return se.rolling(window).min()

# 最大值
def ts_max(se, window=10):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return se.rolling(window).max()

# delta
def delta(se, period=1):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return se.diff(period)

# shift
def delay(se, period=1):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return se.shift(period)

# 排序
def rank(se):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return se.rank(axis=1, pct=True)

def scale(se, k=1):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return se.mul(k).div(np.abs(se).sum())

def ts_argmax(se, window=10):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return se.rolling(window).apply(np.argmax) + 1

def ts_argmin(se, window=10):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return se.rolling(window).apply(np.argmin) + 1

def decay_linear(se, period=10):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return ta.WMA(se.values, period)

# 斜率
def slope(se, period=10):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return ta.LINEARREG_SLOPE(se.values, period)

def atr(df):
    if not isinstance(df, pd.DataFrame):
        df = pd.Series(df)
    return ta.abstract.ATR(df)

def momentum(se, period=10):
    if not isinstance(se, pd.Series):
        se = pd.Series(se)
    return ta.ROCP(se.values, period)

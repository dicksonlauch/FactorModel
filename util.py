import pandas as pnd
import datetime

def to_ticker(code):
    return str(code) + " HK Equity"

def to_code(ticker):
    return int(ticker[:-10])

def get_all_tickers():
    return list(pnd.read_excel("data1.xlsx", sheetname="Sales Growth", header=None, index_col=0).index)

def get_all_codes():
    return list(map(to_code, get_all_tickers()))

def get_field(code, field_name, datetime=None):
    if field_name == "SALES_GROWTH":
        series = pnd.read_excel("data1.xlsx", sheetname="Sales Growth", header=None, index_col=0).iloc[:, 0]
        return series.loc[to_ticker(code)]
    else:
        df = pnd.read_excel("data1.xlsx", sheetname=to_ticker(code), header=4, index_col=0)
        print(df)
        if datetime:
            return df.loc[datetime, field_name]
        else:
            return df.loc[:, field_name]

def get_series(field_name, datetime=None):
    if field_name == "SALES_GROWTH":
        series = pnd.read_excel("data1.xlsx", sheetname="Sales Growth", header=None, index_col=0).iloc[:, 0]
        series.name = 'SALES_GROWTH'
        series.index = map(to_code, series.index)
        return series
    else:
        dict = {}
        for ticker in get_all_tickers():
            df = pnd.read_excel("data1.xlsx", sheetname=ticker, header=4, index_col=0)
            dict[to_code(ticker)] = df.loc[datetime, field_name]
        return pnd.Series(dict, name=field_name)
import pandas as pd
from pandas import DataFrame, concat
from datetime import datetime
import os
from fastapi.responses import JSONResponse
from tabulate import tabulate


# This function stripes spaces in dataframe column name
def stripColVal(df, lLimit, hLimit):
    df.columns = df.columns.str.strip()
    #df.values = df.values.astype(str).apply(pd.Series.str.strip)
    df = df.drop(['AVG_PRICE', 'TTL_TRD_QNTY', 'TURNOVER_LACS', 'NO_OF_TRADES', 'DELIV_QTY', 'DELIV_PER'], axis= 1)
    df = df[df['SERIES'] == ' EQ']
    #df = df[df['PREV_CLOSE'] <= hLimit]
    #df = df[df['PREV_CLOSE'] >= lLimit]
    return df

#It generates the final data frame of bullish thrusting stocks
def checkThrusting(df4, df5)-> pd.DataFrame:
    tempdf = pd.DataFrame(columns= df4.columns)
    for i in df4.index:
        for j in df5.index:
            if df4['SYMBOL'][i] == df5['SYMBOL'][j] and df4['CLOSE_PRICE'][i] < df5['OPEN_PRICE'][j] and df4['OPEN_PRICE'][i] < df5['CLOSE_PRICE'][j] and df4['OPEN_PRICE'][i] > df5['OPEN_PRICE'][j]:
                tempdf.loc[j] = df5.loc[j]
    return tempdf

def outputFun():
    #File Path
    all_files = os.listdir('C:/Users/Administrator/OneDrive - MAQ Software/Whiz/Test/Stock-Market/Hdata/')
    all_files.sort()
    all_files
    #Read File
    df4 = pd.read_csv(f'C:/Users/Administrator/OneDrive - MAQ Software/Whiz/Test/Stock-Market/Hdata/{all_files[0]}')
    df5 = pd.read_csv(f'C:/Users/Administrator/OneDrive - MAQ Software/Whiz/Test/Stock-Market/Hdata/{all_files[1]}')
    # Removing unwanted columns
    df4 = stripColVal(df4, 100, 1000)
    df5 = stripColVal(df5, 100, 1000)
    df5 = df5[df5['SYMBOL'].isin(df4['SYMBOL'])]
    df4 = df4[df4['SYMBOL'].isin(df5['SYMBOL'])]

    # Generating Thrusting
    thrustingdf = checkThrusting(df4, df5)
    

    df = pd.DataFrame(thrustingdf)
    print(df)
    return {df.to_json(orient="table")}

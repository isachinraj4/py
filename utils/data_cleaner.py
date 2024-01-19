import pandas as pd
from pandas import DataFrame, concat
from datetime import datetime
import os
from fastapi.responses import JSONResponse


def strip_col(df):
    df.columns = df.columns.str.strip()
    df = df.drop(
        [
            "AVG_PRICE",
            "TTL_TRD_QNTY",
            "TURNOVER_LACS",
            "NO_OF_TRADES",
            "DELIV_QTY",
            "DELIV_PER",
        ],
        axis=1,
    )
    df = df[df["SERIES"] == " EQ"]
    return df



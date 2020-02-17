import pandas as pd
import numpy as np
from functools import lru_cache


@lru_cache(1)
def get_df_all():
    df1 = pd.read_csv('test - 1.csv', parse_dates=['date'])
    df2 = pd.read_csv('test - 2.csv', parse_dates=['date'])
    df3 = pd.read_csv('test - 3.csv')
    return pd.concat([df1, df2.merge(df3)], sort=False)


def get_some_stuff(month=1):
    df = get_df_all()
    df_month = df[df['date'].month == month]
    df_managers_stats = df.groupby('manager', as_index=False)[['invest', 'registrations']].agg('sum')
    df_managers_stats.replace([np.inf, -np.inf], np.nan, inplace=True)
    
    return df_month, df_managers_stats
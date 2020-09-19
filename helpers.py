
def replace_time_with_datetime(csv_file):
    import os
    import numpy as np
    import pandas as pd
    start_datetime = pd.to_datetime("1-1-2020")
    df = pd.read_csv(csv_file,index_col=0)
    df.loc[:,"datetime"] = start_datetime + pd.to_timedelta(np.round(df.index.values),unit='d')
    df.index = df.pop("datetime")
    df = df.loc[~df.index.duplicated(keep="last"),:]
    raw = os.path.split(csv_file)
    new_file = os.path.join(raw[0],"datetime_" + raw[1])
    df.to_csv(new_file)
    return new_file,df



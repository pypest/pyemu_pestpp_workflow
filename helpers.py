
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


def unwrap_mf6_arrays(org_d,new_d,nrow=120,ncol=60):
    import os
    import shutil
    import numpy as np

    assert os.path.exists(org_d),org_d
    if os.path.exists(new_d):
        shutil.rmtree(new_d)
    shutil.copytree(org_d,new_d)

    arr_files = [f for f in os.listdir(new_d) if "_layer" in f and f.endswith(".txt")]
    print(arr_files)
    for arr_file in arr_files:
        arr = np.loadtxt(os.path.join(new_d,arr_file)).reshape((nrow,ncol))
        fmt = "%15.6E"
        if "idomain" in arr_file:
            fmt = "%2d"

        np.savetxt(os.path.join(new_d,arr_file),arr,fmt=fmt)



if __name__ == "__main__":
    unwrap_mf6_arrays("temp_daily_test","unwrapped")

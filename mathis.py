import pandas as pd
import numpy as np
import math
import re
import scipy.stats as stats

def convert_to_snake_case(df):
    #add a space between any lowercase-capital letter pair, then replace spaces with _, the all to lowercase
    new_cols = {col: re.sub(r"([a-z]{1})([A-Z]{1})", r"\1 \2", col).replace(" ", "_").lower() for col in df.columns}
    return df.rename(columns = new_cols, inplace = True)

def zero_counts(df):
    counts = {col: df[col].value_counts().to_dict().get(0) for col in df.columns if df[col].value_counts().to_dict().get(0) != None}
    return {key: value for key, value in counts.items() if value > 0}

def neg_counts(df):
    counts = {col: sum([val for key, val in df[col].value_counts().items() if type(key) in [float, int] and key < 0]) for col in df.columns}
    return {key: value for key, value in counts.items() if value > 0}

def yes_no_to_bin(word):
    true_words = ['yes', 'true', 'y', 't']
    false_words = ['no', 'false', 'n', 'f']

    if str(word).lower() in true_words:
        return 1
    elif str(word).lower() in false_words:
        return 0
    else:
        return word

def get_corr_above_or_below(df, percentage):
    corr = df.corr()
    col_rows = corr.columns.tolist()

    keep_corrs = {}
    for col in col_rows:
        for row in col_rows:
            if corr.loc[col, row] >= percentage or corr.loc[col, row] <= percentage*-1:
                if col == row:
                    break
                if col in keep_corrs:
                    keep_corrs[col][row] = corr.loc[col, row]
                else:
                    keep_corrs[col] = {row: corr.loc[col, row]}

    return keep_corrs

def outlier_dict(df, deviation = 3):
    cols = df.dtypes.to_dict()

    outlier_values = {}
    for col, dtype in cols.items():
        if dtype in [np.float64, np.int64]:
            locations = np.abs(stats.zscore(df[col])) > deviation #credit to: https://stackoverflow.com/questions/23199796/detect-and-exclude-outliers-in-pandas-data-frame
            out_rows = df[locations]

            for row in out_rows.iterrows():
                loc = df.index.get_loc(row[0])
                if col in outlier_values:
                    outlier_values[col].append(df.iloc[loc, df.columns.get_loc(col)])
                else:
                    outlier_values[col] = [df.iloc[loc, df.columns.get_loc(col)]]

    for key, val in outlier_values.items():
        outlier_values[key].sort()

    return outlier_values

def corrs_selection(df, col, threshold = .5, greater_than = True):
    sale_corr = df.corr().to_dict()[col]
    if greater_than:
        sale_corr = {key: val for key, val in sale_corr.items() if val > threshold}
    else:
        sale_corr = {key: val for key, val in sale_corr.items() if val < threshold}

    return pd.DataFrame(sale_corr, index =[0])

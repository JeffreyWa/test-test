import pandas as pd

def manipulate(df_in: pd.DataFrame, new_col:str, merging_col: list) -> pd.DataFrame:
    df = df_in.copy()
    df[new_col] = df[merging_col[0]]
    for col in merging_col[1:]:
        df[new_col] += df[col]
        del df[col]
    return df

def plot(df: pd.DataFrame, outcome_var: str, feature_var: list, col_var: str) -> None:
    for var in feature_var:
        if var != col_var:
            df.plot.scatter(x = var, y = outcome_var, c = col_var, cmap='viridis')

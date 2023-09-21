import pandas as pd


def manipulate(
    df_in: pd.DataFrame, new_col: str, merging_col: list, keep_col: list
) -> pd.DataFrame:
    df = df_in.copy()
    df[new_col] = 0
    for col in merging_col:
        df[new_col] += df[col]
        if col not in keep_col:
            del df[col]
    return df


def plot(df: pd.DataFrame, outcome_var: str, feature_var: list, col_var: str) -> None:
    plot_count = 0
    for var in feature_var:
        if var != col_var and var != outcome_var:
            df.plot.scatter(x=var, y=outcome_var, c=col_var, cmap="viridis")
            plot_count += 1

    return plot_count

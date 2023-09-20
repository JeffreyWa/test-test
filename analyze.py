from mylib import lib
import pandas as pd


def analyze():
    marketing_data_full = pd.read_csv("data/ifood_df.csv")
    marketing_data = lib.manipulate(
        marketing_data_full,
        "TotalSpending",
        [
            "MntWines",
            "MntFruits",
            "MntMeatProducts",
            "MntFishProducts",
            "MntSweetProducts",
        ],
        ["MntWines", "MntMeatProducts"],
    )
    marketing_data = lib.manipulate(
        marketing_data,
        "AcceptedOffer",
        [
            "AcceptedCmp1",
            "AcceptedCmp2",
            "AcceptedCmp3",
            "AcceptedCmp4",
            "AcceptedCmp5",
        ],
        [],
    )
    marketing_data.describe()

    lib.plot(marketing_data, "Income", "AcceptedOffer")

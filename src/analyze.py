import pandas as pd
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mylib import mylib

def analyze():

    marketing = pd.read_csv("data/ifood_df.csv")
    predictor = "Income"
    product = [
        "MntWines",
        "MntFruits",
        "MntMeatProducts",
        "MntFishProducts",
        "MntSweetProducts",
    ]
    offer = [
        "AcceptedCmp1",
        "AcceptedCmp2",
        "AcceptedCmp3",
        "AcceptedCmp4",
        "AcceptedCmp5",
    ]

    marketing = marketing[[predictor] + product + offer]

    # use mylib.py to manipulate data
    marketing = mylib.manipulate(
        marketing, "TotalSpending", product, ["MntWines", "MntMeatProducts"]
    )
    marketing = mylib.manipulate(marketing, "AcceptedOffer", offer, [])
    marketing.describe()

    plot_num = mylib.scatter_plot_by_col(
        marketing, predictor, marketing.columns.tolist(), "AcceptedOffer"
    )
    return marketing, plot_num

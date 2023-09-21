from src import analyze as an


def test_analyze():
    result = an.analyze()

    assert result[0].columns.tolist() == [
        "Income",
        "MntWines",
        "MntMeatProducts",
        "TotalSpending",
        "AcceptedOffer",
    ]
    assert result[1] == 3

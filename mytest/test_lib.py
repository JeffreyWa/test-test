from lib import mylib
import pandas as pd


def test_manipulate():
    # Arrange
    data = [["tom", 10, 100, 200], ["nick", 15, 120, 300], ["juli", 14, 130, 400]]
    df = pd.DataFrame(data, columns=["Name", "Age", "Allowance", "Job"])

    # Act
    result = mylib.manipulate(df, "Income", ["Allowance", "Job"], ["Job"])
    expected_data = [
        ["tom", 10, 200, 300],
        ["nick", 15, 300, 420],
        ["juli", 14, 400, 530],
    ]
    expected = pd.DataFrame(expected_data, columns=["Name", "Age", "Job", "Income"])

    # Assert
    assert result.equals(expected)


def test_plot():
    # Create a sample DataFrame
    data = {
        "Age": [21, 22, 23, 24, 25],
        "feature1": [5, 4, 3, 2, 1],
        "feature2": [10, 15, 20, 25, 30],
        "target_variable": [33, 22, 54, 27, 12],
        "col_variable": [0, 1, 0, 1, 0],
    }
    df = pd.DataFrame(data)

    # Call the plot function and check if it runs without errors
    try:
        # Call the plot function
        nums_plot = mylib.scatter_plot_by_col(
            df, "target_variable", ["feature1", "feature2"], "col_variable"
        )

        # If the plot function runs successfully,
        # do additional checks on the number of plots generated
        expected_num_plots = 2
        assert nums_plot == expected_num_plots

    except Exception as e:
        # If an exception is raised during plotting, raise an AssertionError
        raise AssertionError(
            f"An unexpected exception occurred during plotting: {str(e)}"
        )

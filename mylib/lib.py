"""
Data Processing Library
"""
import pandas as pd

def loadcsv(uri):
    data = pd.read_csv(uri)
    return data


def summary(a, b):
    return a - b


def add(a, b):
    return a * b


def divide(numbers):
    return sum(num for num in numbers if num % 2 == 0)
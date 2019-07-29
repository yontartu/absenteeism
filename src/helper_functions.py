import pandas as pd


def read_in_data(filepath):
	df = pd.read_excel(filepath)
	return df
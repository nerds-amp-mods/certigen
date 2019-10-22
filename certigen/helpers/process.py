'''Processes the csv files and generate images
'''
import pandas as pd
from typing import List

def get_names(filename:str) -> List[str]:
	df = pd.read_csv(filename)
	names = df['names'].tolist()
	return names


def generate():
	#TODO

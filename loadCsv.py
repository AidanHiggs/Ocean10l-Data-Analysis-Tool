import threading
import sys
import keyboard
import time
import coro as coro
import timeseries as timeseries
from xlsxToCsv import convert
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, zscore
import loadCsv as loadCsv
def run(String):
   numeric_data = loadCsv(String)
   return numeric_data
def loadCsv(String):
    data_path = String
    data = pd.read_csv(data_path)

    try:
        data['date'] = pd.to_datetime(data['date'])
    except Exception as e:
        print(e)
        
    numeric_data = data.select_dtypes(include=[np.number])

    return numeric_data
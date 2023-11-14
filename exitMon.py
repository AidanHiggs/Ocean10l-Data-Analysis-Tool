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
import multiCoro as multiCoro
import limComp as lm
exit = True 

def main():
    intro()
            
def intro():
    path = ""
    while True:
        print("Welcome to Ocean 10 Lab Data Analysis Tool, press 'esc' to exit the program at any time")
        print("If your data is formatted as xlsx press 1, if it is formatted as csv press 2")
        select = input()
        Path = ""  # Initialize Path with an empty string
        if select == '1':  # Compare with '1' as string
            print("Please provide the path to the excel file")
            xlsxPath = input()
            convert(xlsxPath)
            Path = "data.csv"  # Assign a value to Path
            methodSel(Path)
            break # Exit the loop after methodSel is called
        elif select == '2':  # Compare with '2' as string
            print("Please provide the path to the csv file")
            Path = input()
            methodSel(Path)
            break # Exit the loop after methodSel is called
            
def methodSel(Path):
    
    initPath(Path)        
    print("1. Correlation Analysis")
    print("\n2. Time Series Analysis")
    sel = int(input())
    pathFile = ("'" + str(sel) + "'")
    print("Please select the tool you would like to use")
    print(pathFile)
    switch = {
        1: coroInit,
        2: timeseries
    }
    
    while sel not in switch.keys():
        print("Invalid input. Please try again.")
        sel = int(input())
        
    selected_module = switch.get(sel)
    
    if selected_module:
        selected_module(Path)
    else:
        print("Invalid case")
def initPath(Path):
    global data
    data = loadCsv.run(Path)
        
def displayData(Path):
    # Collect multiple column selections
    selected_columns = []
    print("Select data points to compare: \n")
    for i, column in enumerate(data.columns):
        print(f"{i+1}. {column}")
        print("\n")
        return selected_columns
def coroInit(Path):
    selected_columns = []
    print("Please select the tool you would like to use")
    print("1. Compare Selected values")
    print("\n2. Compare all values")
    sel = int(input())
    switch = {
        1: defComp,
        2: multiComp
    }
    while sel not in switch.keys():
        print("Invalid input. Please try again.")
        sel = int(input())
        
    selected_module = switch.get(sel)
    
    if selected_module:
        selected_module(Path)
    else: 
        print("Invalid unput")
        CoroInit(Path)
    
def multiComp(Path):
    displayData()
    selected_columns = []
    while True:
        select = input("Select up to 3 columns type 'done' to finish): ")
        if select.lower() == 'done':
            break
        try:
            select = int(select) - 1
            if select >= 0 and select < len(data.columns):
                selected_columns.append(data.columns[select])
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    if selected_columns:
        print("Selected columns:", selected_columns)
        coro.run(selected_columns, w)
    else:
        print("No columns selected. Exiting...")


def defComp(Path):
    while True:
        select = input("Please select data to be comparered:")
        selected_columns = displayData();
        displayData();
        if select.lower() == 'done':
            break
        try:
            select = int(select) - 1
            if select >= 0 and select < len(data.columns):
                selected_columns.append(data.columns[select])
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

        if selected_columns:
            print("Selected columns:", selected_columns)
            out = limComp.run(selected_columns, Path)
            print(out)
        else:
            print("No columns selected. Exiting...")
            
while True:
        main()        


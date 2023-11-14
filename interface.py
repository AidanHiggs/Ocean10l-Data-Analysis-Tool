import coro
import timeseries
from xlsxToCsv import convert
Path = ""
def main():
    print("welcome to Ocean 10 Lab Data Analysis Tool, type 'exit' to exit the program at any time")
    print("If your data is formatted as xlsx press 1, if it is formatted as csv press 2")
    select = input()
    Path = ""  # Initialize Path with an empty string
    if select == '1':  # Compare with '1' as string
        print("Please provide the path to the excel file")
        xlsxPath = input()
        convert(xlsxPath)
        Path = "data.csv"  # Assign a value to Path
    elif select == '2':  # Compare with '2' as string
        print("Please provide the path to the csv file")
        Path = input()
    else :
        print("Invalid input")
        
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

    selected_module = switch.get(sel)
    
    if selected_module:
        selected_module.run(Path)
    else:
        print("Invalid case")
while True:
    main()

def coroInit(Path):
    limComp(Path)

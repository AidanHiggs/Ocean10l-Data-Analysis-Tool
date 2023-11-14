import pandas as pd

def convert(path):
    # Read the xlsx file
    data = pd.read_excel(path)
    
    # Convert the data to csv format
    csv_data = data.to_csv(index=False)
    
    # Export the csv data to a file
    with open("data.csv", "w") as file:
        file.write(csv_data)
    

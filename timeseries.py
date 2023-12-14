import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def run(analysis_columns, path):
    data = pd.read_csv(path)

    if isinstance(analysis_columns, str):
        analysis_columns = [analysis_columns]

    numeric_columns = data.select_dtypes(include=[np.number]).columns
    selected_columns = [col for col in analysis_columns if col in numeric_columns]

    if not selected_columns:
        print("No valid numeric columns selected for correlation analysis.")
        return

    numeric_data = data[numeric_columns]
    # Convert the 'date' column to datetime
    data['date'] = pd.to_datetime(data['date'])

    # Function to assign a season to a row based on its month
    def get_season(row):
        month = row['date'].month
        if month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        elif month in [9, 10, 11]:
            return 'Autumn'
        else:  # months 12, 1, 2
            return 'Winter'

    # Apply the function to assign seasons
    data['Season'] = data.apply(get_season, axis=1)

    # Handle missing values for plotting by filling them with the mean values
    data_filled = data.copy()
    for col in selected_columns:
        data_filled[col].fillna(data_filled[col].mean(), inplace=True)

    # Creating a time series plot of values over time for each selected column
    sns.set(style="whitegrid")  # Setting the style of the plots
    plt.figure(figsize=(14, 7))

    # Plot each measurement
    for column in selected_columns:
        plt.plot(data_filled['date'], data_filled[column], label=column.capitalize().replace('_', ' '))

    # Improving the plot
    columns_title = ', '.join([col.capitalize().replace('_', ' ') for col in selected_columns])
    plt.title('Time Series - ' + columns_title + ' over time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.tight_layout()

    # Show the plot
    print("would you like to display the graph (not working atm)? (y/n)")
    sel = input()
    if sel == 'y':
        plt.show()
    elif sel == 'n':
        print("Graph not displayed.")
    else:
        print("Invalid input. Graph not displayed. Exiting...")


    # Ask user if they want to save the plot
    save_plot = input("Do you want to save the plot? (y/n): ")
    if save_plot.lower() == 'y':
        plt.savefig('time_series.png')
        print("Plot saved as time_series.png")
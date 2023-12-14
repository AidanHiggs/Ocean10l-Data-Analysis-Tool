from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import pandas as pd

def run(column, Path):
    data = pd.read_csv(Path)
    data['date'] = pd.to_datetime(data['date'])
    data = data.sort_values('date')
    data.set_index('date', inplace=True)

    data[column] = data[column].ffill()

    # Calculate the most common weekly frequency
    data['date_diff'] = data.index.to_series().diff().dt.days.dropna()
    if len(data['date_diff']) > 0:
        freq = round(data['date_diff'].median())  # Using median as a more robust measure
    else:
        freq = 7  # Default to 7 days if no date differences are available

    result = seasonal_decompose(data[column], model='additive', period=freq)

    # Extracting components
    trend = result.trend
    seasonal = result.seasonal
    resid = result.resid

    # Printing components
    print("Trend Component:\n", trend)
    print("\nSeasonal Component:\n", seasonal)
    print("\nResidual Component:\n", resid)

    # Prepare the components for saving
    components_str = f"Trend Component:\n{trend}\n\nSeasonal Component:\n{seasonal}\n\nResidual Component:\n{resid}\n"
    
    # Ask user if they want to save the components to a text file
    save_data = input("Do you want to save the decomposition data to a text file? (y/n): ")
    if save_data.lower() == 'y':
        with open(f'{column}_decomposition_components.txt', 'w') as file:
            file.write(components_str)
        print(f"Data saved as {column}_decomposition_components.txt")

    result.plot()
    plt.title(f'Time Series Decomposition of {column}')
    plt.show()

    save_plot = input(f"Do you want to save the plot for {column}? (y/n): ")
    if save_plot.lower() == 'y':
        plt.savefig(f'{column}_time_series_decomposition_plot.png')
        print(f"Plot saved as {column}_time_series_decomposition_plot.png")

    return result

# Example usage


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the CSV data into a DataFrame
def run(String):
    data_path = Sel
    data = pd.read_csv(data_path)

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
    turbidity_columns = ['surface turbidity', 'mid turbidty', 'deep turbidity']
    data_filled = data.copy()
    for col in turbidity_columns:
        data_filled[col].fillna(data_filled[col].mean(), inplace=True)

    # Creating a time series plot of turbidity at different depths
    sns.set(style="whitegrid")  # Setting the style of the plots
    plt.figure(figsize=(14, 7))

    # Plot each turbidity measurement
    for depth in turbidity_columns:
        plt.plot(data_filled['date'], data_filled[depth], label=depth.capitalize().replace('_', ' '))

    # Improving the plot
    plt.title('Time Series - Turbiditty at different depths over time')
    plt.xlabel('Date')
    plt.ylabel('Turbidity (NTU)')
    plt.legend()
    plt.tight_layout()

    # Save the plot as an SVG file in the desired directory
    plt.savefig('/home/flabbydino/Documents/turbidity_time_series.svg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, zscore
import loadCsv

def run(filtered_data, Path):
    # Load the full CSV data into a DataFrame
    data = loadCsv.run(Path)

    # Ensure that filtered_data is a list of column names
    if isinstance(filtered_data, str):
        filtered_data = [filtered_data]
    
    # Filter out columns that are not in the DataFrame or are not numeric
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    selected_columns = [col for col in filtered_data if col in numeric_columns]

    # Check if there are valid selected columns
    if not selected_columns:
        print("No valid numeric columns selected for correlation analysis.")
        return

    numeric_data = data[numeric_columns]

    # Calculate correlations between selected columns and all other numeric variables
    correlations = {}
    for selected_col in selected_columns:
        for other_col in numeric_data.columns:
            if selected_col != other_col:
                paired_data = numeric_data[[selected_col, other_col]].dropna()
                if not paired_data.empty:
                    corr, _ = pearsonr(paired_data[selected_col], paired_data[other_col])
                    corr = f"-{abs(corr)}" if corr < 0 else corr
                    correlations[f"{selected_col} vs {other_col}"] = corr

    # Find statistical anomalies in the data using Z-scores for the numeric columns
    anomalies = numeric_data.apply(zscore).abs() > 2

    # Convert the correlations dictionary to a series for better display and sort by absolute value
    correlation_series = pd.Series(correlations).astype(float).abs().sort_values(ascending=False)
    
    # Print the correlation coefficients
    print("Correlation coefficients:")
    print(correlation_series)
    
    # Count the number of anomalies for each column
    anomaly_counts = anomalies.sum().sort_values(ascending=False)
    
    # Print the anomaly counts
    print("\nAnomaly counts:")
    anomaly_counts = anomaly_counts.astype(int)  # Convert the counts to integers
    if (anomaly_counts > 1).any():  # Check if there are any counts greater than 1
        print(anomaly_counts)
    
    # Plotting the most significant correlations as scatter plots
    top_correlations = correlation_series.head(3).index
    
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 15))
    
    for i, corr in enumerate(top_correlations):
        selected_col, other_col = corr.split(" vs ")
        axes[i].scatter(numeric_data[selected_col], numeric_data[other_col])
        axes[i].set_xlabel(selected_col)
        axes[i].set_ylabel(other_col)
        axes[i].set_title(f'Scatter plot of {selected_col} vs {other_col} (Correlation: {correlation_series[corr]:.2f})')

    plt.tight_layout()
    
    # Save the figure as a PNG file to the specified directory
    plt.savefig('correlation_scatter_plots.png')
    
    # Export correlation data
    print("Would you like to export the correlation data? (y/n)")
    sel = input()
    if sel == 'y':
        with open(f'{selected_columns}_correlation_data.txt', 'w') as file:
            file.write(str(correlation_series))
            file.write('\n')
            file.write(str(anomaly_counts))
        print("Correlation data exported successfully.")
    elif sel == 'n':
        print("Correlation data not exported.")
    else:
        print("Invalid input. Correlation data not exported.")


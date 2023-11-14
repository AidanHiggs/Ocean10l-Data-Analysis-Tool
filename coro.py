import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, zscore
import loadCsv as loadCsv
def run(selected_columns, Path):
    # Load the CSV data
    data = loadCsv.run(Path)

    # Filter numeric data
    numeric_data = data.select_dtypes(include=[np.number])

    # Calculate correlations
    correlations = {}
    for selected_col in selected_columns:
        if selected_col in numeric_data.columns:
            for other_col in numeric_data.columns:
                if selected_col != other_col:
                    paired_data = numeric_data[[selected_col, other_col]].dropna()
                    if not paired_data.empty:
                        corr, _ = pearsonr(paired_data[selected_col], paired_data[other_col])
                        corr = f"-{abs(corr)}" if corr < 0 else corr
                        correlations[f"{selected_col} vs {other_col}"] = corr
    
    # Convert the correlations dictionary to a series for better display and sort by absolute value
    correlation_series = pd.Series(correlations).astype(float).abs().sort_values(ascending=False)
    
    # Print the correlation coefficients
    print("Correlation coefficients:")
    print(correlation_series)
    
    # Find statistical anomalies in the data using Z-scores for the numeric columns
    anomalies = numeric_data.apply(zscore).abs() > 22
    
    # Count the number of anomalies for each column
    anomaly_counts = anomalies.sum().sort_values(ascending=False)
    
    # Print the anomaly counts
    print("\nAnomaly counts:")
    anomaly_counts = anomaly_counts.astype(int)  # Convert the counts to integers
    if (anomaly_counts > 1).any():  # Check if there are any counts greater than 1
        print(anomaly_counts)
    
    # Plotting the most significant correlations as scatter plots
    # Selecting the top correlations to plot
    top_correlations = correlation_series.head(3).index
     
    # Plotting the significant correlations as scatter plots
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 15))
    print("Would you like to export the corolation data? (y/n)")
    sel = input()
    if sel == 'y':
        filename = input("Enter the filename to save the correlation data: ")
        with open(filename, 'w') as file:
            file.write(str(correlation_series))
            file.write('\n')
            file.write(str(anomaly_counts))
        print("Correlation data exported successfully.")
    elif sel == 'n':
        print("Correlation data not exported.")
    else:
        print("Invalid input. Correlation data not exported.")
    for i, corr in enumerate(top_correlations):
        depth, variable = corr.split(" vs ")
        axes[i].scatter(numeric_data[depth], numeric_data[variable])
        axes[i].set_xlabel(depth)
        axes[i].set_ylabel(variable)
        axes[i].set_title(f'Scatter plot of {depth} vs {variable} (Correlation: {correlation_series[corr]:.2f})')
    
    plt.tight_layout()
    
    # Save the figure as a PNG file to the specified directory
    plt.savefig('/home/flabbydino/Documents/correlation_scatter_plots.png')
    
    if column in anomaly_counts.index and anomaly_counts[column] > 1:
        for column in anomaly_counts.index:
            print(f"\nData for anomalies in '{column}':")
            anomalous_data = data[anomalies[column]]
            print(anomalous_data)
    # Additionally, ensure that the plt.show() line is commented out or removed to prevent the script from trying to open a window for the plot, which is not necessary when running the script from a terminal without a GUI.
    print("would you like to display the 1? (y/n)")
    sel = input()
    if sel == 'y':
        plt.show()
    elif sel == 'n':
        print("Graph not displayed.")
    else:
        print("Invalid input. Graph not displayed. Exiting...")

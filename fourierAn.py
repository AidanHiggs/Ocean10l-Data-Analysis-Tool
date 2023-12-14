import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft
import matplotlib
import pandas as pd
import numpy as np
from scipy.fft import fft
from typing import List
def run(analysis_columns, path: str) -> None:
    data = pd.read_csv(path)
    
    if isinstance(analysis_columns, str):
        analysis_columns = [analysis_columns]
    
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    selected_columns = [col for col in analysis_columns if col in numeric_columns]
    
    if not selected_columns:
        print("No valid numeric columns selected for correlation analysis.")
        return
    
    numeric_data = data[numeric_columns]
    
    for column in selected_columns:
        if column in data.columns:
            y = data[column].dropna().to_numpy()
            N = len(y)
            T = 1.0 / 7.0
            yf = fft(y)
            xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
            
            print(f"Fourier Analysis for {column}:")
            for freq, amplitude in zip(xf[:N // 2], 2.0 / N * np.abs(yf[:N // 2])):
                print(f"Frequency: {freq:.4f}, Amplitude: {amplitude:.4f}")
            
            view_plot = input(f"Do you want to view the plot for {column}? (y/n): ")
            if view_plot.lower() == "y":
                plot_fourier_results(xf, yf, column, N, T)
            
            save_data = input("Do you want to save these results? (y/n): ")
            if save_data.lower() == "y":
                save_fourier_results(xf, yf, column, N, T)

def plot_fourier_results(xf: np.ndarray, yf: np.ndarray, column: str, N: int, T: float) -> None:
    plt.figure(figsize=(10, 4))
    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    plt.grid()
    plt.title(f'Fourier Analysis of {column}')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.show()

def plot_fourier_results(xf, yf, column, N, T):
    plt.figure(figsize=(10, 4))
    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    plt.grid()
    plt.title(f'Fourier Analysis of {column}')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.show()

    # Prompt to save the plot
    save_plot = input(f"Do you want to save the plot for {column}? (y/n): ")
    if save_plot.lower() == 'y':
        plt.savefig(f'{column}_fourier_analysis_plot.png')
        print(f"Plot saved as {column}_fourier_analysis_plot.png")

def save_fourier_results(xf, yf, column, N, T):
    with open(f'{column}_fourier_analysis.txt', 'w') as file:
        file.write(f"Fourier Analysis for {column}:\n")
        for i, freq in enumerate(xf[:N//2]):
            amplitude = 2.0/N * np.abs(yf[i])
            file.write(f"Frequency: {freq:.4f}, Amplitude: {amplitude:.4f}\n")
    print(f"Results saved to {column}_fourier_analysis.txt")




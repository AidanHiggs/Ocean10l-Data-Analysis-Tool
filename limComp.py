import pandas as pd
import numpy as np
from scipy.stats import pearsonr

def run(selected_columns, Path):
    correlations = {}
    data = pd.read_csv(Path)
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    selected_numeric_columns = [col for col in selected_columns if col in numeric_columns]
    for i in range(len(selected_numeric_columns)):
        for j in range(i + 1, len(selected_numeric_columns)):
            paired_data = data[[selected_numeric_columns[i], selected_numeric_columns[j]]].dropna()
            if not paired_data.empty:
                corr, _ = pearsonr(paired_data[selected_numeric_columns[i]], paired_data[selected_numeric_columns[j]])
                corr = f"-{abs(corr)}" if corr < 0 else corr
                correlations[f"{selected_numeric_columns[i]} vs {selected_numeric_columns[j]}"] = corr
    
    return correlations
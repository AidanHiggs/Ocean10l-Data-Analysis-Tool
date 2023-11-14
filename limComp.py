import pandas as pd
import numpy as np
from scipy.stats import pearsonr

def run(selected_columns, Path):
    correlations = {}
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    
    for depth in selected_columns:
        for column in selected_columns:
            if column != depth and column in numeric_columns:
                paired_data = data[[depth, column]].dropna()
                if not paired_data.empty:
                    corr, _ = pearsonr(paired_data[depth], paired_data[column])
                    corr = f"-{abs(corr)}" if corr < 0 else corr
                    correlations[f"{depth} vs {column}"] = corr
    
    return correlations
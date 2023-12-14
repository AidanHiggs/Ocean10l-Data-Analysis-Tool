import pandas as pd
from semopy import Model, semplot

# Load the data
data_path = '/home/aidan/Downloads/data_for_path_analysis.csv'
data_for_path_analysis = pd.read_csv(data_path)

# Correcting the column names to match the model description
# Replace spaces with underscores and ensure they match the model's variable names
data_for_path_analysis.columns = data_for_path_analysis.columns.str.replace(' ', '_')
data_for_path_analysis.rename(columns={
    'Predicted_tide_height_(cm)': 'Predicted_tide_height_cm',
    'air_temp_(C)': 'air_temp_C',
    'secchi_depth_(cm)': 'secchi_depth_cm',
    'flow_rate_(m/s)': 'flow_rate_m_s'
}, inplace=True)
# Define the model
model_description = """
# Structural model
surface_turbidity ~ DOY + Predicted_tide_height_cm + Beaufort_Wind_Speed + air_temp_C + secchi_depth_cm + flow_rate_m_s
mid_turbidty ~ DOY + Predicted_tide_height_cm + Beaufort_Wind_Speed + air_temp_C + secchi_depth_cm + flow_rate_m_s
deep_turbidity ~ DOY + Predicted_tide_height_cm + Beaufort_Wind_Speed + air_temp_C + secchi_depth_cm + flow_rate_m_s
"""

# Define the model
path_model = Model(model_description)

# Estimate the model using the DataFrame
path_model.fit(data_for_path_analysis)

# Get the results
path_results = path_model.inspect()
print(path_results)

# Optional: Plotting the path model (requires 'graphviz' package)
semplot(path_model, "path_model_plot.png")

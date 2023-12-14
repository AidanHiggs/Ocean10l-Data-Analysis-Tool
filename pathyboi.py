import pandas as pd
from semopy import Model, semplot

# Load the data
data_path = '/home/aidan/Downloads/data_for_path_analysis.csv'
data_for_path_analysis = pd.read_csv(data_path)
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


path_model = Model(model_description)

# Estimate the model using the DataFrame
path_model.fit(data_for_path_analysis)

path_results = path_model.inspect()
print(path_results)

semplot(path_model, "path_model_plot.png")

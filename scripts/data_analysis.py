import pandas as pd
import os
import numpy as np

# Define path
cleaned_data_path = './data/processed/cleaned_weather_data.csv'
analysis_results_path = './data/processed/analysis_results.csv'

# Check if cleaned data file exists
if not os.path.exists(cleaned_data_path):
    print(f"Error: Cleaned data file {cleaned_data_path} not found. Please run data_cleaning.py first.")
    exit(1)

# Load the cleaned weather data
weather_data = pd.read_csv(cleaned_data_path)

# Perform statistical analysis
temperature_mean = weather_data['temperature'].mean()
temperature_std = weather_data['temperature'].std()
precipitation_sum = weather_data['precipitation'].sum()

# Calculate correlations
correlations = weather_data[['temperature', 'precipitation']].corr()

# Save analysis results
analysis_results = pd.DataFrame({
    'Temperature Mean': [temperature_mean],
    'Temperature Std Dev': [temperature_std],
    'Precipitation Sum': [precipitation_sum]
})

analysis_results.to_csv(analysis_results_path, index=False)

print("Data analysis completed. Analysis results saved to:", analysis_results_path)
print("Correlation matrix:")
print(correlations)

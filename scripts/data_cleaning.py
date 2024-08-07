import pandas as pd
import os

# Define paths
raw_data_path = './data/raw/weather_data.csv'
cleaned_data_path = './data/processed/cleaned_weather_data.csv'

# Check if raw data file exists
if not os.path.exists(raw_data_path):
    print(f"Error: Raw data file {raw_data_path} not found.")
    # Optional: Create a dummy file for demonstration purposes
    dummy_data = {
        'date': ['2024-01-01', '2024-01-02'],
        'temperature': [20, 21],
        'precipitation': [0.0, 0.1]
    }
    pd.DataFrame(dummy_data).to_csv(raw_data_path, index=False)
    print(f"Dummy data created at {raw_data_path}. Please replace with actual data.")

# Load the raw weather data
weather_data = pd.read_csv(raw_data_path)

# Clean the data
# Drop rows with missing values
weather_data = weather_data.dropna()

# Convert date column to datetime
weather_data['date'] = pd.to_datetime(weather_data['date'])

# Save cleaned data
weather_data.to_csv(cleaned_data_path, index=False)

print("Data cleaning completed. Cleaned data saved to:", cleaned_data_path)

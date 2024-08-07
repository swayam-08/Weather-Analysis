import pandas as pd
import os
import matplotlib.pyplot as plt

# Define path
cleaned_data_path = './data/processed/cleaned_weather_data.csv'

# Check if cleaned data file exists
if not os.path.exists(cleaned_data_path):
    print(f"Error: Cleaned data file {cleaned_data_path} not found. Please run data_cleaning.py first.")
    exit(1)

# Load the cleaned weather data
weather_data = pd.read_csv(cleaned_data_path)

# Create temperature trend plot
plt.figure(figsize=(10, 5))
plt.plot(weather_data['date'], weather_data['temperature'], label='Temperature', color='red')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature Trend Over Time')
plt.legend()
plt.grid(True)
plt.savefig('./data/processed/temperature_trend.png')
plt.show()

# Create precipitation histogram
plt.figure(figsize=(10, 5))
plt.hist(weather_data['precipitation'], bins=30, color='blue', edgecolor='black')
plt.xlabel('Precipitation')
plt.ylabel('Frequency')
plt.title('Precipitation Distribution')
plt.grid(True)
plt.savefig('./data/processed/precipitation_histogram.png')
plt.show()

print("Data visualization completed. Visualizations saved to ../data/processed/")

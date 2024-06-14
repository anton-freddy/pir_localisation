import pandas as pd
import random

# Define the parameters for the dataset
suburbs = ["Central", "Ponsonby", "Mt. Eden", "Manukau", "Takapuna", "Newmarket", "Henderson", "Albany", "North Shore", "Howick", "Epsom", "Greenlane", "Ellerslie", "Onehunga"]
crime_types = ["Theft", "Assault", "Burglary", "Vandalism", "Robbery", "Fraud", "Drug Offense", "Public Disorder", "Domestic Violence"]
times_of_day = ["AM", "PM"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Generate realistic data based on crime rate assumptions
data = {
    "Report ID": range(1, 2001),
    "Suburb": [random.choices(suburbs, weights=[200, 150, 150, 200, 100, 150, 200, 100, 150, 100, 50, 50, 50, 50])[0] for _ in range(2000)],
    "Type of Crime": [random.choice(crime_types) for _ in range(2000)],
    "Number Injured": [random.choices([0, 1, 2, 3, 4, 5], weights=[50, 30, 10, 5, 3, 2])[0] for _ in range(2000)],
    "Number Dead": [random.choices([0, 1, 2], weights=[90, 8, 2])[0] for _ in range(2000)],
    "Time of Day": [random.choices(times_of_day, weights=[30, 70])[0] for _ in range(2000)],
    "Month": [random.choice(months) for _ in range(2000)],
}

predicted_data = {
    "Report ID": range(2001, 4001),
    "Suburb": [random.choices(suburbs, weights=[200, 150, 150, 200, 100, 150, 200, 100, 150, 100, 50, 50, 50, 50])[0] for _ in range(2000)],
    "Type of Crime": [random.choice(crime_types) for _ in range(2000)],
    "Predicted Number Injured": [random.choices([0, 1, 2, 3, 4, 5], weights=[50, 30, 10, 5, 3, 2])[0] for _ in range(2000)],
    "Predicted Number Dead": [random.choices([0, 1, 2], weights=[90, 8, 2])[0] for _ in range(2000)],
    "Time of Day": [random.choices(times_of_day, weights=[30, 70])[0] for _ in range(2000)],
    "Month": [random.choice(months) for _ in range(2000)],
}

# Create dataframes
df_actual = pd.DataFrame(data)
df_predicted = pd.DataFrame(predicted_data)

# Save to CSV files
df_actual.to_csv('C:/Users/anton/Downloads/auckland_crime_actual_realistic.csv', index=False)
df_predicted.to_csv('C:/Users/anton/Downloads/auckland_crime_predicted_realistic.csv', index=False)


df_actual.head(), df_predicted.head()

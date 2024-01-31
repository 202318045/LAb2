import csv
import requests
import pandas as pd

# Your API endpoint and headers
url = "https://myanimelist.p.rapidapi.com/anime/top/movie"
headers = {
    "X-RapidAPI-Key": "965cecf2fcmshf72f9b0702af72cp1ee13cjsn223ea7ca43d2",
    "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
}

# Make the request
response = requests.get(url, headers=headers)
data = response.json()

# Specify the CSV file name
csv_file = "anime_data.csv"

# Write the data to CSV
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(data[0].keys())

    # Write data
    for item in data:
        writer.writerow(item.values())

print(f"CSV file '{csv_file}' has been created successfully.")

pd.read_csv('/home/notrambo614/Documents/GitHub/LAb2/anime_data.csv')
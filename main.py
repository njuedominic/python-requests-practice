# Import the required libraries
import os
import pandas as pd
import requests

# Create a function that takes in the url with the json data and returns a converted csv file

def json_to_csv(url):
    # 1. Fetch the data
    response = requests.get(url)
    data = response.json()
    # 2. Convert the data into a dataframe
    df = pd.DataFrame(data)
    # 3. Convert the dataframe into a csv and save it
    df.to_csv("./data/qatar_airways_data.csv", index = False)
    return df

data_url = input("Enter url with the json data: ")

# Call the function on the url
extracted_df = json_to_csv(data_url)
print("File has been saved!")
print(extracted_df.head())
# Import the required libraries
import os
import pandas as pd
import requests

# Create a function that takes in the url with the jsoin data and returns a converted csv file

def json_to_csv(url):
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    df_to_csv = df_to_csv("../data/qatar_airways_data.csv")
    return df_to_csv


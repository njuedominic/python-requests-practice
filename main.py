# Import the required libraries
import os
import pandas as pd
import requests

# Create a function that takes in the url with the json data and returns a converted csv file

def json_to_csv(url):
    # 1. Fetch the data
    response = requests.get(url)
    data = response.json()

    # 2. Extract the list from the dictionary
    if isinstance(data, dict):
        main_data = next(
            (v for v in data.values() if isinstance(v, list)),
            [data]
            )
    else:
        main_data = data
        
    # 3. Normalize the data (Flattening semi-structured data)
    df = pd.json_normalize(main_data)

    # 4.Flatten nested column
    for col in df.columns:
        # Explode lists
        if any(isinstance(val, list) for val in df[col].dropna()):
            df = df.explode(col)

        # Normalize dictionaries
        if any(isinstance(val, dict) for val in df[col].dropna()):

            nested_df = pd.json_normalize(df[col]).set_index(df.index)

            df = (
                df.drop(columns=[col])
                  .join(nested_df, rsuffix=f"_{col}")
            )
    # Save the file
    df.to_csv("./data/converted_data.csv", index = False)
    return df


data_url = input("Enter url with the json data: ")

# Call the function on the url
extracted_df = json_to_csv(data_url)
print("File has been saved!")
print(extracted_df.head())
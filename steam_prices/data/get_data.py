import pandas as pd
import os
import glob

#extend get_data.py to handle multiple data .csv files # get_data.py extracts the right data 

csv_files_price = glob.glob("data/*_price.csv") #gets price from csv files
csv_files_info = glob.glob("data/*_info.csv") #gets info from csv files
csv_files = list(set(csv_files_price + csv_files_info)) #combine both lists and remove duplicates

for file_path in csv_files:
    df_price = pd.read_csv(file_path, delimiter=";")
    df_info = pd.read_csv(file_path, delimiter=";")

    df_price_first = df_price.iloc[0]
    df_price_last = df_price.iloc[-1]

    first_price = df_price_first["FP"]
    first_date = df_price_first["DateTime"]

    last_price = df_price_last["FP"]
    last_date = df_price_last["DateTime"]

    file_name = os.path.basename(file_path)
    print(f"File: {file_name}")
    print("First and last price and date:")
    print(f"{first_price};{first_date}")
    print(f"{last_price};{last_date}")
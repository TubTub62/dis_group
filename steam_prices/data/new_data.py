#inserts data gotten from get_data.py into our database server # check how the bank example does it
import pandas as pd
import os
import psycopg2
import glob

ip = "localhost"
password = "admin"

conn = psycopg2.connect(
    database="steam_db",
    host=ip,
    user="postgres",
    password=password,
    port="5432"
)

def insert_price_data(file_path):
    df = pd.read_csv(file_path, delimiter=";")
    cur = conn.cursor()
    for _, row in df.iterrows():
        sql = """
        INSERT INTO prices (datetime,
                            fp)
        VALUES (%s, %s);
        """
        cur.execute(sql, (row['DateTime'], row['FP']))
    conn.commit()
    cur.close()

def insert_info_data(file_path):
    df = pd.read_csv(file_path, delimiter=";")
    cur = conn.cursor()
    for _, row in df.iterrows():
        sql = """
        INSERT INTO game_info (name,
                               appid,
                               type,
                               developer,
                               publisher,
                               release_date)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        cur.execute(sql, (row['Name'], row['AppID'], row['Type'], row['Developer'], row['Publisher'], row['ReleaseDate']))
    conn.commit()
    cur.close()

# Insert data from all CSV files in the 'data' directory
csv_files_info = glob.glob("data/*_info.csv")
csv_files_price = glob.glob("data/*_price.csv")
csv_files = list(set(csv_files_info + csv_files_price))  # Combine both lists and remove duplicates
for file_path in csv_files:
    if "_info" in file_path:
        insert_info_data(file_path)
    else:
        insert_price_data(file_path)

conn.close()

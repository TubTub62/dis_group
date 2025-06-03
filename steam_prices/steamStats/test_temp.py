from sql import *
import pandas as pd

df = pd.read_csv("../data/SteamDB_data.csv")

df = df.to_dict(orient="records")

print(df)

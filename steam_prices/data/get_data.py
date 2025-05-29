import pandas as pd

df_price = pd.read_csv("data/rust_price.csv", delimiter=";")
#df_info = pd.read_csv("data/rust_info.csv")


df_price_first = df_price.iloc[0]
df_price_last = df_price.iloc[-1]

first_price = df_price_first["FP"]
first_date = df_price_first["DateTime"]

last_price = df_price_last["FP"]
last_date = df_price_last["DateTime"]

print(f"{first_price};{first_date}")
print(f"{last_price};{last_date}")
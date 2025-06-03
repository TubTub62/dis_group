import pandas as pd
from sql import *

### needs to get data from csv by some python script, pressumably.
### currently only functions with temp data (temp data taken from Christian)

df = pd.read_csv("../data/SteamDB_data.csv")
df = df.to_dict(orient="records")


conn = create_connection()
for game in df:
    #print(game)

    insert_game(conn, game["name"], game["steam_id"])
    insert_update_release(conn, game["last_update"], game["release_date"])
    insert_prices(conn, game["current_price"], game["release_price"])

    insert_costs(conn, game["steam_id"], game["current_price"], game["release_price"])
    insert_dates(conn, game["steam_id"], game["last_update"], game["release_date"])

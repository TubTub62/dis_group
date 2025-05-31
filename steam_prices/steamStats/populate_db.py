from sql import *

### needs to get data from csv by some python script, pressumably.
### currently only functions with temp data (temp data taken from Christian)

games = [ # temp data
        {
            'steam_id': 252490,
            'name': 'Rust',
            'current_price': 39.99,
            'release_price': 18.99,
            'last_update': 'Dec 14 2013',
            'release_date': 'Sep 22 2021'
        },
        {
            'steam_id': 730,
            'name': 'Counter-Strike 2',
            'current_price': 0,
            'release_price': 7.34,
            'last_update': 'Nov 1 2012',
            'release_date': 'Dec 6 2018'
        },
        {
            'steam_id': 570,
            'name': 'Dota 2',
            'current_price': 0,
            'release_price': 0,
            'last_update': 'Jul 9 2013',
            'release_date': 'Jul 9 2013'
        },
        {
            'steam_id': 2622380,
            'name': 'ELDEN RING NIGHTREIGN',
            'current_price': 39.99,
            'release_price': 39.99,
            'last_update': 'Feb 12 2025',
            'release_date': 'Feb 12 2025'
        },
        {
            'steam_id': 553850,
            'name': 'HELLDIVERS™ 2',
            'current_price': 39.99,
            'release_price': 39.99,
            'last_update': 'Sep 22 2023',
            'release_date': 'Sep 22 2023'
        }
    ]


for game in games:
    conn = create_connection()


    insert_game(conn, game["name"], game["steam_id"])
    insert_update_release(conn, game["last_update"], game["release_date"])
    insert_prices(conn, game["current_price"], game["release_price"])

    insert_costs(conn, game["steam_id"], game["current_price"], game["release_price"])
    insert_dates(conn, game["steam_id"], game["last_update"], game["release_date"])

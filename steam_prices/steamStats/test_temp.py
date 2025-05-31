from sql import *

conn = create_connection()

all_games_query = query_game_all(conn)
print(all_games_query)

games = []
for game in all_games_query:
    
    game_name = game[0]
    game_id = game[1]

    cost_q = query_costs(conn, game_id)[0]
    dates_q = query_dates(conn, game_id)[0]

    print(cost_q)
    
    prices_pkeys = [cost_q[1], cost_q[2]]
    update_release_pkeys = [dates_q[1], dates_q[2]]

    prices_q = query_prices(conn, prices_pkeys[0], prices_pkeys[1])[0]
    update_release_q = query_update_release(conn, update_release_pkeys[0], update_release_pkeys[1])[0]

    print(prices_q)

    game_dict = {
        'steam_id': game_id,
        'name': game_name,
        'current_price': prices_q[0],
        'release_price': prices_q[1],
        'last_update': update_release_q[0],
        'release_date': update_release_q[1]
    }

    games.append(game_dict)
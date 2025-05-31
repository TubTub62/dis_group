from sql import *

conn = create_connection()

items = [
    query_game_all(conn),
    query_update_release_all(conn),
    query_prices_all(conn),

    query_costs_all(conn),
    query_dates_all(conn)

]

for item in items:
    print(f"{item}\n")
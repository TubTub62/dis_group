from sql import *

conn = create_connection()

game_id = create_id()

insert_game(conn, "test_game", game_id)

game_all = query_game_all(conn)

print(game_all)

delete_game_all(conn)

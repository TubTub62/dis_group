import psycopg2
import random

ip = "localhost"
password = "admin"

def create_connection(ip=ip, password=password):
    conn = psycopg2.connect(database="steam_db",
                            host=ip,
                            user="postgres",
                            password=password,
                            port="5432")
    conn.autocommit = True
    return conn

def create_id():
    return random.getrandbits(16)

# INSERTING DATA TO DB

def insert_game(conn, name, id):
    exc_statement = f"INSERT INTO steam_stats.game(name, id) VALUES('{name}', {id});"
    cursor = conn.cursor()
    cursor.execute(exc_statement)
    cursor.close()

def insert_update_release(conn, nd, od):
    exc_statement = f"INSERT INTO steam_stats.update_release(newest_date, oldest_date) VALUES({nd}, {od});"
    cursor = conn.cursor()
    cursor.execute(exc_statement)
    cursor.close()

def insert_prices(conn, np, op):
    exc_statement = f"INSERT INTO steam_stats.prices(newest_price, oldest_price) VALUES({np}, {op});"
    cursor = conn.cursor()
    cursor.execute(exc_statement)
    cursor.close()

def insert_dates(conn, id, nd, od):
    exc_statement = f"INSERT INTO steam_stats.dates(steam_game_id, newest_date, oldest_date) VALUES({id}, {nd}, {od});"
    cursor = conn.cursor()
    cursor.execute(exc_statement)
    cursor.close()

def insert_costs(conn, id, np, op):
    exc_statement = f"INSERT INTO steam_stats.costs(steam_game_id, newest_date, oldest_date) VALUES({id}, {np}, {op});"
    cursor = conn.cursor()
    cursor.execute(exc_statement)
    cursor.close()

# QUERYING DATA FROM DB

def query_game_all(conn):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM steam_stats.game;")
    q_res = cursor.fetchall()
    cursor.close()
    return q_res

def query_update_release_all(conn):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM steam_stats.update_release;")
    q_res = cursor.fetchall()
    cursor.close()
    return q_res

def query_prices_all(conn):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM steam_stats.prices;")
    q_res = cursor.fetchall()
    cursor.close()
    return q_res

def query_dates_all(conn):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM steam_stats.dates;")
    q_res = cursor.fetchall()
    cursor.close()
    return q_res

def query_costs_all(conn):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM steam_stats.costs;")
    q_res = cursor.fetchall()
    cursor.close()
    return q_res

# DELETING ENTRIES IN DB

def delete_game_all(conn):
    cursor = conn.cursor()
    exc = f"DELETE FROM steam_stats.game;"
    cursor.execute(exc)
    cursor.close()

def delete_update_release_all(conn):
    cursor = conn.cursor()
    exc = f"DELETE FROM steam_stats.update_release;"
    cursor.execute(exc)
    cursor.close()

def delete_prices_all(conn):
    cursor = conn.cursor()
    exc = f"DELETE FROM steam_stats.prices;"
    cursor.execute(exc)
    cursor.close()

def delete_dates_all(conn):
    cursor = conn.cursor()
    exc = f"DELETE FROM steam_stats.dates;"
    cursor.execute(exc)
    cursor.close()

def delete_costs_all(conn):
    cursor = conn.cursor()
    exc = f"DELETE FROM steam_stats.costs;"
    cursor.execute(exc)
    cursor.close()

if __name__ == "__main__":
    pass
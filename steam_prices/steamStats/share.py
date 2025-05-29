import psycopg2
import random

ip = "localhost"
#ip = "192.168.1.90"
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

def create_person(conn, name):
    exc_statement = f"INSERT INTO alarm_share.person(name) VALUES('{name}');"
    cursor = conn.cursor()
    cursor.execute(exc_statement)
    conn.close()

def share_alarm(conn, time, sender, recipient):
    alarm_id = create_id()
    exc_insert = f"INSERT INTO alarm_share.alarm(ID, stop_time, name_sender, name_recipient) VALUES({alarm_id}, '{time}', '{sender}', '{recipient}');"
    exc_notify = f"NOTIFY as_channel, '{recipient}';"
    cursor = conn.cursor()
    cursor.execute(exc_insert)
    cursor.execute(exc_notify)
    conn.close()

def query_person(conn, name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM alarm_share.person WHERE name = '{name}';")
    q_res = cursor.fetchall()
    conn.close()
    return q_res

def send_notification(conn, message):
    cursor = conn.cursor()
    exc = f"NOTIFY as_channel, '{message}';"
    cursor.execute(exc)
    conn.close()

def delete_share_alarm(conn, sender, recipient):
    cursor = conn.cursor()
    exc = f"DELETE FROM alarm_share.alarm WHERE name_sender = '{sender}' AND name_recipient = '{recipient}';"
    cursor.execute(exc)
    conn.close()

if __name__ == "__main__":
    pass
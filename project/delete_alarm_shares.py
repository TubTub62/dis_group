from share import create_connection

def delete_all():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM alarm_share.alarm;")
    cursor.execute("SELECT * FROM alarm_share.alarm;")

    q = cursor.fetchall()

    print(q)
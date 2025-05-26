from share import create_connection

if __name__ == "__main__":
    ip = ""
    conn = create_connection()
    conn.close()
    print("Succes")
from share import *

if __name__ == "__main__":

    for i in range(100):
        conn = create_connection()
        create_person(conn, f"testp{i}")
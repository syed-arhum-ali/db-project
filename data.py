import sqlite3
from sign_log_set_up import signup_user, log_in

def main():
    
    connection = sqlite3.connect("server.db")
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user(
            name TEXT, 
            email TEXT UNIQUE,
            password TEXT
        )
    """)
    
    connection.commit()
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            signup_user(connection,cursor)
        elif choice == "2":
            log_in(cursor)
        elif choice == "3":
            print("Goodbye!")
            connection.close()
            break
        else:
            print("Invalid choice, pick 1, 2, or 3.")
            
if __name__ == "__main__":
    main()


import sqlite3
from password import email_checker, pass_checker

def signup_user(connection,cursor):
    user_name_save = input("Enter your name: ")
    gmail_address = email_checker()
    user_pass = pass_checker()
    
    # connection = sqlite3.connect("server.db")
    # cursor = connection.cursor()
    
    sign_up_db = {
        "user_name" : user_name_save,
        "gmail_account" : gmail_address,
        "password" : user_pass
    }

    try:
        cursor.execute("""
            INSERT INTO user(name, email, password)
            VALUES(:user_name, :gmail_account, :password)
        """, sign_up_db)
        
        connection.commit()

        cursor.execute("SELECT name, email, password FROM user WHERE email = :gmail_account", sign_up_db)
        all_user = cursor.fetchall()
        for rows in all_user:
            print(f"Name: {rows[0]}, Email: {rows[1]}, Password: {rows[2]}")
        
        print("--- Sign up successful ---")
        
    except sqlite3.IntegrityError:
        print("This email is already registered. Please try a different email address.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    # finally:
        # connection.close()


def log_in(cursor):
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")
    
    # connection = sqlite3.connect("server.db")
    # cursor = connection.cursor()
    
    cursor.execute("select name from user where email = ? and password = ?",(email_input,password_input))
    
    user = cursor.fetchone()
    if user:
        print(f"\nWelcome back, {user[0]}! Login successful.")
    else:
        print("\nInvalid email or password. Please try again.")
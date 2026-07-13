import sqlite3

user_name_save = input("enter your name: ")
gmail_adresss = input("enter your email_addres: ")
user_pass = input("enter your password: ")
connection = sqlite3.connect("loggin.db")

cursor = connection.cursor()

cursor.execute("""
    create table if not exists user(
        name text, 
        email text unique,
        password text
    )
""")

sign_up_db = {
    "user_name" : user_name_save,
    "gmail_account" : gmail_adresss,
    "password" : user_pass
}
try:
    cursor.execute("""
        insert  into user(name, email, password)
        values(:user_name, :gmail_account, :password)
    """,sign_up_db)
    
    connection.commit()
    
    # cursor.
    # current_row_id = cursor.lastrowid
    # idk about th where thing i aied it \D
    cursor.execute("SELECT name, email, password FROM user", sign_up_db)
    
    all_user = cursor.fetchall()
    for rows in  all_user:
        print(f"Name: {rows[0]}, Email: {rows[1]}, Password: {rows[2]}")
    
    
    connection.close()
    print("---sign up successful---")
    
# error name is aied:
except sqlite3.IntegrityError:
    print("away ome with a new email another day")
except Exception as e:
    print(e)

import sqlite3
import random
import string

db = sqlite3.connect("D:\\! Bathspa\\1st Year - 2024-2025\\Intro to Programming\\Assessments\\Assessment 1\\classworks\\user_key\\user_data.db")

def insert(username,key):
    query = "insert into users(username,key) values(?,?);"
    db.execute(query,(username,key))
    db.commit()    

admin_password = "金龙闪耀在雅兹河的尽头，带来机遇"

user_id = input(f"Enter username: ")
query = "select username from users where username = ?;"
if db.execute(query,[user_id]).fetchone() is None:
    # make password
    length = random.randint(8,20)
    chr = string.ascii_letters + string.digits
    generated_key = ''.join(random.choices(chr,k=length))
    insert(user_id,generated_key)
    print(f"Successfully created user:\n{'-'*30}\nUsername: {user_id}\nKey: {generated_key}")

else:
    while True:
        try:
            choice = int(input("Username already exists in registry.\nEnter administration view?\n[1] - Yes\n[2] - No\n"))
            break
        except ValueError:
            print('Invalid input.')

    if choice == 1:
        enter_pw = input("Enter administrator password: ")
        if enter_pw == admin_password:
            result = db.execute("select key from users where username=?",[user_id])
            for x in result:
                displayed_key = x[0]
                print(f"Key for user {user_id} is: {displayed_key}")
        else:
            print('Invalid password. Closing program.')
    elif choice == 2:
        print("Closing program.")
    else:
        print("Invalid input. Closing program.")
from cryptography.fernet import Fernet

def load_key():
    file =  open("Beginner/Key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open("Key.key", "wb") as key_file:
        key_file.write(key)
        
write_key()
'''

def view():
    with open("Beginner/passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip() # rstrip removes the "\n" that is created in the add func
            user, passw = data.split("|") # split outputs an array
            print("User:", user, "Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open("Beginner/passwords.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
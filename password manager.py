from cryptography.fernet import Fernet  # type: ignore

def load_key():
    file= open("key.key", "rb") 
    key=file.read()
    file.close()
    return key

key=load_key()
master_pwd=input("What is the master password? ")

'''def write_key():
    key=Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''
        

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("|")
            print("User: ", user, "|Password: ", passw)


def add():
    name=input('Account Name: ')
    pwd=input("Passord: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode=input("Would you like to add a new passord or view existing ones (view, add), press q to quit? ").lower()

    if mode=="q":
        break

    if mode=="view":
        view()

    elif mode=="add":
        add()

    else:
        print("Invalid Mode.")
        continue
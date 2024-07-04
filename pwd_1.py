from cryptography.fernet import Fernet
'''def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
write_key()'''

def load_key():
    file=open('key.key',"rb")
    key=file.read()
    file.close()
    return key
master_password=input("what is the master password? ")
if(master_password=="hello"):
    key=load_key() + master_password.encode()
    fer=Fernet(key)
    def view():
        with open('passwords.txt','r') as f:
            for line in f.readlines():
                data=line.rstrip()
                user,password= data.split("|")
                print("User:",user,"| Password:",fer.decrypt(password.encode()).decode())

    def add():
        name=input("Account name:")
        pwd=input("Password:")
        print("Sucessfuly your creditials are saved !!")

        with open('passwords.txt','a') as f:
            f.write(name +"|"+ fer.encrypt(pwd.encode()).decode() + "\n")

    while True:
        mode=input("Would you like to add a new password or view existing ones (view,add)? press 'q' for exit ")
        if mode == "q":
            break
        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("invalid mode")
            continue
else:
    print(WindowsError("System is corrupted"))




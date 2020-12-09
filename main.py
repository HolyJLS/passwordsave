import string, random , os.path, time

def newPass():
    length = int(input("How long should the password be? "))
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = []
    for i in range(length):
        password.append(random.choice(password_chars))
    print(''.join(password))

def checkExistance():
    if os.path.exists('passwords.txt'):
        pass
    else:
        file = open('passwords.txt', 'w')
        file.close()

def appendNew():
    file = open('passwords.txt', 'a')
    print()
    print()

    userName = input('Please add the username: ')
    password = input('Please enter password here: ')
    website = input('Please enter the website URL here:')

    print()
    print()

    usrnm = "Username: " + userName + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("--------------------------------------")
    file.write("\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("--------------------------------------\n")
    file.write("\n")
    file.close()


def readPasswords():
    file = open('passwords.txt', 'r')
    content = file.read()
    file.close()
    print(content)

def authUser():
    password = 123456
    chances = 0
    while chances < 3:
        userPin = input('ENTER THE CORRECT PIN: ')
        while not userPin.isdigit() or len(userPin) != 6:
            print('ENTER A SIX DIGIT NUMBER')
            userPin = input('ENTER THE CORRECT PIN: ')
        userPin = int(userPin)
        if userPin == password:
            print("Login Successful")
            readPasswords()
            break
        chances += 1
    else:
        print('TOO MANY ATTEMPTS. TRY AGAIN IN 10 SECONDS')
        seconds = 10
        time.sleep(seconds)
        if input("ENTER THE CORRECT PIN: ") == password:
            print('Login Successful')
            readPasswords()
        else:
            print("GoodBye")

def mainMenu():
    print('What do you want to do today?')
    print('-----------------------------')
    print('1) Make new Password')
    print('2) Save new password')
    print('3) Password Manager')
    print('-----------------------------')
    user = int(input("Type number here: "))
    if user == 1:
        os.system('cls')
        newPass()
    elif user == 2:
        os.system('cls')
        appendNew()
    elif user == 3:
        os.system('cls')
        authUser()
    else:
        print('Invalid Input')

mainMenu()
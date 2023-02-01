# Написати програми для реєстрації і авторизації користувача з наступним функціоналом:
# отримання в інтерактивному режимі логіну і пароля користувача;
# верифікація пароля і його шифрування за алгоритмом обраним алгоритмом шифрування;
# запис пари "логін-пароль" у словник з перевіркою на колізії;
# авторизація користувача за логіном і паролем.

import hashlib

wish = input("If you want to register, press R. If you want to login, press L: ")

def write_to_file(file_name : str, dictionary):
    with open(file_name, 'w') as f:
        for k, v in dictionary.items():
           f.write(f'{k} {v}\n')
    f.close()

def registration():
    while True:
        login = input('Enter your login: ')
        if login in hash_pass_table:
            print('Login alredy used. Try again.')
        else:
            while True:
                pass1 = input('Enter your password: ')
                pass2 = input('Confirm your password: ')
                if pass2 == pass1:
                    pass_hash = hashlib.md5(pass2.encode())
                    hash_pass_table[login] = pass_hash.hexdigest()
                    print("Registration is successful")
                    write_to_file('passwords.txt', hash_pass_table)
                    break
                else:
                    print('Passwords do not match. Try again.')
            break

def read_from_file(file_name : str):
    my_dict = {}
    with open(file_name, mode='r', encoding='utf-8') as f:
       for line in f:
           ls = line.split()
           my_dict[ls[0]] = ls[1]

    return my_dict

def login():
    while True:
        login = input("Enter your login: ")
        if login in hash_pass_table:
            count = 0
            while True and count < 3:
                count += 1
                password = input("Enter your password: ")
                pass_hash = hashlib.md5(password.encode())
                if hash_pass_table[login] != pass_hash.hexdigest():
                    if count != 3:
                        print(f"Unknown password. Try again. {3 - count} attempts left.")
                    else:
                        print("Incorrect password. Access denied. ")
                else:
                    print("Access is allowed.")
                    break
            break

        else:
            print("Unknown login.")
            choice = input("(T)ry again or (R)egister new account or press any key to exit.")
            if choice.lower() == 'r':
                registration()
                break
            elif choice.lower() == 't':
                continue
            else:
                print("Unknown input.")
            break

hash_pass_table = read_from_file('passwords.txt')

if wish == "R":
    print(wish)
    registration()
elif wish == "L":
    login()
else:
    print("You enter incorrect symbol.")


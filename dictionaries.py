import os
import json
from pathlib import Path

path = Path("phones.json")

if path.exists():
    with open("phones.json", "r") as f:
        user_name = json.load(f)
else:
    user_name = {}

def add_user():
    name = input("Input name: ")
    if name in user_name:
        print("----------the name is already here!----------")
        return
    user_name[name] = input("Input phone number")

def show_contacts():
    print("-------------WHOLE LIST--------------")
    for keys in user_name.keys():
        print(f'--------------------------------------\n'
              f'name: {keys}, phone number: {user_name[keys]}\n'
              f'--------------------------------------\n')

def user_interface():
    print("choose an option:\n"
          "add a contact: add\n"
          "show list: show\n")

    command = input("input your cmd:")

    if "show" in command.lower():
        show_contacts()
    elif "add" in command.lower():
        add_user()
    else:
        print("---------invalid cmd---------")



while True:
    user_interface()
    finish = input("Continue? Y/N: ")

    while finish.lower() not in ['y','n']:
        print("-----Invalid cmd!-------\n")
        finish = input("Continue? Y/N: ")

    if "n" in finish.lower():
        print("-----Goodbye-------\n")
        f = open("phones.json", "w")
        json.dump(user_name, f)
        f.close()
        break
    else:
        continue










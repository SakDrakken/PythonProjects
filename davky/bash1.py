import datetime
import os


def batch1():
    print("Davka 1:")
    now = datetime.datetime.now()
    print("Dnesni datum a cas: " + now.strftime("%d-%m-%Y %H:%M"))

#  prikazy pro linux
    if os.name == "posix":
        print("Informace o uzivateli: ")
        os.system("id")
        print("Informace o systemu: ")
        print os.uname()
        print("Informace o hardware: ")
        os.system("lshv")
        print("Systemove cesty: ")
        print os.path
        print("Systemove promenne: ")
        print os.system("set")

#  prikazy pro windows
    if os.name == "nt":
        print("Informace o uzivateli: ")
        os.system("whoami -all")
        print("Informace o uzivateli: ")
        os.system("systeminfo")
        print("Systemove cesty: ")
        print os.path
        print("Systemove promenne: ")
        os.system("set")


if __name__ == "__main__":
    batch1()

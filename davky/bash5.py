import os


def batch5():
    if os.name == "posix":
        f = open("input5.txt")

        for lines in f:
            a = lines.split(",")
            print a[0] + " " + a[1]
            os.system("sudo groupadd " + a[1])
            os.system("sudo useradd -m -d /home/" + a[0] + " -e 2019-12-31 -f 45 -g " + a[1] + a[0])
            os.system(a[0] + ":" + a[0] + " | chpasswd")
    if os.name == "nt":
        f = open("input5.txt")

        for lines in f:
            a = lines.split(",")
            os.system("net user " + a[0] + " /add")
            os.system("net localgroup " + a[1] + " /add")
            os.system("localgroup " + a[1] + " " + a[0] + "/add")


if __name__ == "__main__":
    batch5()

import os


def batch4():
    if os.name == "posix":
        os.system("cat " + "conoutput4.txt")
        os.system("sudo" + "apt-get" + "install" + "whois")
        response = os.system("ping " + "-c " + "4 " + "google.com")
        if response == 0:
            print "Connectivity OK!"
        else:
            print "Connectivity NOK!"
        adresa = input("Enter server address:")
        os.system("sudo " + "apt-get " + "install " + "whois")
        os.system("traceroute " + adresa)
        print(".....")
        os.system("whois " + adresa)
        print(".....")
        os.system("nslookup " + adresa)
    if os.name == "nt":
        print "Testuji konektivitu..."
        response = os.system("ping " + "google.com")
        if response == 0:
            print "Connectivity OK!"
        else:
            print "Connectivity NOK!"
        adresa = input("Enter server address:")
        os.system("tracert " + adresa)
        response = os.system("whois " + adresa)
        if response == -1:
            print("Je potreba nainstalovat whois.")
        os.system("nslookup " + adresa)


if __name__ == "__main__":
    batch4()

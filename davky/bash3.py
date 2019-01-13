import os


def batch3():
    if os.name == "posix":
        print "Spoustim vypisovani korenoveho adresare pro Linux:"
        os.system("sudo" + "mkdir" + "/SCRIPT")
        os.system("sudo" + "chmod" + "777" + "/SCRIPT")
        os.system("sudo" + "mkdir" + "/SCRIPT/$user")
        os.system("sudo" + "apt-get" + "install" + "tree")
        os.system("cd /SCRIPT/$user")
        os.system("tree" + "/" + ">>tree.txt")
        os.system("ls" + "/" + "boot" + "-all" + ">>hidden.txt")

    if os.name == "nt":
        print "Spoustim vypisovani korenoveho adresare:"
        os.system.__call__("batch3.bat")


if __name__ == "__main__":
    batch3()

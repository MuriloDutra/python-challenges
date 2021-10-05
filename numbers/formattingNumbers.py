#Documentation: https://docs.python.org/3/library/string.html#formatexamples

def format():
    print("Tentativa {} de {}".format(1, 3))
    print("Tentativa {1} de {0}".format(1, 3))
    print("R$ {}".format(1.59))
    print("R$ {:f}".format(1.59))
    print("R$ {:.2f}".format(1.59))
    print("R$ {:.2f}".format(1.5))
    print("R$ {:.2f}".format(1234.50))
    print("R$ {:7.2f}".format(1.5))
    print("R$ {:07.2f}".format(1.5))
    print("R$ {:07d}".format(4))
    print("Data {:02d}/{:02d}".format(9, 4))
    print("Data {:02d}/{:02d}".format(19, 11))
    print("R$ {:7.1f}".format(1000.16))#Round a number

if(__name__ == "__main__"):#It enables to execute the file from the command line
    format()

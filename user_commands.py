import riven_relisting
import utils



def ask_for_email():
    """Asks the user for its wfm email"""

    while True:
        try:
            email = str(input("Introduce the email associated to your warframe.market account: "))
        except ValueError:
            print("An error happened when reading your email, please try again. \n")
        if email:
            return email


def ask_for_pass():
    """Asks the user for its wfm password"""

    while True:
        try:
            password = str(input("Introduce your password: "))
        except ValueError:
            print("An error happened when reading your password, please try again. \n")
        if password:
            return password


def ask_for_name():
    """Asks the user for its wfm username"""

    while True:
        try:
            name = str(input("Introduce your profile name: "))
        except ValueError:
            print("An error happened when reading your profile name, please try again. \n")
        if name:
            return name


def relist_auctions():
    """Asks the user about its options for relisting"""

    while True:
        print("Do you want to relist all your auctions or only the ones without bids?:\n")
        print("1. All the auctions\n")
        print("2. Only the ones without bid\n")
        try:
            bids = int(input("Introduce a number: "))
        except ValueError:
            print("Write a number between 1 and 2. \n")
        if 0 < bids < 3:
            break

    relist_type = bids == 2
    print("Introduce your warframe.market login credentials:\n")
    email = ask_for_email()
    password = ask_for_pass()
    utils.login(email, password)
    riven_relisting.relist_auctions(relist_type)


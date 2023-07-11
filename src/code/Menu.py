import DonateBlood as don
import TakeBlood as take
import bloodInfo
from colorama import Fore
import normal


class Menus:
    def __init__(self):
        pass

    def menu(self):
        print(Fore.CYAN)
        normal.printBrand("Blood Bank Management System")
        print()
        print()
        print("1.Show Blood Reserves")
        print("2.Donate Blood")
        print("3.Take Blood")
        print("4.Admin Login")
        print("5.About Me")
        print("6.Quit")

    def displayData(self, records):
        print(Fore.YELLOW)
        print("--------------------------------")
        print("BLOOD TYPE  || PACKETS REMAINING")
        print("--------------------------------")

        for record in records:
            if record[0] != "AB+" and record[0] != "AB-":
                print(f"{record[0]}          || {record[1]}")
            else:
                print(f"{record[0]}         || {record[1]}")
        print("--------------------------------")


obj = Menus()

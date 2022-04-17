import DonateBlood as don
import TakeBlood as take
import bloodInfo


class Menus:

    def __init__(self):
        pass

    def menu(self):
        print("------------------------------------------")
        print("-----------Blood Bank Management----------")
        print("------------------------------------------")

        print("1.Show Data of All Available Blood.")
        print("2.Donate Blood")
        print("3.Take Blood")
        print("4.Admin Login")
        print("5.Quit")

    def displayData(self, records):
        print("--------------------------------")
        print("BLOOD TYPE  || PACKETS REMAINING")
        print("--------------------------------")

        for record in records:
            if record[0] != 'AB+' and record[0] != 'AB-':
                print(f"{record[0]}          || {record[1]}")
            else:
                print(f"{record[0]}         || {record[1]}")
        print("--------------------------------")


obj = Menus()

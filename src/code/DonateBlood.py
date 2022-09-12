import transact
import bloodInfo
from colorama import Fore
import normal

class DonateBlood:
    def accept(self):
        normal.printBrand("Donate Blood", Fore.YELLOW, '-')
        print(Fore.YELLOW)
        name = input("Enter your name :")
        email = input("Enter Email :")
        bloodG = input("Enter Blood Group :")
        try:
            bag = int(input("How much bag filled :"))
        except ValueError:
            print(Fore.RED)
            print("Enter Number..!!")
        donTran = transact.Transaction()
        donTran.addDonatedBlood(name, email, bloodG, bag)
        blood = bloodInfo.BloodInfo()
        blood.addBlood()

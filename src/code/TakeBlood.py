import transact
import bloodInfo
from colorama import Fore
import normal
class TakeBlood:
    def accept(self):
        normal.printBrand("Take Blood", Fore.YELLOW, '-')
        print(Fore.YELLOW)
        name = input("Enter your name :")
        email = input("Enter Email :")
        bloodG = input("Enter Blood Group :")
        try:
            bag = int(input("How much bag needed :"))
        except ValueError:
            print(Fore.RED)
            print("Enter Number..!!")
        donTran = transact.Transaction()
        donTran.addRecBlood(name, email, bloodG, bag)
        blood = bloodInfo.BloodInfo()
        blood.removeBlood()

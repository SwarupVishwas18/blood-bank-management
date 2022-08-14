import transact
import bloodInfo
from colorama import Fore

class TakeBlood:
    def accept(self):
        print(Fore.CYAN)
        name = input("Enter your name :")
        email = input("Enter Email :")
        bloodG = input("Enter Blood Group :")
        bag = int(input("How much bag needed :"))
        donTran = transact.Transaction()
        donTran.addRecBlood(name, email, bloodG, bag)
        blood = bloodInfo.BloodInfo()
        blood.removeBlood()

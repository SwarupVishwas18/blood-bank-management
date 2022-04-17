import transact
import bloodInfo


class TakeBlood:
    def accept(self):
        name = input("Enter your name :")
        email = input("Enter Email :")
        bloodG = input("Enter Blood Group :")
        bag = int(input("How much bag needed :"))
        donTran = transact.Transaction()
        donTran.addRecBlood(name, email, bloodG, bag)
        blood = bloodInfo.BloodInfo()
        blood.removeBlood()

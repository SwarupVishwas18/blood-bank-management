import transact
import bloodInfo


class DonateBlood:
    def accept(self):
        name = input("Enter your name :")
        email = input("Enter Email :")
        bloodG = input("Enter Blood Group :")
        bag = int(input("How much bag filled :"))
        donTran = transact.Transaction()
        donTran.addDonatedBlood(name, email, bloodG, bag)
        blood = bloodInfo.BloodInfo()
        blood.addBlood()

import Menu
import DonateBlood as don
import TakeBlood as take
import bloodInfo
import adminPanel
from colorama import Fore
import normal

def main():
    while True:
        print(Fore.CYAN)
        menu = Menu.Menus()
        menu.menu()
        tk = input("Enter your choice : ")
        if(tk == "1"):
            bl = bloodInfo.BloodInfo()
            records = bl.getAllBloodData()
            menu.displayData(records)
        elif(tk == "2"):
            d = don.DonateBlood()
            d.accept()
        elif (tk == "3"):
            t = take.TakeBlood()
            t.accept()
        elif (tk == "4"):
            adminPanel.login()
        elif (tk == "5"):
            normal.aboutMe()
        elif (tk == "6"):
            normal.quitMe()
            break
        else:
            print(Fore.RED)
            print("Wrong Choice")


try:
    main()
except KeyboardInterrupt:
    normal.quitMe()
except Exception as e:
    normal.logToFile(repr(e))
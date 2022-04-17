import Menu
import DonateBlood as don
import TakeBlood as take
import bloodInfo
import adminPanel


while True:
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
        print("Thank You for using our software")
        break
    else:
        print("Wrong Choice")

import bloodInfo
import transact


def login():
    pwd = input("Enter the password : ")
    if pwd == 'heatwavesHBP':
        panel()
    else:
        print("Incorrect Password..!!")


def displayPanel():
    print("------------------------------------------")
    print("---------------ADMIN PANEL----------------")
    print("------------------------------------------")

    print("1.Show All Transactions")
    print("2.Clear All Transactions")
    print("3.Quit")


def panel():
    while True:
        displayPanel()
        inp = input("Enter the choice : ")
        tran = transact.Transaction()
        blood = bloodInfo.BloodInfo()
        if inp == '1':
            tran.displayAllRecs()
        elif inp == '2':
            tran.deleteAll()
            blood.resetData('A+')
            blood.resetData('B+')
            blood.resetData('AB+')
            blood.resetData('O+')
            blood.resetData('A-')
            blood.resetData('B-')
            blood.resetData('AB-')
            blood.resetData('O-')
        elif inp == '3':
            print("Logging You Out")
            break

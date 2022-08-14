import sqlite3 as sql
from colorama import Fore

class Transaction:
    def __init__(self):
        self.conn = sql.connect('trans.db')
        self.c = self.conn.cursor()

    def addDonatedBlood(self, *data):

        q = f"INSERT INTO trans VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', 'donation', 'success')"
        self.c.execute(q)
        self.conn.commit()

    def deleteAll(self):
        q = "DELETE FROM trans"
        self.c.execute(q)
        self.conn.commit()

    def addRecBlood(self, *data):
        q = f"INSERT INTO trans VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', 'recieve', 'failure')"
        self.c.execute(q)
        self.conn.commit()

    def getBloodRecord(self):
        q = f"SELECT * FROM trans"
        self.c.execute(q)
        res = self.c.fetchall()
        # print(res)
        data = res[-1]
        return data[2], data[3], data[0], data[1]

    def displayAllRecs(self):
        q = f"SELECT * FROM trans"
        self.c.execute(q)
        res = self.c.fetchall()
        print(Fore.YELLOW)
        print("Transaction Found : ", len(res))
        count = 1
        for data in res:
            if data[5] == 'failure':
                print(Fore.RED)
            else:
                print(Fore.GREEN)
            print("--------------------------------------------")
            print("Transaction No ", count)
            print("Name : ", data[0])
            print("Email : ", data[1])
            print("Blood Group : ", data[2])
            print("Packets : ", data[3])
            print("Type of Transaction : ", data[4])
            print("Status of Transaction : ", data[5])
            print("--------------------------------------------")
            print()
            count += 1

    def updateStatus(self):
        data = self.getBloodRecord()
        q = f"UPDATE trans SET status = 'success' WHERE name = '{data[0]}' and email = '{data[1]}'"
        print("Blood Donated Successfully..!!")

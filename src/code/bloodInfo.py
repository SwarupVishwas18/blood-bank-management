import sqlite3 as sql
import transact


class BloodInfo:
    def __init__(self):
        self.conn = sql.connect('blood.db')
        self.c = self.conn.cursor()

    def addBlood(self):
        t = transact.Transaction()
        blood = t.getBloodRecord()
        availpck = self.getAvailablePckt(blood[0]) + blood[1]
        q = f"UPDATE blood SET availablePackets = '{availpck}' WHERE bloodType = '{blood[0]}'"
        self.c.execute(q)
        self.conn.commit()
        print("Blood Donated Successfully..!!")

    def removeBlood(self):
        t = transact.Transaction()
        blood = t.getBloodRecord()
        availpck = self.getAvailablePckt(blood[0])
        if availpck > 0:
            currpck = availpck - blood[1]
            q = f"UPDATE blood SET availablePackets = '{currpck}' WHERE bloodType = '{blood[0]}'"
            self.c.execute(q)
            self.conn.commit()
            print("Blood Given Successfully..!!")
        else:
            print("ERROR!!")
            print("Sorry but no packets available of given blood group")

    def getAvailablePckt(self, bType):
        q = f"SELECT * FROM blood WHERE bloodType = '{bType}'"
        self.c.execute(q)
        res = self.c.fetchone()
        return res[1]

    def getAllBloodData(self):
        q = f"SELECT * FROM blood"
        self.c.execute(q)
        res = self.c.fetchall()
        return res

    def resetData(self, type):
        q = f"UPDATE blood SET availablePackets = '0' WHERE bloodType = '{type}'"
        self.c.execute(q)
        self.conn.commit()

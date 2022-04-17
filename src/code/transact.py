import sqlite3 as sql


class Transaction:
    def __init__(self):
        self.conn = sql.connect('trans.db')
        self.c = self.conn.cursor()

    def addDonatedBlood(self, *data):

        q = f"INSERT INTO trans VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', 'donation')"
        self.c.execute(q)
        self.conn.commit()

    def deleteAll(self):
        q = "DELETE FROM trans"
        self.c.execute(q)
        self.conn.commit()

    def addRecBlood(self, *data):
        q = f"INSERT INTO trans VALUES ('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', 'recieve')"
        self.c.execute(q)
        self.conn.commit()

    def getBloodRecord(self):
        q = f"SELECT * FROM trans"
        self.c.execute(q)
        res = self.c.fetchall()
        # print(res)
        data = res[-1]
        return data[2], data[3]

    def displayAllRecs(self):
        q = f"SELECT * FROM trans"
        self.c.execute(q)
        res = self.c.fetchall()
        print("Transaction Found : ", len(res))
        count = 1
        for data in res:
            print("--------------------------------------------")
            print("Transaction No ", count)
            print("Name : ", data[0])
            print("Email : ", data[1])
            print("Blood Group : ", data[2])
            print("Packets : ", data[3])
            print("Type of Transaction : ", data[4])
            count += 1

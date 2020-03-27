class Students:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1 * other.m1
        m2 = self.m2 * other.m2
        ad = Students(m1, m2)
        return ad
    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        ad = Students(s1, s2)
        if ad.m1 > ad.m2:
            return True
        else:
            return False
    def __str__(self):
        return self.m1, self.m2


import sqlite3
conn = sqlite3.connect("python.db")
c = conn.cursor()

def CreateTable():
    c.execute("CREATE TABLE IF NOT EXISTS Students (Name TEXT, Email TEXT, Number NUMBER)")

def Insert(n):
    c.execute("INSERT INTO Students VALUES (?, ?, ?)", ('Python', 'python@gmail.com', n))
    conn.commit()


def ReadData():
    c.execute("SELECT * FROM Students WHERE Number = 6629449030")
    data = c.fetchall()
    for i in data:
        print(i)

ReadData()




















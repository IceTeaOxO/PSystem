import sqlite3



def SQLinit():
    conn = sqlite3.connect('./DB/test.db')
    print ("数据库打开成功")
    c = conn.cursor()
    c.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);''')
    print ("数据表创建成功")
    conn.commit()
    conn.close()
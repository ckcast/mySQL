import pymysql
import sys

db = pymysql.connect("localhost","testuser","test123","TESTDB" )

cursor = db.cursor()


if len(sys.argv) >= 2:
    if sys.argv[1] == "insert" or sys.argv[1] == "delete" or sys.argv[1] == "update" \
            or sys.argv[1] == "list" or sys.argv[1] == "reset" or sys.argv[1] == "autoset":
        print("")

    else:
        print("請檢查輸入內容是否正確")


if len(sys.argv) == 2:
    sql_Action = sys.argv[1]

    if sys.argv[1] == "reset":
        cursor.execute("DROP TABLE IF EXISTS Employee")

        sql_createTb = """CREATE TABLE Employee (
                         ID INT NOT NULL AUTO_INCREMENT,
                         NAME CHAR(20),
                         AGE INT,
                         SEX CHAR(1),
                         PRIMARY KEY(ID))
                         """
        sql_Default_Insert = "INSERT INTO Employee(NAME,AGE,SEX) VALUES('Coco',18,'F')"

        cursor.execute(sql_createTb)
        cursor.execute(sql_Default_Insert)

    elif sys.argv[1] == "list":


        sql_list = "SELECT * FROM Employee ORDER BY NAME, AGE, SEX"
        cursor.execute(sql_list)
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()

        print()
        print()




        sql_show = "SHOW COLUMNS FROM Employee"
        cursor.execute(sql_show)
        row = cursor.fetchone()
        while row is not None:
            print(str(row[0]) + "\t", end="")
            row = cursor.fetchone()
        print()

        sql_list = "SELECT * FROM Employee ORDER BY NAME, AGE, SEX"
        cursor.execute(sql_list)
        row = cursor.fetchone()
        while row is not None:
            for i in row:
                print(str(i) + "\t", end="")
            print()
            row = cursor.fetchone()

        print()


    elif sys.argv[1] == "autoset":
        sql_AutoID1 = "ALTER TABLE Employee DROP COLUMN `ID`"
        sql_AutoID2 = "ALTER TABLE Employee ADD `ID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST"
        cursor.execute(sql_AutoID1)
        cursor.execute(sql_AutoID2)



elif len(sys.argv) == 3:
    sql_Action = sys.argv[1]
    sql_Name = sys.argv[2]
    if sys.argv[1] == "delete":
        sql_Delete = "DELETE FROM Employee WHERE NAME = '%s'" % (sql_Name)
        cursor.execute(sql_Delete)


elif len(sys.argv) == 5:
    sql_Action = sys.argv[1]
    sql_Name = sys.argv[2]
    sql_Age = sys.argv[3]
    sql_Sex = sys.argv[4]

    if sys.argv[1] == "insert":
        sql_Insert = "INSERT INTO Employee(NAME,AGE,SEX) VALUES('%s',%s,'%s')" % (sql_Name,sql_Age,sql_Sex)
        cursor.execute(sql_Insert)

    if sys.argv[1] == "delete":
        sql_Delete = "DELETE FROM Employee WHERE NAME = '%s' AND AGE = %s AND SEX = '%s'" % (sql_Name,sql_Age,sql_Sex)
        cursor.execute(sql_Delete)

    if sys.argv[1] == "update":
        sql_Update = "UPDATE Employee SET AGE = %s,SEX = '%s' WHERE NAME = '%s' " % (sql_Age,sql_Sex,sql_Name)
        cursor.execute(sql_Update)


db.commit()
db.close()
cursor.close()
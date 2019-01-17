import pymysql
import sys

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='my_python',
)
bank = 1
while bank :
    print('\tBank Account')
    print('Press [1] if you want CREATE ACCOUNT\n')
    print('Press [2] if you want READ ACCOUNT\n')
    print('Press [3] if you want UPDATE ACCOUNT\n')
    print('Press [4] if you want DELETE ACCOUNT\n')
    print('press [5] if you want EXIT ACCOUNT\n')
    bank=input("Please Enter your number choice:")
    if bank == "1":
        firstname=input("Enter your first name:")
        lastname=input("Enter your last name:")
        account_code=input("Enter your acount code:")
        balance=input("Enter your balance:")
        
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO money_bank (`firstname`,`lastname`,`account_code`,`balance`) VALUES (%s,%s, %s, %s)"
                try:
                    cursor.execute(sql, (firstname, lastname, account_code ,balance))
                    print("Task added successfully")
                except:
                    print("Oops! Something wrong")
                    
            connection.commit()
        finally:
            print ("\n")

    elif bank == "2":
          print ("bank account\n")
          try:
              with connection.cursor() as cursor:
                  sql = "select * from money_bank"
                  cursor.execute(sql)
                  connection.commit()
                  results = cursor.fetchall()
                  print("---------------------------------------------------------------------------------------")
                  print("id\tfirstname\t\tlastname\t\taccount_code\t\tbalance")
                  print("---------------------------------------------------------------------------------------")
                  for row in results :
                      print(str(row[0]) + "\t" + row[1] + "\t\t\t" + (row[2]) + "\t\t\t" , row[3]+"\t\t\t"+row[4])
                      connection.commit()

          finally:
                            print ("")
                            
    elif bank == "3":
        print("")
        id = input("Enter the id you want to edit: ")
        firstname = input("Enter your  new first name: ")
        lastname = input("Enter your new last name: ")
        account_code = input("Enter your new code: ")
        balance = input("Enter your new balance:")
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE money_bank SET `firstname`=%s,`lastname`=%s, `account_code`=%s, `balance`=%s WHERE `id` =%s"
                try:
                    cursor.execute(sql, (firstname,lastname, account_code, balance, id))
                    print("Successfully Updated...")
                except:
                    print("Oops! Something wrong")
     
            connection.commit()
        finally:
            print ("")

    elif bank == "4":
        print("")
        id = input("Enter the id that you want to delete: ")
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM money_bank WHERE id = %s"
                try:
                    cursor.execute(sql, (id))
                    print("Successfully Deleted...")
                except:
                    print("Oops! Something wrong")
     
            connection.commit()
        finally:
            print ("")
    elif bank == "5":
        sys.exit(0)

    elif bank=="6":
        print("1-5 ra ang choices!\n")
    elif bank=="7":
        print("1-5 ra ang choices!\n")
    elif bank=="8":
        print("1-5 ra ang choices!\n")
    elif bank=="9":
        print("1-5 ra ang choices!\n")
    elif bank=="10":
        print("1-5 ra ang choices!\n")



    else:
        print("\nInvalid Input number ra ba ang ibutang!\n")
        bank=1
        
    
 
            
    
         

          
        

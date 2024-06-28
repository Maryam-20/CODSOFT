# TASK 5 CONTACT BOOK
import time
import mysql.connector as sql
import datetime as dt
myCon = sql.connect(host = 'Localhost', user = 'root', password = "", database = "contactBook_db")
myCursor = myCon.cursor()
# myCursor.execute("SHOW DATABASES")

# for db in myCursor:
#     print(db)

# myCursor.execute("CREATE DATABASE contactBook_db")
# myCursor.execute("CREATE TABLE ContactDetails(contact_ID INT(4) PRIMARY KEY AUTO_INCREMENT, FULL_NAME VARCHAR(50), EMAIL VARCHAR(40), PHONE_NUMBER VARCHAR(11), ADDRESS VARCHAR(200), BIRTDAY VARCHAR(20))")
# myCursor.execute("ALTER TABLE ContactDetails ADD UNIQUE(EMAIL)")
# myCursor.execute("ALTER TABLE ContactDetails ADD UNIQUE(PHONE_NUMBER)")

def homepage():
    user_input = input("What Operation Would you like to perform? \n \
        AD -- Add Contact \n \
        VW -- View Contact \n \
        UP -- Update Contact \n \
        DC -- Delete Contact \n")
    if user_input.upper() == "AD":
        addContact()
    elif user_input.upper() == "VW":
        viewContact()
    elif user_input.upper() == "UP":
        updateContact()
    elif user_input.upper() == "DC":
        delContact()
    else:
        print("INVALID OPERATION")
         
  
def addContact():
    try:
        full_name = input("Enter the full name:  ")
        email = input("Enter email:  ")
        phone_no = input("Enter Phone Number: ")
        address = input("Enter Adress: ")
        DOB = input("enter DOB in this format yyyy-mm-dd:  ")
        dob_str = dt.datetime.strptime(DOB, "%Y-%m-%d") 
        
        myQuery = "INSERT INTO ContactDetails( FULL_NAME, EMAIL, PHONE_NUMBER, ADDRESS, BIRTDAY) VALUES (%s, %s, %s, %s, %s)"
        myVal = (full_name, email, phone_no, address, dob_str)
        myCursor.execute(myQuery, myVal)
        myCon.commit()
        
        print("Contact succesffully added")  #Coming back for the Validation of each input statement
    except:
        print("Input correctly in all fields")
        
        
def viewContact():
    user_input = input("Do you want to view all contact or the details of a single person? \n \
        A -- All Contact \n \
        S -- Single person contact\n \
             Input Here:  ")
    
    if user_input.upper() == "A":
        query = "SELECT * FROM ContactDetails"
        myCursor.execute(query)
        allContact = myCursor.fetchall()
        for details in allContact:
            print(details)
    elif user_input.upper() == "S":
        query = "SELECT * FROM ContactDetails WHERE PHONE_NUMBER=%s"
        val = input("Input the person Phone number:  ")
        myCursor.execute(query, (val, ))
        output = myCursor.fetchone()
        print(output)
    
    
def updateContact():
    name = input("Which person contact do you want to update? : \n ")
    time.sleep(2)
    full_name = input("Enter the new full name:  ")
    email = input("Enter the new email:  ")
    phone_no = input("Enter the new Phone Number: ")
    
    query = "UPDATE ContactDetails SET PHONE_NUMBER = %s, FULL_NAME = %s, EMAIL = %s WHERE FULL_NAME = %s"
    val = (phone_no, full_name, email, name)
    myCursor.execute(query, val)
    myCon.commit()
    print("Contact updated Successfully")
    
    
def delContact():
    query = "DELETE FROM ContactDetails WHERE FULL_NAME = %s"
    name= input("Enter the name of the person contact to be deleted: \n")
    val = (name, )
    myCursor.execute(query, val)
    myCon.commit()
    print(name, "contact deleted successfully")

homepage()
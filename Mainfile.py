# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:58:34 2016

@author: Blake
"""


# Import database plugin
import sqlite3

# Function Definitions

# Simple UI function to ask what the user wants to do

def Intro ():
    x = 1
    
    while (x == 1):
        print("\n What would you like to do?\n")
        print("1. Retrieve Data\n")
        print("2. Enter Data\n")
        print("3. Exit\n")
    
        task = int(input("Please type a number\n"))
        
        if task > 3 or task < 1:
            print("The option you have selected is out of range, Please choose again")
        else:
           x = 0
    
        print (task)
        return task
    
def RetData ():
    x = 1
    
    while (x == 1):
        print("\n From which table would you like to retrieve data from?\n")
        print("1. Parking Fines\n")
        print("2. User Info\n")
    
        table = int(input("Please type a number\n"))
        
        if table > 2 or table < 1:
            print("The option you have selected is out of range, Please choose again")
        else:
           x = 0
    
        print (table)
        
        if table == 1:
            cursor.execute("SELECT * FROM 'Parking Fines'")
            rows = cursor.fetchall()
            print("Fine Number, Date, Time, Application/Permit Number, Vehicle Registration Number, Vehicle Type, Details of Offence, Location of Offence\n")
            for row in rows:
                print(row)
        
        if table ==2:
            cursor.execute("SELECT * FROM 'User Info'")
            rows = cursor.fetchall()
            print("Application / Permit Number, Staff or Student ID, Title, First Name, Last Name, Date of Birth, Home Phone, Work Phone, Mobile Phone, Email Address, Department / Faculty, Are you applying as a visitor?, Visitor First Name, Visitor Last Name, Reason for Visit, Vehicle Type, Vehicle Registration Number, Vehicle Make and Model\n")
            for row in rows:
                print(row)
        

def EntData ():
    x = 1
    
    while (x == 1):
        #print("\n What table would you like to input data to?\n")
        #print("1. Parking Fines\n")
        #print("2. User Info\n")
    
        #table = int(input("Please type a number\n"))
        
        #if table > 2 or table < 1:
        #    print("The option you have selected is out of range, Please choose again")
        #else:
        #   x = 0
        
        data = input("Please type your entry data in full SQL format\n")
        cursor.execute(data)
        
        table = 1
    
        print (table)
        return table

# Create database
db = sqlite3.connect('example.db')

# Create a cursor to interact with database objects
cursor = db.cursor()



# Create the 'Parking Fines' table
cursor.executescript('''DROP TABLE IF EXISTS `Parking Fines`;

CREATE TABLE `Parking Fines` (
  `Fine Number` INTEGER PRIMARY KEY AUTOINCREMENT, 
  `Date` DATETIME, 
  `Time` DATETIME, 
  `Application / Permit Number` INTEGER DEFAULT 0, 
  `Vehicle Registration Number` VARCHAR(255), 
  `Vehicle Type` VARCHAR(255), 
  `Details of Offence` LONGTEXT, 
  `Location of Offence` VARCHAR(255) 
  
); 
   ''')

# Fill in sample values into 'Parking Fines'
cursor.executescript('''

INSERT INTO `Parking Fines` (`Fine Number`, `Date`, `Time`, `Application / Permit Number`, `Vehicle Registration Number`, `Vehicle Type`, `Details of Offence`, `Location of Offence`) VALUES (1, '2016-09-01 00:00:00', '1899-12-30 11:00:00', 2, 'AMJ 708', 'Small Car', 'Permit Expired', 'Parking bay 89');

''')

cursor.executescript(''' 

DROP TABLE IF EXISTS 'User Info';

CREATE TABLE 'User Info'(
  `Application / Permit Number` INTEGER PRIMARY KEY AUTOINCREMENT,
  `Staff or Student ID` INTEGER DEFAULT 0,
  `Title` VARCHAR,
  `First Name` VARCHAR(255), 
  `Last Name` VARCHAR(255), 
  `Date of Birth` DATETIME, 
  `Home Phone` INTEGER DEFAULT 0, 
  `Work Phone` INTEGER DEFAULT 0, 
  `Mobile Phone` INTEGER DEFAULT 0, 
  `Email Address` LONGTEXT, 
  `Department/Faculty` VARCHAR(255), 
  `Are you Applying for a visitor?` TINYINT(1) DEFAULT 0, 
  `Visitor First Name` VARCHAR(255), 
  `Visitor Last Name` VARCHAR(255), 
  `Reson for Visit` VARCHAR(255), 
  `Vehicle Type` VARCHAR(255), 
  `Vehicle Registration Number` VARCHAR(255),
  `Vehicle Make and Model` LONGTEXT
  
)



''')

# Create an index seperately (sqlite3 doesnt allow you to do it in the table creation)
userind = ("CREATE INDEX 'UserInfoIndex' ON 'User Info' ('Staff or Student ID')")
cursor.execute(userind)

# Fill in User Info with dummy/sample data

cursor.executescript('''

INSERT INTO `User Info` (`Application / Permit Number`, `Staff or Student ID`, `Title`, `First Name`, `Last Name`, `Date of Birth`, `Home Phone`, `Work Phone`, `Mobile Phone`, `Email Address`, `Department/Faculty`, `Are you Applying for a visitor?`, `Visitor First Name`, `Visitor Last Name`, `Reson for Visit`, `Vehicle Type`, `Vehicle Registration Number`, `Vehicle Make and Model`) VALUES (1, 7839281, 'Mr', 'John', 'Smith', '1960-03-10 00:00:00', 0, 38792019, 473829102, 'John.Smith@gmail.com', 'SEF', 0, NULL, NULL, NULL, 'Small Car', 'VHG 785', 'Toyota Yaris');
INSERT INTO `User Info` (`Application / Permit Number`, `Staff or Student ID`, `Title`, `First Name`, `Last Name`, `Date of Birth`, `Home Phone`, `Work Phone`, `Mobile Phone`, `Email Address`, `Department/Faculty`, `Are you Applying for a visitor?`, `Visitor First Name`, `Visitor Last Name`, `Reson for Visit`, `Vehicle Type`, `Vehicle Registration Number`, `Vehicle Make and Model`) VALUES (2, 9876989, 'Ms', 'Anna', 'Jones', '1987-08-07 00:00:00', 0, 0, 478219989, 'Anna.Jones7@hotmail.com', 'Law', 0, NULL, NULL, NULL, 'Small Car', 'AMJ 708', 'Mazda 2');
INSERT INTO `User Info` (`Application / Permit Number`, `Staff or Student ID`, `Title`, `First Name`, `Last Name`, `Date of Birth`, `Home Phone`, `Work Phone`, `Mobile Phone`, `Email Address`, `Department/Faculty`, `Are you Applying for a visitor?`, `Visitor First Name`, `Visitor Last Name`, `Reson for Visit`, `Vehicle Type`, `Vehicle Registration Number`, `Vehicle Make and Model`) VALUES (3, 24350, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `User Info` (`Application / Permit Number`, `Staff or Student ID`, `Title`, `First Name`, `Last Name`, `Date of Birth`, `Home Phone`, `Work Phone`, `Mobile Phone`, `Email Address`, `Department/Faculty`, `Are you Applying for a visitor?`, `Visitor First Name`, `Visitor Last Name`, `Reson for Visit`, `Vehicle Type`, `Vehicle Registration Number`, `Vehicle Make and Model`) VALUES (4, 2340, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `User Info` (`Application / Permit Number`, `Staff or Student ID`, `Title`, `First Name`, `Last Name`, `Date of Birth`, `Home Phone`, `Work Phone`, `Mobile Phone`, `Email Address`, `Department/Faculty`, `Are you Applying for a visitor?`, `Visitor First Name`, `Visitor Last Name`, `Reson for Visit`, `Vehicle Type`, `Vehicle Registration Number`, `Vehicle Make and Model`) VALUES (5, 23450, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL);

''')


    

    
 

y = 1

while y == 1:
    task = Intro()

    if task == 1:
        RetData()
    if task == 2:
        EntData()
    if task == 3:
        y = 0

    









# Commit all the executions into the database
db.commit()











# Close/Save database (used at end of code)
db.close()
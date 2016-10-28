# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:58:34 2016

@author: Blake
"""


# Import database plugin
import sqlite3
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
  `Application / Permint Number` INTEGER DEFAULT 0, 
  `Vehicle Registration Number` VARCHAR(255), 
  `Vehicle Type` VARCHAR(255), 
  `Details of Offence` LONGTEXT, 
  `Location of Offence` VARCHAR(255) 
  
); 
   ''')

# Fill in sample values into 'Parking Fines'
cursor.executescript('''

INSERT INTO `Parking Fines` (`Fine Number`, `Date`, `Time`, `Application / Permint Number`, `Vehicle Registration Number`, `Vehicle Type`, `Details of Offence`, `Location of Offence`) VALUES (1, '2016-09-01 00:00:00', '1899-12-30 11:00:00', 2, 'AMJ 708', 'Small Car', 'Permit Expired', 'Parking bay 89');

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

userind = ("CREATE INDEX UserInfoIndex ON User Info (Staff or Student ID)")
cursor.execute(userind)
# Commit all the executions into the database
db.commit()
# Close/Save database (used at end of code)
db.close()
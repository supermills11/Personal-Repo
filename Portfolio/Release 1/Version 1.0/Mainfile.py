# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:58:34 2016

@author: Blake
"""


# Import database and image support plugins
import sqlite3
from tkinter import *
from PIL import Image, ImageTk

# Global Variables

col = 'hotpink1'
backcol = '#f7b7d3'
textcol = 'black'

## Function Definitions

# This function lifts the frame passed to it to the top

def liftframe(liftee):
    liftee.lift()

# A test function for diagnostic purposes
def testfunc():
    print('success!')


# Initializing the tkinter window

def Init ():
    window = Tk()
    
    # Window configuration
    window.minsize(width=1024, height=768)
    window.configure(background=backcol)

    # Calling the InitHome function
    InitHome(window)

    
    # The loop for the window, which keeps the program running
    window.mainloop()


# This function gets all the information from the database and then displays it in the correct labels
def Update (finenumdata, datedata, timedata, appdata, regdata, vedata, detailsdata, locdata, validdata):

    # Allocating memory for the text variables
    finenumtext = ""
    datedatatext= ""
    timedatatext= ""
    appdatatext= ""
    regdatatext= ""
    vedatatext= ""
    detailsdatatext = ""
    locdatatext = ""
    validdatatext = ""

    # Using the SQL language and sqlite3 plugin to grab all of the information from table 'Parking Fines'
    cursor.execute("SELECT * FROM 'Parking Fines'")
    rows = cursor.fetchall()

    # This loop grabs all of the rows that exist in the database
    for row in rows:
        
        # Here the program grabs each element of each row, assigns it, and then creates a new line for the next row
        finenumtext = finenumtext + "\n" + str(row[0])
        datedatatext = datedatatext + "\n" + str(row[1])
        timedatatext = timedatatext + "\n" + str(row[2])
        appdatatext = appdatatext + "\n" + str(row[3])
        regdatatext = regdatatext + "\n" + str(row[4])
        vedatatext = vedatatext + "\n" + str(row[5])
        detailsdatatext = detailsdatatext + "\n" + str(row[6])
        locdatatext = locdatatext + "\n" + str(row[7])
        validdatatext = validdatatext + "\n" + str(row[8])

    # Resetting the labels text
    finenumdata.configure(text=finenumtext)
    datedata.configure(text=datedatatext)
    timedata.configure(text=timedatatext)
    appdata.configure(text=appdatatext)
    regdata.configure(text=regdatatext)
    vedata.configure(text=vedatatext)
    detailsdata.configure(text=detailsdatatext)
    locdata.configure(text=locdatatext)
    validdata.configure(text=validdatatext)

    

    return

# This function gets all of the information entered into the text boxes, and then uses sqlite3 to put them into the database        
def EnterData (finenumentry, datedataentry, timedataentry, appdataentry, regdataentry, vedataentry, detailsdataentry, locdataentry, validdataentry ):


    # Get all the text from the entry boxes    
    finenum = finenumentry.get()
    datedata = datedataentry.get()
    timedata = timedataentry.get()
    appdata = appdataentry.get()
    regdata = regdataentry.get()
    vedata = vedataentry.get()
    details = detailsdataentry.get()
    loc = locdataentry.get()
    valid = validdataentry.get()

    # Put into 'Parking Fines'
    cursor.execute("INSERT INTO 'Parking Fines' ('Fine Number', 'Date', 'Time', 'Application / Permit Number', 'Vehicle Registration Number', 'Vehicle Type', 'Details of Offence', 'Location of Offence', 'Validity' ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (finenum, datedata, timedata, appdata, regdata, vedata, details, loc, valid))


    return
    
# This function allows the SQL command line tool feature to work
def Edit (editentry):

    # Get the SQL code from the entry box
    command = editentry.get()
    # Execute SQL code
    cursor.execute(command)

    return


    
# This function initializes all the different windows and the majority of the UI
def InitHome (window):
    
    # Opening an image to be read by PIL    
    image = Image.open("header2.jpg")
    photo = ImageTk.PhotoImage(image)
    
    # Set image to a label and display
    header = Label(window, image=photo, borderwidth=0, highlightthickness=0)
    header.image = photo
    header.pack()
    header.place(x=0, y=0)

    # Navigation buttons, each button brings foward their respective frame
    homebut = Button(window, text="Home", width=29, bg=col, command= lambda: liftframe(homeframe))
    homebut.place(x=0,y=90)
    
    permitbut = Button(window, text="Permits", width=29, bg=col, command= lambda: liftframe(permframe))
    permitbut.place(x=210,y=90)
    
    appbut = Button(window, text="Applications", width=29, bg=col, command= lambda: liftframe(appframe))
    appbut.place(x=420, y=90)
    
    sancbut = Button(window, text="Sanctions", width=29, bg = col, command= lambda: liftframe(sancframe))
    sancbut.place(x=630, y=90)
    
    docbut = Button(window, text="Documents", width=29, bg=col, command= lambda: liftframe(docsframe))
    docbut.place(x=840, y=90)

    # Creating the documents frame

    docsframe = Frame(window, height=678, width=1024, bg='#f7b7d3')
    docsframe.place(x=0,y=115)

    # Creating the Sanctions frame

    sancframe = Frame(window, height=678, width=1024, bg='#f7b7d3')
    sancframe.place(x=0,y=115)

    # Creating the applications frame

    appframe = Frame(window, height=678, width=1024, bg='#f7b7d3')
    appframe.place(x=0,y=115)

    # Creating the permits frame

    permframe = Frame(window, height=678, width=1024, bg='#f7b7d3')
    permframe.place(x=0,y=115)

    # Creating the home frame
    
    homeframe = Frame(window, height=678, width=1024, bg='#f7b7d3')
    homeframe.place(x=0,y=115)

    # Opening the images to be displayed on the home page
    homeim = Image.open("homepage2.jpg")
    homephoto = ImageTk.PhotoImage(homeim)

    # Assigning image to a label and displaying
    homepiclabel = Label(homeframe, image=homephoto, borderwidth=0, highlightthickness=0)
    homepiclabel.image = homephoto
    homepiclabel.place(x=750, y=0)

    # Opening the two maps, assigning and displaying
    map1im = Image.open("map1.jpg")
    map1photo = ImageTk.PhotoImage(map1im)

    map1label = Label(homeframe, image=map1photo, borderwidth=0, highlightthickness=0)
    map1label.image = map1photo

    map1label.place(x=550, y=0)

    map2im = Image.open("map2.jpg")
    map2photo = ImageTk.PhotoImage(map2im)

    map2label = Label(homeframe, image=map2photo, borderwidth=0, highlightthickness=0)
    map2label.image = map2photo
    map2label.place(x=550,y=300)

    


    # Further test and placeholder text
    #underpiclabel = Label(homeframe, text="I HAVE TRANSENCDED EXISTENCE", bg=col, font = 'bold')
    #underpiclabel.place(x=750,y=600)
    
    titlelabel = Label(homeframe, text="Parking Rules", bg = '#f7b7d3', fg = textcol, font = 'bold')
    titlelabel.place(x=10, y=10)
    
    textlabel = Label(homeframe, text="All rules must be abided by at all times \n No parking is allowed anywhere other than the allocated spaces \n At no time should the speed limit of 15km/hr be exceeded \n Full payment for the parking permit must be made before the permit can be used \n Only cars and motorbikes are allowed to occupy a parking space. \n No unauthorised vehicles are allowed \n In the instance a permit officer is providing alternative directions, \n these must be followed \n Littering is not allowed anywhere within the parking areas. \n A valid permit must be held in order to occupy a parking space \n The nominated vehicle under the permit is to be \n the only vehicle to use the permit throughout the entire \n duration of the permit \n The parking permit must be wholly visible at all times when the permit is being used \n The permit provided must not be defaced, altered or reproduced under any circumstance \n A damaged parking permit where some/all information is obstructed is considered invalid and the \n permit holder must apply \n for their permit to be reprinted my permit officers. \n A parking officer reserves the right to suspend or withdraw a permit at any time \n The permit holders personal information is needed for parking management and campus safety. \n This information may need to be disclosed to other \n departments of the College for safety reasons, or to law \n and regulatory enforcement agencies (eg. Police), and finally where authorised by law \n A permit cannot be issued unless accurate personal information is provided. \n A permit holder has the \n right at any time to request a copy of the personal information held by Atmiya College \n If a permit is being purchased upon arrival at the parking areas, \n Atmiya College is not responsible if \n there are no available spaces left. \n Availabilities are given on a first in first serve basis, \n Atmiya College \n will under no circumstance reserve a parking space \n for anyone who doesn’t already hold a parking permit \n Atmiya College does not accept liability for any loss, injury or damage \n that has occurred to any private \n vehicle on college property.\n The vehicle owner accepts all liability after a permit is accepted \n A breach of any of the above rules may result in fines, suspension or withdrawal of parking privileges", bg = '#f7b7d3', fg = textcol, justify=LEFT)
    textlabel.place(x = 10, y = 60)

    # Putting test data in each from for identification

    docstest = Label(docsframe, text = "documents frame")
    docstest.place(x = 10, y = 60)

    sanctest = Label(sancframe, text = "sanctions frame")
    sanctest.place(x = 10, y = 60)
    

    permtest = Label(permframe, text = "permit frame")
    permtest.place(x = 512, y = 10)

    # Creating the frame for displaying the database


    # The following Labels are all the labels used to display the database info
    parkfines = Frame(permframe, height=600, width=1024, bg = '#f7b7d3')
    parkfines.place(x= 0, y=60)

    finenum = Label(parkfines, text="Fine Num")
    finenum.place(x=50, y = 0)    

    finenumdata = Label(parkfines, text="test")
    finenumdata.place(x=50, y=50)

    date = Label(parkfines, text="Date")
    date.place(x= 150, y = 0)

    datedata = Label(parkfines, text="test2")
    datedata.place(x=150, y=50)

    time = Label(parkfines, text="Time")
    time.place(x= 300, y = 0)

    timedata = Label(parkfines, text="test3")
    timedata.place(x=300, y=50)

    appnum = Label(parkfines, text="App Num")
    appnum.place(x=450, y = 0)

    appdata = Label(parkfines, text="test4")
    appdata.place(x=450, y=50)

    regnum = Label(parkfines, text="Vehicle Reg \n Number")
    regnum.place(x=550, y= 0)

    regdata = Label(parkfines, text="test5")
    regdata.place(x=550, y=50)

    vetype = Label(parkfines, text="Vehicle Type")
    vetype.place(x=650, y= 0)

    vedata = Label(parkfines, text="test6")
    vedata.place(x=650, y=50)

    details = Label(parkfines, text="Details")
    details.place(x=750, y= 0)

    detailsdata = Label(parkfines, text="test7")
    detailsdata.place(x=750, y=50)

    loc = Label(parkfines, text="Location")
    loc.place(x=850, y=0)

    locdata = Label(parkfines, text="test8")
    locdata.place(x=850, y=50)

    valid = Label(parkfines, text="Valid")
    valid.place(x=950, y=0)

    validdata = Label(parkfines, text="test9")
    validdata.place(x=950, y=50)

    updatebut = Button(permframe, text="Update", width=29, bg = col, command=  lambda: Update(finenumdata, datedata, timedata, appdata, regdata, vedata, detailsdata, locdata, validdata))
    updatebut.place(x=800, y=5)

    # Entry on the permit page

    finenum2 = Label(appframe, text="Fine Num")
    finenum2.place(x=50, y = 20)    

    finenumentry = Entry(appframe)
    finenumentry.place(x=150, y=20)

    date2 = Label(appframe, text="Date")
    date2.place(x= 50, y = 60)

    datedataentry = Entry(appframe)
    datedataentry.place(x=150, y=60)

    time2 = Label(appframe, text="Time")
    time2.place(x= 50, y = 100)

    timedataentry = Entry(appframe)
    timedataentry.place(x=150, y=100)

    appnum2 = Label(appframe, text="App Num")
    appnum2.place(x=50, y = 140)
     

    appdataentry = Entry(appframe)
    appdataentry.place(x=150, y=140)

    regnum2 = Label(appframe, text="Vehicle Reg \n Number")
    regnum2.place(x=50, y= 180)

    regdataentry = Entry(appframe)
    regdataentry.place(x=150, y=180)

    vetype2 = Label(appframe, text="Vehicle Type")
    vetype2.place(x=50, y= 220)

    vedataentry = Entry(appframe)
    vedataentry.place(x=150, y=220)

    details2 = Label(appframe, text="Details")
    details2.place(x=50, y= 260)

    detailsdataentry = Entry(appframe)
    detailsdataentry.place(x=150, y=260)

    loc2 = Label(appframe, text="Location")
    loc2.place(x=50, y=300)

    locdataentry = Entry(appframe)
    locdataentry.place(x=150, y=300)

    valid2 = Label(appframe, text="Valid")
    valid2.place(x=50, y=340)

    validdataentry = Entry(appframe)
    validdataentry.place(x=150, y=340)

    enterdatabut = Button(appframe, text="Enter Data", width=30, bg=col, command =lambda: EnterData(finenumentry, datedataentry, timedataentry, appdataentry, regdataentry, vedataentry, detailsdataentry, locdataentry, validdataentry ))
    enterdatabut.place(x=50,y=380)

    # The button and labels for the editing feature

    editbut = Button(appframe, text="Edit", width=30, bg=col, command= lambda: Edit(editentry))
    editbut.place(x=450,y= 500)

    editentry = Entry(appframe, width=150)
    editentry.place(x=50, y = 450)

    return
    

###
###  The following functions are for a simple text based version of the program.
###  
###  This was the very first version of the program, however it has been left intact
###  in order to serve as a backup and a testing platform for the database


# Simple UI function to ask what the user wants to do

def Intro ():
    x = 1

    # Ask the user
    while (x == 1):
        print("\n What would you like to do?\n")
        print("1. Retrieve Data\n")
        print("2. Enter Data\n")
        print("3. Exit\n")
        # Get input
        task = int(input("Please type a number\n"))
        # Out of bounds trapping, exit loop if in bounds
        if task > 3 or task < 1:
            print("The option you have selected is out of range, Please choose again")
        else:
           x = 0
    
        print (task)
        return task

# A function for retrieving the data from the database    
def RetData ():
    x = 1
    # Ask the user which table they want to retrieve data from
    while (x == 1):
        print("\n From which table would you like to retrieve data from?\n")
        print("1. Parking Fines\n")
        print("2. User Info\n")
        # Get input
        table = int(input("Please type a number\n"))
        # Out of bounds trapping
        if table > 2 or table < 1:
            print("The option you have selected is out of range, Please choose again")
        else:
           x = 0
    
        print (table)
        # Depending on the user selection, the program either dumps all of the data from 'Parking Fines' or 'User Info'
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
        
# A function for being able to type pure SQL commands (effectively a dumb SQL shell)
def EntData ():
    x = 1
    # A while loop to act as a shell
    while (x == 1):        
        
        data = input("Please type your entry data in full SQL format\n")
        cursor.execute(data)

        # Test data to ensure loop is iterating
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
  `Date` VARCHAR, 
  `Time` VARCHAR, 
  `Application / Permit Number` INTEGER DEFAULT 0, 
  `Vehicle Registration Number` VARCHAR, 
  `Vehicle Type` VARCHAR(255), 
  `Details of Offence` LONGTEXT, 
  `Location of Offence` VARCHAR(255),
  `Validity` VARCHAR(255)
  
); 
   ''')

# Fill in sample values into 'Parking Fines'
cursor.executescript('''

INSERT INTO `Parking Fines` (`Fine Number`, `Date`, `Time`, `Application / Permit Number`, `Vehicle Registration Number`, `Vehicle Type`, `Details of Offence`, `Location of Offence`, `Validity`) VALUES (1, '2016-09-01 00:00:00', '1899-12-30 11:00:00', 2, 'AMJ 708', 'Small Car', 'Permit Expired', 'Parking bay 89', 'Yes');

''')

# Create the table 'User Info'
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


# Start of program

Init()


 
# Old console operation (Uncomment to enable the old version)
#y = 1

#while y == 1:
#    task = Intro()
#
#    if task == 1:
#        RetData()
#    if task == 2:
#        EntData()
#    if task == 3:
#        y = 0

    


# Commit all the executions into the database
db.commit()

# Close/Save database 
db.close()

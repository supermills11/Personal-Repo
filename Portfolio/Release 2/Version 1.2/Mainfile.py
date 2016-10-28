# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:58:34 2016

@author: Blake Mills
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

## Update functions: these functions update the relevant labels in the database display modules


# Update the Health and Safety display
def UpdateHandS(numlabeldata, loclabeldata, reportlabeldata, desclabeldata, sevlabeldata, risklabeldata, datelabeldata, timelabeldata):
    # Allocate memory
    print("UpdateHS entered")
    numtext = ""
    loctext = ""
    reporttext = ""
    desctext = ""
    sevtext = ""
    risktext = ""
    datetext = ""
    timetext = ""
	# Get all contents from relevant table
    cursor.execute("SELECT * FROM 'Health & Safety Violations'")
    rows = cursor.fetchall()
	# Here the program grabs each element of each row, assigns it, and then creates a new line for the next row
    for row in rows:
        numtext = numtext + "\n" + str(row[0])
        loctext = loctext + "\n" + str(row[1])
        reporttext = reporttext + "\n" + str(row[2])
        desctext = desctext + "\n" + str(row[3])
        sevtext = sevtext + "\n" + str(row[4])
        risktext = risktext + "\n" + str(row[5])
        datetext = datetext + "\n" + str(row[6])
        timetext = timetext + "\n" + str(row[7])
	# Changing the text of the labels
    numlabeldata.configure(text=numtext)
    loclabeldata.configure(text=loctext)
    reportlabeldata.configure(text=reporttext)
    desclabeldata.configure(text=desctext)
    sevlabeldata.configure(text=sevtext)
    risklabeldata.configure(text=risktext)
    datelabeldata.configure(text=datetext)
    timelabeldata.configure(text=timetext)
    


    return



def UpdateS (snumdata, snamedata, sstudata, sdatedata, stimedata, splacedata):
	# Allocate memory
    snumtext = ""
    snametext = ""
    stutext = ""
    sdatetext = ""
    stimetext = ""
    splacetext = ""
	# Get all contents from relevant table
    cursor.execute("SELECT * FROM 'Smoking Violations'")
    rows = cursor.fetchall()
	# Here the program grabs each element of each row, assigns it, and then creates a new line for the next row
    for row in rows:
        snumtext = snumtext + "\n" + str(row[0])
        snametext= snametext + "\n" + str(row[1])
        stutext= stutext + "\n" + str(row[2])
        sdatetext = sdatetext + "\n" + str(row[3])
        stimetext = stimetext + "\n" + str(row[4])
        splacetext = splacetext + "\n" + str(row[5])
	# Changing the text of the labels
    snumdata.configure(text=snumtext)
    snamedata.configure(text=snametext)
    sstudata.configure(text=stutext)
    sdatedata.configure(text=sdatetext)
    stimedata.configure(text=stimetext)
    splacedata.configure(text=splacetext)


    return



# This function gets the relevant information from the database and then displays it in the correct labels
def UpdatePark (finenumdata, datedata, timedata, appdata, regdata, vedata, detailsdata, locdata, validdata):

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

def UpdateUser (uappnumdata, ufirstdata, ulastdata, udobdata, uphonedata, udepdata, uvisitdata, uvetypedata, uregodata, umakedata):
	# Allocating memory
    apptext = ""
    firsttext = ""
    lasttext = ""
    dobtext = ""
    phonetext = ""
    deptext = ""
    visittext = ""
    typetext = ""
    regotext = ""
    maketext = ""
	# Using the SQL language and sqlite3 plugin to grab all of the information from table 'User Info'
    cursor.execute("SELECT * FROM 'User Info'")
    rows = cursor.fetchall()
	# Here the program grabs each element of each row, assigns it, and then creates a new line for the next row
    for row in rows:

        apptext = apptext + "\n" + str(row[0])
        firsttext = firsttext + "\n" + str(row[1])
        lasttext = lasttext + "\n" + str(row[2])
        dobtext = dobtext + "\n" + str(row[3])
        phonetext = phonetext + "\n" + str(row[4])
        deptext = deptext + "\n" + str(row[5])
        visittext = visittext + "\n" + str(row[6])
        typetext = typetext + "\n" + str(row[7])
        regotext = regotext + "\n" + str(row[8])
        maketext = maketext + "\n" + str(row[9])
        
	# Resetting the labels text
    uappnumdata.configure(text=apptext)
    ufirstdata.configure(text=firsttext)
    ulastdata.configure(text=lasttext)
    udobdata.configure(text=dobtext)
    uphonedata.configure(text=phonetext)
    udepdata.configure(text=deptext)
    uvisitdata.configure(text=visittext)
    uvetypedata.configure(text=typetext)
    uregodata.configure(text=regotext)
    umakedata.configure(text=maketext)

    return

    


# This function gets all of the information entered into the relevant text boxes, and then uses sqlite3 to put them into the database        
def EnterDataPark (finenumentry, datedataentry, timedataentry, appdataentry, regdataentry, vedataentry, detailsdataentry, locdataentry, validdataentry ):

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

    # Make sure there is a fine number
    if finenum == "":
        messagebox.showinfo("Invalid Input, A fine number is required")
        return
    

    # Put into 'Parking Fines'
    cursor.execute("INSERT INTO 'Parking Fines' ('Fine Number', 'Date', 'Time', 'Application / Permit Number', 'Vehicle Registration Number', 'Vehicle Type', 'Details of Offence', 'Location of Offence', 'Validity' ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (finenum, datedata, timedata, appdata, regdata, vedata, details, loc, valid))
    db.commit()

    return

# This function gets all of the information from the text boxes related to the User Info and then places it into the database
def EnterDataUser (appnumentry, firstentry, lastentry, dobentry, phoneentry, depentry, visitentry, vetypeentry, regoentry, vemakeentry):
	# Get all the text from the entry boxes    
    appnum = appnumentry.get()
    first = firstentry.get()
    last = lastentry.get()
    dob = dobentry.get()
    phone = phoneentry.get()
    dep = depentry.get()
    visit = visitentry.get()
    vetype = vetypeentry.get()
    rego = regoentry.get()
    vemake = vemakeentry.get()

    # Make sure there is a application number
    if appnum == "":
        messagebox.showinfo("Invalid Input, An application number is required")
        return

    # Insert and commit to database
    cursor.execute("INSERT INTO 'User Info' ('Application / Permit Number', 'First Name', 'Last Name', 'Date of Birth', 'Phone', 'Department/Faculty', 'Are you Applying for a visitor?', 'Vehicle Type', 'Vehicle Registration Number', 'Vehicle Make and Model' ) VALUES (?, ?, ?,?, ?, ?, ?, ?, ?, ?)", (appnum, first, last,dob, phone, dep, visit, vetype, rego, vemake))
    db.commit()  

# This function gets all the entry data for Health and Safety and then places it into the database
def EnterDataHS(numentry, locationentry, reportentry, descentry, seventry, riskentry, date3entry, time3entry):
	# Get all the text from the entry boxes   
    num = numentry.get()
    loc = locationentry.get()
    rep = reportentry.get()
    desc = descentry.get()
    sev = seventry.get()
    risk = riskentry.get()
    date = date3entry.get()
    time = time3entry.get()
	# Make sure there is an offence number
    if num == "":
        messagebox.showinfo("Invalid Input, An Offence Number is Required")
        return
	# Insert and commit to database
    cursor.execute("INSERT INTO 'Health & Safety Violations' ('Number', 'Location of issue', 'Reportee', 'Decription of Issue', 'Severity', 'Risk Status', 'Date', 'Time') VALUES (?,?,?,?,?,?,?,?)", (num, loc, rep,desc, sev, risk, date, time))
    db.commit()

    return
# This function gets all the entry data for Smoking Violations and then places it into the database
def EnterDataS(num2entry, name2entry, stunumentry, date4entry, time4entry, place2entry):
	# Get all the text from the entry boxes 
    num = num2entry.get()
    name = name2entry.get()
    stu = stunumentry.get()
    date = date4entry.get()
    time = time4entry.get()
    place = place2entry.get()
	# Make sure there is an offence number
    if num == "":
        messagebox.showinfo("Invalid Input, An Offence Number is Required")
        return

    cursor.execute("INSERT INTO 'Smoking Violations' ('Fine Number', 'Full Name', 'Staff or Student Number', 'Date', 'Time', 'Place') VALUES (?,?,?,?,?,?)", (num, name, stu, date, time, place))
    db.commit()


    return


# This function is called when the 'Launch Client' button is pressed. It opens a child window containing the client side of the application
def ClientLaunch(window):
    # Launching the new window
    
    client = Toplevel()
    client.minsize(width=1024, height=768)
    client.configure(background=backcol)

    # Bring in graphics and menus

    # Opening an image to be read by PIL    
    image2 = Image.open("header2.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    
    # Set image to a label and display
    header2 = Label(client, image=photo2, borderwidth=0, highlightthickness=0)
    header2.image = photo2
    header2.pack()
    header2.place(x=0, y=0)

    titlelabel2 = Label(client, text="Client", bg = '#f7b7d3', fg = textcol, font = 'bold')
    titlelabel2.place(x=700, y= 50)

    # Navigation buttons
    homebut = Button(client, text="Home", width=37, bg=col, command= lambda: liftframe(home2frame))
    homebut.place(x=0,y=90)

    aboutbut = Button(client, text="About", width=37, bg=col, command= lambda: liftframe(aboutframe))
    aboutbut.place(x=260,y=90)

    servicesbut = Button(client, text="Services", width=37, bg=col, command= lambda: liftframe(servicesframe))
    servicesbut.place(x=520, y=90)

    accbut = Button(client, text="My Account", width=37, bg=col, command= lambda: liftframe(accframe))
    accbut.place(x=770, y=90)

    # Frames for each of the buttons

    home2frame = Frame(client, height=678, width = 1024, bg='#f7b7d3')
    home2frame.place(x=0,y=115)

    aboutframe = Frame(client, height=678, width= 1024, bg='#f7b7d3')
    aboutframe.place(x=0,y=115)

    servicesframe = Frame(client, height=678, width=1024, bg='#f7b7d3')
    servicesframe.place(x=0, y=115)

    accframe = Frame(client, height=678, width= 1024, bg='#f7b7d3')
    accframe.place(x=0, y=115)

    # lift the home frame
    liftframe(home2frame)

    # background for the home frame
    backgr = Image.open("homeback.jpg")
    backgrphoto = ImageTk.PhotoImage(backgr)

    backgrlabel = Label(home2frame, image=backgrphoto, borderwidth=0, highlightthickness=0)
    backgrlabel.image  = backgrphoto
    backgrlabel.place(x=0,y=0)

    ## Labels and entry for User Info

    appnum = Label(accframe, text="App / Permit Number")
    appnum.place(x = 350, y = 20)

    appnumentry = Entry(accframe)
    appnumentry.place(x=500, y = 20)

    first = Label(accframe, text="First Name")
    first.place(x = 350, y = 60)

    firstentry = Entry(accframe)
    firstentry.place(x=500, y=60)

    last = Label(accframe, text = "Last Name")
    last.place(x=350, y=100)

    lastentry = Entry(accframe)
    lastentry.place(x=500, y=100)

    dob = Label(accframe, text ="Date of Birth")
    dob.place(x=350, y=140)

    dobentry = Entry(accframe)
    dobentry.place(x=500, y=140)

    phone = Label(accframe, text = "Phone Number")
    phone.place(x=350, y=180)

    phoneentry = Entry(accframe)
    phoneentry.place(x=500, y=180)

    dep = Label(accframe, text = "Department / Faculty")
    dep.place(x=350, y=220)

    depentry = Entry(accframe)
    depentry.place(x=500, y=220)

    visit = Label(accframe, text = "Are you a visitor?")
    visit.place(x=350, y=260)

    visitentry = Entry(accframe)
    visitentry.place(x=500, y=260)

    vetype = Label(accframe, text = "Vehicle Type")
    vetype.place(x=350, y=300)

    vetypeentry = Entry(accframe)
    vetypeentry.place(x=500, y=300)

    rego = Label(accframe, text = "Vehicle Registration")
    rego.place(x=350, y= 340)

    regoentry = Entry(accframe)
    regoentry.place(x=500, y= 340)

    vemake = Label(accframe, text = "Vehicle Make/Model")
    vemake.place(x= 350, y= 380)

    vemakeentry = Entry(accframe)
    vemakeentry.place(x=500, y= 380)

    # Button for entering the data typed into the entry boxes
    enterdatabut2 = Button(accframe, text="Enter Data", width=38, bg=col, command = lambda: EnterDataUser (appnumentry, firstentry, lastentry, dobentry, phoneentry, depentry, visitentry, vetypeentry, regoentry, vemakeentry))
    enterdatabut2.place(x=350,y=410)
    # Button for updating the existing information
    updatebut2 = Button(accframe, text="Update", width=38, bg=col)
    updatebut2.place(x=350,y=450)




# This function updates information entered into the sanctions table

def UpdateSancdb (finenumentry, datedataentry, timedataentry, appdataentry, regdataentry, vedataentry, detailsdataentry, locdataentry, validdataentry ):

    # Get text from entry boxes
    finenum = finenumentry.get()
    datedata = datedataentry.get()
    timedata = timedataentry.get()
    appdata = appdataentry.get()
    regdata = regdataentry.get()
    vedata = vedataentry.get()
    details = detailsdataentry.get()
    loc = locdataentry.get()
    valid = validdataentry.get()

    # Make sure there is a fine number
    if finenum == "":
        messagebox.showinfo("Invalid Input", "A fine number is required")
        return

    # Update into 'Parking Fines'
    cursor.execute("UPDATE 'Parking Fines' SET 'Date'= ?, 'Time'= ?, 'Application / Permit Number'=?, 'Vehicle Registration Number'=?, 'Vehicle Type' =?, 'Details of Offence'=?, 'Location of Offence'=?, 'Validity'=? WHERE 'Fine Number' = ?", (datedata, timedata, appdata, regdata, vedata, details, loc, valid, int(finenum)))
    db.commit()
    print("committed")
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

    # Navigation buttons, each button brings forward their respective frame
    homebut = Button(window, text="Home", width=29, bg=col, command= lambda: liftframe(homeframe))
    homebut.place(x=0,y=90)
    
    permitbut = Button(window, text="Parking Fines and User Info", width=29, bg=col, command= lambda: liftframe(permframe))
    permitbut.place(x=210,y=90)
    
    appbut = Button(window, text="Other Violations", width=29, bg=col, command= lambda: liftframe(appframe))
    appbut.place(x=420, y=90)
    
    sancbut = Button(window, text="Violation Forms", width=29, bg = col, command= lambda: liftframe(sancframe))
    sancbut.place(x=630, y=90)
    
    docbut = Button(window, text="Parking Rules", width=29, bg=col, command= lambda: liftframe(docsframe))
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

    ## Opening the extra maps, assigning and displaying
    backgr = Image.open("homeback.jpg")
    backgrphoto = ImageTk.PhotoImage(backgr)

    backgrlabel = Label(homeframe, image=backgrphoto, borderwidth=0, highlightthickness=0)
    backgrlabel.image  = backgrphoto
    backgrlabel.place(x=0,y=0)

    
    map1im = Image.open("map3.jpg")
    map1photo = ImageTk.PhotoImage(map1im)

    map1label = Label(homeframe, image=map1photo, borderwidth=0, highlightthickness=0)
    map1label.image = map1photo

    map1label.place(x=550, y=0)

    map2im = Image.open("map4.jpg")
    map2photo = ImageTk.PhotoImage(map2im)

    map2label = Label(homeframe, image=map2photo, borderwidth=0, highlightthickness=0)
    map2label.image = map2photo
    map2label.place(x=550,y=300)

    homeim1 = Image.open("im1.jpg")
    homeim1photo = ImageTk.PhotoImage(homeim1)

    homeim1label = Label(homeframe, image=homeim1photo, borderwidth=0, highlightthickness=0)
    homeim1label.image = homeim1photo
    homeim1label.place(x=440,y=300)

    # Client side launch button  
    clientlaunchbut = Button(homeframe, text="Launch Client", width=29, bg = col, command=lambda: ClientLaunch(window))
    clientlaunchbut.place(x=150, y = 50)

    ## Heading labels

    fineslabel = Label(sancframe, text= "Parking Fine Entry", bg = '#f7b7d3', fg = textcol)
    fineslabel.place(x=100,y=0)

    hslabel = Label(sancframe, text= "Health and Safety Violations", bg = '#f7b7d3', fg = textcol)
    hslabel.place(x=450, y=0)

    smokinglabel = Label(sancframe, text= "Smoking Violations Entry", bg = '#f7b7d3', fg = textcol)
    smokinglabel.place(x=750, y=0)
    
    titlelabel = Label(docsframe, text="Parking Rules", bg = '#f7b7d3', fg = textcol, font = 'bold')
    titlelabel.place(x=10, y=10)
    # The parking rules
    textlabel = Label(docsframe, text="All rules must be abided by at all times \n No parking is allowed anywhere other than the allocated spaces \n At no time should the speed limit of 15km/hr be exceeded \n Full payment for the parking permit must be made before the permit can be used \n Only cars and motorbikes are allowed to occupy a parking space. \n No unauthorised vehicles are allowed \n In the instance a permit officer is providing alternative directions, \n these must be followed \n Littering is not allowed anywhere within the parking areas. \n A valid permit must be held in order to occupy a parking space \n The nominated vehicle under the permit is to be \n the only vehicle to use the permit throughout the entire \n duration of the permit \n The parking permit must be wholly visible at all times when the permit is being used \n The permit provided must not be defaced, altered or reproduced under any circumstance \n A damaged parking permit where some/all information is obstructed is considered invalid and the \n permit holder must apply \n for their permit to be reprinted my permit officers. \n A parking officer reserves the right to suspend or withdraw a permit at any time \n The permit holders personal information is needed for parking management and campus safety. \n This information may need to be disclosed to other \n departments of the College for safety reasons, or to law \n and regulatory enforcement agencies (eg. Police), and finally where authorised by law \n A permit cannot be issued unless accurate personal information is provided. \n A permit holder has the \n right at any time to request a copy of the personal information held by Atmiya College \n If a permit is being purchased upon arrival at the parking areas, \n Atmiya College is not responsible if \n there are no available spaces left. \n Availabilities are given on a first in first serve basis, \n Atmiya College \n will under no circumstance reserve a parking space \n for anyone who doesn’t already hold a parking permit \n Atmiya College does not accept liability for any loss, injury or damage \n that has occurred to any private \n vehicle on college property.\n The vehicle owner accepts all liability after a permit is accepted \n A breach of any of the above rules may result in fines, suspension or withdrawal of parking privileges", bg = '#f7b7d3', fg = textcol, justify=LEFT)
    textlabel.place(x = 10, y = 60)

    permtest = Label(permframe, text = "permit frame")
    permtest.place(x = 512, y = 10)

    


    ## The following Labels are all the labels used to display the database info


    # Used for H&S violations

    hslabel = Label(appframe, text="Health and Safety Violations")
    hslabel.place(x=450,y=10)

    numlabel = Label(appframe, text="Violation Number")
    numlabel.place(x=50, y=50)

    numlabeldata = Label(appframe, text="test1")
    numlabeldata.place(x=50, y=100)

    loclabel = Label(appframe, text="Location of Issue")
    loclabel.place(x=170, y=50)

    loclabeldata = Label(appframe, text="test2")
    loclabeldata.place(x=170,y=100)

    reportlabel = Label(appframe, text="Reportee")
    reportlabel.place(x=300,y=50)

    reportlabeldata = Label(appframe, text="test3")
    reportlabeldata.place(x=300, y=100)

    desclabel = Label(appframe, text="Description")
    desclabel.place(x=450, y=50)

    desclabeldata = Label(appframe, text="test4")
    desclabeldata.place(x=450,y=100)

    sevlabel = Label(appframe, text="Severity")
    sevlabel.place(x=550, y=50)

    sevlabeldata = Label(appframe, text="test5")
    sevlabeldata.place(x=550, y=100)

    risklabel = Label(appframe, text="Risk")
    risklabel.place(x=650, y=50)

    risklabeldata = Label(appframe, text="test6")
    risklabeldata.place(x=650, y=100)

    datelabel = Label(appframe, text = "Date")
    datelabel.place(x=750, y=50)

    datelabeldata = Label(appframe, text = "test7")
    datelabeldata.place(x=750, y=100)

    timelabel = Label(appframe, text = "Time")
    timelabel.place(x=850, y=50)

    timelabeldata = Label(appframe, text = "test8")
    timelabeldata.place(x=850, y=100)

    # Used for Smoking violations

    stitle = Label(appframe, text = "Smoking Violations")
    stitle.place(x=450,y=310)

    snum = Label(appframe, text = "Fine Number")
    snum.place(x=50, y=350)

    snumdata = Label(appframe, text = "test1")
    snumdata.place(x=50, y=400)

    sname = Label(appframe, text = "Full Name")
    sname.place(x=200, y=350)

    snamedata = Label(appframe, text = "test2")
    snamedata.place(x=200, y=400)

    sstu = Label(appframe, text = "Staff/Student Number")
    sstu.place(x=350, y=350)

    sstudata = Label(appframe, text = "test3")
    sstudata.place(x=350, y=400)

    sdate = Label(appframe, text="Date")
    sdate.place(x=500, y=350)

    sdatedata = Label(appframe, text="test4")
    sdatedata.place(x=500, y=400)

    stime = Label(appframe, text = "Time")
    stime.place(x=650, y=350)

    stimedata = Label(appframe, text = "test5")
    stimedata.place(x=650, y=400)

    splace = Label(appframe, text = "Place")
    splace.place(x=800, y=350)

    splacedata = Label(appframe, text = "test6")
    splacedata.place(x=800, y=400)



    # Used for parking fines
    parkfines = Frame(permframe, height=600, width=1024, bg = '#f7b7d3')
    parkfines.place(x= 0, y=60)

    finenum = Label(parkfines, text="Fine Num", bg='#f7b7d3')
    finenum.place(x=50, y = 0)    

    finenumdata = Label(parkfines, text="test", bg='#f7b7d3')
    finenumdata.place(x=50, y=50)

    date = Label(parkfines, text="Date", bg='#f7b7d3')
    date.place(x= 150, y = 0)

    datedata = Label(parkfines, text="test2", bg='#f7b7d3')
    datedata.place(x=150, y=50)

    time = Label(parkfines, text="Time", bg='#f7b7d3')
    time.place(x= 300, y = 0)

    timedata = Label(parkfines, text="test3", bg='#f7b7d3')
    timedata.place(x=300, y=50)

    appnum = Label(parkfines, text="App Num", bg='#f7b7d3')
    appnum.place(x=450, y = 0)

    appdata = Label(parkfines, text="test4", bg='#f7b7d3')
    appdata.place(x=450, y=50)

    regnum = Label(parkfines, text="Vehicle Reg \n Number", bg='#f7b7d3')
    regnum.place(x=550, y= 0)

    regdata = Label(parkfines, text="test5", bg='#f7b7d3')
    regdata.place(x=550, y=50)

    vetype = Label(parkfines, text="Vehicle Type", bg='#f7b7d3')
    vetype.place(x=650, y= 0)

    vedata = Label(parkfines, text="test6", bg='#f7b7d3')
    vedata.place(x=650, y=50)

    details = Label(parkfines, text="Details", bg='#f7b7d3')
    details.place(x=750, y= 0)

    detailsdata = Label(parkfines, text="test7", bg='#f7b7d3')
    detailsdata.place(x=750, y=50)

    loc = Label(parkfines, text="Location", bg='#f7b7d3')
    loc.place(x=850, y=0)

    locdata = Label(parkfines, text="test8", bg='#f7b7d3')
    locdata.place(x=850, y=50)

    valid = Label(parkfines, text="Valid", bg='#f7b7d3')
    valid.place(x=950, y=0)

    validdata = Label(parkfines, text="test9", bg='#f7b7d3')
    validdata.place(x=950, y=50)


    # For user info

    usertitle = Label(parkfines, text="User Info")
    usertitle.place(x=470, y=250)

    uappnum = Label(parkfines, text="Application Number")
    uappnum.place(x=50, y=300)

    uappnumdata = Label(parkfines, text="test1")
    uappnumdata.place(x=50,y=350)

    ufirst = Label(parkfines, text="First name")
    ufirst.place(x=170, y=300)

    ufirstdata = Label(parkfines, text="test2")
    ufirstdata.place(x=170, y=350)

    ulast = Label(parkfines, text="Last Name")
    ulast.place(x=250, y=300)

    ulastdata = Label(parkfines, text="test3")
    ulastdata.place(x=250, y=350)

    udob = Label(parkfines, text="Date of Birth")
    udob.place(x=320, y=300)

    udobdata = Label(parkfines, text= "test4")
    udobdata.place(x=320, y=350)

    uphone = Label(parkfines, text="Phone")
    uphone.place(x=400, y=300)

    uphonedata = Label(parkfines, text="test5")
    uphonedata.place(x=400, y=350)

    udep = Label(parkfines, text="Department")
    udep.place(x=500, y=300)

    udepdata = Label(parkfines, text="test6")
    udepdata.place(x=500, y=350)

    uvisit = Label(parkfines, text= "Are You a \n Visitor?")
    uvisit.place(x=600, y=300)

    uvisitdata = Label(parkfines, text = "test7")
    uvisitdata.place(x=600, y=350)

    uvetype = Label(parkfines, text = "Vehicle Type")
    uvetype.place(x=700, y=300)

    uvetypedata = Label(parkfines, text= "test8")
    uvetypedata.place(x=700, y=350)

    urego = Label(parkfines, text="Vehicle Registration")
    urego.place(x=780, y=300)

    uregodata = Label(parkfines, text="test9")
    uregodata.place(x=780, y=350)

    umake = Label(parkfines, text="Vehicle Make/Model")
    umake.place(x=900, y=300)

    umakedata = Label(parkfines, text="test10")
    umakedata.place(x=900, y=350)

    
    ## The update buttons for refreshing the database display
	
    updatebut = Button(permframe, text="Update", width=29, bg = col, command=  lambda: UpdatePark(finenumdata, datedata, timedata, appdata, regdata, vedata, detailsdata, locdata, validdata))
    updatebut.place(x=800, y=5)

    updatebut2 = Button(appframe, text="Update", width=29, bg = col, command= lambda: UpdateHandS(numlabeldata, loclabeldata, reportlabeldata, desclabeldata, sevlabeldata, risklabeldata, datelabeldata, timelabeldata))
    updatebut2.place(x=800, y=5)

    updatebut3 = Button(appframe, text="Update", width=29, bg = col, command= lambda: UpdateS(snumdata, snamedata, sstudata, sdatedata, stimedata, splacedata))
    updatebut3.place(x=800, y=310)

    updatebut4 = Button(permframe, text="Update", width=29, bg = col, command=lambda: UpdateUser (uappnumdata, ufirstdata, ulastdata, udobdata, uphonedata, udepdata, uvisitdata, uvetypedata, uregodata, umakedata))
    updatebut4.place(x=800, y=600)
	
    ## Entry on the permit page for Parking Fines

    finenum2 = Label(sancframe, text="Fine Num")
    finenum2.place(x=50, y = 20)    

    finenumentry = Entry(sancframe)
    finenumentry.place(x=150, y=20)

    date2 = Label(sancframe, text="Date")
    date2.place(x= 50, y = 60)

    datedataentry = Entry(sancframe)
    datedataentry.place(x=150, y=60)

    time2 = Label(sancframe, text="Time")
    time2.place(x= 50, y = 100)

    timedataentry = Entry(sancframe)
    timedataentry.place(x=150, y=100)

    appnum2 = Label(sancframe, text="App Num")
    appnum2.place(x=50, y = 140)
     
    appdataentry = Entry(sancframe)
    appdataentry.place(x=150, y=140)

    regnum2 = Label(sancframe, text="Vehicle Reg \n Number")
    regnum2.place(x=50, y= 180)

    regdataentry = Entry(sancframe)
    regdataentry.place(x=150, y=180)

    vetype2 = Label(sancframe, text="Vehicle Type")
    vetype2.place(x=50, y= 220)

    vedataentry = Entry(sancframe)
    vedataentry.place(x=150, y=220)

    details2 = Label(sancframe, text="Details")
    details2.place(x=50, y= 260)

    detailsdataentry = Entry(sancframe)
    detailsdataentry.place(x=150, y=260)

    loc2 = Label(sancframe, text="Location")
    loc2.place(x=50, y=300)

    locdataentry = Entry(sancframe)
    locdataentry.place(x=150, y=300)

    valid2 = Label(sancframe, text="Valid")
    valid2.place(x=50, y=340)

    validdataentry = Entry(sancframe)
    validdataentry.place(x=150, y=340)

	
    ## The enter data and update buttons
	
    enterdatabut = Button(sancframe, text="Enter Data", width=30, bg=col, command =lambda: EnterDataPark(finenumentry, datedataentry, timedataentry, appdataentry, regdataentry, vedataentry, detailsdataentry, locdataentry, validdataentry ))
    enterdatabut.place(x=50,y=380)

    updatebut = Button(sancframe, text="Update", width=30, bg=col, command =lambda: UpdatePark(finenumentry, datedataentry, timedataentry, appdataentry, regdataentry, vedataentry, detailsdataentry, locdataentry, validdataentry ))
    updatebut.place(x=50,y=410)

    # The button and labels for the editing feature

    editbut = Button(sancframe, text="Edit", width=30, bg=col, command= lambda: Edit(editentry))
    editbut.place(x=450,y= 500)

    editentry = Entry(sancframe, width=150)
    editentry.place(x=50, y = 450)


    ## Labels and entry boxes for H&S

    num = Label(sancframe, text="Offence Number")
    num.place(x=350, y=20)

    numentry = Entry(sancframe)
    numentry.place(x=500, y=20)

    location = Label(sancframe, text="Location of Issue")
    location.place(x=350, y=60)

    locationentry = Entry(sancframe)
    locationentry.place(x=500, y=60)

    report = Label(sancframe, text="Reportee")
    report.place(x=350, y=100)

    reportentry = Entry(sancframe)
    reportentry.place(x=500, y=100)

    desc  = Label(sancframe, text="Description")
    desc.place(x=350, y=140)

    descentry = Entry(sancframe)
    descentry.place(x=500, y=140)

    sev = Label(sancframe, text="Severity of Offense")
    sev.place(x=350, y=180)

    seventry = Entry(sancframe)
    seventry.place(x=500, y=180)

    risk = Label(sancframe, text="Risk Status")
    risk.place(x=350, y=220)

    riskentry = Entry(sancframe)
    riskentry.place(x=500, y=220)

    date3 = Label(sancframe, text="Date")
    date3.place(x=350, y=260)

    date3entry = Entry(sancframe)
    date3entry.place(x=500, y=260)

    time3 = Label(sancframe, text="Time")
    time3.place(x=350, y=300)

    time3entry = Entry(sancframe)
    time3entry.place(x=500, y=300)

    enterdatabut3 = Button(sancframe, text="Enter Data", width=30, bg=col, command= lambda:EnterDataHS(numentry, locationentry, reportentry, descentry, seventry, riskentry, date3entry, time3entry))
    enterdatabut3.place(x=400,y=340)
            
    ## Labels and entry boxes for smoking violations

    num2 = Label(sancframe, text="Fine Number")
    num2.place(x=700, y=20)

    num2entry = Entry(sancframe)
    num2entry.place(x=850, y=20)

    name2 = Label(sancframe, text="Full Name")
    name2.place(x=700, y=60)

    name2entry = Entry(sancframe)
    name2entry.place(x=850, y=60)

    stunum = Label(sancframe, text="Staff / Student ID")
    stunum.place(x=700, y=100)

    stunumentry = Entry(sancframe)
    stunumentry.place(x=850,y=100)

    date4 = Label(sancframe, text="Date")
    date4.place(x=700, y=140)

    date4entry = Entry(sancframe)
    date4entry.place(x=850, y=140)

    time4 = Label(sancframe, text="Time")
    time4.place(x=700, y=180)

    time4entry = Entry(sancframe)
    time4entry.place(x=850, y=180)

    place2 = Label(sancframe, text="Place")
    place2.place(x=700, y=220)

    place2entry = Entry(sancframe)
    place2entry.place(x=850,y=220)
    
    # The enter data button
    enterdatabut4 = Button(sancframe, text="Enter Data", width=30, bg=col, command = lambda:EnterDataS(num2entry, name2entry, stunumentry, date4entry, time4entry, place2entry))
    enterdatabut4.place(x=750,y=270)
	
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

# Create the 'H&S' table
cursor.executescript('''DROP TABLE IF EXISTS `Health & Safety Violations`;

CREATE TABLE `Health & Safety Violations` (
  `Number` VARCHAR(255), 
  `Location of issue` VARCHAR(255), 
  `Reportee` VARCHAR(255), 
  `Decription of Issue` VARCHAR(255), 
  `Severity` VARCHAR(255), 
  `Risk Status` VARCHAR(255), 
  `Date` VARCHAR(255), 
  `Time` VARCHAR(255) 
  
);
''')


# Create the 'Smoking Violations' table

cursor.executescript('''DROP TABLE IF EXISTS `Smoking Violations`;

CREATE TABLE `Smoking Violations` (
  `Fine Number` INTEGER, 
  `Full Name` VARCHAR(255), 
  `Staff or Student Number` VARCHAR(255), 
  `Date` INTEGER DEFAULT 0, 
  `Time` VARCHAR(255), 
  `Place` VARCHAR(255)
   
  
);
''')

# Create the 'Parking Fines' table
cursor.executescript('''DROP TABLE IF EXISTS `Parking Fines`;

CREATE TABLE `Parking Fines` (
  `Fine Number` INTEGER, 
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
  `Application / Permit Number` INTEGER, 
  `First Name` VARCHAR(255), 
  `Last Name` VARCHAR(255), 
  `Date of Birth` VARCHAR(255),       
  `Phone` VARCHAR(255),   
  `Department/Faculty` VARCHAR(255), 
  `Are you Applying for a visitor?` VARCHAR(255),         
  `Vehicle Type` VARCHAR(255), 
  `Vehicle Registration Number` VARCHAR(255),
  `Vehicle Make and Model` VARCHAR(255)
  
)



''')

# Create an index seperately (sqlite3 doesnt allow you to do it in the table creation)


# Fill in User Info with dummy/sample data

##cursor.executescript('''
##
##INSERT INTO `User Info` (`Application / Permit Number`, `Staff or Student ID`, `Title`, `First Name`, `Last Name`, `Date of Birth`, `Home Phone`, `Work Phone`, `Mobile Phone`, `Email Address`, `Department/Faculty`, `Are you Applying for a visitor?`, `Visitor First Name`, `Visitor Last Name`, `Reson for Visit`, `Vehicle Type`, `Vehicle Registration Number`, `Vehicle Make and Model`) VALUES (1, 7839281, 'Mr', 'John', 'Smith', '1960-03-10 00:00:00', 0, 38792019, 473829102, 'John.Smith@gmail.com', 'SEF', 0, NULL, NULL, NULL, 'Small Car', 'VHG 785', 'Toyota Yaris');
##INSERT INTO `User Info` (`Application / Permit Number`, `Staff or Student ID`, `Title`, `First Name`, `Last Name`, `Date of Birth`, `Home Phone`, `Work Phone`, `Mobile Phone`, `Email Address`, `Department/Faculty`, `Are you Applying for a visitor?`, `Visitor First Name`, `Visitor Last Name`, `Reson for Visit`, `Vehicle Type`, `Vehicle Registration Number`, `Vehicle Make and Model`) VALUES (2, 9876989, 'Ms', 'Anna', 'Jones', '1987-08-07 00:00:00', 0, 0, 478219989, 'Anna.Jones7@hotmail.com', 'Law', 0, NULL, NULL, NULL, 'Small Car', 'AMJ 708', 'Mazda 2');
##INSERT INTO `User Info` (`Application / Permit Number`, `Staff or Student ID`, `Title`, `First Name`, `Last Name`, `Date of Birth`, `Home Phone`, `Work Phone`, `Mobile Phone`, `Email Address`, `Department/Faculty`, `Are you Applying for a visitor?`, `Visitor First Name`, `Visitor Last Name`, `Reson for Visit`, `Vehicle Type`, `Vehicle Registration Number`, `Vehicle Make and Model`) VALUES (3, 24350, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL);
##INSERT INTO `User Info` (`Application / Permit Number`, `Staff or Student ID`, `Title`, `First Name`, `Last Name`, `Date of Birth`, `Home Phone`, `Work Phone`, `Mobile Phone`, `Email Address`, `Department/Faculty`, `Are you Applying for a visitor?`, `Visitor First Name`, `Visitor Last Name`, `Reson for Visit`, `Vehicle Type`, `Vehicle Registration Number`, `Vehicle Make and Model`) VALUES (4, 2340, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL);
##INSERT INTO `User Info` (`Application / Permit Number`, `Staff or Student ID`, `Title`, `First Name`, `Last Name`, `Date of Birth`, `Home Phone`, `Work Phone`, `Mobile Phone`, `Email Address`, `Department/Faculty`, `Are you Applying for a visitor?`, `Visitor First Name`, `Visitor Last Name`, `Reson for Visit`, `Vehicle Type`, `Vehicle Registration Number`, `Vehicle Make and Model`) VALUES (5, 23450, NULL, NULL, NULL, NULL, 0, 0, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL);
##
##''')


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

Blake Mills #### 21/09/2016 #### IFB299

## Instructions On Installing, and on Operation of the Program ##

Installing:

The program runs on python 3.5.2. Python 3.x is required as minimum, the program may work on versions other than 3.5.2, but is untested and may encounter errors.

The program requires sqlite3 and tkinter, these plugins should be installed in python 3.x as default

The program also requires the PIL fork pillow, which is not installed by default.

To install pillow, open the windows command prompt and type "easy_install pillow".

This will install pillow and all its dependencies. The program should now work.



Operation:

To start the program, load and run "Mainfile.py".

Operation of the program is fairly simple, to display data from the database, click the "Permits" button, at first, only test data will be displayed.

To fetch and display data from the database, click the "Update" button. The test data labels should now change to the correct text.

To enter data into the database, click the "Applications" button. Here you can enter in your desired entries into the text boxes at the top.

Once you have entered your desired data, hit the "Enter Data" button. The data will now be stored in the database.

The data you have entered can be viewed by going back to the "Permits" tab and hitting the update button.


Potential Errors: 

errors like "cannot import imagingtk/image" etc result from a bad install of the pillow imaging library, try reinstalling.

The error: "sqlite3.IntegrityError: UNIQUE constraint failed: Parking Fines.Fine Number" Occurs when you have attempted to enter a "Fine Number" that already exists in the 
database. To fix this, simply change the Fine Number you are trying to enter and submit again.


# import all methods and classes from the tkinter
from tkinter import *
from tkcalendar import Calendar

import mysql.connector
from datetime import date
import time
import requests
from plyer import notification

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Butterfly123",
    database="caldb"
)

mycursor = mydb.cursor()

# sqlFormula = "INSERT INTO dates (type, year, message) VALUES (%s, %s, %s)"

# sqlFormula = "CREATE TABLE events (type VARCHAR(255), day INTEGER(2), month INTEGER(2), year INTEGER(4), " \
#              "message VARCHAR(255))"
# dates = [("birthday", 2022, "Ivan's birthday"),
# ("assignment", 2022, "cs341"),
# ("assignment", 2022, "cs348"),
# ("birthday", 2022, "mom's birthday")]

# mycursor.execute(sqlFormula)
# mydb.commit()


def addEvent():
    my_label = Label(gui, text="New event!!")
    my_label.pack()


def openEventWindow():
    new_window = Toplevel(gui)
    new_window.title("Enter event information")
    new_window.geometry("200x200")
    Label(new_window,
          text="Give the details of your event", bg="#C1FFC1").pack()


def extractDate(self):
    Label(gui, text=cal.get_date(), fg="#68838B").pack()


# Driver Code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window
    gui.config(background="white")

    # set the name of tkinter GUI window
    gui.title("CALENDAR")

    # Set the configuration of GUI window
    gui.geometry("700x700")

    today = date.today()
    year = int(today.strftime("%Y"))
    month = int(today.strftime("%m"))
    day = int(today.strftime("%d"))
    cal = Calendar(gui, selectmode='day',
                   year=year, month=month,
                   day=day)
    cal.pack(pady=20, fill="both", expand=True)

    cal.bind("<<CalendarSelected>>", extractDate)

    Button(gui, text="Add Event",
           command=openEventWindow).pack(pady=20)

    gui.mainloop()

    while True:
        notification.notify(
            title="here is a reminder! It has been 5 minutes",
            timeout=10
        )
        time.sleep(300)

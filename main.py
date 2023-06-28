# import all methods and classes from the tkinter
from tkinter import *
from tkcalendar import Calendar

import mysql.connector
from datetime import date
import time
import requests
from plyer import notification
import pyobjus

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="caldb"
)

mycursor = mydb.cursor()


# sqlFormula = "INSERT INTO dates (type, year, message) VALUES (%s, %s, %s)"

# sqlFormula = "CREATE TABLE events (type VARCHAR(255), day INTEGER(2), month INTEGER(2), year INTEGER(4), " \
#              "message VARCHAR(255))"
# sqlFormula = "ALTER TABLE events DROP COLUMN message"
# dates = [("birthday", 2022, "Ivan's birthday"),
# ("assignment", 2022, "cs341"),
# ("assignment", 2022, "cs348"),
# ("birthday", 2022, "mom's birthday")]

# mycursor.execute(sqlFormula)
# mydb.commit()


# Save the event to the db
def storeEvent(event_type, selected_date):
    inp = event_type.get()
    tokens = selected_date.split(sep='-')
    print(tokens)
    new_event = (inp, tokens[2], tokens[1], tokens[0])
    # sql_formula = "INSERT INTO events (type, day, month, year) VALUES(%s, %s, %s, %s)"
    # mycursor.execute(sql_formula, new_event)
    # mydb.commit()


# Open a new window and get information about the event
def openEventWindow(calendar, selected):
    new_window = Toplevel(gui)
    new_window.title("Enter event information")
    new_window.geometry("300x300")
    Label(new_window,
          text="Give the details of your event").pack()

    Label(new_window,
          text="What type of event are you entering").pack()
    label = Label(new_window, text="")
    label.pack()

    event_type = StringVar()

    entry = Entry(new_window, textvariable=event_type, width=50)
    entry.focus_set()
    entry.pack()

    # selected_date = calendar.bind("<<CalendarSelected>>", extractDate)

    Button(new_window,
           text="Save",
           command=lambda: storeEvent(event_type, selected)).pack(pady=20)


def extractDate(self):
    print(cal.get_date())
    # return cal.get_date()


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

    selected = cal.bind("<<CalendarSelected>>", extractDate)

    print(selected)
    Button(gui, text="Add Event",
           command=lambda: openEventWindow(cal, selected)).pack(pady=20)

    # notification test
    notification.notify(
        title="It's been an hour!! Switch to a new task",
        timeout=10
    )
    gui.mainloop()
    time.sleep(3600)



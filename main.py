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

# Run this line once to set up the Table
# sqlFormula = "CREATE TABLE events (type VARCHAR(255), day INTEGER(2), month INTEGER(2), year INTEGER(4), " \
#              "message VARCHAR(255))"
# dates = [("birthday", 2022, "Ivan's birthday"),
# ("assignment", 2022, "cs341"),
# ("assignment", 2022, "cs348"),
# ("birthday", 2022, "mom's birthday")]


# mycursor.execute(sqlFormula)
# mydb.commit()


# Save the event to the db
def storeEvent(event_type, selected_date):
    inp = event_type.get()
    print("event_type: " + inp + '\n')
    tokens = selected_date.get().split(sep='-')
    print(tokens)
    new_event = (inp, tokens[2], tokens[1], tokens[0])
    sql_formula = "INSERT INTO events (type, day, month, year) VALUES(%s, %s, %s, %s)"
    mycursor.execute(sql_formula, new_event)
    mydb.commit()


# Open a new window and get information about the event
def openEventWindow(calendar, selected):
    new_window = Toplevel(gui)
    new_window.title("Enter event information")
    new_window.geometry("300x300")

    Label(new_window,
          text="What type of event are you adding").pack()
    label = Label(new_window, text="")
    label.pack()

    event_type = StringVar()
    date_entry = StringVar()

    entry1 = Entry(new_window, textvariable=event_type)
    entry1.focus_set()
    entry1.pack()

    Label(new_window,
          text="choose a date for this new event").pack()
    label = Label(new_window, text="")
    label.pack()
    entry2 = Entry(new_window, textvariable=date_entry)
    entry2.focus_set()
    entry2.pack()
    # selected_date = calendar.bind("<<CalendarSelected>>", extractDate)

    Button(new_window,
           text="Save",
           command=lambda: storeEvent(event_type, date_entry)).pack(pady=20)


def extractDate(self):
    print("here " + cal.get_date() + '\n')
    return cal.get_date()


# Driver Code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window
    gui.config(background="light blue")

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

    selectedDate = extractDate(cal)

    cal.pack(pady=20, fill="both", expand=True)

    print("selected: " + selectedDate + '\n')
    Button(gui, text="Add Event",
           command=lambda: openEventWindow(cal, selectedDate)).pack(pady=20)

    # notification test
    notification.notify(
        title="It's been an hour!! Switch to a new task",
        timeout=10
    )
    gui.mainloop()
    time.sleep(3600)

import sys 
import datetime,time
import sqlite3
from Notification import Birthday_Today_Notification, Three_Days_Notification

#------------------------------------------Variables-----------------
CurrentDate = datetime.datetime.today().date()
CurrentYear = CurrentDate.year
CurrentTime = datetime.datetime.now().strftime("%H:%M:%S")
days_in_year = 365.2425

Database = sqlite3.connect("Birthdays.db")
Cursor = Database.cursor()

Top_Frame_Color = "#E2C391"
Main_Background_Color = "#A8B7AB"
Calendar_Color = "#E4C99C" #also #C7CB85
#-------------------------------------------------------------------


def GenerateDate():
    Formatted = ""
    if CurrentDate.month in (1, 21, 31):
        Formatted = "st"
    if CurrentDate.month in (2,22):
        Formatted = "nd"
    if CurrentDate.month in (3, 23):
        Formatted = "rd"
    else:
        Formatted = "th"
    return CurrentDate.strftime(f"%A, %B %d{Formatted} %Y")



#Create Birthday Database
try:
    Database.execute("""CREATE TABLE IF NOT EXISTS Birthdays (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        First_Name TEXT NOT NULL,
        Last_Name TEXT NOT NULL,
        Birthdate TEXT NOT NULL,
        Age INTEGER NOT NULL,
        DaysUntilBirthday REAL NOT NULL);""")
    Database.commit()
except Exception as e:
    print(f"Error occured when creating Birthdays Database : {e}")



# #Update the Database based on the date to give accurate information

def DBUpdate():
    try:
        AllDays = Cursor.execute("SELECT id, Birthdate, DaysUntilBirthday From Birthdays")
        Result = Cursor.fetchall()
        for row in Result:
            SBirthdate = row[1]
            Birthdate = datetime.datetime.strptime(SBirthdate, "%Y-%m-%d").date()
            CurrentBDay = datetime.date(CurrentYear, Birthdate.month, Birthdate.day)
            Timedelta = datetime.date(CurrentYear, Birthdate.month, Birthdate.day) - CurrentDate
            NumDaysUntilBirthdays = Timedelta.total_seconds() / 60 /60 /24
            if NumDaysUntilBirthdays < 0 :
                NumDaysUntilBirthdays = 365 + NumDaysUntilBirthdays 
            Cursor.execute("UPDATE Birthdays SET DaysUntilBirthday = :NumDaysUntilBirthdays WHERE id = :id",    {"NumDaysUntilBirthdays":NumDaysUntilBirthdays, "id": row[0]})
    except Exception as e:
        print(f"Error occured when Updating the Database: {e}")
    



def Three_Days_Before():
    try:
        Cursor.execute("SELECT * FROM Birthdays WHERE DaysUntilBirthday = 3.0")
        Results = Cursor.fetchall()
        for row in Results:
            Three_Days_Notification(row[1], row[2], row[4] + 1, row[3])
    except Exception as e:
        print(f"Error creating notification : {e}")

def Birthday_Today():
    try:
        Cursor.execute("SELECT * FROM Birthdays WHERE DaysUntilBirthday = 0.0")
        Results = Cursor.fetchall()
        for row in Results:
            Birthday_Today_Notification(row[1], row[2], row[4] + 1)
    except Exception as e:
        print(f"Error creating notification : {e}")



def ReturnAll():
    try:
        values = Cursor.execute("SELECT ID, First_Name, Last_Name, Birthdate, Age, DaysUntilBirthday FROM Birthdays")
        for row in values:
            print(f"ID : {row[0]}")
            print(f"First Name : {row[1]}")
            print(f"Last Name : {row[2]}")
            print(f"Birthdate : {row[3]}")
            print(f"Current Age : {row[4]}")
            print(f"Days Until Birthday : {row[5]}\n")
    except Exception as e:
        print(f"Error raised when returning all values of Database: {e}")



def CalculateDaysUntilBirthday(Birthdate):
    CurrentBDay = datetime.date(CurrentYear, Birthdate.month, Birthdate.day)
    Timedelta = (datetime.date(int(CurrentYear), int(Birthdate.month), int(Birthdate.day)) - datetime.datetime.today().date())
    NumDaysUntilBirthdays = Timedelta.total_seconds() / 60 /60 /24
    if NumDaysUntilBirthdays == 0.0:
        NumDaysUntilBirthdays = 0
    elif NumDaysUntilBirthdays < 1.0:
        NumDaysUntilBirthdays = 365 + NumDaysUntilBirthdays
    return NumDaysUntilBirthdays
    

def CalculateAge(Birthdate):
    UserBday = datetime.date(int(Birthdate.year), int(Birthdate.month), int(Birthdate.day))
    CurrentAge = int((CurrentDate - UserBday).days / days_in_year)
    return CurrentAge


def Add_New_Birthday(First, Last, Birthdate):
    Age = CalculateAge(Birthdate)   
    DaysUntilBirthday = CalculateDaysUntilBirthday(Birthdate)
    try:
        Database.execute("INSERT INTO BIRTHDAYS (First_Name, Last_Name, Birthdate, Age, DaysUntilBirthday) VALUES (:First, :Last, :Birthdate, :Age, :DaysUntilBirthday)", {"First": First, "Last": Last, "Birthdate": Birthdate, "Age": Age, "DaysUntilBirthday":DaysUntilBirthday})
        print(f"{First} {Last}. Birthday : {Birthdate}. Age : {Age}. Days until Birthday : {DaysUntilBirthday}")
        Database.commit()
    except Exception as e:
        print(f"Error When Adding User to DB : {e}")



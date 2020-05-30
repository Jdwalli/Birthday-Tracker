from notifypy import Notify
import datetime



def Birthday_Today_Notification(First, Last, Age):
    notification = Notify()
    notification.title = f"{First} {Last}'s Birthday!!!"
    notification.message = f"{First} is turning {Age} today! Make sure to wish them a happy birthday!"
    notification.icon = "Images\BirthdayCakeIcon.png"
    notification.application_name = "Birthday Tracker"
    notification.audio = r"Images\NotificationSound.wav"
    notification.send()

def Three_Days_Notification(First, Last, Age, Birthday):
    Birthday = datetime.datetime.strptime(Birthday, "%Y-%m-%d")
    Day = Birthday.day
    Formatted = "th"
    if Day == 1 or Day == 21 or Day == 31:
        Formatted = "st"
    if Day == 2 or Day == 22:
        Formatted = "nd"
    if Day == 3 or Day == 23:
        Formatted = "rd"
    Birthday = Birthday.strftime(f"%B {Day}{Formatted}!")
    notification = Notify()
    notification.title = f"{First} {Last}'s Birthday is in 3 days!"
    notification.message = f"{First} turns {Age} years old on {Birthday}!"
    notification.icon = "Images\BirthdayCakeIcon.png"
    notification.application_name = "Birthday Tracker"
    notification.audio = r"Images\NotificationSound.wav"
    notification.send()







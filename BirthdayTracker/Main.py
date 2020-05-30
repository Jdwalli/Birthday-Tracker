from PyQt5 import QtCore, QtGui, QtWidgets
from Database import *
import datetime


class Ui_Birthday_Tracker(object):
    def Update_Home_Page(self):
        try:
            values = Cursor.execute("Select * FROM Birthdays")
        except Exception as e:
            print(f"Error occured : {e}")
        Length_Of_DB = values.fetchall()
        if Length_Of_DB != 0:
            try: 
                self.scrollArea = QtWidgets.QScrollArea(self.Page_Home)
                self.scrollArea.setGeometry(QtCore.QRect(43, 64, 971, 681))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
                self.scrollArea.setSizePolicy(sizePolicy)
                self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
                self.scrollArea.setLineWidth(3)
                self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
                self.scrollArea.setWidgetResizable(True)
                self.scrollArea.setObjectName("scrollArea")
                self.scrollAreaWidgetContents = QtWidgets.QWidget()
                self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 971, 681))
                self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
                self.verticalLayout.setObjectName("verticalLayout")
                values = Cursor.execute("SELECT * FROM Birthdays ORDER BY DaysUntilBirthday ASC")

                y = 3
                for row in values:
                    Birthday = datetime.datetime.strptime(row[3], "%Y-%m-%d")
                    Day = Birthday.day
                    Formatted = "th"
                    if Day == 1 or Day == 21 or Day == 31:
                        Formatted = "st"
                    if Day == 2 or Day == 22:
                        Formatted = "nd"
                    if Day == 3 or Day == 23:
                        Formatted = "rd"
                    Birthday = Birthday.strftime(f"%B {Day}{Formatted}!")
                    Day_Until = int(row[5])


                    self.BirthdayFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
                    # self.BirthdayFrame.setGeometry(QtCore.QRect(10, y, 951, 71))
                    self.BirthdayFrame.setFrameShape(QtWidgets.QFrame.Box)
                    self.BirthdayFrame.setFrameShadow(QtWidgets.QFrame.Plain)
                    self.BirthdayFrame.setMinimumSize(QtCore.QSize(951, 71))
                    self.BirthdayFrame.setMaximumSize(QtCore.QSize(951, 71))
                    self.BirthdayFrame.setLineWidth(3)
                    self.BirthdayFrame.setMidLineWidth(2)
                    self.BirthdayFrame.setObjectName("BirthdayFrame")
                    self.Cake_Picture = QtWidgets.QLabel(self.BirthdayFrame)
                    self.Cake_Picture.setGeometry(QtCore.QRect(10, 3, 91, 65))
                    self.Cake_Picture.setFrameShape(QtWidgets.QFrame.NoFrame)
                    self.Cake_Picture.setText("")
                    self.Cake_Picture.setPixmap(QtGui.QPixmap("Images/BirthdayCakeIcon.png"))
                    self.Cake_Picture.setScaledContents(True)
                    self.Cake_Picture.setObjectName("Cake_Picture")
                    self.First_and_Last_Name = QtWidgets.QLabel(self.BirthdayFrame)
                    self.First_and_Last_Name.setGeometry(QtCore.QRect(120, 4, 521, 31))
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift SemiBold")
                    font.setPointSize(14)
                    font.setBold(False)
                    font.setItalic(False)
                    font.setWeight(50)
                    self.First_and_Last_Name.setFont(font)
                    self.First_and_Last_Name.setFrameShape(QtWidgets.QFrame.NoFrame)
                    self.First_and_Last_Name.setFrameShadow(QtWidgets.QFrame.Plain)
                    self.First_and_Last_Name.setText(f"{row[1]} {row[2]}")
                    self.First_and_Last_Name.setAlignment(QtCore.Qt.AlignCenter)
                    self.First_and_Last_Name.setObjectName("First_and_Last_Name")
                    self.Turns_Age_On_Date = QtWidgets.QLabel(self.BirthdayFrame)
                    self.Turns_Age_On_Date.setGeometry(QtCore.QRect(120, 37, 521, 31))
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift SemiBold")
                    font.setPointSize(14)
                    font.setBold(False)
                    font.setItalic(False)
                    font.setWeight(50)
                    self.Turns_Age_On_Date.setFont(font)
                    self.Turns_Age_On_Date.setFrameShape(QtWidgets.QFrame.NoFrame)
                    self.Turns_Age_On_Date.setFrameShadow(QtWidgets.QFrame.Plain)
                    self.Turns_Age_On_Date.setText(f"Turns {row[4] + 1} on {Birthday} ")
                    self.Turns_Age_On_Date.setAlignment(QtCore.Qt.AlignCenter)
                    self.Turns_Age_On_Date.setObjectName("Turns_Age_On_Date")
                    self.Number_of_Days = QtWidgets.QLabel(self.BirthdayFrame)
                    self.Number_of_Days.setGeometry(QtCore.QRect(840, 3, 61, 31))
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift SemiBold")
                    font.setPointSize(14)
                    font.setBold(False)
                    font.setItalic(False)
                    font.setWeight(50)
                    self.Number_of_Days.setFont(font)
                    self.Number_of_Days.setFrameShape(QtWidgets.QFrame.NoFrame)
                    self.Number_of_Days.setFrameShadow(QtWidgets.QFrame.Plain)
                    self.Number_of_Days.setAlignment(QtCore.Qt.AlignCenter)
                    self.Number_of_Days.setObjectName("Number_of_Days")
                    self.Day_or_Days = QtWidgets.QLabel(self.BirthdayFrame)
                    self.Day_or_Days.setGeometry(QtCore.QRect(820, 36, 101, 31))
                    font = QtGui.QFont()
                    font.setFamily("Bahnschrift SemiBold")
                    font.setPointSize(14)
                    font.setBold(False)
                    font.setItalic(False)
                    font.setWeight(50)
                    self.Day_or_Days.setFont(font)
                    self.Day_or_Days.setFrameShape(QtWidgets.QFrame.NoFrame)
                    self.Day_or_Days.setFrameShadow(QtWidgets.QFrame.Plain)
                    self.Day_or_Days.setAlignment(QtCore.Qt.AlignCenter)
                    self.Day_or_Days.setObjectName("Day_or_Days")
                    if Day_Until == 1:
                        print("Equal to one")
                        self.Day_or_Days.setText("Day")
                        self.Number_of_Days.setText(f"{int(row[5])}")
                    if Day_Until == 0:
                        self.Day_or_Days.setText("TODAY")
                        self.Day_or_Days.setGeometry(QtCore.QRect(820, 20, 101, 31))
                        self.Number_of_Days.setText("")
                    if Day_Until != 0 and Day_Until != 1:
                        self.Day_or_Days.setText("Days")
                        self.Number_of_Days.setText(f"{int(row[5])}")
                    self.verticalLayout.addWidget(self.BirthdayFrame)
                    y += 80
            except Exception as e:
                print(f"Error raised when returning all values of Database and making birthday build: {e}")

    def Check_Length(self):
        self.No_Entries_Label = QtWidgets.QLabel(self.Page_Home)
        self.No_Entries_Label.setGeometry(QtCore.QRect(0, 200, 1061, 101))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.No_Entries_Label.setFont(font)
        self.No_Entries_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.No_Entries_Label.setObjectName("No_Entries_Label")
        try:
            values = Cursor.execute("Select * FROM Birthdays")
            values = values.fetchall()
            if len(values) == 0:
                self.No_Entries_Label.setText("Add a person to get started!")
                self.No_Entries_Label.show() #Should already be showing but....
            if len(values) > 0:
                self.No_Entries_Label.setText("Add a person to get started!")
                self.No_Entries_Label.hide()
        except Exception as e:
            print(f"Error when getting length data from DB : {e}")
    
    def Update_Birthday(self):
        Day = self.Calendar.selectedDate().toPyDate().day
        Formatted = "th"
        if Day == 1 or Day == 21 or Day == 31:
            Formatted = "st"
        if Day == 2 or Day == 22:
            Formatted = "nd"
        if Day == 3 or Day == 23:
            Formatted = "rd"
        Birthday = self.Calendar.selectedDate().toPyDate().strftime(f"%B {Day}{Formatted} %Y")
        self.Birthday_Information.setText(f"Birthday : {Birthday}")
    def To_Add_User_Page(self):
        self.stackedWidget.setCurrentIndex(1)

    def To_Home_Page(self):
        self.Check_Length()
        self.Update_Home_Page()
        self.stackedWidget.setCurrentIndex(0)

    def Submit_New_Person(self):
        Clear = False
        Submit = False

        First_Name = self.First_Name_Input
        Last_Name = self.Last_Name_Input
        Orginal_Birthday = self.Calendar.selectedDate().toPyDate()
        Formatted_Birthday = Orginal_Birthday.strftime("%B %d %Y")
        self.Birthday_Information.setText(f"Birthday : {Formatted_Birthday}")

        if First_Name.text() == "":
            Submit = False
            First_Name.setStyleSheet("border-style: solid; border-color: red; border-width: 3px;")
        else:
            First_Name.setStyleSheet("border-style: solid; border-color: green; border-width: 3px;")
        
        if Last_Name.text() == "":
            Submit = False
            self.Last_Name_Input.setStyleSheet("border-style: solid; border-color: red; border-width: 3px;")
        else:
            Last_Name.setStyleSheet("border-style: solid; border-color: green; border-width: 3px;")
        
        if First_Name.text() != "" and Last_Name.text() != "":
            Submit = True
            First_Name.setStyleSheet("border-style: solid; border-color: green; border-width: 3px;")
            Last_Name.setStyleSheet("border-style: solid; border-color: green; border-width: 3px;")
            self.Submit_Button.setStyleSheet("border-style: solid; border-color: green; border-width: 3px;")
            self.Birthday_Information.setStyleSheet("border-style: solid; border-color: green; border-width: 3px;")

            Add_New_Birthday(First_Name.text(), Last_Name.text(), Orginal_Birthday)
            Clear = True
            
        
        if Clear == True:
            time.sleep(2)
            First_Name.setText("")
            Last_Name.setText("")
            self.Birthday_Information.setText("Birthday : ")
            self.Birthday_Information.setStyleSheet("border-color: black;")
            First_Name.setStyleSheet("border-color: black;")
            Last_Name.setStyleSheet("border-color: black;")
            self.Submit_Button.setStyleSheet("border-color: black;")
            self.Submit_Button.setStyleSheet(f"background-color: {Calendar_Color};")
            self.First_Name_Input.setStyleSheet(f"background-color: {Calendar_Color};")
            self.Last_Name_Input.setStyleSheet(f"background-color: {Calendar_Color};")
            self.Birthday_Information.setStyleSheet(f"background-color: {Calendar_Color};")
            

    def setupUi(self, Birthday_Tracker):
        Birthday_Tracker.setObjectName("Birthday_Tracker")
        Birthday_Tracker.resize(1080, 751)
        Birthday_Tracker.setMaximumHeight(751)
        Birthday_Tracker.setMaximumWidth(1080)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/BirthdayCakeIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Birthday_Tracker.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Birthday_Tracker)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 100, 1060, 581))
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setLineWidth(3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Page_Home = QtWidgets.QWidget()
        self.Page_Home.setObjectName("Page_Home")
        self.Birthdays_Label = QtWidgets.QLabel(self.Page_Home)
        self.Birthdays_Label.setGeometry(QtCore.QRect(0, 5, 1060, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.Birthdays_Label.setFont(font)
        self.Birthdays_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Birthdays_Label.setObjectName("Birthdays_Label")
        self.stackedWidget.addWidget(self.Page_Home)
        self.Page_New_User = QtWidgets.QWidget()
        self.Page_New_User.setObjectName("Page_New_User")
        self.Calendar = QtWidgets.QCalendarWidget(self.Page_New_User)
        self.Calendar.setGeometry(QtCore.QRect(190, 10, 691, 261))
        self.Calendar.setAutoFillBackground(False)
        self.Calendar.setStyleSheet("")
        self.Calendar.setMinimumDate(QtCore.QDate(1890, 9, 14))
        self.Calendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.Calendar.setGridVisible(False)
        self.Calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.Calendar.setNavigationBarVisible(True)
        self.Calendar.setObjectName("Calendar")
        self.First_Name_Input = QtWidgets.QLineEdit(self.Page_New_User)
        self.First_Name_Input.setGeometry(QtCore.QRect(190, 300, 290, 55))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(13)
        self.First_Name_Input.setFont(font)
        self.First_Name_Input.setText("")
        self.First_Name_Input.setAlignment(QtCore.Qt.AlignCenter)
        self.First_Name_Input.setObjectName("First_Name_Input")
        self.Last_Name_Input = QtWidgets.QLineEdit(self.Page_New_User)
        self.Last_Name_Input.setGeometry(QtCore.QRect(580, 300, 290, 55))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(13)
        self.Last_Name_Input.setFont(font)
        self.Last_Name_Input.setText("")
        self.Last_Name_Input.setAlignment(QtCore.Qt.AlignCenter)
        self.Last_Name_Input.setObjectName("Last_Name_Input")
        self.Birthday_Information = QtWidgets.QLineEdit(self.Page_New_User)
        self.Birthday_Information.setGeometry(QtCore.QRect(400, 385, 290, 55))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(13)
        self.Birthday_Information.setFont(font)
        self.Birthday_Information.setText("")
        self.Birthday_Information.setAlignment(QtCore.Qt.AlignCenter)
        self.Birthday_Information.setReadOnly(True)
        self.Birthday_Information.setObjectName("Birthday_Information")
        self.Submit_Button = QtWidgets.QPushButton(self.Page_New_User)
        self.Submit_Button.setGeometry(QtCore.QRect(410, 480, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Submit_Button.setFont(font)
        self.Submit_Button.setObjectName("Submit_Button")
        self.stackedWidget.addWidget(self.Page_New_User)
        self.Top_Frame = QtWidgets.QFrame(self.centralwidget)
        self.Top_Frame.setGeometry(QtCore.QRect(0, 0, 1080, 85))
        self.Top_Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Top_Frame.setLineWidth(0)
        self.Top_Frame.setObjectName("Top_Frame")
        self.Home_Button = QtWidgets.QPushButton(self.Top_Frame)
        self.Home_Button.setGeometry(QtCore.QRect(10, 5, 93, 71))
        self.Home_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/HomeIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home_Button.setIcon(icon1)
        self.Home_Button.setIconSize(QtCore.QSize(100, 70))
        self.Home_Button.setObjectName("Home_Button")
        self.Home_Button.setFlat(True)
        self.NewPerson_Button = QtWidgets.QPushButton(self.Top_Frame)
        self.NewPerson_Button.setGeometry(QtCore.QRect(950, 5, 93, 71))
        self.NewPerson_Button.setText("")
        self.NewPerson_Button.setFlat(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/AddUserIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NewPerson_Button.setIcon(icon2)
        self.NewPerson_Button.setIconSize(QtCore.QSize(100, 65))
        self.NewPerson_Button.setObjectName("NewPerson_Button")
        self.Date_Label = QtWidgets.QLabel(self.Top_Frame)
        self.Date_Label.setGeometry(QtCore.QRect(300, 20, 500, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.Date_Label.setFont(font)
        self.Date_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Date_Label.setObjectName("Date_Label")
        Birthday_Tracker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Birthday_Tracker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        Birthday_Tracker.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Birthday_Tracker)
        self.statusbar.setObjectName("statusbar")
        Birthday_Tracker.setStatusBar(self.statusbar)

        self.retranslateUi(Birthday_Tracker)
        self.stackedWidget.setCurrentIndex(0)
        self.Home_Button.clicked.connect(self.To_Home_Page)
        self.NewPerson_Button.clicked.connect(self.To_Add_User_Page)
        self.Date_Label.setText(GenerateDate())
        self.Submit_Button.clicked.connect(self.Submit_New_Person)
        self.Calendar.clicked.connect(self.Update_Birthday)
        QtCore.QMetaObject.connectSlotsByName(Birthday_Tracker)
        
        DBUpdate()
        Three_Days_Before()
        Birthday_Today()
        
        self.Check_Length()
        self.Update_Home_Page()

        #Colors:
        self.Top_Frame.setStyleSheet(f"background-color: {Top_Frame_Color};")
        self.centralwidget.setStyleSheet(f"background-color: {Main_Background_Color};")
        self.Calendar.setStyleSheet(f"Background-color: {Calendar_Color};")
        self.Submit_Button.setStyleSheet(f"background-color: {Calendar_Color};")
        self.First_Name_Input.setStyleSheet(f"background-color: {Calendar_Color};")
        self.Last_Name_Input.setStyleSheet(f"background-color: {Calendar_Color};")
        self.Birthday_Information.setStyleSheet(f"background-color: {Calendar_Color};")
        
    def retranslateUi(self, Birthday_Tracker):
        _translate = QtCore.QCoreApplication.translate
        Birthday_Tracker.setWindowTitle(_translate("Birthday_Tracker", "Birthday Tracker"))
        self.Birthdays_Label.setText(_translate("Birthday_Tracker", "Birthdays"))
        self.First_Name_Input.setPlaceholderText(_translate("Birthday_Tracker", "First Name"))
        self.Last_Name_Input.setPlaceholderText(_translate("Birthday_Tracker", "Last Name"))
        self.Birthday_Information.setPlaceholderText(_translate("Birthday_Tracker", "Birthday"))
        self.Submit_Button.setText(_translate("Birthday_Tracker", "Submit"))
        self.Birthday_Information.setText(_translate("Birthday_Tracker", "Birthday : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Birthday_Tracker = QtWidgets.QMainWindow()
    ui = Ui_Birthday_Tracker()
    ui.setupUi(Birthday_Tracker)
    Birthday_Tracker.show()
    sys.exit(app.exec_())

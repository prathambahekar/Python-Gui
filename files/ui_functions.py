from main import *
import json

f = open("settings.json")
Data = json.load(f) 

defaultTheme = Data["app-info"]["theme"]


class UIFunctions(MainWindow):

	def SetTheme(self):
		
		str = open(f"files\\themes\{defaultTheme}.qss", 'r').read()
		self.ui.centralwidget.setStyleSheet(str)

	def SwitchTheme(self):

		global defaultTheme
		
		if defaultTheme == "light":
			str = open(f"files\\themes\dark.qss", 'r').read()
			self.ui.centralwidget.setStyleSheet(str)

			defaultTheme = "dark"

		elif defaultTheme == "dark":
			str = open(f"files\\themes\light.qss", 'r').read()
			self.ui.centralwidget.setStyleSheet(str)

			defaultTheme = "light"

	def ToggleMenu(self, min, max):

		presentWidth = self.ui.leftMenu.width()

		startToggle = ""
		endToggle = ""

		if presentWidth == min:
			startToggle = min
			endToggle = max
			
			self.ui.home_btn.setText("Home")
			self.ui.settings_btn.setText("Settings")
			self.ui.theme_btn.setText("Theme")

		elif presentWidth == max:
			startToggle = max
			endToggle = min

			self.ui.home_btn.setText("")
			self.ui.settings_btn.setText("")
			self.ui.theme_btn.setText("")


		self.animation = QPropertyAnimation(self.ui.leftMenu, b"minimumWidth")
		self.animation.setDuration(200)
		self.animation.setStartValue(startToggle)
		self.animation.setEndValue(endToggle)
		self.animation.setEasingCurve(QEasingCurve.InOutQuart)
		self.animation.start()

	def AboutApp(self):

		pass


	def Setup_GUI(self):

		# set window title
		self.setWindowTitle(Data["app-info"]["name"])

		UIFunctions.AboutApp(self)

		# set windows default size
		self.resize(Data["app-info"]["window-size"]["default"][0], Data["app-info"]["window-size"]["default"][1])

		# set window min size
		if Data["app-info"]["window-size"]["isMin"] != False:
			self.setMinimumSize(Data["app-info"]["window-size"]["min"][0], Data["app-info"]["window-size"]["min"][1])
		
		# set window max size
		if Data["app-info"]["window-size"]["isMax"] != False:
			self.setMaximumSize(Data["app-info"]["window-size"]["max"][0], Data["app-info"]["window-size"]["max"][1])
			

		self.ui.home_btn.clicked.connect(lambda : self.ui.switchPage.setCurrentIndex(0))
		self.ui.settings_btn.clicked.connect(lambda : self.ui.switchPage.setCurrentIndex(1))

		self.ui.theme_btn.clicked.connect(lambda : UIFunctions.SwitchTheme(self))

		self.ui.menu_btn.clicked.connect(lambda : UIFunctions.ToggleMenu(self, 50, 300))

		# WindowIcon = QIcon()
		# WindowIcon.addFile("files/assest/icon.png")
		# self.setWindowIcon(WindowIcon)
		


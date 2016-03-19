# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, x, y):
		self.label = []
		self.desktopX = x
		self.desktopY = y

		QtWidgets.QMainWindow.__init__(self)

		self.configure_win()
		self.configure_menu_bar()


	# наш win
	def configure_win(self):
		self.setMinimumSize(780, 610)
		self.setMaximumSize(self.desktopX, self.desktopY)
		self.setWindowTitle('Просмотр изображений')
		self.setWindowIcon(QtGui.QIcon('appicon.ico'))
		self.move(50, 30)

	# меню - бар
	def configure_menu_bar(self):
		openPictureAction = QtWidgets.QAction('&Open', self)
		openPictureAction.setShortcut('Ctrl+0')
		openPictureAction.triggered.connect(self.get_path_image_event)

		exitAction = QtWidgets.QAction('&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.triggered.connect(self.close_event)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&Picture')
		fileMenu.addAction(openPictureAction)
		fileMenu.addAction(exitAction)
		faq = menubar.addMenu('&FAQ')


	# меню => путь к изображению
	def get_path_image_event(self):
		fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open', '/home')
		print(fileName)
		self.configure_central_widget(fileName)


	# меню => закрытие с проверкой, там есть sys.exit()
	def close_event(self):
		if len(self.label) != 0:
			reply = QtWidgets.QMessageBox()
			reply.setWindowModality(1)
			reply.question(self, 
					'Confirm exit', 
					'Are you sure you want to quit?', 
					QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)		
			if reply == QtWidgets.QMessageBox.Yes:
				sys.exit()
		else:
			sys.exit()

	# центральный виджет
	def configure_central_widget(self, path):
		# изображение
		image = QtGui.QPixmap(path[0])

		# сам label
		self.label.append(QtWidgets.QLabel(self))
		self.label[0].setMaximumSize(740, 570)
		self.label[0].setPixmap(image)

		self.setCentralWidget(self.label[0])
		

app = QtWidgets.QApplication(sys.argv)

desktopRect = app.desktop() # рабочий стол
rect = desktopRect.availableGeometry() # прямоугольник

mainWindow = MainWindow(rect.width(), rect.height()) # передаем размеры

mainWindow.show()

sys.exit(app.exec_())

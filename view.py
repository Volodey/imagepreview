# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, x, y):
		# контейнер для нашего изображения
		self.labels = []
		# размеры рабочей области нашего рабочего стола
		self.desktopX = x
		self.desktopY = y

		QtWidgets.QMainWindow.__init__(self)

		# конфигурируем наше окно
		self.configure_win()
		# делаем меню бар
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
		# получаем путь к файлу
		fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open', '/home')
		print(fileName)
		# вызываем создание центральной области нашего MainWindow
		self.configure_central_widget(fileName)


	# меню => закрытие с проверкой, там есть sys.exit()
	def close_event(self):
		if len(self.labels) != 0:
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
		self.labels.append(QtWidgets.QLabel(self))
		self.labels[0].setMaximumSize(740, 570) # временно нужно
		self.labels[0].setPixmap(image)


		self.setCentralWidget(self.labels[0])
		

app = QtWidgets.QApplication(sys.argv)

# рабочий стол
desktopRect = app.desktop()
# информация о размерах рабочего стола (только доступная часть экрана)
rect = desktopRect.availableGeometry()

# главное окно
mainWindow = MainWindow(rect.width(), rect.height())

mainWindow.show()

sys.exit(app.exec_())

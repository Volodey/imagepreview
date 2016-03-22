# coding: utf8
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QAction, QLineEdit, QLabel
from PyQt5.QtWidgets import QFileDialog, QDesktopWidget, QWidget
from PyQt5.uic import loadUi
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt

app = QApplication(sys.argv)
app.setApplicationName('Imagepreview')


class MainWindow(QMainWindow):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        loadUi('ui.ui', self)
        self.setStatusTip('ready')

        # контейнер для нашего изображения
        self.labels = []

    def get_path_image_event(self):
        # получаем путь к файлу
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open', '/home')
        # если файл выбран продолжаем, если нет то ничего не делаем
        if fileName:
            print(fileName)
            # вызываем создание центральной области нашего MainWindow
            # self.configure_central_widget(fileName)
            # изображение
            image = QtGui.QPixmap(fileName[0])
            image = image.scaled(740, 740, QtCore.Qt.KeepAspectRatio)  # сам label
            self.labels.append(self.label_image0)
            self.labels[0].setPixmap(image)

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

    # функция центрирования главного окна
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        # self.move(qr.topLeft())


# -----------------------------------------------------#
form = MainWindow()
form.setWindowTitle('Imagepreview')
form.show()
sys.exit(app.exec_())

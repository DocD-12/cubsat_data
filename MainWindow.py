# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 486)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(192, 191, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Загрузки/satsearch_0aawcw_endurosat_1u_platform.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName("centralwidget")
        self.inputbutton = QtWidgets.QPushButton(self.centralwidget)
        self.inputbutton.setGeometry(QtCore.QRect(10, 10, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputbutton.setFont(font)
        self.inputbutton.setObjectName("inputbutton")
        self.compare_button = QtWidgets.QPushButton(self.centralwidget)
        self.compare_button.setGeometry(QtCore.QRect(510, 10, 481, 71))
        self.compare_button.setObjectName("compare_button")
        self.textBrowser_one = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_one.setGeometry(QtCore.QRect(10, 85, 230, 51))
        self.textBrowser_one.setObjectName("textBrowser_one")
        self.textBrowser_three = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_three.setGeometry(QtCore.QRect(510, 85, 481, 50))
        self.textBrowser_three.setObjectName("textBrowser_three")
        self.textBrowser_two = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_two.setGeometry(QtCore.QRect(250, 85, 230, 51))
        self.textBrowser_two.setObjectName("textBrowser_two")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(487, 0, 17, 491))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.file_path_window = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.file_path_window.setGeometry(QtCore.QRect(10, 380, 471, 41))
        self.file_path_window.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.file_path_window.setReadOnly(True)
        self.file_path_window.setObjectName("file_path_window")
        self.graph_out = PlotWidget(self.centralwidget)
        self.graph_out.setGeometry(QtCore.QRect(510, 140, 301, 311))
        self.graph_out.setObjectName("graph_out")
        self.grap_db = PlotWidget(self.centralwidget)
        self.grap_db.setGeometry(QtCore.QRect(10, 140, 230, 230))
        self.grap_db.setObjectName("grap_db")
        self.graph_sun = PlotWidget(self.centralwidget)
        self.graph_sun.setGeometry(QtCore.QRect(250, 140, 230, 230))
        self.graph_sun.setObjectName("graph_sun")
        self.input_button_sun = QtWidgets.QPushButton(self.centralwidget)
        self.input_button_sun.setGeometry(QtCore.QRect(250, 10, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setKerning(True)
        self.input_button_sun.setFont(font)
        self.input_button_sun.setObjectName("input_button_sun")
        self.CorrBox = QtWidgets.QTextEdit(self.centralwidget)
        self.CorrBox.setGeometry(QtCore.QRect(820, 140, 171, 31))
        self.CorrBox.setMouseTracking(False)
        self.CorrBox.setReadOnly(True)
        self.CorrBox.setObjectName("CorrBox")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 430, 471, 24))
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Корреляция данных СТЦ"))
        self.inputbutton.setText(_translate("MainWindow", "Выбрать файл \"мощность сигнала\""))
        self.compare_button.setText(_translate("MainWindow", "Сопоставить солнечную активность с сигналом"))
        self.textBrowser_one.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">График зависимости мощности сигнала CubeSat (dBm) ко времени (UNIX).</span></p></body></html>"))
        self.textBrowser_three.setMarkdown(_translate("MainWindow", "График корреляции мощности сигнала CubeSat и солнечной активности.\n"
"\n"
""))
        self.textBrowser_three.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:7px; margin-bottom:7px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">График корреляции мощности сигнала CubeSat и солнечной активности.</p></body></html>"))
        self.textBrowser_two.setMarkdown(_translate("MainWindow", "График зависимости солнечной активности ко времени.\n"
"\n"
""))
        self.textBrowser_two.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:7px; margin-bottom:7px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">График зависимости солнечной активности ко времени.</span></p></body></html>"))
        self.file_path_window.setPlainText(_translate("MainWindow", "Файл мощности не выбран"))
        self.input_button_sun.setText(_translate("MainWindow", "Получить солнечную активность из сети"))
        self.CorrBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Кореляция: -</span></p></body></html>"))
from pyqtgraph import PlotWidget
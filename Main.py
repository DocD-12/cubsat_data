from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PyQt5 import QtWidgets, uic
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(936, 443)
        palette = QPalette()
        brush = QBrush(QColor(192, 191, 188, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush2 = QBrush(QColor(222, 221, 218, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        brush3 = QBrush(QColor(239, 239, 239, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        MainWindow.setPalette(palette)
        icon = QIcon()
        icon.addFile(u"../../\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0438/satsearch_0aawcw_endurosat_1u_platform.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.centralwidget.setPalette(palette1)
        self.inputbutton = QPushButton(self.centralwidget)
        self.inputbutton.setObjectName(u"inputbutton")
        self.inputbutton.setGeometry(QRect(10, 10, 471, 71))
        self.compare_button = QPushButton(self.centralwidget)
        self.compare_button.setObjectName(u"compare_button")
        self.compare_button.setGeometry(QRect(540, 10, 380, 71))
        self.graph_one = QFrame(self.centralwidget)
        self.graph_one.setObjectName(u"graph_one")
        self.graph_one.setGeometry(QRect(10, 140, 230, 230))
        self.graph_one.setFrameShape(QFrame.StyledPanel)
        self.graph_one.setFrameShadow(QFrame.Raised)
        self.textBrowser_one = QTextBrowser(self.centralwidget)
        self.textBrowser_one.setObjectName(u"textBrowser_one")
        self.textBrowser_one.setGeometry(QRect(10, 85, 230, 51))
        self.textBrowser_three = QTextBrowser(self.centralwidget)
        self.textBrowser_three.setObjectName(u"textBrowser_three")
        self.textBrowser_three.setGeometry(QRect(540, 85, 380, 50))
        self.graph_out = QFrame(self.centralwidget)
        self.graph_out.setObjectName(u"graph_out")
        self.graph_out.setGeometry(QRect(590, 140, 280, 280))
        self.graph_out.setFrameShape(QFrame.StyledPanel)
        self.graph_out.setFrameShadow(QFrame.Raised)
        self.graph_two = QFrame(self.centralwidget)
        self.graph_two.setObjectName(u"graph_two")
        self.graph_two.setGeometry(QRect(250, 140, 230, 230))
        self.graph_two.setFrameShape(QFrame.StyledPanel)
        self.graph_two.setFrameShadow(QFrame.Raised)
        self.textBrowser_two = QTextBrowser(self.centralwidget)
        self.textBrowser_two.setObjectName(u"textBrowser_two")
        self.textBrowser_two.setGeometry(QRect(250, 85, 230, 51))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(510, -10, 17, 441))
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.VLine)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u044f \u0434\u0430\u043d\u043d\u044b\u0445 \u0421\u0422\u0426", None))
        self.inputbutton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b \"\u043c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u0441\u0438\u0433\u043d\u0430\u043b\u0430\"", None))
        self.compare_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u043b\u043d\u0435\u0447\u043d\u0443\u044e \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c \u0441 \u0441\u0438\u0433\u043d\u0430\u043b\u043e\u043c", None))
        self.textBrowser_one.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0413\u0440\u0430\u0444\u0438\u043a \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438 \u0441\u0438\u0433\u043d\u0430\u043b\u0430 \u043e\u0442 db \u043a \u0432\u0440\u0435\u043c\u0435\u043d\u0438</span></p></body></html>", None))
        self.textBrowser_three.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0413\u0440\u0430\u0444\u0438\u043a \u043f\u0440\u044f\u043c\u043e\u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0439 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043a\u043e\u0440\u0440\u0435\u043b\u044f\u0446\u0438\u0438 \u0441\u043e\u043b\u043d\u0435\u0447\u043d\u043e\u0439 \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438 \u0438 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438 \u0441\u0438\u0433\u043d\u0430\u043b\u0430</span></p></body></html>", None))
        self.textBrowser_two.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u0413\u0440\u0430\u0444\u0438\u043a \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u0441\u043e\u043b\u043d\u0435\u0447\u043d\u043e\u0439 \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438 \u043a\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438</span></p></body></html>", None))
    # retranslateUi

app = QtWidgets.QApplication(sys.argv)

window = Ui_MainWindow()
window.show()
app.exec()
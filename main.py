import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox

from MainWindow import Ui_MainWindow

import numpy as np

import openpyxl

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.inputbutton.clicked.connect(self.choose_txt)
        self.ui.compare_button.clicked.connect(self.compare_click)
        self.ui.input_button_sun.clicked.connect(self.update_sun_activity)

        plot_db = self.ui.grap_db
        plot_db.setLabel(axis='left', text='Мощность')
        plot_db.setLabel(axis='bottom', text='Время')

        plot_sun = self.ui.graph_sun
        plot_sun.setLabel(axis='left', text='Мощность солнца')
        plot_sun.setLabel(axis='bottom', text='Время')

        plot_out = self.ui.graph_out
        plot_out.setLabel(axis='left', text='Активность солнца')
        plot_out.setLabel(axis='bottom', text='Мощность сигнала со спутника')

    filepath_txt = ["", ""]
    filepath_sun_txt = ["", ""]
    successful_updated = False

    data_list_db_X = []
    data_list_db_Y = []

    corr_list_db_Y = []

    data_list_sun_X = []
    data_list_sun_Y = []

    corr_list_sun_Y = []

    range_end = 0

    _filepath_txt = None
    excel1 = None
    lists1 = None
    lists_num1 = None

    _filepath_sun_txt = None
    excel2 = None
    lists2 = None
    lists_num2 = None

    def ClearDB(self):
        self.data_list_db_X.clear()
        self.data_list_db_Y.clear()
        self.ui.grap_db.clear()

    def ClearSun(self):
        self.data_list_sun_X.clear()
        self.data_list_sun_Y.clear()
        self.ui.graph_sun.clear()

    def ClearCompare(self):
        self.corr_list_db_Y.clear()
        self.corr_list_sun_Y.clear()
        self.ui.graph_out.clear()
    def choose_txt(self):
        self.ClearDB()
        self._filepath_txt = QFileDialog.getOpenFileName(self, str("Загрузить .xlsx мощности"), "/", str("xlsx (*.xlsx)"))

        if (str(self._filepath_txt[0]) == "" or self._filepath_txt == None):
            print("Empty file!!!")
            return

        self.excel1 = openpyxl.open(self._filepath_txt[0], read_only=True)
        self.lists1 = self.excel1.worksheets
        self.lists_num1 = 0
        A_list = 0
        B_list = 1
        for i in range(1, self.lists1[self.lists_num1].max_row + 1):
            self.data_list_db_X.append(self.lists1[self.lists_num1][i][A_list].value)
            self.data_list_db_Y.append(self.lists1[self.lists_num1][i][B_list].value)

        self.data_list_db_X = list(map(float, self.data_list_db_X))
        self.data_list_db_Y = list(map(float, self.data_list_db_Y))

        if (self._filepath_txt[0] != ""):
            self.ui.file_path_window.setPlainText("Выбран файл мощности по пути: " + str(self._filepath_txt))
            self.set_db_graph(self.data_list_db_X, self.data_list_db_Y, False) # Нужно передавать судя данные из txt файла и алгоритма построения графика
            # self.set_sun_graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [34, 23, 34, 89, 12, 89, 12, 14, 100, 0], False) # Нужно передавать судя данные из txt файла и алгоритма построения графика
        else:
            self.ui.file_path_window.setPlainText("Файл мощности не выбран")
            self.set_db_graph(0, 0, True)
            # self.set_sun_graph(0, 0, True)
            self.compare_out(0, 0, True)
        self.filepath_txt = self._filepath_txt

    def update_sun_activity(self):
        # Программа парсера погоды
        successful = True # Получена ли успешно погода?
        self.ClearSun()
        self._filepath_sun_txt = QFileDialog.getOpenFileName(self, str("Загрузить .xlsx файл солнечной активности"), "/", str("xlsx (*.xlsx)"))

        if (str(self._filepath_sun_txt[0]) == "" or self._filepath_sun_txt == None):
            print("Empty file!!!")
            return
        self.excel2 = openpyxl.open(self._filepath_sun_txt[0], read_only=True)
        self.lists2 = self.excel2.worksheets
        self.lists_num2 = 0
        A_list = 0
        B_list = 1
        for i in range(1, self.lists2[self.lists_num2].max_row + 1):
            self.data_list_sun_X.append(self.lists2[self.lists_num2][i][A_list].value)
            self.data_list_sun_Y.append(self.lists2[self.lists_num2][i][B_list].value)

        self.data_list_sun_X = list(map(float, self.data_list_sun_X))
        self.data_list_sun_Y = list(map(float, self.data_list_sun_Y))

        if (self._filepath_sun_txt[0] != ""):
            self.set_sun_graph(self.data_list_sun_X, self.data_list_sun_Y, False) # Нужно передавать судя данные из txt файла и алгоритма построения графика
        else:
            self.ui.file_path_window.setPlainText("Файл солнечной активности не выбран")
            self.set_db_graph(0, 0, True)
            # self.set_sun_graph(0, 0, True)
            self.compare_out(0, 0, True)
        self.filepath_sun_txt = self._filepath_sun_txt
        self._filepath_sun_txt = 0
        """"
        if (successful):
            self.set_sun_graph(0, 0, True)
            self.set_sun_graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [34, 23, 34, 89, 12, 89, 12, 14, 100, 0], False)
            self.successful_updated = True
        else:
            self.successful_updated = False
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не удалось получить доступ к данным солнечной активности, проверьте подключение к интернету')
            msg.setWindowTitle("Получение солнечной активности")
            msg.exec_()
            self.successful_updated = False
        """

    def compare_click(self):
        error = 0

        self.ClearCompare()

        if (self.filepath_txt[0] == ""):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Файл мощности (.xlsx) не был выбран!')
            msg.setWindowTitle("Сопостовленние данных")
            msg.exec_()
            return
        if (self.filepath_sun_txt[0] == ""): # НУЖНО ПОМЕНЯТЬ НА ПАРСЕР ПОГОДЫ
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Файл солнечной активности (.xlsx) не был выбран!')
            msg.setWindowTitle("Сопостовленние данных")
            msg.exec_()
            return

        if (self.lists1[self.lists_num1].max_row + 1) > (self.lists2[self.lists_num2].max_row + 1):
            self.range_end = self.lists2[self.lists_num2].max_row + 1
            error += 1
        elif (self.lists1[self.lists_num1].max_row + 1) < (self.lists2[self.lists_num2].max_row + 1):
            self.range_end = self.lists1[self.lists_num1].max_row + 1
            error += 1
        else:
            self.range_end = self.lists1[self.lists_num1].max_row + 1

        for i in range(1, self.range_end):
            self.corr_list_db_Y.append(self.lists1[self.lists_num1][i][1].value)
            self.corr_list_sun_Y.append(self.lists2[self.lists_num2][i][1].value)

        corr = np.corrcoef(self.corr_list_sun_Y, self.corr_list_db_Y)[0, 1]

        if (self.filepath_txt[0] == ""):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Файл мощности (.xlsx) не был выбран!')
            msg.setWindowTitle("Сопостовленние данных")
            msg.exec_()
        else:
            if error == 0:
                print("error 0")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Успешно")
                msg.setInformativeText('Данные сопоставленны успешно')
                msg.setWindowTitle("Сопостовление данных")
                msg.exec_()
                self.compare_out(self.corr_list_db_Y, self.corr_list_sun_Y, False)  # Нужно передавать судя данные из алгоритма, которыми занимаются математики
                print(self.corr_list_db_Y)
                print(self.corr_list_sun_Y)
                print(corr)
                self.ui.CorrBox.setPlainText(f"Корреляция: {corr:.2f}")
            else:
                print("No error")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Обнаружена неточность")
                msg.setInformativeText('Количество строк двух таблиц не совпадает!')
                msg.setWindowTitle("Сопостовленние данных")
                msg.exec_()
                self.compare_out(self.corr_list_db_Y, self.corr_list_sun_Y,False)  # Нужно передавать судя данные из алгоритма, которыми занимаются математики
                print(self.corr_list_db_Y)
                print(self.corr_list_sun_Y)
                print(corr)
                self.ui.CorrBox.setPlainText(f"Корреляция: {corr:.2f}")

        """
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не получена солнечная активность!')
            msg.setWindowTitle("Сопостовленние данных")
            msg.exec_()
        """
    def compare_out(self, activity, power_db, clear): # Вывод графика зависимости солнечной активности от db
        if not(clear):
            poly = np.polyfit(self.corr_list_db_Y, self.corr_list_sun_Y, deg=3)
            line = np.polyval(poly, self.corr_list_db_Y)

            self.ui.graph_out.plot(activity, power_db, pen=None, name="blue", symbol='o')
            self.ui.graph_out.plot(self.corr_list_db_Y, line, pen ='g', symbolBrush=1)
        else:
            self.ui.graph_out.clear()
    def set_db_graph(self, time, db, clear): # Вывод графика зависимости времени от db
        if not(clear):
            self.ui.grap_db.plot(time, db)
        else:
            self.ui.grap_db.clear()
    def set_sun_graph(self, activity, time, clear): # Вывод графика зависимости солнечной активности от времени
        if not(clear):
            self.ui.graph_sun.plot(activity, time)
        else:
            self.ui.graph_sun.clear()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(975, 443)
window.show()
app.exec()
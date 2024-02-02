import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox

from MainWindow import Ui_MainWindow

import  openpyxl

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.inputbutton.clicked.connect(self.choose_txt)
        self.ui.compare_button.clicked.connect(self.compare_click)
        self.ui.input_button_sun.clicked.connect(self.update_sun_activity)

    filepath_txt = ["", ""]
    successful_updated = False



    def choose_txt(self):
        _filepath_txt = QFileDialog.getOpenFileName(self, str("Загрузить txt файл мощности"), "/", str("TEXT (*.xlsx)"))
        excel = openpyxl.open(_filepath_txt[0], read_only=True)
        lists = excel.worksheets
        lists_num = 0
        A_list = 0
        B_list = 1
        data_list_X = []
        data_list_Y = []
        for i in range(1, lists[lists_num].max_row + 1):
            data_list_X.append(lists[lists_num][i][A_list].value)
            data_list_Y.append(lists[lists_num][i][B_list].value)

        data_list_X = list(map(float,data_list_X))
        data_list_Y = list(map(float, data_list_Y))

        if (_filepath_txt[0] != ""):
            self.ui.file_path_window.setPlainText("Выбран файл мощности по пути: " + str(_filepath_txt))
            self.set_db_graph(data_list_X, data_list_Y, False) # Нужно передавать судя данные из txt файла и алгоритма построения графика
            # self.set_sun_graph([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [34, 23, 34, 89, 12, 89, 12, 14, 100, 0], False) # Нужно передавать судя данные из txt файла и алгоритма построения графика
        else:
            self.ui.file_path_window.setPlainText("Файл мощности не выбран")
            self.set_db_graph(0, 0, True)
            # self.set_sun_graph(0, 0, True)
            self.compare_out(0, 0, True)
        self.filepath_txt = _filepath_txt


    def update_sun_activity(self):
        # Программа парсера погоды
        successful = True # Получена ли успешно погода?
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

    def compare_click(self):
        if (self.filepath_txt[0] == ""):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Файл мощности (.txt) не был выбран!')
            msg.setWindowTitle("Сопостовленние данных")
            msg.exec_()
        elif (self.successful_updated):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Успешно")
            msg.setInformativeText('Данные сопоставленны успешно')
            msg.setWindowTitle("Сопостовление данных")
            msg.exec_()
            self.compare_out([1,2,3,4,5,6,7,8,9,10], [90,32,34,32,33,31,29,32,35,45], False) # Нужно передавать судя данные из алгоритма, которыми занимаются математики
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не получена солнечная активность!')
            msg.setWindowTitle("Сопостовленние данных")
            msg.exec_()

    def compare_out(self, activity, power_db, clear): # Вывод графика зависимости солнечной активности от db
        if not(clear):
            self.ui.graph_out.plot(activity, power_db)
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
window.setFixedSize(936, 443)
window.show()
app.exec()
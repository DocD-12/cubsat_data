import functools as functools
import sys
from datetime import datetime

import numpy as np
import openpyxl
from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

functools.lru_cache(None)

print("_" * 100)

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
        plot_out.setLabel(axis='left', text='Коэффициент корреляции')
        plot_out.setLabel(axis='bottom', text='Время')

    filepath_txt = ["", ""]
    filepath_sun_txt = ["", ""]
    successful_updated = False

    data_list_db_X = []
    data_list_db_Y = []

    corr_list_db_Y = []

    data_list_sun_X = []
    data_list_sun_Y = []

    corr_list_sun_Y = []

    range_1 = 0
    range_2 = 0
    range_end = 0

    _filepath_txt = None
    excel1 = None
    lists1 = None
    lists_num1 = None

    lists_combo = None

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

    def read_selected_sheet(self, index):
        self.ClearDB()
        self.set_db_graph(0, 0, True)

        selected_sheet_name = self.lists_combo[index]  # Получаем имя выбранного листа по индексу
        selected_sheet = self.excel1[selected_sheet_name]  # Получаем выбранный лист

        self.data_list_db_X.clear()
        self.data_list_db_Y.clear()

        for row in selected_sheet.iter_rows(min_row=2, max_row=selected_sheet.max_row, min_col=1, max_col=2):
            if all(cell.value is not None for cell in row):
                try:
                    self.data_list_db_X.append(self.to_UNIX(row[0].value))
                    self.data_list_db_Y.append(row[1].value)
                except:
                    self.data_list_db_X.clear()
                    self.data_list_db_Y.clear()

                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Ошибка")
                    msg.setInformativeText(
                        f'Не удалось конвертировать время в UNIX формат. Строка: {row}')
                    msg.setWindowTitle("Конвертация данных")
                    msg.exec_()
                    break
            else:
                self.show_warning_message("Неправильные строки")
                break

        print("CubeSat")
        print(f"Выбран лист: {selected_sheet_name}")
        print("Количество строк:", selected_sheet.max_row)
        print("data_list_db_X:", self.data_list_db_X)
        print("data_list_db_Y:", self.data_list_db_Y)
        print("_" * 100)

        try:
            self.data_list_db_X = list(map(float, self.data_list_db_X))
            self.data_list_db_Y = list(map(float, self.data_list_db_Y))
        except ValueError:
            self.show_critical_message("Неправильные строки", "Вероятно часть строк не соответствует нужному формату!")

        self.ui.file_path_window.setPlainText("Выбран файл мощности по пути: " + str(self._filepath_txt))
        self.set_db_graph(self.data_list_db_X, self.data_list_db_Y, False)


    def to_UNIX(self, date_string):
        from datetime import datetime

        date_string = date_string.strip("'")
        date_components = date_string.split('-')

        months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
                  'Nov': 11, 'Dec': 12}
        month = months[date_components[1]]

        year = int(date_components[2][:4])
        time_components = date_components[2].split()
        time_parts = time_components[1].split(':')
        hour = int(time_parts[0])
        minute = int(time_parts[1])
        second = int(time_parts[2])

        datetime_obj = datetime(year, month, int(date_components[0]), hour, minute, second)
        unix_time = datetime_obj.timestamp()

        return unix_time

    def choose_txt(self):
        self.ClearDB()
        self._filepath_txt = QFileDialog.getOpenFileName(self, str("Загрузить .xlsx мощности"), "./",
                                                         str("xlsx (*.xlsx)"))

        if not self._filepath_txt[0]:
            print("Выбран пустой файл или ничего не выбрано!")
            return

        self.excel1 = openpyxl.open(self._filepath_txt[0], read_only=True)
        self.lists1 = self.excel1.worksheets
        self.lists_num1 = 0
        A_list = 0
        B_list = 1

        self.lists_combo = self.excel1.sheetnames
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(self.lists_combo)
        self.ui.comboBox.currentIndexChanged.connect(self.read_selected_sheet)
        self._filepath_txt = self._filepath_txt[0]

        self.data_list_db_X = []
        self.data_list_db_Y = []

        for row in self.lists1[self.lists_num1].iter_rows(min_row=2, max_row=self.lists1[self.lists_num1].max_row, min_col=1, max_col=2):
            if all(cell.value is not None for cell in row):
                try:
                    self.data_list_db_X.append(self.to_UNIX(row[A_list].value))
                    self.data_list_db_Y.append(row[B_list].value)
                except:
                    self.data_list_db_X = []
                    self.data_list_db_Y = []

                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Ошибка")
                    msg.setInformativeText(
                        f'Не удалось конвертировать время в UNIX формат. Строка: {row}')
                    msg.setWindowTitle("Конвертация данных")
                    msg.exec_()
                    break
            else:
                self.show_warning_message("Неправильные строки")
                break

        print("CubeSat")
        print(f"Выбран файл: {self._filepath_txt}")
        print("Количество строк:", self.lists1[self.lists_num1].max_row)
        print("data_list_db_X", self.data_list_db_X)
        print("data_list_db_Y", self.data_list_db_Y)
        print("_" * 100)

        try:
            self.data_list_db_X = list(map(float, self.data_list_db_X))
            self.data_list_db_Y = list(map(float, self.data_list_db_Y))
        except ValueError:
            self.show_critical_message("Неправильные строки", "Вероятно часть строк не соответствует нужному формату!")

        if self._filepath_txt[0]:
            self.ui.file_path_window.setPlainText("Выбран файл мощности по пути: " + str(self._filepath_txt))
            self.set_db_graph(self.data_list_db_X, self.data_list_db_Y, False)
        else:
            self.ui.file_path_window.setPlainText("Файл мощности не выбран")
            self.set_db_graph(0, 0, True)

        self.filepath_txt = self._filepath_txt

    def update_sun_activity(self):
        successful = True
        self.ClearSun()
        self._filepath_sun_txt = QFileDialog.getOpenFileName(self, str("Загрузить .xlsx файл солнечной активности"),
                                                             "./", str("xlsx (*.xlsx)"))

        if not self._filepath_sun_txt[0]:
            print("Выбран пустой файл или ничего не выбрано!")
            return

        self.excel2 = openpyxl.open(self._filepath_sun_txt[0], read_only=True)
        self.lists2 = self.excel2.worksheets
        self.lists_num2 = 0
        A_list = 0
        B_list = 1

        self.data_list_sun_X = []
        self.data_list_sun_Y = []

        for row in self.lists2[self.lists_num2].iter_rows(min_row=2, max_row=self.lists2[self.lists_num2].max_row, min_col=1, max_col=2):
            if all(cell.value is not None for cell in row):
                self.data_list_sun_X.append(row[A_list].value)
                self.data_list_sun_Y.append(row[B_list].value)
            else:
                self.show_warning_message("Неправильные строки")
                break

        print("Солнечная активность")
        print(f"Выбран файл: {self._filepath_sun_txt}")
        print("Количество строк:", self.lists2[self.lists_num2].max_row)
        print("data_list_sun_X", self.data_list_sun_X)
        print("data_list_sun_Y", self.data_list_sun_Y)
        print("_" * 100)

        try:
            self.data_list_sun_X = list(map(float, self.data_list_sun_X))
            self.data_list_sun_Y = list(map(float, self.data_list_sun_Y))
        except ValueError:
            self.show_critical_message("Неправильные строки", "Вероятно часть строк не соответствует нужному формату!")

        if self._filepath_sun_txt[0]:
            self.set_sun_graph(self.data_list_sun_X, self.data_list_sun_Y, False)
        else:
            self.ui.file_path_window.setPlainText("Файл солнечной активности не выбран!")
            self.set_db_graph(0, 0, True)

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
        self.ClearCompare()

        if not self.filepath_txt[0]:
            self.show_critical_message("Ошибка", "Файл солнечной активности (.xlsx) не был выбран!")
            return

        if not self.filepath_sun_txt[0]:
            self.show_critical_message("Ошибка", "Файл солнечной активности (.xlsx) не был выбран!")
            return

        self.corr_list_db_Y = []
        self.corr_list_sun_Y = []

        for i in range(min(len(self.data_list_db_X), len(self.data_list_sun_X))):
            self.corr_list_db_Y.append(self.data_list_db_Y[i])
            self.corr_list_sun_Y.append(self.data_list_sun_Y[i])

        self.corr_list_db_Y = list(map(float, self.corr_list_db_Y))
        self.corr_list_sun_Y = list(map(float, self.corr_list_sun_Y))

        corr = np.corrcoef(self.corr_list_sun_Y, self.corr_list_db_Y)[0, 1]

        if not self.filepath_txt[0]:
            self.show_critical_message("Ошибка", "Файл солнечной активности (.xlsx) не был выбран!")
        else:
            self.show_information_message("Успешно", "Данные сопоставлены успешно.")
            self.compare_out(self.corr_list_db_Y, self.corr_list_sun_Y, False)
            print("Корреляция:")
            print("Количество объектов:", min(len(self.corr_list_db_Y), len(self.corr_list_sun_Y)))
            print("corr_list_db_Y:", self.corr_list_db_Y)
            print("corr_list_sun_Y", self.corr_list_sun_Y)
            print("Коэффициент корреляции:", corr)
            self.ui.CorrBox.setPlainText(f"Корреляция: {corr:.2f}")

        """
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Не получена солнечная активность!')
            msg.setWindowTitle("Сопоставление данных")
            msg.exec_()
        """

    def show_warning_message(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(text)
        msg.setInformativeText('Часть строк была обрезана, во избежание ошибки!')
        msg.setWindowTitle("Сопоставление данных")
        msg.exec_()

    def show_critical_message(self, text, informative_text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setInformativeText(informative_text)
        msg.setWindowTitle("Сопоставление данных")
        msg.exec_()

    def show_information_message(self, text, informative_text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setInformativeText(informative_text)
        msg.setWindowTitle("Сопоставление данных")
        msg.exec_()

    def compare_out(self, activity, power_db, clear):  # Вывод графика зависимости солнечной активности от db
        if not clear:
            poly = np.polyfit(self.corr_list_db_Y, self.corr_list_sun_Y, deg=3)
            line = np.polyval(poly, self.corr_list_db_Y)

            self.ui.graph_out.plot(activity, power_db, pen=None, name="blue", symbol='o')
            self.ui.graph_out.plot(self.corr_list_db_Y, line, pen='g', symbolBrush=1)
        else:
            self.ui.graph_out.clear()

    def set_db_graph(self, time, db, clear):  # Вывод графика зависимости времени от db
        if not clear:
            self.ui.grap_db.plot(time, db)
        else:
            self.ui.grap_db.clear()

    def set_sun_graph(self, activity, time, clear):  # Вывод графика зависимости солнечной активности от времени
        if not clear:
            self.ui.graph_sun.plot(activity, time)
        else:
            self.ui.graph_sun.clear()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.setFixedSize(997, 486)
window.show()
app.exec()
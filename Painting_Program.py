from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # создаём окно программы
        self.setWindowTitle("Программа для рисования")
        self.setWindowIcon(QIcon('./icons/palitra.png'))
        for screen in QApplication.screens():
            a = screen.size().width()
            b = screen.size().height()
        self.setFixedSize(a, b)
        self.move(0, 0)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        # созаём параметры рисования
        self.risovanie = False
        self.razmer = 4
        self.zvet = Qt.black
        self.razmer_lastika = 4
        self.razmer_kisti = 4
        self.zvet_lastika = Qt.white
        self.zvet_kisti = Qt.black
        self.flag_kisti = True
        self.flag_lastika = False
        self.flag_linii = False
        self.flag = 1
        self.now = 'Кисть'

        # создаём перо
        self.ruchka = QPen()
        self.ruchka.setBrush(self.zvet)
        self.ruchka.setWidth(self.razmer)
        self.ruchka.setStyle(Qt.SolidLine)
        self.ruchka.setCapStyle(Qt.RoundCap)
        self.ruchka.setJoinStyle(Qt.RoundJoin)

        self.posled = QPoint()
        self.last = QPoint()

        # создаём панель меню
        mainmenu = self.menuBar()
        filemenu = mainmenu.addMenu("&Файл")
        instrument = mainmenu.addMenu("&Инструмент")
        b_size = mainmenu.addMenu("&Толщина")
        b_color = mainmenu.addMenu("&Цвет ")
        options = mainmenu.addMenu("&Параметры")
        tek = mainmenu.addMenu(f"&Текущий инструмент:")

        # Файл
        save_action = QAction(QIcon("./icons/save.png"), "Сохранить лист", self)
        save_action.setShortcut("Ctrl+S")
        filemenu.addAction(save_action)
        save_action.triggered.connect(self.save)

        clear_action = QAction(QIcon("./icons/clear.png"),  "Очистить лист", self)
        clear_action.setShortcut("Ctrl+R")
        filemenu.addAction(clear_action)
        clear_action.triggered.connect(self.clear)

        open_action = QAction(QIcon("./icons/papka.png"), "Открыть", self)
        open_action.setShortcut("Ctrl+O")
        filemenu.addAction(open_action)
        open_action.triggered.connect(self.open)
        filemenu.addSeparator()

        exit_action = QAction(QIcon("./icons/exit.png"), "Выйти", self)
        filemenu.addAction(exit_action)
        exit_action.triggered.connect(self.close)

        # Инструмент
        brush_action = QAction(QIcon("./icons/paint-brush.png"), "Кисть", self)
        brush_action.setShortcut("Ctrl+B")
        instrument.addAction(brush_action)
        brush_action.triggered.connect(self.brush)

        eraser_submenu = instrument.addMenu(QIcon("./icons/eraser.png"), "Ластик")

        line_submenu = instrument.addMenu(QIcon("./icons/line.png"), "Прямая линия")

        # Стиль прямой
        solid_action = QAction(QIcon('./icons/line.png'), "Цельная", self)
        solid_action.setShortcut("Ctrl+F")
        line_submenu.addAction(solid_action)
        solid_action.triggered.connect(self.solid)

        dash_action = QAction(QIcon('./icons/dashes.png'), "Отрывистая", self)
        dash_action.setShortcut("Ctrl+D")
        line_submenu.addAction(dash_action)
        dash_action.triggered.connect(self.dash)

        dot_action = QAction(QIcon('./icons/dots.png'), "Точечная", self)
        dot_action.setShortcut("Ctrl+Z")
        line_submenu.addAction(dot_action)
        dot_action.triggered.connect(self.dot)

        # Толщина
        pixeley_4 = QAction(QIcon("./icons/4.png"), "Очень тонкая", self)
        b_size.addAction(pixeley_4)
        pixeley_4.triggered.connect(self.pixeleyel_4)

        pixeley_7 = QAction(QIcon("./icons/7.png"), "Тонкая", self)
        b_size.addAction(pixeley_7)
        pixeley_7.triggered.connect(self.pixeleyel_7)

        pixeley_9 = QAction(QIcon("./icons/9.png"), "Средняя", self)
        b_size.addAction(pixeley_9)
        pixeley_9.triggered.connect(self.pixeleyel_9)

        pixeley_12 = QAction(QIcon("./icons/12.png"), "Толстая", self)
        b_size.addAction(pixeley_12)
        pixeley_12.triggered.connect(self.pixeleyel_12)

        pixeley_19 = QAction(QIcon("./icons/19.png"), "Очень толстая", self)
        b_size.addAction(pixeley_19)
        pixeley_19.triggered.connect(self.pixeleyel_19)
        b_size.addSeparator()

        own = QAction("Своя", self)
        b_size.addAction(own)
        own.triggered.connect(self.pixeleyel_other)

        # Размер ластика
        pixel_4 = QAction(QIcon("./icons/4.png"), "Очень тонкий", self)
        eraser_submenu.addAction(pixel_4)
        pixel_4.triggered.connect(self.pixeleye_4)

        pixel_7 = QAction(QIcon("./icons/7.png"), "Тонкий", self)
        eraser_submenu.addAction(pixel_7)
        pixel_7.triggered.connect(self.pixeleye_7)

        pixel_9 = QAction(QIcon("./icons/9.png"), "Средний", self)
        eraser_submenu.addAction(pixel_9)
        pixel_9.triggered.connect(self.pixeleye_9)

        pixel_12 = QAction(QIcon("./icons/12.png"), "Толстый", self)
        eraser_submenu.addAction(pixel_12)
        pixel_12.triggered.connect(self.pixeleye_12)

        pixel_19 = QAction(QIcon("./icons/19.png"), "Очень толстый", self)
        eraser_submenu.addAction(pixel_19)
        pixel_19.triggered.connect(self.pixeleye_19)
        eraser_submenu.addSeparator()

        own_e = QAction("Свой", self)
        eraser_submenu.addAction(own_e)
        own_e.triggered.connect(self.pixeleye_other)

        # Цвет
        red = QAction(QIcon("./icons/redd.png"), "Красный", self)
        b_color.addAction(red)
        red.triggered.connect(self.redcolor)

        orange = QAction(QIcon("./icons/orangee.png"), "Оранжевый", self)
        b_color.addAction(orange)
        orange.triggered.connect(self.orangecolor)

        yellow = QAction(QIcon("./icons/yelloww.png"), "Жёлтый", self)
        b_color.addAction(yellow)
        yellow.triggered.connect(self.yellowcolor)

        green = QAction(QIcon("./icons/greenn.png"), "Зелёный", self)
        b_color.addAction(green)
        green.triggered.connect(self.greencolor)

        l_blue = QAction(QIcon("./icons/l_bluee.png"), "Голубой", self)
        b_color.addAction(l_blue)
        l_blue.triggered.connect(self.light_bluecolor)

        blue = QAction(QIcon("./icons/bluee.png"), "Синий", self)
        b_color.addAction(blue)
        blue.triggered.connect(self.bluecolor)

        purple = QAction(QIcon("./icons/purplee.png"), "Фиолетовый", self)
        b_color.addAction(purple)
        purple.triggered.connect(self.purplecolor)

        black = QAction(QIcon("./icons/blackk.png"), "Черный", self)
        b_color.addAction(black)
        black.triggered.connect(self.blackcolor)

        white = QAction(QIcon("./icons/whitee.png"), "Белый", self)
        b_color.addAction(white)
        white.triggered.connect(self.whitecolor)
        b_color.addSeparator()

        other = QAction("Другой", self)
        b_color.addAction(other)
        other.triggered.connect(self.othercolor)

        # Параметры
        zvet_fona = QAction(QIcon("./icons/zalivka.png"), "Цвет фона", self)
        options.addAction(zvet_fona)
        zvet_fona.triggered.connect(self.bg_zvet)

        menu_color = QAction("Цвет панели меню", self)
        options.addAction(menu_color)
        menu_color.triggered.connect(self.menucolor)

        # Текущий инструмент
        self.brush_h = tek.addAction(QIcon("./icons/paint-brush.png"), 'Кисть')
        self.brush_h.triggered.connect(self.b_h)
        self.eraser_h = tek.addAction(QIcon("./icons/eraser.png"), 'Ластик')
        self.eraser_h.triggered.connect(self.e_h)
        self.solid_h = tek.addAction(QIcon("./icons/line.png"), 'Цельная прямая линия')
        self.solid_h.triggered.connect(self.so_h)
        self.dash_h = tek.addAction(QIcon("./icons/dashes.png"), 'Отрывистая прямая линия')
        self.dash_h.triggered.connect(self.da_h)
        self.dot_h = tek.addAction(QIcon("./icons/dots"), 'Точечная прямая линия')
        self.dot_h.triggered.connect(self.do_h)
        self.brush_h.setVisible(True)
        self.eraser_h.setVisible(False)
        self.solid_h.setVisible(False)
        self.dash_h.setVisible(False)
        self.dot_h.setVisible(False)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.risovanie = True
            self.posled = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.risovanie:
            if self.flag_linii:
                painter = QPainter(self.image)
                painter.setPen(self.ruchka)
                painter.drawPoint(self.posled)
                self.update()
            else:
                painter = QPainter(self.image)
                painter.setPen(self.ruchka)
                painter.drawLine(self.posled, event.pos())
                self.posled = event.pos()
                self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.risovanie = False
            self.last = event.pos()
            if self.flag_linii:
                painter = QPainter(self.image)
                painter.setPen(self.ruchka)
                painter.drawLine(self.posled, self.last)
                self.update()

    def paintEvent(self, event):
        risovat = QPainter(self)
        risovat.drawImage(self.rect(), self.image, self.image.rect())

    # Файл
    def save(self):
        file, _ = QFileDialog.getSaveFileName(self, "Сохранить лист", "",
                                                    "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if file == "":
            return
        self.image.save(file)

    def clear(self):
        self.image.fill(Qt.white)
        self.setStyleSheet("background-color: {}".format(Qt.white))
        self.zvet_lastika = Qt.white
        self.zvet = self.zvet_kisti
        self.razmer = self.razmer_kisti
        self.ruchka.setBrush(self.zvet)
        self.ruchka.setWidth(self.razmer)
        self.ruchka.setStyle(Qt.SolidLine)
        self.flag_linii = False
        self.flag_kisti = True

        self.update()

    def open(self):
        for screen in QApplication.screens():
            a = screen.size().width()
            b = screen.size().height()
        QMessageBox.warning(self, "Важно!", f"Выберите картинку разрешением до {a} x {b}")

        file = QFileDialog.getOpenFileName(self, f"Выберите картинку разрешением до {a} x {b}", '')[0]
        ex = QImageReader(file).size()
        w = ex.width()
        h = ex.height()
        if w > a and h > b:
            QMessageBox.critical(self, "Ошибка!", f"Разрешение выбранного фото больше, чем {a} x {b}")
        if file != "" and w <= a and h <= b:
            self.move(0, 0)
            self.setFixedSize(w, h)
            self.image.load(file)
            self.zvet_lastika = Qt.white
            if self.flag_lastika:
                self.zvet = self.zvet_lastika
            self.ruchka.setBrush(self.zvet)
            self.ruchka.setWidth(self.razmer)
            self.update()

    def close(self):
        QCoreApplication.quit()

    # Инструмент
    def brush(self):
        self.zvet = self.zvet_kisti
        self.razmer = self.razmer_kisti
        self.flag_kisti = True
        self.flag_lastika = False
        self.flag_linii = False
        self.now = 'Кисть'

        self.ruchka.setStyle(Qt.SolidLine)
        self.ruchka.setBrush(self.zvet)
        self.ruchka.setWidth(self.razmer)

        self.brush_h.setVisible(True)
        self.eraser_h.setVisible(False)
        self.solid_h.setVisible(False)
        self.dash_h.setVisible(False)
        self.dot_h.setVisible(False)

    # Стиль прямой
    def solid(self):
        self.flag = 1
        self.flag_linii = True
        self.flag_lastika = False
        self.zvet = self.zvet_kisti
        self.razmer = self.razmer_kisti
        self.ruchka.setStyle(Qt.SolidLine)
        self.ruchka.setBrush(self.zvet)
        self.ruchka.setWidth(self.razmer)
        self.now = 'Прямая'
        self.brush_h.setVisible(False)
        self.eraser_h.setVisible(False)
        self.solid_h.setVisible(True)
        self.dash_h.setVisible(False)
        self.dot_h.setVisible(False)
        self.update()

    def dash(self):
        self.flag = 2
        self.flag_linii = True
        self.flag_lastika = False
        self.zvet = self.zvet_kisti
        self.razmer = self.razmer_kisti
        self.ruchka.setStyle(Qt.DashLine)
        self.ruchka.setBrush(self.zvet)
        self.ruchka.setWidth(self.razmer)
        self.now = 'Прямая'
        self.brush_h.setVisible(False)
        self.eraser_h.setVisible(False)
        self.solid_h.setVisible(False)
        self.dash_h.setVisible(True)
        self.dot_h.setVisible(False)
        self.update()

    def dot(self):
        self.flag = 3
        self.flag_linii = True
        self.flag_lastika = False
        self.zvet = self.zvet_kisti
        self.razmer = self.razmer_kisti
        self.ruchka.setStyle(Qt.DotLine)
        self.ruchka.setBrush(self.zvet)
        self.ruchka.setWidth(self.razmer)
        self.now = 'Прямая'
        self.brush_h.setVisible(False)
        self.eraser_h.setVisible(False)
        self.solid_h.setVisible(False)
        self.dash_h.setVisible(False)
        self.dot_h.setVisible(True)
        self.update()

    # Толщина
    def pixeleyel_4(self):
        self.razmer_kisti = 4
        if self.flag_kisti:
            self.razmer = 4
            self.ruchka.setWidth(self.razmer)

    def pixeleyel_7(self):
        self.razmer_kisti = 7
        if self.flag_kisti:
            self.razmer = 7
            self.ruchka.setWidth(self.razmer)

    def pixeleyel_9(self):
        self.razmer_kisti = 9
        if self.flag_kisti:
            self.razmer = 9
            self.ruchka.setWidth(self.razmer)

    def pixeleyel_12(self):
        self.razmer_kisti = 12
        if self.flag_kisti:
            self.razmer = 12
            self.ruchka.setWidth(self.razmer)

    def pixeleyel_19(self):
        self.razmer_kisti = 19
        if self.flag_kisti:
            self.razmer = 19
            self.ruchka.setWidth(self.razmer)

    def pixeleyel_other(self):
        width, ok_pressed = QInputDialog.getInt(self, " ", "Толщина:", 10, 1, 1000, 1)
        if ok_pressed:
            self.razmer_kisti = width
            if self.flag_kisti:
                self.razmer = width
                self.ruchka.setWidth(self.razmer)

    # Размер ластика
    def pixeleye_4(self):
        self.razmer_lastika = 4
        self.razmer = 4
        self.ruchka.setWidth(self.razmer)
        self.zvet = self.zvet_lastika
        self.razmer = self.razmer_lastika
        self.flag_lastika = True
        self.flag_kisti = False
        self.flag_linii = False
        self.now = 'Ластик'
        self.ruchka.setBrush(self.zvet)
        self.ruchka.setWidth(self.razmer)
        self.brush_h.setVisible(False)
        self.eraser_h.setVisible(True)
        self.solid_h.setVisible(False)
        self.dash_h.setVisible(False)
        self.dot_h.setVisible(False)

    def pixeleye_7(self):
        self.razmer_lastika = 7
        self.razmer = 7
        self.ruchka.setWidth(self.razmer)
        self.zvet = self.zvet_lastika
        self.razmer = self.razmer_lastika
        self.flag_lastika = True
        self.flag_kisti = False
        self.flag_linii = False
        self.now = 'Ластик'
        self.ruchka.setBrush(self.zvet)
        self.ruchka.setWidth(self.razmer)
        self.brush_h.setVisible(False)
        self.eraser_h.setVisible(True)
        self.solid_h.setVisible(False)
        self.dash_h.setVisible(False)
        self.dot_h.setVisible(False)

    def pixeleye_9(self):
        self.razmer_lastika = 9
        self.razmer = 9
        self.ruchka.setWidth(self.razmer)
        self.zvet = self.zvet_lastika
        self.razmer = self.razmer_lastika
        self.flag_lastika = True
        self.flag_kisti = False
        self.flag_linii = False
        self.now = 'Ластик'
        self.ruchka.setBrush(self.zvet)
        self.ruchka.setWidth(self.razmer)
        self.brush_h.setVisible(False)
        self.eraser_h.setVisible(True)
        self.solid_h.setVisible(False)
        self.dash_h.setVisible(False)
        self.dot_h.setVisible(False)

    def pixeleye_12(self):
        self.razmer_lastika = 12
        self.razmer = 12
        self.ruchka.setWidth(self.razmer)
        self.zvet = self.zvet_lastika
        self.razmer = self.razmer_lastika
        self.flag_lastika = True
        self.flag_kisti = False
        self.flag_linii = False
        self.now = 'Ластик'
        self.ruchka.setBrush(self.zvet)
        self.ruchka.setWidth(self.razmer)
        self.brush_h.setVisible(False)
        self.eraser_h.setVisible(True)
        self.solid_h.setVisible(False)
        self.dash_h.setVisible(False)
        self.dot_h.setVisible(False)

    def pixeleye_19(self):
        self.razmer_lastika = 19
        self.razmer = 19
        self.ruchka.setWidth(self.razmer)
        self.zvet = self.zvet_lastika
        self.razmer = self.razmer_lastika
        self.flag_lastika = True
        self.flag_kisti = False
        self.flag_linii = False
        self.now = 'Ластик'
        self.ruchka.setBrush(self.zvet)
        self.ruchka.setWidth(self.razmer)
        self.brush_h.setVisible(False)
        self.eraser_h.setVisible(True)
        self.solid_h.setVisible(False)
        self.dash_h.setVisible(False)
        self.dot_h.setVisible(False)

    def pixeleye_other(self):
        width, ok_pressed = QInputDialog.getInt(self, " ", "Толщина:", 10, 1, 1000, 1)
        if ok_pressed:
            self.razmer_lastika = width
            self.razmer = width
            self.ruchka.setWidth(self.razmer)
            self.zvet = self.zvet_lastika
            self.razmer = self.razmer_lastika
            self.flag_lastika = True
            self.flag_kisti = False
            self.flag_linii = False
            self.now = 'Ластик'
            self.ruchka.setBrush(self.zvet)
            self.ruchka.setWidth(self.razmer)
            self.brush_h.setVisible(False)
            self.eraser_h.setVisible(True)
            self.solid_h.setVisible(False)
            self.dash_h.setVisible(False)
            self.dot_h.setVisible(False)

    # Цвет
    def redcolor(self):
        self.zvet_kisti = QColor(255, 0, 0)
        if self.flag_kisti:
            self.zvet = QColor(255, 0, 0)
            self.ruchka.setBrush(self.zvet)

    def orangecolor(self):
        self.zvet_kisti = QColor(255, 102, 0)
        if self.flag_kisti:
            self.zvet = QColor(255, 102, 0)
            self.ruchka.setBrush(self.zvet)

    def yellowcolor(self):
        self.zvet_kisti = QColor(255, 255, 0)
        if self.flag_kisti:
            self.zvet = QColor(255, 255, 0)
            self.ruchka.setBrush(self.zvet)

    def greencolor(self):
        self.zvet_kisti = QColor(0, 255, 0)
        if self.flag_kisti:
            self.zvet = QColor(0, 255, 0)
            self.ruchka.setBrush(self.zvet)

    def purplecolor(self):
        self.zvet_kisti = QColor(139, 0, 255)
        if self.flag_kisti:
            self.zvet = QColor(139, 0, 255)
            self.ruchka.setBrush(self.zvet)

    def light_bluecolor(self):
        self.zvet_kisti = QColor(128, 166, 255)
        if self.flag_kisti:
            self.zvet = QColor(128, 166, 255)
            self.ruchka.setBrush(self.zvet)

    def bluecolor(self):
        self.zvet_kisti = QColor(0, 0, 255)
        if self.flag_kisti:
            self.zvet = QColor(0, 0, 255)
            self.ruchka.setBrush(self.zvet)

    def blackcolor(self):
        self.zvet_kisti = Qt.black
        if self.flag_kisti:
            self.zvet = Qt.black
            self.ruchka.setBrush(self.zvet)

    def whitecolor(self):
        self.zvet_kisti = Qt.white
        if self.flag_kisti:
            self.zvet = Qt.white
            self.ruchka.setBrush(self.zvet)

    def othercolor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.zvet_kisti = color
            if self.flag_kisti:
                self.zvet = color
                self.ruchka.setBrush(self.zvet)

    # Параметры
    def bg_zvet(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.image.fill(color)
            self.zvet_lastika = color
            if self.flag_lastika:
                self.ruchka.setBrush(color)

    def menucolor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet("background-color: {}".format(color.name()))

    # Текущий инструмент
    def b_h(self):
        pass

    def e_h(self):
        pass

    def so_h(self):
        pass

    def da_h(self):
        pass

    def do_h(self):
        pass


App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())

import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import Qt


class Route(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Route")
        self.setWindowIcon(QIcon("static\icon.jpg"))
        self.setGeometry(850, 200, 400, 400)

        self.BasePath = os.getcwd()
        self.File_Path = "static"

        self.Image()


    def Image(self):

        path = os.path.join(self.BasePath, self.File_Path, "Route.png")
        image_label = QLabel()

        image_label.setPixmap(QPixmap(path))
        layout = QHBoxLayout(self)
        layout.addWidget(image_label)



class Route2(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Route")
        self.setWindowIcon(QIcon("static\icon.jpg"))
        self.setGeometry(850, 200, 400, 400)

        self.BasePath = os.getcwd()
        self.File_Path = "static"

        self.Tabs()
        self.Image()


    def Tabs(self):

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        self.FirstTab = QWidget()
        self.SecondTab = QWidget()

        self.tabs.addTab(self.FirstTab, "Clothoid")
        self.tabs.addTab(self.SecondTab, "Transition Curve")


    def Image(self):

        path1 = os.path.join(self.BasePath, self.File_Path, "Clothoid.png")
        path2 = os.path.join(self.BasePath, self.File_Path, "Route_With_Transition_Curve.png")

        image_label1 = QLabel()
        image_label2 = QLabel()

        image_label1.setPixmap(QPixmap(path1))
        image_label2.setPixmap(QPixmap(path2))

        layout1 = QHBoxLayout(self)
        layout1.addWidget(image_label1)
        layout2 = QHBoxLayout(self)
        layout2.addWidget(image_label2)

        self.FirstTab.setLayout(layout1)
        self.SecondTab.setLayout(layout2)


class Route3(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Route")
        self.setWindowIcon(QIcon("static\icon.jpg"))
        self.setGeometry(350, 100, 400, 400)

        self.BasePath = os.getcwd()
        self.File_Path = "static"

        self.Image()


    def Image(self):

        path = os.path.join(self.BasePath, self.File_Path, "Transition_Curves.png")
        image_label = QLabel()

        image_label.setPixmap(QPixmap(path))
        layout = QHBoxLayout(self)
        layout.addWidget(image_label)



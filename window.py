import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout, QTabWidget, QLabel, QLineEdit, QListWidget, QMessageBox, QComboBox, QRadioButton
from PyQt5.QtGui import QIcon, QFont

from Popups import *

import numpy as np




def Grad2Radyan(angle):
    return (angle * np.pi) / 200

def Radyan2Grad(Radyan):
    return (Radyan * 200) / np.pi

def Grad2Degree(Grad):
    return (Grad * 9) / 10

def Degree2Grad(Degree):
    return (Degree * 10) / 9

def Azimuth(YA, XA, YB, XB):

    DeltaY = (YB - YA)
    DeltaX = (XB - XA)

    tAB = np.round(Radyan2Grad(np.arctan(DeltaY / DeltaX)), 4)

    if DeltaY >= 0:
        if DeltaX >= 0:
            tAB = tAB
        else:
            tAB = tAB + 200
    else:
        if DeltaX >= 0:
            tAB = tAB + 400
        else:
            tAB = tAB + 200

    return tAB



class Window(QMainWindow):

    def __init__(self):

        super().__init__()

        self.width = 1280
        self.height = 720

        self.setWindowTitle("Surveying App 4.0.1")
        self.setGeometry(350, 150, self.width, self.height)
        self.setWindowIcon(QIcon("static\icon.jpg"))

        self.Tabs()
        self.Widgets1()
        self.Layouts1()
        self.Widgets2()
        self.Layouts2()
        self.Widgets3()
        self.Layouts3()

        self.show()


    def Tabs(self):

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.Fundamental = QWidget()
        self.SecondTab = QWidget()
        self.ThirdTab = QWidget()

        self.tabs.addTab(self.Fundamental, "Fundamental Computations")
        self.tabs.addTab(self.SecondTab, "Route Geometry")
        self.tabs.addTab(self.ThirdTab, "Transition Curve")


    def Widgets1(self):

        # Temel Ödevler
        # 1. Temel ödev
        self.YA1Label = QLabel("YA: ")
        self.XA1Label = QLabel("XA: ")

        self.YA1 = QLineEdit()
        self.YA1.setMaximumWidth(150)
        self.XA1 = QLineEdit()
        self.XA1.setMaximumWidth(150)

        self.tAB1Label = QLabel("t(AB):")
        self.tAB1 = QLineEdit()
        self.tAB1.setMaximumWidth(150)

        self.SAB1Label = QLabel("S(AB): ")
        self.SAB1 = QLineEdit()
        self.SAB1.setMaximumWidth(150)

        self.button111 = QPushButton("Calculate")
        self.button111.setMaximumWidth(150)
        self.button111.clicked.connect(self.FirstFundamentalFunction)

        self.clearbutton111 = QPushButton("Clear")
        self.clearbutton111.setMaximumWidth(150)
        self.clearbutton111.clicked.connect(self.clear111Function)

        self.YB1Label = QLabel("YB = ")
        self.XB1Label = QLabel("XB = ")

        # 2. Temel Ödev
        self.YA2Label = QLabel("YA: ")
        self.XA2Label = QLabel("XA: ")

        self.YA2 = QLineEdit()
        self.YA2.setMaximumWidth(150)
        self.XA2 = QLineEdit()
        self.XA2.setMaximumWidth(150)

        self.YB2Label = QLabel("YB: ")
        self.XB2Label = QLabel("XB: ")

        self.YB2 = QLineEdit()
        self.YB2.setMaximumWidth(150)
        self.XB2 = QLineEdit()
        self.XB2.setMaximumWidth(150)

        self.button112 = QPushButton("Calculate")
        self.button112.setMaximumWidth(150)
        self.button112.clicked.connect(self.SecondFundamentalFunction)

        self.clearbutton112 = QPushButton("Clear")
        self.clearbutton112.setMaximumWidth(200)
        self.clearbutton112.clicked.connect(self.clear112Function)

        self.SAB2Label = QLabel("S(AB) = ")
        self.tAB2Label = QLabel("t(AB) = ")
        self.tBA2Label = QLabel("t(BA) = ")

        # 3. temel ödev
        self.tAB3Label = QLabel("t(AB)")
        self.tAB3 = QLineEdit()
        self.tAB3.setMaximumWidth(150)

        self.BetaBLabel3 = QLabel("ßB:")
        self.BetaB = QLineEdit()
        self.BetaB.setMaximumWidth(150)

        self.button113 = QPushButton("Calculate")
        self.button113.setMaximumWidth(150)
        self.button113.clicked.connect(self.ThirdFundamentalFunction)

        self.clearbutton113 = QPushButton("Clear")
        self.clearbutton113.setMaximumWidth(150)
        self.clearbutton113.clicked.connect(self.clear113Function)

        self.tBC3Label = QLabel("t(BC) = ")

        # Mühendislik Ölçmeleri
        # Horizontal Layout with Polar Coordianates
        self.Gauss_KruegerLabel = QLabel("Gauss-Krueger Radius : 6376.8 (km)")
        self.Gauss_Krueger = QLineEdit()
        self.Gauss_Krueger.setMaximumWidth(150)

        self.Geoid_UndulationLabel = QLabel("Geoid Undulation :  (m)")
        self.Geoid_Undulation = QLineEdit()
        self.Geoid_Undulation.setMaximumWidth(150)

        self.YP101Label = QLabel("Y(P101) : ")
        self.YP101 = QLineEdit()
        self.YP101.setMaximumWidth(150)

        self.XP101Label = QLabel("X(P101) : ")
        self.XP101 = QLineEdit()
        self.XP101.setMaximumWidth(150)

        self.H_orth_P101Label = QLabel("H(orthometric) for P101 : (m)")
        self.H_orth_P101 = QLineEdit()
        self.H_orth_P101.setMaximumWidth(150)

        self.YP102Label = QLabel("Y(P102): ")
        self.YP102 = QLineEdit()
        self.YP102.setMaximumWidth(150)

        self.XP102Label = QLabel("X(P102): ")
        self.XP102 = QLineEdit()
        self.XP102.setMaximumWidth(150)

        self.YPLabel = QLabel("Y(P): ")
        self.YP = QLineEdit()
        self.YP.setMaximumWidth(150)

        self.XPLabel = QLabel("X(P): ")
        self.XP = QLineEdit()
        self.XP.setMaximumWidth(150)

        self.sigma_pLabel = QLabel("\u03C3_p = ")
        self.sigma_p = QLineEdit()
        self.sigma_p.setMaximumWidth(150)

        self.clearbutton12 = QPushButton("Clear")
        self.clearbutton12.setMaximumWidth(150)
        self.clearbutton12.clicked.connect(self.clear121Function)

        self.button12 = QPushButton("Calculate")
        self.button12.setMaximumWidth(150)
        self.button12.clicked.connect(self.button121Function)

        self.outputList1 = QListWidget()
        self.outputList1.addItems(["S(P101,P) = ", "Ym = ",  "Se = ",  "Sg = ",  "S(AP) = ", "t(P101,P) = ", "t(P101,P102) = ", "\u03B2 = "])


        # Centering Error at Layout Point
        self.sigma_lqLabel = QLabel("\u03C3_lq : ")
        self.sigma_lq = QLineEdit()
        self.sigma_lq.setPlaceholderText("2+3ppm")
        self.sigma_lq.setMaximumWidth(150)

        self.sigma_rLabel = QLabel("\u03C3_r : (cc)")
        self.sigma_r = QLineEdit()
        self.sigma_r.setMaximumWidth(150)

        self.esLabel = QLabel("e(s) : (mm)")
        self.es = QLineEdit()
        self.es.setMaximumWidth(150)

        self.etLabel = QLabel("e(t) : (mm)")
        self.et = QLineEdit()
        self.et.setMaximumWidth(150)

        self.elLabel = QLabel("e(L) : (mm)")
        self.el = QLineEdit()
        self.el.setMaximumWidth(150)

        self.SP101_A22Label = QLabel("S(P101-A) : (m)")
        self.SP101_A_22 = QLineEdit()
        self.SP101_A_22.setMaximumWidth(150)

        self.SP101_P102_22Label = QLabel("S(P101-P102) : (m)")
        self.SP101_P102_22 = QLineEdit()
        self.SP101_P102_22.setMaximumWidth(150)

        self.Beta_22Label = QLabel("\u03B2 : (g)")
        self.Beta_22 = QLineEdit()
        self.Beta_22.setMaximumWidth(150)

        self.n_22Label = QLabel("Number of Repetation (n) : ")
        self.n_22 = QLineEdit()
        self.n_22.setMaximumWidth(150)

        self.clearbutton13 = QPushButton("Clear")
        self.clearbutton13.setMaximumWidth(150)
        self.clearbutton13.clicked.connect(self.clear122Function)

        self.button13 = QPushButton("Calculate")
        self.button13.setMaximumWidth(150)
        self.button13.clicked.connect(self.button122Function)

        self.outputList2 = QListWidget()
        self.outputList2.addItems([ "\u03C3_qs = ", "\u03C3_qq = ", "\u03C3_qt = ", "\u03C3_ls = ", "\u03C3_ll = ", "\u03C3_ql = ", "\u03C3_lq = ", "\u03C3_q = ", "\u03C3_l = ", "\u03C3_p = "])


    def clear111Function(self):

        self.YA1.clear()
        self.XA1.clear()
        self.SAB1.clear()
        self.tAB1.clear()
        self.YB1Label.setText("YB = ")
        self.XB1Label.setText("XB = ")


    def clear112Function(self):

        self.YA2.clear()
        self.XA2.clear()
        self.YB2.clear()
        self.XB2.clear()
        self.SAB2Label.setText("S(AB) = ")
        self.tAB2Label.setText("t(AB) = ")
        self.tBA2Label.setText("t(BA) = ")


    def clear113Function(self):

        self.tAB3.clear()
        self.BetaB.clear()
        self.tBC3Label.setText("t(BC) = ")


    def FirstFundamentalFunction(self):

        try:
            YB = float(self.YA1.text()) + float(self.SAB1.text()) * np.sin(Grad2Radyan(float(self.tAB1.text())))
            YB = np.round(YB, 3)
            XB = float(self.XA1.text()) + float(self.SAB1.text()) * np.cos(Grad2Radyan(float(self.tAB1.text())))
            XB = np.round(XB, 3)

            self.YB1Label.setText("YB = " + str(YB))
            self.XB1Label.setText("XB = " + str(XB))

        except:
            QMessageBox.warning(self, "Hata!", "Lütfen YA, XA, S(AB) ve t(AB) değerlerini doğru giriniz")


    def SecondFundamentalFunction(self):

        try:
            DeltaYAB = (float(self.YB2.text()) - float(self.YA2.text()))
            DeltaXAB = (float(self.XB2.text()) - float(self.XA2.text()))
            DeltaYBA = (float(self.YA2.text()) - float(self.YB2.text()))
            DeltaXBA = (float(self.XA2.text()) - float(self.XB2.text()))

            SAB = np.round((DeltaYAB ** 2 + DeltaXAB ** 2) ** 0.5, 3)
            tAB = np.round(Radyan2Grad(np.round(np.arctan(DeltaYAB / DeltaXAB), 4)), 4)
            tBA = np.round(Radyan2Grad(np.round(np.arctan(DeltaYBA / DeltaXBA), 4)), 4)

            if DeltaYAB >= 0:
                if DeltaXAB >= 0:
                    tAB = tAB
                else:
                    tAB = tAB + 200
            else:
                if DeltaXAB >= 0:
                    tAB = tAB + 400
                else:
                    tAB = tAB + 200

            if DeltaYBA >= 0:
                if DeltaXBA >= 0:
                    tBA = tBA
                else:
                    tBA = tBA + 200
            else:
                if DeltaXBA >= 0:
                    tBA = tBA + 400
                else:
                    tBA = tBA + 200

            self.SAB2Label.setText("S(AB) = " + str(SAB))
            self.tAB2Label.setText("t(AB) = " + str(tAB))
            self.tBA2Label.setText("t(BA) = " + str(tBA))

        except:
            QMessageBox.warning(self, "Hata!", "Lütfen YA, XA, YB ve XB değerlerini doğru giriniz")



    def ThirdFundamentalFunction(self):

        try:
            tBC = float(self.tAB3.text()) + float(self.BetaB.text())

            if tBC >= 200:
                tBC = tBC - 200
                if tBC >= 400:
                    tBC = tBC - 400
            elif tBC < 200:
                tBC = tBC + 200
            else:
                tBC = tBC

            tBC = np.round(tBC, 4)
            self.tBC3Label.setText("t(BC) = " + str(tBC))


        except:
            QMessageBox.warning(self, "Hata!", "Lütfen t(AB) ve ßB değerlerini doğru giriniz")


    def clear121Function(self):

        self.Gauss_Krueger.clear()
        self.Geoid_Undulation.clear()
        self.YP101.clear()
        self.XP101.clear()
        self.H_orth_P101.clear()
        self.YP102.clear()
        self.XP102.clear()
        self.YP.clear()
        self.XP.clear()
        self.outputList1.clear()
        self.outputList1.addItems([
            "S(P101,P) = ",
            "Ym = ",
            "Se = ",
            "Sg = ",
            "S(AP) = ",
            "t(P101,P) = ",
            "t(P101,P102) = ",
            "\u03B2 = "
        ])


    def clear122Function(self):

        self.sigma_lq.clear()
        self.sigma_r.clear()
        self.es.clear()
        self.et.clear()
        self.el.clear()
        self.SP101_A_22.clear()
        self.SP101_P102_22.clear()
        self.Beta_22.clear()
        self.n_22.clear()
        self.sigma_p.clear()
        self.outputList2.clear()
        self.outputList2.addItems([
            "\u03C3_qs = ",
            "\u03C3_qq = ",
            "\u03C3_qt = ",
            "\u03C3_ls = ",
            "\u03C3_ll = ",
            "\u03C3_ql = ",
            "\u03C3_lq = ",
            "\u03C3_q = ",
            "\u03C3_l = ",
            "\u03C3_p = "
        ])


    def button121Function(self):

        if self.Gauss_Krueger.text() != "":
            R = float(self.Gauss_Krueger.text())
        else:
            R = 6376.8

        try:
            NA = float(self.Geoid_Undulation.text())
            YP101 = float(self.YP101.text())
            XP101 = float(self.XP101.text())
            HA = float(self.H_orth_P101.text())
            YP102 = float(self.YP102.text())
            XP102 = float(self.XP102.text())
            YP = float(self.YP.text())
            XP = float(self.XP.text())
        except:
            QMessageBox.warning(self, "Hata!", "Lütfen bütün değerler sayı olarak giriniz")
            return

        Sp = np.round(np.sqrt((YP101 - YP) ** 2 + (XP101 - XP) ** 2), 3)
        Ym = np.round(- ((YP101 - 500000) + (YP - 500000)) / 2, 3)
        Se = np.round(Sp / (1 + (Ym ** 2 / (2 * (R * 1000) ** 2))), 3)
        Sg = np.round(Se * (1 + (NA / (6376.8 * 1000))), 3)
        SAP = np.round(Sg * (((R * 1000) + HA) / (R * 1000)), 3)


        DeltaY_P101_P102 = YP102 - YP101
        DeltaX_P101_P102 = XP102 - XP101
        DeltaY_P101_P = YP - YP101
        DeltaX_P101_P = XP - XP101

        t_P101_P = np.round(Radyan2Grad(np.arctan(DeltaY_P101_P / DeltaX_P101_P)), 4)
        t_P101_P102 = np.round(Radyan2Grad(np.arctan(DeltaY_P101_P102 / DeltaX_P101_P102)), 4)

        if DeltaY_P101_P102 >= 0:
            if DeltaX_P101_P102 >= 0:
                t_P101_P102 = t_P101_P102
            else:
                t_P101_P102 = t_P101_P102 + 200

        else:
            if DeltaX_P101_P102 >= 0:
                t_P101_P102 = t_P101_P102 + 400
            else:
                t_P101_P102 = t_P101_P102 + 200

        if DeltaY_P101_P >= 0:
            if DeltaX_P101_P >= 0:
                t_P101_P = t_P101_P
            else:
                t_P101_P= t_P101_P + 200
        else:
            if DeltaX_P101_P >= 0:
                t_P101_P = t_P101_P + 400
            else:
                t_P101_P = t_P101_P + 200

        Beta = np.round(t_P101_P - t_P101_P102, 4)
        if Beta < 0:
            Beta += 400

        self.outputList1.clear()
        self.outputList1.addItems([
            "S(P101,P) = {}m".format(str(Sp)),
            "Ym = {}".format(str(Ym)),
            "Se = {}m".format(str(Se)),
            "Sg = {}m".format(str(Sg)),
            "S(AP) = {}m".format(str(SAP)),
            "t(P101,P) = {}g".format(str(t_P101_P)),
            "t(P101,P102) = {}g".format(str(t_P101_P102)),
            "\u03B2 = {}g".format(str(Beta))
        ])



    def button122Function(self):

        def Forward():

            if S and n and sigma_r:
                sigma_qq = np.round((S * ((2 / n) ** 0.5) * (sigma_r / Ro)) * 1000, 2)
            else:
                sigma_qq = ""

            if sigma_qs != "" and sigma_qt != "" and sigma_ql != "" and sigma_qq != "":
                sigma_q = np.round(np.sqrt((sigma_qs + sigma_qt + sigma_ql) ** 2 + sigma_qq ** 2), 3)

            else:
                sigma_q = ""

            if sigma_ls != "" and sigma_ll != "" and sigma_lq != "":
                sigma_l = np.round(np.sqrt((sigma_ls + sigma_ll) ** 2 + sigma_lq ** 2), 3)

            else:
                sigma_l = ""

            if sigma_q != "" and sigma_l != "":
                sigma_p = np.round(np.sqrt(sigma_q ** 2 + sigma_l ** 2), 3)

            else:
                sigma_p = ""

            self.outputList2.clear()
            self.outputList2.addItems([
                "\u03C3_qs = {}mm".format(str(sigma_qs)),
                "\u03C3_qq = {}mm".format(str(sigma_qq)),
                "\u03C3_qt = {}mm".format(str(sigma_qt)),
                "\u03C3_ls = {}mm".format(str(sigma_ls)),
                "\u03C3_ll = {}mm".format(str(sigma_ll)),
                "\u03C3_ql = {}mm".format(str(sigma_ql)),
                "\u03C3_lq = {}mm".format(str(sigma_lq)),
                "\u03C3_q = {}mm".format(str(sigma_q)),
                "\u03C3_l = {}mm".format(str(sigma_l)),
                "\u03C3_p = {}mm".format(str(sigma_p))
            ])


        def Backward():

            sigma_l = np.round(np.sqrt((sigma_ls + sigma_ll) ** 2 + sigma_lq ** 2), 2)
            if sigma_p:
                sigma_q = np.round(np.sqrt(sigma_p ** 2 - sigma_l ** 2), 2)
            else:
                raise ValueError("That is not a positive number!")
            sigma_qq = np.round((sigma_q ** 2 - (sigma_qs + sigma_qt + sigma_ql) ** 2) ** 0.5, 2)
            n = np.round(((S * np.sqrt(2) * sigma_r) / ((sigma_qq / 1000) * Ro)) ** 2, 2)


            self.outputList2.clear()
            self.outputList2.addItems([
                "\u03C3_qs = {}mm".format(str(sigma_qs)),
                "\u03C3_qq = {}mm".format(str(sigma_qq)),
                "\u03C3_qt = {}mm".format(str(sigma_qt)),
                "\u03C3_ls = {}mm".format(str(sigma_ls)),
                "\u03C3_ll = {}mm".format(str(sigma_ll)),
                "\u03C3_ql = {}mm".format(str(sigma_ql)),
                "\u03C3_lq = {}mm".format(str(sigma_lq)),
                "\u03C3_q = {}mm".format(str(sigma_q)),
                "\u03C3_l = {}mm".format(str(sigma_l)),
                "\u03C3_p = {}mm".format(str(sigma_p)),
                "n = {}".format(str(n))
            ])


        Ro = 2000000 / np.pi

        if self.sigma_lq.text() != "":
            try:
                sigma_lq = (self.sigma_lq.text())
                a = float(sigma_lq.split("+")[0])
                c = float(sigma_lq.split("+")[1][0])
            except:
                QMessageBox.warning(self, "Hata!", "Lütfen \u03C3_lq değerini a+cppm (örnek: 3+4ppm) şeklinde giriniz.")
                return
        else:
            sigma_lq = False
            a = False
            c = False

        if self.sigma_r.text() != "":
            sigma_r = float(self.sigma_r.text())
        else:
            sigma_r = False

        if self.es.text() != "":
            es = float(self.es.text())
        else:
            es = False

        if self.et.text() != "":
            et = float(self.et.text())
        else:
            et = False

        if self.el.text() != "":
            el = float(self.el.text())
        else:
            el = False

        if self.SP101_A_22.text() != "":
            S = float(self.SP101_A_22.text())
        else:
            S = False

        if self.SP101_P102_22.text() != "":
            b = float(self.SP101_P102_22.text())
        else:
            b = False

        if self.Beta_22.text() != "":
            Beta = float(self.Beta_22.text())
        else:
            Beta = False

        if self.n_22.text() != "":
            n = float(self.n_22.text())
        else:
            n = False


        if es and b and Beta and S:
            sigma_qs = np.round((((es / 1000) / (3 * b)) * np.sqrt(b ** 2 - 2 * b * S * np.cos(Grad2Radyan(Beta)) + S ** 2)) * 1000, 2)
            sigma_ls = np.round(((es / 1000) / 3) * 1000, 2)
        else:
            sigma_qs = ""
            sigma_ls = ""

        if et and b:
            sigma_qt = np.round(((S * (et / 1000)) / (3 * b)) * 1000, 2)
        else:
            sigma_qt = ""

        if el:
            sigma_ll = np.round(((el / 1000) / 3) * 1000, 2)
            sigma_ql = np.round(((el / 1000) / 3) * 1000, 2)
        else:
            sigma_ll = ""
            sigma_ql = ""

        if a and c and S:
            sigma_lq = np.round((a ** 2 + c ** 2 * (S / 1000) ** 2) ** 0.5, 3)
        else:
            sigma_lq = ""


        if self.sigma_p.text() == "":
            Forward()

        else:
            try:
                sigma_p = float(self.sigma_p.text())
                Backward()
            except:
                Forward()


    def Layouts1(self):

        # Temel Ödevler
        mainlayout = QHBoxLayout()

        # 1. Temel Ödev
        FirstMainLayout = QVBoxLayout()

        hbox111 = QHBoxLayout()
        hbox112 = QHBoxLayout()
        hbox113 = QHBoxLayout()
        hbox114 = QHBoxLayout()
        hbox115 = QHBoxLayout()
        hbox116 = QHBoxLayout()
        hbox117 = QHBoxLayout()
        vbox11 = QVBoxLayout()

        TopLayoutGroupBox = QGroupBox("1. Fundamental Surveying")
        hbox111.addWidget(self.YA1Label)
        hbox111.addWidget(self.YA1)
        hbox112.addWidget(self.XA1Label)
        hbox112.addWidget(self.XA1)
        hbox113.addWidget(self.tAB1Label)
        hbox113.addWidget(self.tAB1)
        hbox114.addWidget(self.SAB1Label)
        hbox114.addWidget(self.SAB1)
        hbox115.addStretch()
        hbox115.addWidget(self.clearbutton111)
        hbox115.addWidget(self.button111)
        hbox115.addStretch()
        hbox116.addWidget(self.YB1Label)
        hbox117.addWidget(self.XB1Label)

        vbox11.addLayout(hbox111)
        vbox11.addLayout(hbox112)
        vbox11.addLayout(hbox113)
        vbox11.addLayout(hbox114)
        vbox11.addLayout(hbox115)
        vbox11.addLayout(hbox116)
        vbox11.addLayout(hbox117)
        vbox11.addStretch()

        TopLayoutGroupBox.setLayout(vbox11)

        # 2. Temel Ödev
        hbox121 = QHBoxLayout()
        hbox122 = QHBoxLayout()
        hbox123 = QHBoxLayout()
        hbox124 = QHBoxLayout()
        hbox125 = QHBoxLayout()
        hbox126 = QHBoxLayout()
        hbox127 = QHBoxLayout()
        hbox128 = QHBoxLayout()
        vbox12 = QVBoxLayout()

        MiddleLayoutGroupBox = QGroupBox("2. Fundamental Surveying")
        hbox121.addWidget(self.YA2Label)
        hbox121.addWidget(self.YA2)
        hbox122.addWidget(self.XA2Label)
        hbox122.addWidget(self.XA2)
        hbox123.addWidget(self.YB2Label)
        hbox123.addWidget(self.YB2)
        hbox124.addWidget(self.XB2Label)
        hbox124.addWidget(self.XB2)
        hbox125.addStretch()
        hbox125.addWidget(self.clearbutton112)
        hbox125.addWidget(self.button112)
        hbox125.addStretch()
        hbox126.addWidget(self.SAB2Label)
        hbox127.addWidget(self.tAB2Label)
        hbox128.addWidget(self.tBA2Label)

        vbox12.addLayout(hbox121)
        vbox12.addLayout(hbox122)
        vbox12.addLayout(hbox123)
        vbox12.addLayout(hbox124)
        vbox12.addLayout(hbox125)
        vbox12.addLayout(hbox126)
        vbox12.addLayout(hbox127)
        vbox12.addLayout(hbox128)
        vbox12.addStretch()

        MiddleLayoutGroupBox.setLayout(vbox12)

        # 3. Temel Ödev
        hbox131 = QHBoxLayout()
        hbox132 = QHBoxLayout()
        hbox133 = QHBoxLayout()
        hbox134 = QHBoxLayout()
        hbox135 = QHBoxLayout()
        vbox13 = QVBoxLayout()

        BottomLayoutGroupBox = QGroupBox("3. Fundamental Surveying")
        hbox131.addWidget(self.tAB3Label)
        hbox131.addWidget(self.tAB3)
        hbox133.addWidget(self.BetaBLabel3)
        hbox133.addWidget(self.BetaB)
        hbox134.addStretch()
        hbox134.addWidget(self.clearbutton113)
        hbox134.addWidget(self.button113)
        hbox134.addStretch()
        hbox135.addWidget(self.tBC3Label)
        vbox13.addLayout(hbox131)
        vbox13.addLayout(hbox132)
        vbox13.addLayout(hbox133)
        vbox13.addLayout(hbox134)
        vbox13.addLayout(hbox135)
        vbox13.addStretch()

        BottomLayoutGroupBox.setLayout(vbox13)

        FirstMainLayout.addWidget(TopLayoutGroupBox, 33)
        FirstMainLayout.addWidget(MiddleLayoutGroupBox, 33)
        FirstMainLayout.addWidget(BottomLayoutGroupBox, 34)

        # Mühendislik Ölçmeleri
        # Horizontal Layout with Polar Coordianates
        hbox21 = QHBoxLayout()
        hbox22 = QHBoxLayout()
        hbox23 = QHBoxLayout()
        hbox24 = QHBoxLayout()
        hbox25 = QHBoxLayout()
        hbox27 = QHBoxLayout()
        hbox28 = QHBoxLayout()
        hbox29 = QHBoxLayout()
        hbox210 = QHBoxLayout()
        hbox211 = QHBoxLayout()
        hbox212 = QHBoxLayout()
        vbox2 = QVBoxLayout()

        SecondLayoutGroupBox = QGroupBox("Horizontal Layout with Polar Coordinates")
        hbox21.addWidget(self.Gauss_KruegerLabel)
        hbox21.addWidget(self.Gauss_Krueger)
        hbox22.addWidget(self.Geoid_UndulationLabel)
        hbox22.addWidget(self.Geoid_Undulation)
        hbox23.addWidget(self.YP101Label)
        hbox23.addWidget(self.YP101)
        hbox24.addWidget(self.XP101Label)
        hbox24.addWidget(self.XP101)
        hbox25.addWidget(self.H_orth_P101Label)
        hbox25.addWidget(self.H_orth_P101)
        hbox27.addWidget(self.YP102Label)
        hbox27.addWidget(self.YP102)
        hbox28.addWidget(self.XP102Label)
        hbox28.addWidget(self.XP102)
        hbox29.addWidget(self.YPLabel)
        hbox29.addWidget(self.YP)
        hbox210.addWidget(self.XPLabel)
        hbox210.addWidget(self.XP)
        hbox211.addStretch()
        hbox211.addWidget(self.clearbutton12)
        hbox211.addWidget(self.button12)
        hbox211.addStretch()
        hbox212.addWidget(self.outputList1)

        vbox2.addLayout(hbox21)
        vbox2.addLayout(hbox22)
        vbox2.addLayout(hbox23)
        vbox2.addLayout(hbox24)
        vbox2.addLayout(hbox25)
        vbox2.addLayout(hbox27)
        vbox2.addLayout(hbox28)
        vbox2.addLayout(hbox29)
        vbox2.addLayout(hbox210)
        vbox2.addLayout(hbox211)
        vbox2.addLayout(hbox212)
        SecondLayoutGroupBox.setLayout(vbox2)

        # Centering Error at Layout Point
        hbox31 = QHBoxLayout()
        hbox32 = QHBoxLayout()
        hbox33 = QHBoxLayout()
        hbox34 = QHBoxLayout()
        hbox35 = QHBoxLayout()
        hbox36 = QHBoxLayout()
        hbox37 = QHBoxLayout()
        hbox38 = QHBoxLayout()
        hbox39 = QHBoxLayout()
        hbox310 = QHBoxLayout()
        hbox311 = QHBoxLayout()
        hbox312 = QHBoxLayout()
        vbox3 = QVBoxLayout()

        ThirdLayoutGroupBox = QGroupBox("Centering Errors")
        hbox31.addWidget(self.sigma_lqLabel)
        hbox31.addWidget(self.sigma_lq)
        hbox32.addWidget(self.sigma_rLabel)
        hbox32.addWidget(self.sigma_r)
        hbox33.addWidget(self.esLabel)
        hbox33.addWidget(self.es)
        hbox34.addWidget(self.etLabel)
        hbox34.addWidget(self.et)
        hbox35.addWidget(self.elLabel)
        hbox35.addWidget(self.el)
        hbox36.addWidget(self.SP101_A22Label)
        hbox36.addWidget(self.SP101_A_22)
        hbox37.addWidget(self.SP101_P102_22Label)
        hbox37.addWidget(self.SP101_P102_22)
        hbox38.addWidget(self.Beta_22Label)
        hbox38.addWidget(self.Beta_22)
        hbox39.addWidget(self.n_22Label)
        hbox39.addWidget(self.n_22)
        hbox310.addWidget(self.sigma_pLabel)
        hbox310.addWidget(self.sigma_p)
        hbox311.addStretch()
        hbox311.addWidget(self.clearbutton13)
        hbox311.addWidget(self.button13)
        hbox311.addStretch()
        hbox312.addWidget(self.outputList2)

        vbox3.addLayout(hbox31)
        vbox3.addLayout(hbox32)
        vbox3.addLayout(hbox33)
        vbox3.addLayout(hbox34)
        vbox3.addLayout(hbox35)
        vbox3.addLayout(hbox36)
        vbox3.addLayout(hbox37)
        vbox3.addLayout(hbox38)
        vbox3.addLayout(hbox39)
        vbox3.addLayout(hbox310)
        vbox3.addLayout(hbox311)
        vbox3.addLayout(hbox312)

        ThirdLayoutGroupBox.setLayout(vbox3)

        # groupBoxes
        mainlayout.addLayout(FirstMainLayout, 33)
        mainlayout.addWidget(SecondLayoutGroupBox, 34)
        mainlayout.addWidget(ThirdLayoutGroupBox, 33)

        self.Fundamental.setLayout(mainlayout)


    def Widgets2(self):

        self.R_Label_1 = QLabel("                    R : ")
        self.R_1 = QLineEdit()
        self.R_1.setMaximumWidth(130)
        self.R_1.setFont(QFont('Times', 10))
        self.Delta_Label_1 = QLabel("Deviation Angle : ")
        self.Delta_1 = QLineEdit()
        self.Delta_1.setMaximumWidth(130)
        self.Delta_1.setFont(QFont('Times', 10))

        # KSN-1
        self.KSn_1_Label_1 = QLabel("  KSn-1 : ")
        self.KSn_1_1 = QLineEdit()
        self.KSn_1_1.setMaximumWidth(130)
        self.KSn_1_1.setFont(QFont('Times', 10))
        self.YSn_1_Label_1 = QLabel("  Y(Sn-1) : ")
        self.YSn_1_1 = QLineEdit()
        self.YSn_1_1.setMaximumWidth(130)
        self.YSn_1_1.setFont(QFont('Times', 10))
        self.XSn_1_Label_1 = QLabel("  X(Sn-1) : ")
        self.XSn_1_1 = QLineEdit()
        self.XSn_1_1.setMaximumWidth(130)
        self.XSn_1_1.setFont(QFont('Times', 10))

        #TFn-1, TFn, TFn+1
        self.KTFn_1_Label_1 = QLabel("KTFn-1 : ")
        self.KTFn_1_1 = QLineEdit()
        self.KTFn_1_1.setMaximumWidth(130)
        self.KTFn_1_1.setFont(QFont('Times', 10))
        self.YTFn_1_Label_1 = QLabel("Y(TFn-1) : ")
        self.YTFn_1_1 = QLineEdit()
        self.YTFn_1_1.setMaximumWidth(130)
        self.YTFn_1_1.setFont(QFont('Times', 10))
        self.XTFn_1_Label_1 = QLabel("X(TFn-1) : ")
        self.XTFn_1_1 = QLineEdit()
        self.XTFn_1_1.setMaximumWidth(130)
        self.XTFn_1_1.setFont(QFont('Times', 10))

        self.KTFn_Label_1 = QLabel("   KTFn : ")
        self.KTFn_1 = QLineEdit()
        self.KTFn_1.setMaximumWidth(130)
        self.KTFn_1.setFont(QFont('Times', 10))
        self.YTFn_Label_1 = QLabel("   Y(TFn) : ")
        self.YTFn_1 = QLineEdit()
        self.YTFn_1.setMaximumWidth(130)
        self.YTFn_1.setFont(QFont('Times', 10))
        self.XTFn_Label_1 = QLabel("   X(TFn) : ")
        self.XTFn_1 = QLineEdit()
        self.XTFn_1.setMaximumWidth(130)
        self.XTFn_1.setFont(QFont('Times', 10))

        # KSn
        self.KSn_Label_1 = QLabel("     KSn : ")
        self.KSn_1 = QLineEdit()
        self.KSn_1.setMaximumWidth(130)
        self.KSn_1.setFont(QFont('Times', 10))
        self.YSn_Label_1 = QLabel("     Y(Sn) : ")
        self.YSn_1 = QLineEdit()
        self.YSn_1.setMaximumWidth(130)
        self.YSn_1.setFont(QFont('Times', 10))
        self.XSn_Label_1 = QLabel("     X(Sn) : ")
        self.XSn_1 = QLineEdit()
        self.XSn_1.setMaximumWidth(130)
        self.XSn_1.setFont(QFont('Times', 10))

        # TOn, TOn+1
        self.KTOn_Label_1 = QLabel("   KTOn : ")
        self.KTOn_1 = QLineEdit()
        self.KTOn_1.setMaximumWidth(130)
        self.KTOn_1.setFont(QFont('Times', 10))
        self.YTOn_Label_1 = QLabel("   Y(TOn) : ")
        self.YTOn_1 = QLineEdit()
        self.YTOn_1.setMaximumWidth(130)
        self.YTOn_1.setFont(QFont('Times', 10))
        self.XTOn_Label_1 = QLabel("   X(TOn) : ")
        self.XTOn_1 = QLineEdit()
        self.XTOn_1.setMaximumWidth(130)
        self.XTOn_1.setFont(QFont('Times', 10))

        self.KTOn1_Label_1 = QLabel("KTOn+1 :")
        self.KTOn1_1 = QLineEdit()
        self.KTOn1_1.setMaximumWidth(130)
        self.KTOn1_1.setFont(QFont('Times', 10))
        self.YTOn1_Label_1 = QLabel("Y(TOn+1) :")
        self.YTOn1_1 = QLineEdit()
        self.YTOn1_1.setMaximumWidth(130)
        self.YTOn1_1.setFont(QFont('Times', 10))
        self.XTOn1_Label_1 = QLabel("X(TOn+1) :")
        self.XTOn1_1 = QLineEdit()
        self.XTOn1_1.setMaximumWidth(130)
        self.XTOn1_1.setFont(QFont('Times', 10))

        # KSN-1
        self.KSn1_Label_1 = QLabel(" KSn+1 : ")
        self.KSn1_1 = QLineEdit()
        self.KSn1_1.setMaximumWidth(130)
        self.KSn1_1.setFont(QFont('Times', 10))
        self.YSn1_Label_1 = QLabel(" Y(Sn+1) : ")
        self.YSn1_1 = QLineEdit()
        self.YSn1_1.setMaximumWidth(130)
        self.YSn1_1.setFont(QFont('Times', 10))
        self.XSn1_Label_1 = QLabel(" X(Sn+1) : ")
        self.XSn1_1 = QLineEdit()
        self.XSn1_1.setMaximumWidth(130)
        self.XSn1_1.setFont(QFont('Times', 10))

        # M
        self.YM_Label_1 = QLabel("Y(M) : ")
        self.YM_1 = QLineEdit()
        self.YM_1.setMaximumWidth(130)
        self.YM_1.setFont(QFont('Times', 10))
        self.XM_label_1 = QLabel("X(M) : ")
        self.XM_1 = QLineEdit()
        self.XM_1.setMaximumWidth(130)
        self.XM_1.setFont(QFont('Times', 10))

        # distance
        self.SSn_1_TFn_1_Label_1 = QLabel("   S(Sn-1,TFn-1) : ")
        self.SSn_1_TFn_1_1 = QLineEdit()
        self.SSn_1_TFn_1_1.setMaximumWidth(130)
        self.SSn_1_TFn_1_1.setFont(QFont('Times', 10))
        self.STFn_1_TOn_Label_1 = QLabel("    S(TFn-1,TOn) : ")
        self.STFn_1_TOn_1 = QLineEdit()
        self.STFn_1_TOn_1.setMaximumWidth(130)
        self.STFn_1_TOn_1.setFont(QFont('Times', 10))
        self.STFn_TOn1_Label_1 = QLabel("  S(TFn, TOn+1) : ")
        self.STFn_TOn1_1= QLineEdit()
        self.STFn_TOn1_1.setMaximumWidth(130)
        self.STFn_TOn1_1.setFont(QFont('Times', 10))
        self.STOn1_Sn1_Label_1 = QLabel("S(TOn+1, Sn+1) : ")
        self.STOn1_Sn1_1 = QLineEdit()
        self.STOn1_Sn1_1.setMaximumWidth(130)
        self.STOn1_Sn1_1.setFont(QFont('Times', 10))
        self.SSn_Sn_1_label_1 = QLabel("        S(Sn,Sn-1) : ")
        self.SSn_Sn_1_1 = QLineEdit()
        self.SSn_Sn_1_1.setMaximumWidth(130)
        self.SSn_Sn_1_1.setFont(QFont('Times', 10))
        self.SSn_Sn1_label_1 = QLabel("       S(Sn,Sn+1) : ")
        self.SSn_Sn1_1 = QLineEdit()
        self.SSn_Sn1_1.setMaximumWidth(130)
        self.SSn_Sn1_1.setFont(QFont('Times', 10))

        # azimuth
        self.t_Sn_1_Sn_Label_1 = QLabel("          t(Sn-1,Sn) : ")
        self.t_Sn_1_Sn_1 = QLineEdit()
        self.t_Sn_1_Sn_1.setMaximumWidth(130)
        self.t_Sn_1_Sn_1.setFont(QFont('Times', 10))
        self.t_Sn_Sn1_Label_1 = QLabel("        t(Sn,Sn+1) : ")
        self.t_Sn_Sn1_1 = QLineEdit()
        self.t_Sn_Sn1_1.setMaximumWidth(130)
        self.t_Sn_Sn1_1.setFont(QFont('Times', 10))

        self.KP_Label_1 = QLabel("K(P) : ")
        self.KP_1 = QLineEdit()
        self.KP_1.setMaximumWidth(130)
        self.KP_1.setFont(QFont('Times', 10))

        self.clearButton21 = QPushButton("Clear")
        self.clearButton21.setMaximumWidth(120)
        self.clearButton21.clicked.connect(self.clear21Function)

        self.button21 = QPushButton("Calculate")
        self.button21.setMaximumWidth(120)
        self.button21.clicked.connect(self.button21Function)

        self.RouteButton21 = QPushButton("Route")
        self.RouteButton21.setMaximumWidth(120)
        self.RouteButton21.clicked.connect(self.Route21Function)

        self.combobox2 = QComboBox()
        self.combobox2.addItems(["Right Curve", "Left Curve"])
        self.combobox2.setMinimumHeight(25)
        self.combobox2.setMaximumWidth(120)

        self.outputList3 = QListWidget()
        self.outputList3.setMinimumHeight(600)
        self.outputList3.setFont(QFont("Times", 9))
        self.outputList3.addItems([
            "R = ",
            "L = ",
            "\u0394 = ",
            "",
            "t(Sn-1,Sn) = ",
            "t(Sn, Sn-1) = ",
            "t(Sn,Sn+1) = ",
            "t(Sn+1,Sn) = ",
            "t(TOn,TFn) = ",
            "t(TFn,TOn) = ",
            "",
            "S(Sn,M) = ",
            "S(Sn,TOn) = ",
            "S(Sn,TFn) = ",
            "",
            "S(Sn,TFn-1) = ",
            "S(Sn,TOn+1) = ",
            "S(Sn,Sn-1) = ",
            "S(Sn,Sn+1) = ",
            "",
            "S(Fn-1,TOn) = ",
            "S(TFn,TOn+1) = ",
            "S(Sn-1,TFn-1) = ",
            "S(TOn+1,Sn+1) = ",
            "",
            "S(TOn,TFn) = ",
            "",
            "KS(n-1) = ",
            "KTF(n-1) = ",
            "KTO(n) = ",
            "KSn = ",
            "KTF(n) = ",
            "KTO(n+1) = ",
            "KSn1 = ",
            "",
            "S(n-1)(Y = , X = )",
            "TF(n-1)(Y = , X = )",
            "TOn(Y = ,  X = )",
            "Sn(Y = , X = )",
            "TFn(Y = , X = )",
            "TOn(n+1)(Y = , X = )",
            "S(n+1)(Y = , X = )",
            "",
            "P(Y = , X = )",
        ])

        self.HS1_Label_2 = QLabel("H(S1) :")
        self.HS1_2 = QLineEdit()
        self.HS1_2.setMaximumWidth(150)
        self.HS1_2.setFont(QFont('Times', 10))
        self.KS1_Label_2 = QLabel("K(S1) :")
        self.KS1_2 = QLineEdit()
        self.KS1_2.setMaximumWidth(150)
        self.KS1_2.setFont(QFont('Times', 10))

        self.HS2_Label_2 = QLabel("H(S2) :")
        self.HS2_2 = QLineEdit()
        self.HS2_2.setMaximumWidth(150)
        self.HS2_2.setFont(QFont('Times', 10))
        self.KS2_Label_2 = QLabel("K(S2) :")
        self.KS2_2 = QLineEdit()
        self.KS2_2.setMaximumWidth(150)
        self.KS2_2.setFont(QFont('Times', 10))

        self.HS3_Label_2 = QLabel("H(S3) :")
        self.HS3_2 = QLineEdit()
        self.HS3_2.setMaximumWidth(150)
        self.HS3_2.setFont(QFont('Times', 10))
        self.KS3_Label_2 = QLabel("K(S3) :")
        self.KS3_2 = QLineEdit()
        self.KS3_2.setMaximumWidth(150)
        self.KS3_2.setFont(QFont('Times', 10))

        self.L_Label_2 = QLabel("       L :")
        self.L_2 = QLineEdit()
        self.L_2.setMaximumWidth(150)
        self.L_2.setFont(QFont('Times', 10))

        self.KP_Label_2 = QLabel("  K(P) :")
        self.KP_2 = QLineEdit()
        self.KP_2.setMaximumWidth(150)
        self.KP_2.setFont(QFont('Times', 10))

        self.clearButton22 = QPushButton("Clear")
        self.clearButton22.setMaximumWidth(120)
        self.clearButton22.clicked.connect(self.clear22Function)

        self.button22 = QPushButton("Calculate")
        self.button22.setMaximumWidth(120)
        self.button22.clicked.connect(self.button22Function)

        self.outputList4 = QListWidget()
        self.outputList4.setFont(QFont("Times", 9))
        self.outputList4.setMinimumHeight(348)
        self.outputList4.addItems([
            "g1 = ",
            "g2 = ",
            "G = ",
            "",
            "K(S1) = ",
            "K(TO) = ",
            "K(S2) = ",
            "K(TF) = ",
            "K(S3) = ",
            "",
            "H(S1) = ",
            "H(TO) = ",
            "H(S2) = ",
            "H(TF) = ",
            "H(S3) = ",
            "",
            "XE = ",
            "YE = ",
            "KE = ",
            "HE = ",
            "",
            "XP = ",
            "YP = ",
            "KP = ",
            "HP = ",
        ])

    def clear21Function(self):

        self.R_1.clear()
        self.Delta_1.clear()
        self.KSn_1_1.clear()
        self.YSn_1_1.clear()
        self.XSn_1_1.clear()
        self.KTFn_1_1.clear()
        self.YTFn_1_1.clear()
        self.XTFn_1_1.clear()
        self.KTFn_1.clear()
        self.YTFn_1.clear()
        self.XTFn_1.clear()
        self.KSn_1.clear()
        self.YSn_1.clear()
        self.XSn_1.clear()
        self.KTOn_1.clear()
        self.YTOn_1.clear()
        self.XTOn_1.clear()
        self.KTOn1_1.clear()
        self.YTOn1_1.clear()
        self.XTOn1_1.clear()
        self.KSn1_1.clear()
        self.YSn1_1.clear()
        self.XSn1_1.clear()
        self.YM_1.clear()
        self.XM_1.clear()
        self.SSn_1_TFn_1_1.clear()
        self.STFn_1_TOn_1.clear()
        self.STFn_TOn1_1.clear()
        self.STOn1_Sn1_1.clear()
        self.SSn_Sn_1_1.clear()
        self.SSn_Sn1_1.clear()
        self.t_Sn_1_Sn_1.clear()
        self.t_Sn_Sn1_1.clear()
        self.KP_1.clear()
        self.outputList3.clear()
        self.outputList3.addItems([
            "R = ",
            "L = ",
            "\u0394 = ",
            "",
            "t(Sn-1,Sn) = ",
            "t(Sn, Sn-1) = ",
            "t(Sn,Sn+1) = ",
            "t(Sn+1,Sn) = ",
            "t(TOn,TFn) = ",
            "t(TFn,TOn) = ",
            "",
            "S(Sn,M) = ",
            "S(Sn,TOn) = ",
            "S(Sn,TFn) = ",
            "",
            "S(Sn,TFn-1) = ",
            "S(Sn,TOn+1) = ",
            "S(Sn,Sn-1) = ",
            "S(Sn,Sn+1) = ",
            "",
            "S(Fn-1,TOn) = ",
            "S(TFn,TOn+1) = ",
            "S(Sn-1,TFn-1) = ",
            "S(TOn+1,Sn+1) = ",
            "",
            "S(TOn,TFn) = ",
            "",
            "KS(n-1) = ",
            "KTF(n-1) = ",
            "KTO(n) = ",
            "KSn = ",
            "KTF(n) = ",
            "KTO(n+1) = ",
            "KSn1 = ",
            "",
            "S(n-1)(Y = , X = )",
            "TF(n-1)(Y = , X = )",
            "TOn(Y = ,  X = )",
            "Sn(Y = , X = )",
            "TFn(Y = , X = )",
            "TOn(n+1)(Y = , X = )",
            "S(n+1)(Y = , X = )",
            "",
            "P(Y = , X = )",
        ])



    def button21Function(self):

        t = False
        L = False
        alfa = False
        STOn_TFn = False
        t_Sn_Sn_1 = False
        t_Sn1_Sn = False
        t_TOn_TFn = False
        t_TFn_TOn = False
        SSn_M = False
        STFn_1_Sn = False
        SSn_TOn1 = False
        SSn_1_TOn = False
        STFn_Sn1 = False
        XP = False
        YP = False

        try:

            if self.R_1.text() != "":
                R = float(self.R_1.text())
            else:
                R = False

            if self.Delta_1.text() != "":
                Delta = float(self.Delta_1.text())
            else:
                Delta = False

            if self.KSn_1_1.text() != "":
                KSn_1 = float(self.KSn_1_1.text())
            else:
                KSn_1 = False

            if self.YSn_1_1.text() != "":
                YSn_1 = float(self.YSn_1_1.text())
            else:
                YSn_1 = False

            if self.XSn_1_1.text() != "":
                XSn_1 = float(self.XSn_1_1.text())
            else:
                XSn_1 = False

            if self.KTFn_1_1.text() != "":
                KTFn_1 = float(self.KTFn_1_1.text())
            else:
                KTFn_1 = False

            if self.YTFn_1_1.text() != "":
                YTFn_1 = float(self.YTFn_1_1.text())
            else:
                YTFn_1 = False

            if self.XTFn_1_1.text() != "":
                XTFn_1 = float(self.XTFn_1_1.text())
            else:
                XTFn_1 = False

            if self.KTFn_1.text() != "":
                KTFn = float(self.KTFn_1.text())
            else:
                KTFn = False

            if self.YTFn_1.text() != "":
                YTFn = float(self.YTFn_1.text())
            else:
                YTFn = False

            if self.XTFn_1.text() != "":
                XTFn = float(self.XTFn_1.text())
            else:
                XTFn = False

            if self.KSn_1.text() != "":
                KSn = float(self.KSn_1.text())
            else:
                KSn = False

            if self.YSn_1.text() != "":
                YSn = float(self.YSn_1.text())
            else:
                YSn = False

            if self.XSn_1.text() != "":
                XSn = float(self.XSn_1.text())
            else:
                XSn = False

            if self.KTOn_1.text() != "":
                KTOn = float(self.KTOn_1.text())
            else:
                KTOn = False

            if self.YTOn_1.text() != "":
                YTOn = float(self.YTOn_1.text())
            else:
                YTOn = False

            if self.XTOn_1.text() != "":
                XTOn = float(self.XTOn_1.text())
            else:
                XTOn = False

            if self.KTOn1_1.text() != "":
                KTOn1 = float(self.KTOn1_1.text())
            else:
                KTOn1 = False

            if self.YTOn1_1.text() != "":
                YTOn1 = float(self.YTOn1_1.text())
            else:
                YTOn1 = False

            if self.XTOn1_1.text() != "":
                XTOn1 = float(self.XTOn1_1.text())
            else:
                XTOn1 = False

            if self.KSn1_1.text() != "":
                KSn1 = float(self.KSn1_1.text())
            else:
                KSn1 = False

            if self.YSn1_1.text() != "":
                YSn1 = float(self.YSn1_1.text())
            else:
                YSn1 = False

            if self.XSn1_1.text() != "":
                XSn1 = float(self.XSn1_1.text())
            else:
                XSn1 = False

            if self.YM_1.text() != "":
                YM = float(self.YM_1.text())
            else:
                YM = False

            if self.XM_1.text() != "":
                XM = float(self.XM_1.text())
            else:
                XM = False

            if self.SSn_1_TFn_1_1.text() != "":
                SSn_1_TFn_1 = float(self.SSn_1_TFn_1_1.text())
            else:
                SSn_1_TFn_1 = False

            if self.STFn_1_TOn_1.text() != "":
                STFn_1_TOn = float(self.STFn_1_TOn_1.text())
            else:
                STFn_1_TOn = False

            if self.STFn_TOn1_1.text() != "":
                STFn_TOn1 = float(self.STFn_TOn1_1.text())
            else:
                STFn_TOn1 = False

            if self.STOn1_Sn1_1.text() != "":
                STOn1_Sn1 = float(self.STOn1_Sn1_1.text())
            else:
                STOn1_Sn1 = False

            if self.SSn_Sn_1_1.text() != "":
                SSn_Sn_1 = float(self.SSn_Sn_1_1.text())
            else:
                SSn_Sn_1 = False

            if self.SSn_Sn1_1.text() != "":
                SSn_Sn1 = float(self.SSn_Sn1_1.text())
            else:
                SSn_Sn1 = False

            if self.t_Sn_1_Sn_1.text() != "":
                t_Sn_1_Sn = float(self.t_Sn_1_Sn_1.text())
            else:
                t_Sn_1_Sn = False

            if self.t_Sn_Sn1_1.text() != "":
                t_Sn_Sn1 = float(self.t_Sn_Sn1_1.text())
            else:
                t_Sn_Sn1 = False

            Curve = self.combobox2.currentText()

            for _ in range(25):

                if R and Delta:
                    t = np.round(R * np.tan(Grad2Radyan(Delta) / 2), 3)

                if Delta:
                    alfa = Delta / 2

                if YM and XM and YSn and XSn:
                    SSn_M = np.round(((YM - YSn) ** 2 + (XM - XSn) ** 2) ** 0.5, 3)
                    if Delta:
                        t = np.round(SSn_M * np.sin(Grad2Radyan(Delta / 2)), 3)
                        R = np.round(SSn_M * np.cos(Grad2Radyan(Delta / 2)), 3)

                if R and Delta:
                    L = np.round((Delta * np.pi * R) / 200, 3)

                if SSn_Sn_1 == False:
                    if YSn_1 and YSn and XSn_1 and XSn:
                        SSn_Sn_1 = np.round(((YSn_1 - YSn) ** 2 + (XSn_1 - XSn) ** 2) ** 0.5, 3)
                    elif SSn_1_TFn_1 and STFn_1_TOn and t:
                        SSn_Sn_1 = np.round(SSn_1_TFn_1 + STFn_1_TOn + t, 3)
                    elif SSn_1_TOn and t:
                        SSn_Sn_1 = np.round(SSn_1_TOn + t, 3)

                if SSn_1_TFn_1 == False:
                    if SSn_1_TOn and STFn_1_TOn:
                        SSn_1_TFn_1 = np.round(SSn_1_TOn - STFn_1_TOn, 3)
                    elif STFn_1_Sn and t:
                        SSn_1_TFn_1 = np.round(STFn_1_Sn -t, 3)
                    elif YTFn_1 and XTFn_1 and YTOn and XTOn:
                        SSn_1_TFn_1 = np.round(((YTFn_1 - YTOn) ** 2 + (XTFn_1 - XTOn) ** 2) ** 0.5, 3)
                    elif KTFn_1 and KSn_1:
                        SSn_1_TFn_1 = np.round(KTFn_1 - KSn_1, 3)

                if STFn_1_TOn == False:
                    if SSn_Sn_1 and t and SSn_1_TFn_1:
                        STFn_1_TOn = np.round(SSn_Sn_1 - t - SSn_1_TFn_1, 3)
                    elif SSn_1_TOn and SSn_1_TFn_1:
                        STFn_1_TOn = np.round(SSn_1_TOn - SSn_1_TFn_1, 3)
                    elif YTOn and XTOn and YTFn_1 and XTFn_1:
                        STFn_1_TOn = np.round(((YTOn - YTFn_1) ** 2 + (XTOn - XTFn_1) ** 2) ** 0.5, 3)
                    elif KTOn and KTFn_1:
                        STFn_1_TOn = np.round(KTOn - KTFn_1, 3)

                if STOn_TFn == False:
                    if R and Delta:
                        STOn_TFn = np.round(2 * R * np.sin(Grad2Radyan(Delta) / 2), 3)
                    elif YTOn and XTOn and YTFn and XTFn:
                        STOn_TFn = np.round(((YTOn - YTFn) ** 2 + (XTOn - XTFn) ** 2) ** 0.5, 3)

                if t == False:
                    if R and Delta:
                        t = np.round(R * np.tan(Grad2Radyan(Delta) / 2), 3)
                    elif SSn_Sn_1 and SSn_1_TOn:
                        t = np.round(SSn_Sn_1 - SSn_1_TOn)
                    elif SSn_Sn1 and STFn_Sn1:
                        t = np.round(SSn_Sn1 - STFn_Sn1)
                    elif STFn_1_Sn and STFn_1_TOn:
                        t = np.round(STFn_1_Sn - STFn_1_TOn)
                    elif SSn_TOn1 and STFn_TOn1:
                        t = np.round(SSn_TOn1 - STFn_TOn1)
                    elif YTOn and XTOn and YSn and XSn:
                        t = np.round(((YTOn - YSn) ** 2 + (XTOn - XSn) ** 2) ** 0.5, 3)
                    elif YTFn and XTFn and YSn and XSn:
                        t = np.round(((YTFn - YSn) ** 2 + (XTFn - XSn) ** 2) ** 0.5, 3)

                if STFn_TOn1 == False:
                    if SSn_TOn1 and t:
                        STFn_TOn1 = np.round(SSn_TOn1 - t, 3)
                    elif STFn_Sn1 and STOn1_Sn1:
                        STFn_TOn1 = np.round(STFn_Sn1 - STOn1_Sn1, 3)
                    elif SSn_TOn1 and t:
                        STFn_TOn1 = np.round(SSn_TOn1 - t, 3)
                    elif YTFn and XTFn and YTOn1 and XTOn1:
                        STFn_TOn1 = np.round(((YTFn - YTOn1) ** 2 + (XTFn - XTOn1) ** 2) ** 0.5, 3)
                    elif KTOn1 and KTFn:
                        STFn_TOn1 = np.round(KTOn1 - KTFn, 3)

                if STOn1_Sn1 == False:
                    if STFn_Sn1 and STFn_TOn1:
                        STOn1_Sn1 = np.round(STFn_Sn1 - STFn_TOn1, 3)
                    elif SSn_TOn1 and SSn_Sn1:
                        STOn1_Sn1 = np.round(SSn_Sn1 - SSn_TOn1, 3)
                    elif YSn1 and XSn1 and YTOn1 and XTOn1:
                        STOn1_Sn1 = np.round(((YSn1 - YTOn1) ** 2 + (XSn1 - XTOn1) ** 2) ** 0.5, 3)
                    elif KSn1 and KTOn1:
                        STOn1_Sn1 = np.round(KSn1 - KTOn1, 3)

                if SSn_Sn1 == False:
                    if YSn and XSn and YSn1 and XSn1:
                        SSn_Sn1 = np.round(((YSn - YSn1) ** 2 + (XSn - XSn1) ** 2) ** 0.5, 3)
                    elif t and STFn_TOn1 and STOn1_Sn1:
                        SSn_Sn1 = np.round(t + STFn_TOn1 + STOn1_Sn1, 3)
                    elif t and STFn_Sn1:
                        SSn1_Sn1 = np.round(t + STFn_Sn1, 3)

                if KSn_1 == False:
                    if KTFn_1 and SSn_1_TFn_1:
                        KSn_1 = np.round(KTFn_1 - SSn_1_TFn_1, 3)

                if KTFn_1 == False:
                    if KSn_1 and SSn_1_TFn_1:
                        KTFn_1 = np.round(KSn_1 + SSn_1_TFn_1, 3)
                    elif KTOn and STFn_1_TOn:
                        KTFn_1 = np.round(KTOn - STFn_1_TOn, 3)
                    elif KSn and STFn_1_Sn:
                        KTFn_1 = np.round(KSn - STFn_1_Sn, 3)

                if KTOn == False:
                    if KTFn_1 and STFn_1_TOn:
                        KTOn = np.round(KTFn_1 + STFn_1_TOn, 3)
                    elif KSn_1 and SSn_1_TOn:
                        KTOn = np.round(KSn_1 + SSn_1_TOn, 3)
                    elif KSn and t:
                        KTOn = np.round(KSn - t, 3)
                    elif KTFn and L:
                        KTOn = np.round(KTFn - L, 3)

                if KSn == False:
                    if KTOn and t:
                        KSn = np.round(KTOn + t)
                    elif KTFn and t:
                        KSn = np.round(KTFn - t)

                if KTFn == False:
                    if KTOn and L:
                        KTFn = np.round(KTOn + L, 3)
                    elif KSn and t:
                        KTFn = np.round(KSn + t, 3)
                    elif KTOn1 and STFn_TOn1:
                        KTFn = np.round(KTOn1 - STFn_TOn1, 3)
                    elif KSn1 and STFn_Sn1:
                        KTFn =np.round(KSn1 - STFn_Sn1, 3)

                if KTOn1 == False:
                    if KTFn and STFn_TOn1:
                        KTOn1 = np.round(KTFn + STFn_TOn1, 3)
                    elif KSn and SSn_TOn1:
                        KTOn1 = np.round(KSn + SSn_TOn1, 3)
                    elif KSn1 and STOn1_Sn1:
                        KTOn1 = np.round(KSn1 - STOn1_Sn1, 3)

                if t_Sn_1_Sn == False:
                    if YSn_1 and XSn_1 and YSn and XSn:
                        t_Sn_1_Sn = Azimuth(YSn_1, XSn_1, YSn, XSn)
                    elif YTFn_1 and XTFn_1 and YTOn and XTOn:
                        t_Sn_1_Sn = Azimuth(YTFn_1, XTFn_1, YTOn, XTOn)
                    elif YSn_1 and XSn_1 and YTFn_1 and XTFn_1:
                        t_Sn_1_Sn = Azimuth(YSn_1, XSn_1, YTFn_1, XTFn_1)
                    elif YTOn and XTOn and YSn and XSn:
                        t_Sn_1_Sn = Azimuth(YTOn, XTOn, YSn, XSn)

                if t_Sn_Sn1 == False:
                    if YSn and XSn and YSn1 and XSn1:
                        t_Sn_Sn1 = Azimuth(YSn, XSn, YSn1, XSn1)
                    elif YTFn and XTFn and YTOn1 and XTOn1:
                        t_Sn_Sn1 = Azimuth(YTFn, XTFn, YTOn1, XTOn1)
                    elif YSn and XSn and YTFn and XTFn:
                        t_Sn_Sn1 = Azimuth(YSn, XSn, YTFn, XTFn)
                    elif YTOn1 and XTOn1 and YSn1 and XSn1:
                        t_Sn_Sn1 = Azimuth(YTOn1, XTOn1, YSn1, XSn1)

                if t_Sn_1_Sn:
                    t_Sn_Sn_1 = t_Sn_1_Sn + 200
                    if t_Sn_Sn_1 >= 400:
                        t_Sn_Sn_1 = t_Sn_Sn_1 - 400
                    if Curve == "Right Curve" and alfa:
                        t_TOn_TFn = t_Sn_1_Sn + alfa
                        t_TFn_TOn = t_TOn_TFn + 200
                        if t_TFn_TOn >= 400:
                            t_TFn_TOn = t_TFn_TOn - 400
                    if Curve == "Left Curve" and alfa:
                        t_TOn_TFn = t_Sn_1_Sn - alfa
                        t_TFn_TOn = t_TOn_TFn + 200
                        if t_TFn_TOn >= 400:
                            t_TFn_TOn = t_TFn_TOn - 400

                if t_Sn_Sn1:
                    t_Sn1_Sn = t_Sn_Sn1 + 200
                    if t_Sn1_Sn >= 400:
                        t_Sn1_Sn = t_Sn1_Sn - 400

                if YSn_1 == False:
                    if YTFn_1 and SSn_1_TFn_1 and t_Sn_Sn_1:
                        YSn_1 = np.round(YTFn_1 + SSn_1_TFn_1 * np.sin(Grad2Radyan(t_Sn_Sn_1)), 3)

                if XSn_1 == False:
                    if XTFn_1 and SSn_1_TFn_1 and t_Sn_Sn_1:
                        XSn_1 = np.round(XTFn_1 + SSn_1_TFn_1 * np.cos(Grad2Radyan(t_Sn_Sn_1)), 3)

                if YTFn_1 == False:
                    if YSn_1 and SSn_1_TFn_1 and t_Sn_1_Sn:
                        YTFn_1 = np.round(YSn_1 + SSn_1_TFn_1 * np.sin(Grad2Radyan(t_Sn_1_Sn)), 3)
                    elif YTOn and STFn_1_TOn and t_Sn_Sn_1:
                        YTFn_1 = np.round(YTOn + STFn_1_TOn * np.sin(Grad2Radyan(t_Sn_Sn_1)), 3)

                if XTFn_1 == False:
                    if XSn_1 and SSn_1_TFn_1 and t_Sn_1_Sn:
                        XTFn_1 = np.round(XSn_1 + SSn_1_TFn_1 * np.cos(Grad2Radyan(t_Sn_1_Sn)), 3)
                    elif XTOn and STFn_1_TOn and t_Sn_Sn_1:
                        XTFn_1 = np.round(XTOn + STFn_1_TOn * np.cos(Grad2Radyan(t_Sn_Sn_1)), 3)

                if YTOn == False:
                    if YTFn_1 and STFn_1_TOn and t_Sn_1_Sn:
                        YTOn = np.round(YTFn_1 + STFn_1_TOn * np.sin(Grad2Radyan(t_Sn_1_Sn)), 3)
                    elif YSn and t and t_Sn_Sn_1:
                        YTOn = np.round(YSn + t * np.sin(Grad2Radyan(t_Sn_Sn_1)), 3)
                    elif YTFn and STOn_TFn and t_TFn_TOn:
                        YTOn = np.round(YTFn + STOn_TFn * np.sin(Grad2Radyan(t_TFn_TOn)), 3)

                if XTOn == False:
                    if XTFn_1 and STFn_1_TOn and t_Sn_1_Sn:
                        XTOn = np.round(XTFn_1 + STFn_1_TOn * np.cos(Grad2Radyan(t_Sn_1_Sn)), 3)
                    elif XSn and t and t_Sn_Sn_1:
                        XTOn = np.round(XSn + t * np.cos(Grad2Radyan(t_Sn_Sn_1)), 3)
                    elif XTFn and STOn_TFn and t_TFn_TOn:
                        XTOn = np.round(XTFn + STOn_TFn * np.cos(Grad2Radyan(t_TFn_TOn)), 3)

                if YSn == False:
                    if YTOn and t and t_Sn_1_Sn:
                        YSn = np.round(YTOn + t * np.sin(Grad2Radyan(t_Sn_1_Sn)), 3)
                    if YTFn and t and t_Sn1_Sn:
                        YSn = np.round(YTFn + t * np.sin(Grad2Radyan(t_Sn1_Sn)), 3)

                if XSn == False:
                    if XTOn and t and t_Sn_1_Sn:
                        XSn = np.round(XTOn + t * np.cos(Grad2Radyan(t_Sn_1_Sn)), 3)
                    if XTFn and t and t_Sn1_Sn:
                        XSn = np.round(XTFn + t * np.cos(Grad2Radyan(t_Sn1_Sn)), 3)

                if YTFn == False:
                    if YSn and t and t_Sn_Sn1:
                        YTFn = np.round(YSn + t * np.sin(Grad2Radyan(t_Sn_Sn1)), 3)
                    elif YTOn and STOn_TFn and t_TOn_TFn:
                        YTFn = np.round(YTOn + STOn_TFn * np.sin(Grad2Radyan(t_TOn_TFn)), 3)
                    elif YTOn1 and STFn_TOn1 and t_Sn_Sn1:
                        YTFn = np.round(YTOn1 + STFn_TOn1 * np.sin(Grad2Radyan(t_Sn_Sn1)), 3)

                if XTFn == False:
                    if XSn and t and t_Sn_Sn1:
                        XTFn = np.round(XSn + t * np.cos(Grad2Radyan(t_Sn_Sn1)), 3)
                    elif XTOn and STOn_TFn and t_TOn_TFn:
                        XTFn = np.round(XTOn + STOn_TFn * np.cos(Grad2Radyan(t_TOn_TFn)), 3)
                    elif XTOn1 and STFn_TOn1 and t_Sn_Sn1:
                        XTFn = np.round(XTOn1 + STFn_TOn1 * np.cos(Grad2Radyan(t_Sn_Sn1)), 3)

                if YTOn1 == False:
                    if YTFn and STFn_TOn1 and t_Sn_Sn1:
                        YTOn1 = np.round(YTFn + STFn_TOn1 * np.sin(Grad2Radyan(t_Sn_Sn1)), 3)
                    elif YSn1 and STOn1_Sn1 and t_Sn1_Sn:
                        YTOn1 = np.round(YSn1 + STOn1_Sn1 * np.sin(Grad2Radyan(t_Sn1_Sn)), 3)

                if XTOn1 == False:
                    if XTFn and STFn_TOn1 and t_Sn_Sn1:
                        XTOn1 = np.round(XTFn + STFn_TOn1 * np.cos(Grad2Radyan(t_Sn_Sn1)), 3)
                    elif XSn1 and STOn1_Sn1 and t_Sn1_Sn:
                        XTOn1 = np.round(XSn1 + STOn1_Sn1 * np.cos(Grad2Radyan(t_Sn1_Sn)), 3)

                if YSn1 == False:
                    if YTOn1 and STOn1_Sn1 and t_Sn_Sn_1:
                        YSn1 = np.round(YTOn1 + STOn1_Sn1 * np.sin(Grad2Radyan(t_Sn_Sn_1)), 3)

                if XSn1 == False:
                    if XTOn1 and STOn1_Sn1 and t_Sn_Sn_1:
                        XSn1 = np.round(XTOn1 + STOn1_Sn1 * np.cos(Grad2Radyan(t_Sn_Sn_1)), 3)

        except:
            QMessageBox.warning(self, "Warning", "Unexpected Error occured")
            return


        if self.KP_1.text() != "":

            KP = float(self.KP.text())


        self.outputList3.clear()
        self.outputList3.addItems([
            "R = {}".format(str(R)),
            "L = {}".format(str(L)),
            "\u0394 = {}".format(str(Delta)),
            "",
            "t(Sn-1,Sn) = {}".format(str(t_Sn_1_Sn)),
            "t(Sn, Sn-1) = {}".format(str(t_Sn_Sn_1)),
            "t(Sn,Sn+1) = {}".format(str(t_Sn_Sn1)),
            "t(Sn+1,Sn) = {}".format(str(t_Sn1_Sn)),
            "t(TOn,TFn) = {}".format(str(t_TOn_TFn)),
            "t(TFn,TOn) = {}".format(str(t_TFn_TOn)),
            "",
            "S(Sn,M) = {}".format(str(SSn_M)),
            "S(Sn,TOn) = {}".format(str(t)),
            "S(Sn,TFn) = {}".format(str(t)),
            "",
            "S(Sn,TFn-1) = {}".format(str(STFn_1_Sn)),
            "S(Sn,TOn+1) = {}".format(str(SSn_TOn1)),
            "S(Sn,Sn-1) = {}".format(str(SSn_Sn_1)),
            "S(Sn,Sn+1) = {}".format(str(SSn_Sn1)),
            "",
            "S(Fn-1,TOn) = {}".format(str(STFn_1_TOn)),
            "S(TFn,TOn+1) = {}".format(str(STFn_TOn1)),
            "S(Sn-1,TFn-1) = {}".format(str(SSn_1_TFn_1)),
            "S(TOn+1,Sn+1) = {}".format(str(STOn1_Sn1)),
            "",
            "S(TOn,TFn) = {}".format(str(STOn_TFn)),
            "",
            "KS(n-1) = {}".format(str(KSn_1)),
            "KTF(n-1) = {}".format(str(KTFn_1)),
            "KTO(n) = {}".format(str(KTOn)),
            "KSn = {}".format(str(KSn)),
            "KTF(n) = {}".format(str(KTFn)),
            "KTO(n+1) = {}".format(str(KTOn1)),
            "KSn1 = {}".format(str(KSn1)),
            "",
            "S(n-1)(Y = {}, X = {})".format(str(YSn_1), str(XSn_1)),
            "TF(n-1)(Y = {}, X = {})".format(str(YTFn_1), str(YTFn_1)),
            "TOn(Y = {},  X = {})".format(str(YTOn), str(XTOn)),
            "Sn(Y = {}, X = {})".format(str(YSn), str(XSn)),
            "TFn(Y = {}, X = {})".format(str(YTFn), str(XTFn)),
            "TOn(n+1)(Y = {}, X = {})".format(str(YTOn1), str(XTOn1)),
            "S(n+1)(Y = {}, X = {})".format(str(YSn1), str(XSn1)),
            "",
            "P(Y = {}, X = {})".format(str(YP), str(XP))
        ])



    def Route21Function(self):

        self.new_window = Route()
        self.new_window.show()

    def clear22Function(self):

        self.HS1_2.clear()
        self.KS1_2.clear()
        self.HS2_2.clear()
        self.KS2_2.clear()
        self.HS3_2.clear()
        self.KS3_2.clear()
        self.KP_2.clear()
        self.L_2.clear()
        self.outputList4.clear()
        self.outputList4.addItems([
            "g1 = ",
            "g2 = ",
            "G = ",
            "",
            "K(S1) = ",
            "K(TO) = ",
            "K(S2) = ",
            "K(TF) = ",
            "K(S3) = ",
            "",
            "H(S1) = ",
            "H(TO) = ",
            "H(S2) = ",
            "H(TF) = ",
            "H(S3) = ",
            "",
            "XE = ",
            "YE = ",
            "KE = ",
            "HE = ",
            "",
            "XP = ",
            "YP = ",
            "KP = ",
            "HP = ",
        ])

    def button22Function(self):

        g1 = False
        g2 = False
        G = False
        XE = False
        YE = False
        KE = False
        HE = False
        XP = False
        YP = False
        HP = False
        HTO = False
        KTO = False
        HTF = False
        KTF = False

        try:

            if self.HS1_2.text() != "":
                HS1 = float(self.HS1_2.text())
            else:
                HS1 = False

            if self.KS1_2.text() != "":
                KS1 = float(self.KS1_2.text())
            else:
                KS1 = False

            if self.HS2_2.text() != "":
                HS2 = float(self.HS2_2.text())
            else:
                HS2 = False

            if self.KS2_2.text() != "":
                KS2 = float(self.KS2_2.text())
            else:
                KS2 = False

            if self.HS3_2.text() != "":
                HS3 = float(self.HS3_2.text())
            else:
                HS3 = False

            if self.KS3_2.text() != "":
                KS3 = float(self.KS3_2.text())
            else:
                KS3 = False

            if self.KP_2.text() != "":
                KP = float(self.KP_2.text())
            else:
                KP = False

            if self.L_2.text() != "":
                L = float(self.L_2.text())
            else:
                L = False


            if HS2 and HS1 and KS2 and KS1:
                g1 = np.round((HS2 - HS1) / (KS2 - KS1), 2)

            if HS3 and HS2 and KS3 and KS2:
                g2 = np.round((HS3 - HS2) / (KS3 - KS2), 2)

            if g1 and g2:
                G = np.round(g2 - g1, 2)

            if HS2 and g1 and L:
                HTO = np.round(HS2 - g1 * (L / 2), 2)
                HTF = np.round(HS2 + g2 * (L / 2), 2)

            if KS2 and L:
                KTO = np.round(KS2 - L / 2, 3)
                KTF = np.round(KS2 + L / 2, 3)

            if g1 and L and G:
                XE = np.round(- g1 * (L / G), 4)
                if XE:
                    YE = np.round((G / (2 * L)) * XE ** 2 + g1 * XE, 4)

            if KTO and XE:
                KE = np.round(KTO + XE, 3)

            if KTO and YE:
                HE = np.round(HTO + YE, 3)

            if XE and YE and KP:
                XP = np.round(KP - KTO, 3)

            if XP and G and L and g1:
                YP = np.round((G / (2 * L)) * XP ** 2 + g1 * XP, 3)

            if HTO and YP:
                HP = np.round(HTO + YP, 3)

        except:
            QMessageBox.warning(self, "Warning", "Unexpected Error occured")
            return


        self.outputList4.clear()
        self.outputList4.addItems([
            "g1 = {}".format(str(g1)),
            "g2 = {}".format(str(g2)),
            "G = {}".format(str(G)),
            "",
            "K(S1) = {}".format(str(KS1)),
            "K(TO) = {}".format(str(KTO)),
            "K(S2) = {}".format(str(KS2)),
            "K(TF) = {}".format(str(KTF)),
            "K(S3) = {}".format(str(KS3)),
            "",
            "H(S1) = {}".format(str(HS1)),
            "H(TO) = {}".format(str(HTO)),
            "H(S2) = {}".format(str(HS2)),
            "H(TF) = {}".format(str(HTF)),
            "H(S3) = {}".format(str(HS3)),
            "",
            "XE = {}".format(str(XE)),
            "YE = {}".format(str(YE)),
            "KE = {}".format(str(KE)),
            "HE = {}".format(str(HE)),
            "",
            "XP = {}".format(str(XP)),
            "YP = {}".format(str(YP)),
            "KP = {}".format(str(KP)),
            "HP = {}".format(str(HP)),
        ])


    def Layouts2(self):

        mainLayout = QHBoxLayout()

        lowerLayout1 = QHBoxLayout()

        leftGroupBox = QGroupBox("Horizontal Route Geomety")

        leftLayout1 = QVBoxLayout()
        emptyLayout1 = QVBoxLayout()
        rightLayout1 = QVBoxLayout()

        hbox10_1 = QHBoxLayout()
        hbox11_1 = QHBoxLayout()
        hbox12_1 = QHBoxLayout()
        hbox13_1 = QHBoxLayout()
        hbox14_1 = QHBoxLayout()
        hbox15_1 = QHBoxLayout()
        hbox16_1 = QHBoxLayout()
        hbox17_1 = QHBoxLayout()
        hbox18_1 = QHBoxLayout()
        hbox19_1 = QHBoxLayout()
        hbox20_1 = QHBoxLayout()
        hbox21_1 = QHBoxLayout()
        hbox22_1 = QHBoxLayout()
        hbox23_1 = QHBoxLayout()
        hbox24_1 = QHBoxLayout()
        hbox25_1 = QHBoxLayout()
        hbox26_1 = QHBoxLayout()
        hbox27_1 = QHBoxLayout()
        hbox28_1 = QHBoxLayout()
        hbox29_1 = QHBoxLayout()
        hbox30_1 = QHBoxLayout()
        hbox31_1 = QHBoxLayout()
        hbox35_1 = QHBoxLayout()
        hbox36_1 = QHBoxLayout()
        hbox37_1 = QHBoxLayout()

        hbox11_1.addStretch()
        hbox11_1.addWidget(self.R_Label_1)
        hbox11_1.addWidget(self.R_1)
        hbox11_1.addStretch()
        hbox12_1.addStretch()
        hbox12_1.addWidget(self.Delta_Label_1)
        hbox12_1.addWidget(self.Delta_1)
        hbox12_1.addStretch()

        # M
        hbox13_1.addWidget(QLabel())
        hbox14_1.addStretch()
        hbox14_1.addWidget(self.YM_Label_1)
        hbox14_1.addWidget(self.YM_1)
        hbox14_1.addStretch()
        hbox14_1.addWidget(self.XM_label_1)
        hbox14_1.addWidget(self.XM_1)
        hbox14_1.addStretch()

        hbox15_1.addWidget(QLabel())
        hbox16_1.addStretch()
        hbox16_1.addWidget(self.KSn_1_Label_1)
        hbox16_1.addWidget(self.KSn_1_1)
        hbox16_1.addStretch()
        hbox16_1.addWidget(self.YSn_1_Label_1)
        hbox16_1.addWidget(self.YSn_1_1)
        hbox16_1.addStretch()
        hbox16_1.addWidget(self.XSn_1_Label_1)
        hbox16_1.addWidget(self.XSn_1_1)
        hbox16_1.addStretch()

        hbox17_1.addStretch()
        hbox17_1.addWidget(self.KTFn_1_Label_1)
        hbox17_1.addWidget(self.KTFn_1_1)
        hbox17_1.addStretch()
        hbox17_1.addWidget(self.YTFn_1_Label_1)
        hbox17_1.addWidget(self.YTFn_1_1)
        hbox17_1.addStretch()
        hbox17_1.addWidget(self.XTFn_1_Label_1)
        hbox17_1.addWidget(self.XTFn_1_1)
        hbox17_1.addStretch()

        # TOn, TOn+1
        hbox18_1.addStretch()
        hbox18_1.addWidget(self.KTOn_Label_1)
        hbox18_1.addWidget(self.KTOn_1)
        hbox18_1.addStretch()
        hbox18_1.addWidget(self.YTOn_Label_1)
        hbox18_1.addWidget(self.YTOn_1)
        hbox18_1.addStretch()
        hbox18_1.addWidget(self.XTOn_Label_1)
        hbox18_1.addWidget(self.XTOn_1)
        hbox18_1.addStretch()

        hbox19_1.addStretch()
        hbox19_1.addWidget(self.KSn_Label_1)
        hbox19_1.addWidget(self.KSn_1)
        hbox19_1.addStretch()
        hbox19_1.addWidget(self.YSn_Label_1)
        hbox19_1.addWidget(self.YSn_1)
        hbox19_1.addStretch()
        hbox19_1.addWidget(self.XSn_Label_1)
        hbox19_1.addWidget(self.XSn_1)
        hbox19_1.addStretch()

        hbox20_1.addStretch()
        hbox20_1.addWidget(self.KTFn_Label_1)
        hbox20_1.addWidget(self.KTFn_1)
        hbox20_1.addStretch()
        hbox20_1.addWidget(self.YTFn_Label_1)
        hbox20_1.addWidget(self.YTFn_1)
        hbox20_1.addStretch()
        hbox20_1.addWidget(self.XTFn_Label_1)
        hbox20_1.addWidget(self.XTFn_1)
        hbox20_1.addStretch()

        hbox21_1.addStretch()
        hbox21_1.addWidget(self.KTOn1_Label_1)
        hbox21_1.addWidget(self.KTOn1_1)
        hbox21_1.addStretch()
        hbox21_1.addWidget(self.YTOn1_Label_1)
        hbox21_1.addWidget(self.YTOn1_1)
        hbox21_1.addStretch()
        hbox21_1.addWidget(self.XTOn1_Label_1)
        hbox21_1.addWidget(self.XTOn1_1)
        hbox21_1.addStretch()

        hbox22_1.addStretch()
        hbox22_1.addWidget(self.KSn1_Label_1)
        hbox22_1.addWidget(self.KSn1_1)
        hbox22_1.addStretch()
        hbox22_1.addWidget(self.YSn1_Label_1)
        hbox22_1.addWidget(self.YSn1_1)
        hbox22_1.addStretch()
        hbox22_1.addWidget(self.XSn1_Label_1)
        hbox22_1.addWidget(self.XSn1_1)
        hbox22_1.addStretch()

        # distance
        hbox23_1.addWidget(QLabel())

        hbox24_1.addStretch()
        hbox24_1.addWidget(self.SSn_1_TFn_1_Label_1)
        hbox24_1.addWidget(self.SSn_1_TFn_1_1)
        hbox24_1.addStretch()
        hbox24_1.addWidget(self.STOn1_Sn1_Label_1)
        hbox24_1.addWidget(self.STOn1_Sn1_1)
        hbox24_1.addStretch()

        hbox25_1.addStretch()
        hbox25_1.addWidget(self.STFn_1_TOn_Label_1)
        hbox25_1.addWidget(self.STFn_1_TOn_1)
        hbox25_1.addStretch()
        hbox25_1.addWidget(self.STFn_TOn1_Label_1)
        hbox25_1.addWidget(self.STFn_TOn1_1)
        hbox25_1.addStretch()

        hbox26_1.addStretch()
        hbox26_1.addWidget(self.SSn_Sn_1_label_1)
        hbox26_1.addWidget(self.SSn_Sn_1_1)
        hbox26_1.addStretch()
        hbox26_1.addWidget(self.SSn_Sn1_label_1)
        hbox26_1.addWidget(self.SSn_Sn1_1)
        hbox26_1.addStretch()

        # azimuth
        hbox27_1.addWidget(QLabel())

        hbox28_1.addStretch()
        hbox28_1.addWidget(self.t_Sn_1_Sn_Label_1)
        hbox28_1.addWidget(self.t_Sn_1_Sn_1)
        hbox28_1.addStretch()
        hbox28_1.addWidget(self.t_Sn_Sn1_Label_1)
        hbox28_1.addWidget(self.t_Sn_Sn1_1)
        hbox28_1.addStretch()

        hbox29_1.addWidget(QLabel())

        hbox30_1.addStretch()
        hbox30_1.addWidget(self.KP_Label_1)
        hbox30_1.addWidget(self.KP_1)
        hbox30_1.addStretch()

        hbox31_1.addWidget(QLabel())

        hbox35_1.addWidget(self.combobox2)
        hbox35_1.addWidget(self.clearButton21)
        hbox35_1.addWidget(self.button21)
        hbox35_1.addWidget(self.RouteButton21)

        hbox37_1.addWidget(self.outputList3)

        leftLayout1.addLayout(hbox10_1)
        leftLayout1.addLayout(hbox11_1)
        leftLayout1.addLayout(hbox12_1)
        leftLayout1.addLayout(hbox13_1)
        leftLayout1.addLayout(hbox14_1)
        leftLayout1.addLayout(hbox15_1)
        leftLayout1.addLayout(hbox16_1)
        leftLayout1.addLayout(hbox17_1)
        leftLayout1.addLayout(hbox18_1)
        leftLayout1.addLayout(hbox19_1)
        leftLayout1.addLayout(hbox20_1)
        leftLayout1.addLayout(hbox21_1)
        leftLayout1.addLayout(hbox22_1)
        leftLayout1.addLayout(hbox23_1)
        leftLayout1.addLayout(hbox24_1)
        leftLayout1.addLayout(hbox25_1)
        leftLayout1.addLayout(hbox26_1)
        leftLayout1.addLayout(hbox27_1)
        leftLayout1.addLayout(hbox28_1)
        leftLayout1.addLayout(hbox29_1)
        leftLayout1.addLayout(hbox30_1)
        leftLayout1.addLayout(hbox31_1)
        leftLayout1.addStretch()
        leftLayout1.addStretch()
        leftLayout1.addLayout(hbox35_1)
        leftLayout1.addStretch()

        rightLayout1.addLayout(hbox36_1)
        rightLayout1.addLayout(hbox37_1)

        lowerLayout1.addLayout(leftLayout1, 64)
        lowerLayout1.addLayout(emptyLayout1, 2)
        lowerLayout1.addLayout(rightLayout1, 34)

        leftGroupBox.setLayout(lowerLayout1)

        ## vertical Route geometry
        rightGroupBox = QGroupBox("Vertical Route Geometry")

        lowerLayout2 = QHBoxLayout()

        TopLayout2 = QVBoxLayout()

        hbox10_2 = QHBoxLayout()
        hbox12_2 = QHBoxLayout()
        hbox14_2 = QHBoxLayout()
        hbox15_2 = QHBoxLayout()
        hbox18_2 = QHBoxLayout()
        hbox19_2 = QHBoxLayout()
        hbox20_2 = QHBoxLayout()

        hbox10_2.addStretch()
        hbox10_2.addWidget(self.HS1_Label_2)
        hbox10_2.addWidget(self.HS1_2)
        hbox10_2.addWidget(self.KS1_Label_2)
        hbox10_2.addWidget(self.KS1_2)
        hbox10_2.addStretch()
        hbox12_2.addStretch()
        hbox12_2.addWidget(self.HS2_Label_2)
        hbox12_2.addWidget(self.HS2_2)
        hbox12_2.addWidget(self.KS2_Label_2)
        hbox12_2.addWidget(self.KS2_2)
        hbox12_2.addStretch()
        hbox14_2.addStretch()
        hbox14_2.addWidget(self.HS3_Label_2)
        hbox14_2.addWidget(self.HS3_2)
        hbox14_2.addWidget(self.KS3_Label_2)
        hbox14_2.addWidget(self.KS3_2)
        hbox14_2.addStretch()

        hbox15_2.addStretch()
        hbox15_2.addWidget(self.L_Label_2)
        hbox15_2.addWidget(self.L_2)
        hbox15_2.addWidget(self.KP_Label_2)
        hbox15_2.addWidget(self.KP_2)
        hbox15_2.addStretch()

        hbox18_2.addWidget(QLabel())

        hbox19_2.addStretch()
        hbox19_2.addWidget(self.clearButton22)
        hbox19_2.addWidget(self.button22)
        hbox19_2.addStretch()

        hbox20_2.addWidget(self.outputList4)

        TopLayout2.addLayout(hbox10_2)
        TopLayout2.addLayout(hbox12_2)
        TopLayout2.addLayout(hbox14_2)
        TopLayout2.addLayout(hbox15_2)
        TopLayout2.addLayout(hbox18_2)
        TopLayout2.addLayout(hbox19_2)
        TopLayout2.addLayout(hbox20_2)

        lowerLayout2.addLayout(TopLayout2)

        rightGroupBox.setLayout(lowerLayout2)


        mainLayout.addWidget(leftGroupBox, 70)
        mainLayout.addWidget(rightGroupBox, 30)

        self.SecondTab.setLayout(mainLayout)


    def Widgets3(self):

        self.R_Label_3_1 = QLabel("          R :")
        self.R_3_1 = QLineEdit()
        self.R_3_1.setMaximumWidth(150)
        self.R_3_1.setFont(QFont("Times", 9))

        self.Tau_Label_3_1 = QLabel("          \u03C4 :")
        self.Tau_3_1 = QLineEdit()
        self.Tau_3_1.setMaximumWidth(150)
        self.Tau_3_1.setFont(QFont("Times", 9))

        self.A_Label_3_1 = QLabel("          A :")
        self.A_3_1 = QLineEdit()
        self.A_3_1.setMaximumWidth(150)
        self.A_3_1.setFont(QFont("Times", 9))

        self.YO_Label_3_1 = QLabel("        YO :")
        self.YO_3_1 = QLineEdit()
        self.YO_3_1.setMaximumWidth(150)
        self.YO_3_1.setFont(QFont("Times", 9))
        self.XO_Label_3_1 = QLabel("        XO :")
        self.XO_3_1 = QLineEdit()
        self.XO_3_1.setMaximumWidth(150)
        self.XO_3_1.setFont(QFont("Times", 9))

        self.t_O_TO_Label_3_1 = QLabel(" t(O,TO) :")
        self.t_O_TO_3_1 = QLineEdit()
        self.t_O_TO_3_1.setMaximumWidth(150)
        self.t_O_TO_3_1.setFont(QFont("Times", 9))

        self.clearButton31 = QPushButton("Clear")
        self.clearButton31.setMaximumWidth(120)
        self.clearButton31.clicked.connect(self.clear31Function)

        self.button31 = QPushButton("Calculate")
        self.button31.setMaximumWidth(120)
        self.button31.clicked.connect(self.button31Function)

        self.RouteButton31 = QPushButton("Route")
        self.RouteButton31.setMaximumWidth(120)
        self.RouteButton31.clicked.connect(self.Route31Function)

        self.outputList5 = QListWidget()
        self.outputList5.setMinimumHeight(300)
        self.outputList5.setMinimumWidth(290)
        self.outputList5.setMaximumWidth(360)
        self.outputList5.setFont(QFont("Times", 9))
        self.outputList5.addItems([
            "   A = ",
            "   L = ",
            "   \u03C4 = ",
            "   x = ",
            "   y = ",
            "   \u03B1 = ",
            "   S(O,TO) = ",
            "   TO(Y = , X = )",
        ])


        #Transition Curves
        self.Delta_Label_3 = QLabel("\u0394 :")
        self.Delta_3 = QLineEdit()
        self.Delta_3.setMaximumWidth(150)
        self.Delta_3.setFont(QFont("Times", 9))

        self.R_Label_3 = QLabel("R :")
        self.R_3 = QLineEdit()
        self.R_3.setMaximumWidth(150)
        self.R_3.setFont(QFont("Times", 9))

        self.Tau1_Label_3 = QLabel("  \u03C41 :")
        self.Tau1_3 = QLineEdit()
        self.Tau1_3.setMaximumWidth(150)
        self.Tau1_3.setFont(QFont("Times", 9))

        self.Tau2_Label_3 = QLabel("  \u03C42 :")
        self.Tau2_3 = QLineEdit()
        self.Tau2_3.setMaximumWidth(150)
        self.Tau2_3.setFont(QFont("Times", 9))

        self.L1_Label_3 = QLabel("  L1 :")
        self.L1_3 = QLineEdit()
        self.L1_3.setMaximumWidth(150)
        self.L1_3.setFont(QFont("Times", 9))

        self.L2_Label_3 = QLabel("  L2 :")
        self.L2_3 = QLineEdit()
        self.L2_3.setMaximumWidth(150)
        self.L2_3.setFont(QFont("Times", 9))

        self.y1_Label_3 = QLabel("  y1 :")
        self.y1_3 = QLineEdit()
        self.y1_3.setMaximumWidth(150)
        self.y1_3.setFont(QFont("Times", 9))
        self.x1_Label_3 = QLabel("  x1 :")
        self.x1_3 = QLineEdit()
        self.x1_3.setMaximumWidth(150)
        self.x1_3.setFont(QFont("Times", 9))

        self.y2_Label_3 = QLabel("  y2 :")
        self.y2_3 = QLineEdit()
        self.y2_3.setMaximumWidth(150)
        self.y2_3.setFont(QFont("Times", 9))
        self.x2_Label_3 = QLabel("  x2 :")
        self.x2_3 = QLineEdit()
        self.x2_3.setMaximumWidth(150)
        self.x2_3.setFont(QFont("Times", 9))

        self.YSn_Label_3 = QLabel("YSn :")
        self.YSn_3 = QLineEdit()
        self.YSn_3.setMaximumWidth(150)
        self.YSn_3.setFont(QFont("Times", 9))
        self.XSn_Label_3 = QLabel("XSn :")
        self.XSn_3 = QLineEdit()
        self.XSn_3.setMaximumWidth(150)
        self.XSn_3.setFont(QFont("Times", 9))

        self.t_Sn_On_Label_3 = QLabel("         t(Sn, On) :")
        self.t_Sn_On_3 = QLineEdit()
        self.t_Sn_On_3.setMaximumWidth(150)
        self.t_Sn_On_3.setFont(QFont("Times", 9))

        self.t_Sn_On_Prime_Label_3 = QLabel("t(Sn,On(prime)) :")
        self.t_Sn_On_Prime_3 = QLineEdit()
        self.t_Sn_On_Prime_3.setMaximumWidth(150)
        self.t_Sn_On_Prime_3.setFont(QFont("Times", 9))

        self.alpha_Label_3 = QLabel("                     \u03B1 :")
        self.alpha_3 = QLineEdit()
        self.alpha_3.setMaximumWidth(150)
        self.alpha_3.setFont(QFont("Times", 9))

        self.KOn_Label_3 = QLabel("                 KOn :")
        self.KOn_3 = QLineEdit()
        self.KOn_3.setMaximumWidth(150)
        self.KOn_3.setFont(QFont("Times", 9))

        self.A_A1_A2 = QRadioButton("A1 = A2")
        self.A_A1_A2.setFont(QFont("Times", 9))
        self.A_A1_A2.setChecked(True)

        self.clearButton32 = QPushButton("Clear")
        self.clearButton32.setMaximumWidth(120)
        self.clearButton32.clicked.connect(self.clear32Function)

        self.button32 = QPushButton("Calculate")
        self.button32.setMaximumWidth(120)
        self.button32.clicked.connect(self.button32Function)

        self.RouteButton32 = QPushButton("Route")
        self.RouteButton32.setMaximumWidth(120)
        self.RouteButton32.clicked.connect(self.Route32Function)

        self.outputList6 = QListWidget()
        self.outputList6.setMinimumHeight(300)
        self.outputList6.setMaximumWidth(360)
        self.outputList6.setFont(QFont("Times", 9))
        self.outputList6.addItems([
            "   DR = ",
            "   t = ",
            "   Xm = ",
            "   T = ",
            "   On (Y = , X = )",
            "   On(prime) (Y = , X = )",
            "   \u03B1 = ",
            "   Ld = ",
            "   KOn = ",
            "   KTo = ",
            "   KTf = ",
            "   KOn(prime) = ",
        ])


    def clear31Function(self):

        self.R_3_1.clear()
        self.Tau_3_1.clear()
        self.A_3_1.clear()
        self.YO_3_1.clear()
        self.XO_3_1.clear()
        self.t_O_TO_3_1.clear()
        self.outputList5.clear()
        self.outputList5.addItems([
            "   A = ",
            "   L = ",
            "   \u03C4 = ",
            "   x = ",
            "   y = ",
            "   \u03B1 = ",
            "   S(O,TO) = ",
            "   TO(Y = , X = )",
        ])


    def button31Function(self):

        Ro = 200 / np.pi

        L = False
        x = False
        y = False
        alpha = False
        S_O_TO = False
        t_O_TO = False
        YTO = False
        XTO = False


        try:
            if self.R_3_1.text() != "":
                R = float(self.R_3_1.text())
            else:
                R = False

            if self.Tau_3_1.text() != "":
                Tau = float(self.Tau_3_1.text())
            else:
                Tau = False

            if self.A_3_1.text() != "":
                A = float(self.A_3_1.text())
            else:
                A = False

            if self.YO_3_1.text() != "":
                YO = float(self.YO_3_1.text())
            else:
                YO = False

            if self.XO_3_1.text() != "":
                XO = float(self.XO_3_1.text())
            else:
                XO = False

            if self.t_O_TO_3_1.text() != "":
                t_O_TO = float(self.t_O_TO_3_1.text())
            else:
                t_O_TO = False


            for i in range(5):

                if A == False:
                    if R and Tau:
                        A = np.round((2 * (R ** 2) * Tau * (1 / Ro)) ** 0.5)

                if L == False:
                    if A and R:
                        L = np.round(A ** 2 / R, 3)

                if Tau == False:
                    if L and A:
                        Tau = np.round((L ** 2 / (2 * A ** 2)) * Ro, 4)

                if x == False:
                    if L:
                        x = np.round(L - (L ** 5) / (40 * (A ** 4)) + (L ** 9) / (3456 * (A ** 8)) - (L * 13) / (599040 * (A ** 12)), 3)


                if y == False:
                    if L:
                        y = np.round((L ** 3) / (6 * (A ** 2)) - (L ** 7) / (336 * (A ** 6)) + (L ** 11) / (42240 * (A ** 10)) - (L ** 15) / (9676800 * (A ** 14)), 3)

                if alpha == False:
                    if x and y:
                        alpha = np.round(Radyan2Grad(np.arctan(y / x)), 4)

                if S_O_TO == False:
                    if x and y:
                        S_O_TO = np.round((x ** 2 + y ** 2) ** 0.5, 3)

                if YTO == False or XTO == False:
                    if t_O_TO and YO and XO and S_O_TO:
                        YTO = np.round(YO + S_O_TO * np.sin(Grad2Radyan(t_O_TO)), 4)
                        XTO = np.round(XO + S_O_TO * np.cos(Grad2Radyan(t_O_TO)), 4)

        except:
            QMessageBox.warning(self, "Warning", "Unexpected Error occured")
            return

        self.outputList5.clear()
        self.outputList5.addItems([
            "   A = {}".format(str(A)),
            "   L = {}".format(str(L)),
            "   \u03C4 = {}".format(str(Tau)),
            "   x = {}".format(str(x)),
            "   y = {}".format(str(y)),
            "   \u03B1 = {}".format(str(alpha)),
            "   S(O,TO) = {}".format(str(S_O_TO)),
            "   TO(Y = {}, X = {})".format(str(YTO), str(XTO))
        ])


    def Route31Function(self):
        self.route2 = Route2()
        self.route2.show()


    def clear32Function(self):

        self.Delta_3.clear()
        self.R_3.clear()
        self.Tau1_3.clear()
        self.Tau2_3.clear()
        self.KOn_3.clear()
        self.L1_3.clear()
        self.L2_3.clear()
        self.y1_3.clear()
        self.x1_3.clear()
        self.y2_3.clear()
        self.x2_3.clear()
        self.YSn_3.clear()
        self.XSn_3.clear()
        self.t_Sn_On_3.clear()
        self.t_Sn_On_Prime_3.clear()
        self.alpha_3.clear()
        self.A_A1_A2.setChecked(True)
        self.outputList6.clear()
        self.outputList6.addItems([
            "   DR = ",
            "   t = ",
            "   Xm = ",
            "   T = ",
            "   On (Y = , X = )",
            "   On(prime) (Y = , X = )",
            "   \u03B1 = ",
            "   Ld = ",
            "   KOn = ",
            "   KTo = ",
            "   KTf = ",
            "   KOn(prime) = ",
        ])


    def button32Function(self):

        Ro = 200 / np.pi

        DR1 = False
        DR2 = False
        Xm1 = False
        Xm2 = False
        t1 = False
        t2 = False
        z1 = False
        z2 = False
        T1 = False
        T2 = False
        YOn = False
        XOn = False
        YOn_Prime = False
        XOn_Prime = False
        Ld = False
        KTo = False
        KTf = False
        KOn_prime = False

        try:
            if self.Delta_3.text() != "":
                Delta = float(self.Delta_3.text())
            else:
                Delta = False

            if self.R_3.text() != "":
                R = float(self.R_3.text())
            else:
                R = False

            if self.Tau1_3.text() != "":
                Tau1 = float(self.Tau1_3.text())
            else:
                Tau1 = False

            if self.Tau2_3.text() != "":
                Tau2 = float(self.Tau2_3.text())
            else:
                Tau2 = False

            if self.KOn_3.text() != "":
                KOn = float(self.KOn_3.text())
            else:
                KOn = False

            if self.L1_3.text() != "":
                L1 = float(self.L1_3.text())
            else:
                L1 = False

            if self.L2_3.text() != "":
                L2 = float(self.L2_3.text())
            else:
                L2 = False

            if self.y1_3.text() != "":
                y1 = float(self.y1_3.text())
            else:
                y1 = False

            if self.x1_3.text() != "":
                x1 = float(self.x1_3.text())
            else:
                x1 = False

            if self.y2_3.text() != "":
                y2 = float(self.y2_3.text())
            else:
                y2 = False

            if self.x2_3.text() != "":
                x2 = float(self.x2_3.text())
            else:
                x2 = False

            if self.YSn_3.text() != "":
                YSn = float(self.YSn_3.text())
            else:
                YSn = False

            if self.XSn_3.text() != "":
                XSn = float(self.XSn_3.text())
            else:
                XSn = False

            if self.t_Sn_On_3.text() != "":
                t_Sn_On = float(self.t_Sn_On_3.text())
            else:
                t_Sn_On = False

            if self.t_Sn_On_Prime_3.text() != "":
                t_Sn_On_Prime = float(self.t_Sn_On_Prime_3.text())
            else:
                t_Sn_On_Prime = False

            if self.alpha_3.text() != "":
                alpha = float(self.alpha_3.text())
            else:
                alpha = False


            for _ in range(10):

                if y1 and R and Tau1:
                    DR1 = np.round(y1 + R * np.cos(Grad2Radyan(Tau1)) - R, 3)
                    if not self.A_A1_A2.isChecked():
                        if Tau2 and y2:
                            DR2 = np.round(y2 + R * np.cos(Grad2Radyan(Tau2)) - R, 3)

                if DR1 and R and Delta:
                    t1 = np.round((R + DR1) * np.tan(Grad2Radyan(Delta / 2)), 3)
                    if not self.A_A1_A2.isChecked():
                        if DR2:
                            t2 = np.round((R + DR2) * np.tan(Grad2Radyan(Delta / 2)), 3)

                if x1 and R and Tau1:
                    Xm1 = np.round(x1 - R * np.sin(Grad2Radyan(Tau1)), 3)
                    if not self.A_A1_A2.isChecked():
                        if x2 and Tau2:
                            Xm2 = np.round(x2 - R * np.sin(Grad2Radyan(Tau2)), 3)

                if not self.A_A1_A2.isChecked():
                    if DR1 and DR2 and Delta:
                        z1 = np.round((DR1 - DR2) / np.sin(Grad2Radyan(Delta)), 3)
                        z2 = np.round((DR1 - DR2) / np.tan(Grad2Radyan(Delta)), 3)

                if T1 == False:
                    if self.A_A1_A2.isChecked():
                        if Xm1 and t1:
                            T1 = np.round(Xm1 + t1, 3)
                    else:
                        if Xm1 and t1 and z1:
                            T1 = np.round(Xm1 + t1 - z1, 3)

                if T2 == False:
                    if not self.A_A1_A2.isChecked():
                        if Xm2 and t2 and z2:
                            T2 = np.round(Xm2 + t2 + z2, 3)

                if YOn == False:
                    if YSn and T1 and t_Sn_On:
                        YOn = np.round(YSn + T1 * np.sin(Grad2Radyan(t_Sn_On)), 4)

                if XOn == False:
                    if XSn and T1 and t_Sn_On:
                        XOn = np.round(XSn + T1 * np.cos(Grad2Radyan(t_Sn_On)), 4)

                if YOn_Prime == False:
                    if self.A_A1_A2.isChecked():
                        if YSn and T1 and t_Sn_On_Prime:
                            YOn_Prime = np.round(YSn + T1 * np.sin(Grad2Radyan(t_Sn_On_Prime)), 4)
                    else:
                        if YSn and T2 and t_Sn_On_Prime:
                            YOn_Prime = np.round(YSn + T2 * np.sin(Grad2Radyan(t_Sn_On_Prime)), 4)

                if XOn_Prime == False:
                    if self.A_A1_A2.isChecked():
                        if XSn and T1 and t_Sn_On_Prime:
                            XOn_Prime = np.round(XSn + T1 * np.cos(Grad2Radyan(t_Sn_On_Prime)), 4)
                    else:
                        if XSn and T2 and t_Sn_On_Prime:
                            XOn_Prime = np.round(XSn + T2 * np.cos(Grad2Radyan(t_Sn_On_Prime)), 4)

                if alpha == False:
                    if self.A_A1_A2.isChecked():
                        if Delta and Tau1:
                            alpha = np.round(Delta - 2 * Tau1, 4)
                    else:
                        if Delta and Tau1 and Tau2:
                            alpha = np.round(Delta - Tau1 - Tau2, 4)

                if Ld == False:
                    if alpha and R:
                        Ld = np.round((np.pi * R * alpha) / 200, 3)

                if KTo == False:
                    if KOn and L1:
                        KTo = np.round(KOn + L1, 3)

                if KTf == False:
                    if KTo and Ld:
                        KTf = np.round(KTo + Ld, 3)

                if KOn_prime == False:
                    if self.A_A1_A2.isChecked():
                        if KTf and L1:
                            KOn_prime = np.round(KTf + L1, 3)
                    else:
                        if KTf and L2:
                            KOn_prime = np.round(KTf + L2, 3)

        except:
            QMessageBox.warning(self, "Warning", "Unexpected Error occured")
            return

        if self.A_A1_A2.isChecked():
            self.outputList6.clear()
            self.outputList6.addItems([
                "   DR = {}".format(str(DR1)),
                "   t = {}".format(str(t1)),
                "   Xm = {}".format(str(Xm1)),
                "   T = {}".format(str(T1)),
                "   On (Y = {}, X = {})".format(str(YOn), str(XOn)),
                "   On(prime) (Y = {}, X = {})".format(str(YOn_Prime), str(XOn_Prime)),
                "   \u03B1 = {}".format(str(alpha)),
                "   Ld = {}".format(str(Ld)),
                "   KOn = {}".format(str(KOn)),
                "   KTo = {}".format(str(KTo)),
                "   KTf = {}".format(str(KTf)),
                "   KOn(prime) = {}".format(str(KOn_prime))
            ])

        else:
            self.outputList6.clear()
            self.outputList6.addItems([
                "   DR1 = {}".format(str(DR1)),
                "   DR2 = {}".format(str(DR2)),
                "   t1 = {}".format(str(t1)),
                "   t2 = {}".format(str(t2)),
                "   Xm1 = {}".format(str(Xm1)),
                "   Xm2 = {}".format(str(Xm2)),
                "   z1 = {}".format(str(z1)),
                "   z2 = {}".format(str(z2)),
                "   T1 = {}".format(str(T1)),
                "   T2 = {}".format(str(T2)),
                "   On (Y = {}, X = {})".format(str(YOn), str(XOn)),
                "   On(prime) (Y = {}, X = {})".format(str(YOn_Prime), str(XOn_Prime)),
                "   \u03B1 = {}".format(str(alpha)),
                "   Ld = {}".format(str(Ld)),
                "   KOn = {}".format(str(KOn)),
                "   KTo = {}".format(str(KTo)),
                "   KTf = {}".format(str(KTf)),
                "   KOn(prime) = {}".format(str(KOn_prime))
            ])


    def Route32Function(self):

        self.route3 = Route3()
        self.route3.show()


    def Layouts3(self):

        mainLayout = QHBoxLayout()

        FirstGroupBoxLayout = QGroupBox("Clothoid Paramaters")

        SecondGroupBoxLayout = QGroupBox("Transition Curves")

        lowerLayout1 = QVBoxLayout()

        hbox9_1 = QHBoxLayout()
        hbox10_1 = QHBoxLayout()
        hbox11_1 = QHBoxLayout()
        hbox12_1 = QHBoxLayout()
        hbox13_1 = QHBoxLayout()
        hbox14_1 = QHBoxLayout()
        hbox15_1 = QHBoxLayout()
        hbox16_1 = QHBoxLayout()
        hbox17_1 = QHBoxLayout()
        hbox18_1 = QHBoxLayout()
        hbox19_1 = QHBoxLayout()

        hbox9_1.addStretch()
        hbox9_1.addWidget(self.R_Label_3_1)
        hbox9_1.addWidget(self.R_3_1)
        hbox9_1.addStretch()

        hbox10_1.addStretch()
        hbox10_1.addWidget(self.Tau_Label_3_1)
        hbox10_1.addWidget(self.Tau_3_1)
        hbox10_1.addStretch()

        hbox11_1.addStretch()
        hbox11_1.addWidget(self.A_Label_3_1)
        hbox11_1.addWidget(self.A_3_1)
        hbox11_1.addStretch()

        hbox12_1.addStretch()
        hbox12_1.addWidget(self.YO_Label_3_1)
        hbox12_1.addWidget(self.YO_3_1)
        hbox12_1.addStretch()

        hbox13_1.addStretch()
        hbox13_1.addWidget(self.XO_Label_3_1)
        hbox13_1.addWidget(self.XO_3_1)
        hbox13_1.addStretch()

        hbox15_1.addStretch()
        hbox15_1.addWidget(self.t_O_TO_Label_3_1)
        hbox15_1.addWidget(self.t_O_TO_3_1)
        hbox15_1.addStretch()

        hbox18_1.addStretch()
        hbox18_1.addWidget(self.clearButton31)
        hbox18_1.addWidget(self.button31)
        hbox18_1.addWidget(self.RouteButton31)
        hbox18_1.addStretch()

        hbox19_1.addStretch()
        hbox19_1.addWidget(self.outputList5)
        hbox19_1.addStretch()

        lowerLayout1.addLayout(hbox9_1)
        lowerLayout1.addLayout(hbox10_1)
        lowerLayout1.addLayout(hbox11_1)
        lowerLayout1.addLayout(hbox12_1)
        lowerLayout1.addLayout(hbox13_1)
        lowerLayout1.addLayout(hbox14_1)
        lowerLayout1.addLayout(hbox15_1)
        lowerLayout1.addLayout(hbox16_1)
        lowerLayout1.addLayout(hbox17_1)
        lowerLayout1.addLayout(hbox18_1)
        lowerLayout1.addLayout(hbox19_1)

        # transition Curves
        lowerLayout2 = QVBoxLayout()

        hbox9_2 = QHBoxLayout()
        hbox10_2 = QHBoxLayout()
        hbox11_2 = QHBoxLayout()
        hbox13_2 = QHBoxLayout()
        hbox14_2 = QHBoxLayout()
        hbox15_2 = QHBoxLayout()
        hbox16_2 = QHBoxLayout()
        hbox18_2 = QHBoxLayout()
        hbox19_2 = QHBoxLayout()
        hbox20_2 = QHBoxLayout()
        hbox21_2 = QHBoxLayout()
        hbox23_2 = QHBoxLayout()
        hbox24_2 = QHBoxLayout()
        hbox25_2 = QHBoxLayout()

        hbox9_2.addStretch()
        hbox9_2.addWidget(self.Delta_Label_3)
        hbox9_2.addWidget(self.Delta_3)
        hbox9_2.addStretch()

        hbox10_2.addStretch()
        hbox10_2.addWidget(self.R_Label_3)
        hbox10_2.addWidget(self.R_3)
        hbox10_2.addStretch()

        hbox11_2.addStretch()
        hbox11_2.addWidget(self.Tau1_Label_3)
        hbox11_2.addWidget(self.Tau1_3)
        hbox11_2.addWidget(self.Tau2_Label_3)
        hbox11_2.addWidget(self.Tau2_3)
        hbox11_2.addStretch()

        hbox13_2.addStretch()
        hbox13_2.addWidget(self.L1_Label_3)
        hbox13_2.addWidget(self.L1_3)
        hbox13_2.addWidget(self.L2_Label_3)
        hbox13_2.addWidget(self.L2_3)
        hbox13_2.addStretch()

        hbox14_2.addStretch()
        hbox14_2.addWidget(self.y1_Label_3)
        hbox14_2.addWidget(self.y1_3)
        hbox14_2.addWidget(self.x1_Label_3)
        hbox14_2.addWidget(self.x1_3)
        hbox14_2.addStretch()

        hbox15_2.addStretch()
        hbox15_2.addWidget(self.y2_Label_3)
        hbox15_2.addWidget(self.y2_3)
        hbox15_2.addWidget(self.x2_Label_3)
        hbox15_2.addWidget(self.x2_3)
        hbox15_2.addStretch()

        hbox16_2.addStretch()
        hbox16_2.addWidget(self.YSn_Label_3)
        hbox16_2.addWidget(self.YSn_3)
        hbox16_2.addWidget(self.XSn_Label_3)
        hbox16_2.addWidget(self.XSn_3)
        hbox16_2.addStretch()

        hbox18_2.addStretch()
        hbox18_2.addWidget(self.t_Sn_On_Label_3)
        hbox18_2.addWidget(self.t_Sn_On_3)
        hbox18_2.addStretch()

        hbox19_2.addStretch()
        hbox19_2.addWidget(self.t_Sn_On_Prime_Label_3)
        hbox19_2.addWidget(self.t_Sn_On_Prime_3)
        hbox19_2.addStretch()

        hbox20_2.addStretch()
        hbox20_2.addWidget(self.alpha_Label_3)
        hbox20_2.addWidget(self.alpha_3)
        hbox20_2.addStretch()

        hbox21_2.addStretch()
        hbox21_2.addWidget(self.KOn_Label_3)
        hbox21_2.addWidget(self.KOn_3)
        hbox21_2.addStretch()

        hbox23_2.addStretch()
        hbox23_2.addWidget(self.A_A1_A2)
        hbox23_2.addStretch()

        hbox24_2.addStretch()
        hbox24_2.addWidget(self.clearButton32)
        hbox24_2.addWidget(self.button32)
        hbox24_2.addWidget(self.RouteButton32)
        hbox24_2.addStretch()

        hbox25_2.addWidget(self.outputList6)

        lowerLayout2.addLayout(hbox9_2)
        lowerLayout2.addLayout(hbox10_2)
        lowerLayout2.addLayout(hbox11_2)
        lowerLayout2.addLayout(hbox13_2)
        lowerLayout2.addLayout(hbox14_2)
        lowerLayout2.addLayout(hbox15_2)
        lowerLayout2.addLayout(hbox16_2)
        lowerLayout2.addLayout(hbox18_2)
        lowerLayout2.addLayout(hbox19_2)
        lowerLayout2.addLayout(hbox20_2)
        lowerLayout2.addLayout(hbox21_2)
        lowerLayout2.addLayout(hbox23_2)
        lowerLayout2.addLayout(hbox24_2)
        lowerLayout2.addLayout(hbox25_2)

        FirstGroupBoxLayout.setLayout(lowerLayout1)

        SecondGroupBoxLayout.setLayout(lowerLayout2)

        mainLayout.addWidget(FirstGroupBoxLayout)
        mainLayout.addWidget(SecondGroupBoxLayout)

        self.ThirdTab.setLayout(mainLayout)




def StartWindow():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    StartWindow()

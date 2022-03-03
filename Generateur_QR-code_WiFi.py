import wifi_qrcode_generator
from pathlib import Path
import os
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout,\
    QHBoxLayout, QWidget, QLabel, QLineEdit, QMessageBox

ssid = ""
pwd = ""


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Générateur de QR-code")
        self.modify_widgets()

        main_layout = QHBoxLayout(self)  # self apparente layout à ma classe
        # je crer une main layout horizontale avec dedant 3 layout verticaux
        self.resize(700, 100)

        generer_qrcode = self.generer_qrcode

        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout)
        for i in ("Maison", "vide", "vide", "vide"):
            button = QPushButton(str(i))
            #left_layout.addWidget(button)
        
        bas_layout = QVBoxLayout()
        btn_layout = QHBoxLayout()
        main_layout.addLayout(bas_layout)
        
        
        self.lbl_text = QLabel("Pour générer un QR-code de connexion à votre WiFi "\
            "entrer ses identifiants puis appuyer sur Générer\nUn fichier QR-code.png"\
            " sera créé sur votre bureau  ")
        self.le_ssid = QLineEdit()
        self.le_ssid.setCursorPosition(0)
        self.le_ssid.setPlaceholderText("Entrer içi le nom de votre réseau")
        self.le_pwd = QLineEdit()
        self.le_pwd.setPlaceholderText("Entrer içi le mot de passe de votre box")

        bas_layout.addWidget(self.lbl_text)
        bas_layout.addWidget(self.le_ssid)
        bas_layout.addWidget(self.le_pwd)
        

        bas_layout.addLayout(btn_layout)
        self.btn_generer = QPushButton("Générer")
        self.btn_clear = QPushButton("Effacer")
        self.btn_aide = QPushButton("Aide")
        btn_layout.addWidget(self.btn_generer)
        btn_layout.addWidget(self.btn_clear)
        btn_layout.addWidget(self.btn_aide)
        

        self.btn_generer.clicked.connect(self.generer_qrcode)
        self.btn_clear.clicked.connect(self.efface)
        self.btn_aide.clicked.connect(self.aide)
        
    def generer_qrcode(self):
        """ va générer un fichier contenant un qr-code pour la conexion au WiFi """
        home = Path.home()
        qrcode_wifi = home /"Bureau"/"QR-code.png"
        qrcode = wifi_qrcode_generator.wifi_qrcode(self.le_ssid.text(), False, "WPA", self.le_pwd.text())
        print(qrcode)
        qrcode_wifi.touch()
        qrcode.save(qrcode_wifi)
        

    def efface(self):
        self.btn_clear.clicked.connect(self.le_ssid.clear)
        self.btn_clear.clicked.connect(self.le_pwd.clear)

    def aide(self):
        message_box = QMessageBox()
        message_box.setWindowTitle("Aide")
        message_box.setText("Ce logiciel va vous créer le fichier QR-code.png \n"\
        "qui contiendra l'image du QR-code. \n"\
        "Avec une application de scan de QR-code sur \n"\
        "votre smart-phone ou votre tablette. Vous allez\n"\
        "pouvoir récupérer les identifiants de votre WiFi \n"\
        "afin de vous y connecter.\n"\
        "Pour ce faire: \n"\
        "Compléter les 2 lignes de saisie avec le nom de votre \n"\
        "réseau (ssid) et son mot de passe\n"\
        "Puis appuyer sur le bouton Générer pour créer le fichier.\n"\
        "Le fichier sera sur votre bureau\n"\
        "Ecrit le 11 février 2022 par Alain Meynard.\n"\
        "E-mail:  f5gfe@wanadoo.fr"
        )
        message_box.exec_()

    def modify_widgets(self):
        css_file = Path.cwd() /"style.css"
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())


app = QApplication()
mainwindow = MainWindow()
mainwindow.show()
app.exec()
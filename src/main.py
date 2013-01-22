#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
from PyQt4 import QtCore, QtGui
from gui import Ui_MainWindow

class principal(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)

        command = 'systemctl is-active firewalld.service'
        serviceStatus = os.system(command)

        if serviceStatus == 0:
            self.ventana.label_2.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Activado</span></p></body></html>")
            self.ventana.pushButton.setText("Desactivar")

        self.connect(self.ventana.pushButton, QtCore.SIGNAL('clicked()'), self.switch)

    def switch(self):

        command = 'systemctl is-active firewalld.service'
        serviceStatus = os.system(command)

        if serviceStatus == 0:
            os.system('beesu systemctl stop firewalld.service')
            self.ventana.label_2.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#FF0000\">Desactivado</span></p></body></html>")
            self.ventana.pushButton.setText("Activar")
        elif serviceStatus == 768:
            os.system('beesu systemctl start firewalld.service')
            self.ventana.label_2.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Activado</span></p></body></html>")
            self.ventana.pushButton.setText("Desactivar")

def main():
    app = QtGui.QApplication(sys.argv)
    ventana = principal()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

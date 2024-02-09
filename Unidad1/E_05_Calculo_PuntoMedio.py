import sys
from PyQt5 import uic,QtWidgets
qtCreatorFile = "E_05_Calculo_PuntoMedio.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los signals
        self.pushButton.clicked.connect(self.puntomedio)

    def puntomedio(self):
        puntomedio = int((int(self.numero1.text())+int(self.numero2.text()))/2)
        calculo = "El punto medio de los valores ingresados es " + str(puntomedio)
        self.resultado.setText(calculo)
        self.numero1.clear()
        self.numero2.clear()


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())

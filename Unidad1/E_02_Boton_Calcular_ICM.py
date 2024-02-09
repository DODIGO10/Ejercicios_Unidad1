import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_02_Boton_Calcular_ICM.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_ICM.clicked.connect(self.icm)
        self.txt_resultado.setEnabled(False)
    # Área de los Slots
    def icm(self):
        peso = float(self.txt_peso.text())
        altura = float(self.txt_altura.text())
        cadena = "Tu ICM es de:"+" "+str(peso/(altura*altura))
        self.txt_resultado.setText(cadena)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
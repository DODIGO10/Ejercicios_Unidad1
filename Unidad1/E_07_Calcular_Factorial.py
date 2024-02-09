import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_07_Calcular_Factorial.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcularfactorial)

    # Área de los Slots
    def calcularfactorial(self):
        numero = int(self.txt_numero.text())
        factorial = self.factorial(numero)
        cadena = "El factorial de "+ str(numero)+" es:" + str(factorial)

        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


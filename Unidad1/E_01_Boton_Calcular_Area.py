import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_01_Boton_Calcular_Area.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_area.clicked.connect(self.area)
        self.txt_resultado.setEnabled(False)

    # Área de los Slots
    def area(self):
        base = float(self.txt_base.text())
        altura = float(self.txt_altura.text())
        cadena = "La area es de:"+" "+str(base*altura)

        self.txt_resultado.setText(cadena)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
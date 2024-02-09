import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_06_Promedio_Calificaciones.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Area de los signals
        self.buttonCalc.clicked.connect(self.promedio)
        self.resultado.setEnabled(False)

    def promedio(self):
        promedio = (float(self.calif1.text()) + float(self.calif2.text()) + float(self.calif3.text()) + float(self.calif4.text()) + float(self.calif5.text()))/5
        calculo = "El promedio de tu calificacion es "+str(promedio)
        self.resultado.setText(calculo)
        self.calif1.clear()
        self.calif2.clear()
        self.calif3.clear()
        self.calif4.clear()
        self.calif5.clear()

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec_())

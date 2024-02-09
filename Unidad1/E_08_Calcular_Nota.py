import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E_08_Calcular_Nota.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular_nota)

    # Área de los Slots
    def calcular_nota(self):#se supone que el usuario no pondra un numero menor que 0 o mayor que 10
        calificacion = int(self.txt_nota.text())

        if calificacion == 10:
            nota = "A"
        elif calificacion == 9:
            nota = "B"
        elif calificacion == 8:
            nota = "C"
        elif calificacion == 7:
            nota = "D"
        elif calificacion == 6:
            nota = "E"
        else:
            nota = "F"

        cadena ="La nota del alumno es: "+ nota
        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


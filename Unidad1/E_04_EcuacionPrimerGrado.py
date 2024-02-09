import math
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QFont
qtCreatorFile = "E_04_EcuacionPrimerGrado.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_resuelto.clicked.connect(self.ecuacion)

    # Área de los Slots

    def ecuacion(self):
        a = int(self.txt_a.text())
        b = int(self.txt_b.text())
        n = int(self.txt_n.text())
        x = symbols('x')

        r = sympy.solve(sympy.Eq(a * x + b,n),x)

        msj = QtWidgets.QMessageBox()
        msj.setStyleSheet(
            "background-color: rgb(13, 72, 127);"
            "color: #333333;"
        )

        font = QFont("Arial", 12)
        msj.setFont(font)
        msj.setText(str(r))
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


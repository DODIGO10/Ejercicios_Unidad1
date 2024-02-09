import math
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QFont

qtCreatorFile = "E_03_Distancia2puntos.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_distancia.clicked.connect(self.distance)

    # Área de los Slots

    def distance(self):
        ax = int(self.txt_Ax.text())
        ay = int(self.txt_Ay.text())
        bx = int(self.txt_Bx.text())
        by = int(self.txt_By.text())
        dist = math.sqrt((bx - ax)**2 + (by - ay)**2)

        cadena = "La distancia entre punto A y punto B es : " + str(dist)

        msj = QtWidgets.QMessageBox()
        msj.setStyleSheet(
            "background-color: rgb(188, 224, 255);"  
            "color: #333333;"
        )

        font = QFont("Arial", 12)
        msj.setFont(font)
        msj.setText(cadena)
        msj.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6 import uic

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Login.ui', self)
        self.setWindowTitle('UniSkema')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
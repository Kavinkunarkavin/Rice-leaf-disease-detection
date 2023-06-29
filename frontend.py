import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Image Viewer'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 400
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 300, 300)
        self.button = QPushButton('Select Image', self)
        self.button.setGeometry(150, 360, 100, 30)
        self.button.clicked.connect(self.showFileDialog)
        self.setStyleSheet('''
            QWidget {
                background-color: #F6F6F6;
            }
            QLabel {
                background-color: #FFFFFF;
                border: 2px solid #CCCCCC;
                border-radius: 10px;
                padding: 5px;
            }
            QPushButton {
                background-color: #3B5998;
                border: 2px solid #2D4373;
                border-radius: 5px;
                color: #FFFFFF;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #4C70BA;
            }
        ''')
        self.show()

    def showFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Images (*.png *.xpm *.jpg *.bmp *.gif)", options=options)
        if fileName:
            # Load the image file and display it in the label
            pixmap = QPixmap(fileName)
            self.label.setPixmap(pixmap.scaled(self.label.size(), aspectRatioMode = Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
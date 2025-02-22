import sys 
from PyQt6.QtWidgets import QApplication, QWidget


# this is a simple window in PyQt6 <3
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ma premiere fenetre ^///^ ")
        self.resize(400, 300)


app = QApplication(sys.argv) 
window = MainWindow()
window.show()
sys.exit(app.exec())


# but how to insert a bouton ? 
# it simple my little heart <3

from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout

class Mainwindow2(QWidget):
        def __init__(self): 
            super().__init__()
            self.setWindowTitle("my hot little bouton")

            self.label = QLabel("clicks with your hot mouse...")
            self.button = QPushButton("yes !! push me my love !!!")
            self.button.clicked.connect(self.update_label)

            layout = QVBoxLayout()
            layout.addWidget(self.label)
            layout.addWidget(self.button)

            self.setLayout(layout)
        def update_label(self):
            self.label.setText("you can do more")

#Now how to use Layout to organize the widget in my window ?


#Layout Vertical (QVBoxLayout)
layout = QVBoxLayout()
layout.addWidget(widget1)
layout.addWidget(widget2)
self.setLayout(layout)

#Layout Horizontal (QHBoxLayout)
layout = QHBoxLayout()
layout.addWidget(widget1)
layout.addWidget(widget2)
self.setLayout(layout)

#Gestion of Signal and Slot
layout = QGridLayout()
layout.addWidget(widget1, 0, 0)
layout.addWidget(widget2, 0, 1)
layout.addWidget(widget3, 1, 0, 1, 2) # Étendu sur 2 colonnes
self.setLayout(layout)

# finaly create your Menu window !!!!!!!

from PyQt6.QtWidgets import QMainWindow, QMenuBar, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu window !!")
        
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Fichier")
        exit_action = QAction("Quitter", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
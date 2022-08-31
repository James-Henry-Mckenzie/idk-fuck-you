from dataclasses import dataclass
#from multiprocessing.sharedctypes import Value
from PySide6.QtWidgets import *
import os


# ----- GUI ----- #

# Set app and main window
app = QApplication()
main_window = QMainWindow()
main_window.setWindowTitle("Shop")

# Set main widget and layout
main_widget = QWidget()
main_window.setCentralWidget(main_widget)
main_window.resize(440, 280)
vbox = QVBoxLayout()
main_widget.setLayout(vbox)

text = QTextEdit()
button = QPushButton("Sumbit")
vbox.addWidget(text)
vbox.addWidget(button)


def clicked():
    t = text.toPlainText()
    print(t)

    
    test.show()




button.clicked.connect(clicked)

test = QWidget()
layout = QVBoxLayout()
test.label = QLabel("Another Window")
layout.addWidget(test.label)
test.setLayout(layout)


main_window.setStyleSheet("border: 1px solid black")
main_window.show()
app.exec()

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

def say_hello():
    print("Hello from PyQt!")

app = QApplication([])
window = QWidget()
window.setWindowTitle("PyQt Example")

layout = QVBoxLayout()

button = QPushButton('Say Hello')
button.clicked.connect(say_hello)
layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec_()

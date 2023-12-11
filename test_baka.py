from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app=QApplication([])
win=QWidget()

win.resize(500,500)
win.setWindowTitle("Міша купить мені пиво")

Title=QLabel('мяв мяв мяв гав гав гав')

Line_h=QHBoxLayout()
Line_h.addWidget(Title)

win.setLayout(Line_h)

win.show()
app.exec_()


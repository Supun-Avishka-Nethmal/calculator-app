import sys
from PySide6.QtWidgets import QApplication
from calculator import Cal

app=QApplication(sys.argv)

window=Cal()
window.show()

app.exec()
from PyQt5 import QtWidgets, uic
import sys
from basic import Ui_Form

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog() ### create new dialog
ui = Ui_Form() ### create a new instance of your gui
ui.setupUi(Dialog) ### apply the gui to the created dialog
Dialog.show()
sys.exit(app.exec_())



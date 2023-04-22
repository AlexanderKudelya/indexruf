from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QRadioButton,QGroupBox,QPushButton,QLabel,QListWidget,QLineEdit
from second_win import *
from instr import *
                        
class FinalWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
 
    def initUI(self):
        self.work_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)      
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)          
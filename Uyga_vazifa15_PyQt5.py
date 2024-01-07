from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class V_box(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        # self.setFixedSize(90, 40)

class Calculator(QWidget):  
    def __init__(self) -> None:
        super().__init__()
        self.v_box = QVBoxLayout()
        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()

        self.line = QLineEdit(self)
        self.line.setAlignment(Qt.AlignRight)
        # self.line.move(10, 10)

        self.setWindowTitle("Calculator")       
        self.setFixedSize(400, 200)
        
        self.button1 = V_box("1")
        self.button2 = V_box("2")
        self.button3 = V_box("3")
        self.button4 = V_box("/")
        self.button5 = V_box('4')
        self.button6 = V_box('5')
        self.button7 = V_box('6')
        self.button8 = V_box('*')
        self.button9 = V_box('7')
        self.button10 = V_box('8')
        self.button11 = V_box('9')
        self.button12 = V_box('-')
        self.button13 = V_box('0')
        self.button14 = V_box('=')
        self.button15 = V_box('+')

        self.h_box1.addWidget(self.button1)
        self.h_box1.addWidget(self.button2)
        self.h_box1.addWidget(self.button3)
        self.h_box1.addWidget(self.button4)

        self.h_box2.addWidget(self.button5)
        self.h_box2.addWidget(self.button6)
        self.h_box2.addWidget(self.button7)
        self.h_box2.addWidget(self.button8)

        self.h_box3.addWidget(self.button9)
        self.h_box3.addWidget(self.button10)
        self.h_box3.addWidget(self.button11)
        self.h_box3.addWidget(self.button12)

        self.h_box4.addWidget(self.button13)
        self.h_box4.addWidget(self.button14)
        self.h_box4.addWidget(self.button15)

        self.v_box.addWidget(self.line)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)

        self.setLayout(self.v_box)
        
        self.button1.clicked.connect(self.press)
        
    def press(self):
        self.line.setText(str(V_box))               

app = QApplication([])
Calc = Calculator()
Calc.show()
app.exec_()
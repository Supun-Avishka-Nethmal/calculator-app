from PySide6.QtWidgets import QWidget, QPushButton
from ui_calculator import Ui_Calculator

class Cal(QWidget,Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Calculator")
        self.setGeometry(350,110,300,450)
        self.setMaximumHeight(650)
        self.setMaximumWidth(400)
        self.setMinimumHeight(650)
        self.setMinimumWidth(400)
        


        self.btn_0.clicked.connect(self.on_button_click)
        self.btn_1.clicked.connect(self.on_button_click)
        self.btn_2.clicked.connect(self.on_button_click)
        self.btn_3.clicked.connect(self.on_button_click)
        self.btn_4.clicked.connect(self.on_button_click)
        self.btn_5.clicked.connect(self.on_button_click)
        self.btn_6.clicked.connect(self.on_button_click)
        self.btn_7.clicked.connect(self.on_button_click)
        self.btn_8.clicked.connect(self.on_button_click)
        self.btn_9.clicked.connect(self.on_button_click)
        self.btn_mul.clicked.connect(self.on_button_click)
        self.btn_min.clicked.connect(self.on_button_click)
        self.btn_plus.clicked.connect(self.on_button_click)
        self.btn_div.clicked.connect(self.on_button_click)
        self.btn_equals.clicked.connect(self.on_button_click)
        self.btn_dot.clicked.connect(self.on_button_click)
        self.btn_c.clicked.connect(self.on_button_click)






    def on_button_click(self):
        button=self.sender()
        current_text=self.main_label.text()

        if current_text=="0":
            current_text=""
        if button.text()=="=":
            try :
                result=str(eval(current_text))
                self.main_label.setText(result)
                self.main_label2.setText(current_text+button.text())

            except ZeroDivisionError:
                self.main_label.setText("Error : Divition By Zero")

            except Exception as e:
                self.main_label.setText("Error : Invalid Expression")    

        else:
            self.main_label.setText(current_text+button.text())    
            self.main_label2.setText(current_text+button.text())   

        if button.text()=="C":
            self.main_label.setText("0")
            self.main_label2.setText("")
        
        
          



    


import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import QSize

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.final_nums = []
        self.setMaximumSize(QSize(100,100))

        self.show()

    def num_press(self,num):
        self.temp_nums.append(num)
        temp_string = ''.join(self.temp_nums)
        if self.final_nums:
            self.result_field.setText(''.join(self.final_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def func_press(self,op):
        temp_string = ''.join(self.temp_nums)
        self.final_nums.append(temp_string)
        self.final_nums.append(op)
        self.temp_nums = []
        self.result_field.setText(''.join(self.final_nums))

    def func_result(self,func):
        fin_string = ''.join(self.final_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.result_field .setText(fin_string)

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.final_nums = []

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        self.result_field = qtw.QLineEdit()
        btn_result = qtw.QPushButton('Enter',clicked = self.func_result)
        btn_clear = qtw.QPushButton('Clear', clicked = self.clear_calc)
        buttons = []
        for i in range(10):
            buttons.append(qtw.QPushButton(str(i),clicked = lambda checked,num = i:self.num_press(str(num))))
        btn_plus = qtw.QPushButton('+',clicked = lambda:self.func_press('+'))
        btn_mins = qtw.QPushButton('-',clicked = lambda:self.func_press('-'))
        btn_mult = qtw.QPushButton('*',clicked = lambda:self.func_press('*'))
        btn_divd = qtw.QPushButton('÷',clicked = lambda:self.func_press('/'))

        # Adding the buttons to the layout
        container.layout().addWidget(self.result_field,0,0,1,4)
        container.layout().addWidget(btn_result,1,0,1,2)
        container.layout().addWidget(btn_clear,1,2,1,2)

        container.layout().addWidget(buttons[0],5,0)
        container.layout().addWidget(buttons[1],2,0)
        container.layout().addWidget(buttons[2],2,1)
        container.layout().addWidget(buttons[3],2,2)
        container.layout().addWidget(btn_plus,2,3)
        container.layout().addWidget(buttons[4],3,0)
        container.layout().addWidget(buttons[5],3,1)
        container.layout().addWidget(buttons[6],3,2)
        container.layout().addWidget(btn_mins,3,3)
    
        container.layout().addWidget(buttons[7],4,0)
        container.layout().addWidget(buttons[8],4,1)
        container.layout().addWidget(buttons[9],4,2)
        container.layout().addWidget(btn_mult,4,3)
        container.layout().addWidget(btn_divd,5,3)

        self.layout().addWidget(container)

if __name__ == "__main__":
    app =qtw.QApplication([])
    mw = MainWindow()
    app.setStyle(qtw.QStyleFactory.create('Fusion'))
    app.exec_()

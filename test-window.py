from PyQt5.QtWidgets import(
    QApplication,QWidget,
    QLabel,QGridLayout,
    QPushButton,QLineEdit,
    QVBoxLayout, QHBoxLayout,
    QMessageBox,QAction
)
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtGui import QIcon
from past import PastMatchup
from Results import Results

class GridWindow(QWidget):
    labels = []
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.interfejs()

    def interfejs(self):
        self.resize(500,200)
        self.setWindowTitle('text')


        self.textbox = QLineEdit(self)
        self.textbox.move(120,0)
        
        self.searchButton = QPushButton('search',self)
        self.searchButton.move(80,1)
        self.searchButton.clicked.connect(self.on_click)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.textbox)
        vbox1.addWidget(self.searchButton)
        
        vbox2 = QVBoxLayout()
        
        grid = QGridLayout()
        
        labels = []

        for x in range(0,10):
            labels.append(QLabel("{x}".format(x=x),self))

        x = 0
        
        for label1 in range(0,len(labels)):
            grid.addWidget(labels[label1],x,0)
            if label1 %2==0:
                grid.addWidget(QPushButton('details'.format(x=x),self),x,1)
                    
            x+=1

        vbox2.addItem(grid)    
        main_vbox = QVBoxLayout()
        main_vbox.addSpacing(1)
        main_vbox.addLayout(vbox1)
        main_vbox.addLayout(vbox2)
        self.setLayout(main_vbox)   
        

        self.show()

    @pyqtSlot()  
    def on_click(self):
        textValue = self.textbox.text()
        msg = QMessageBox()
        msg.setText(textValue)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    qw = GridWindow()
    sys.exit(app.exec_())
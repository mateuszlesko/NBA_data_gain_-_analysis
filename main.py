import sys

from PyQt5.QtWidgets import (
QApplication,QWidget,QMainWindow,QTableWidget,
QTableWidgetItem,QVBoxLayout,QPushButton,
QMessageBox,QAction, QLineEdit)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon

from bs4 import BeautifulSoup as bs

from past import PastMatchup
from live import LiveMatchup
from future import UpcomingSchedule
from conditions import Condition
from Results import Results


class App(QWidget):
    
    dataEnded = []
    
    def __init__(self):
        super().__init__()
        self.title='NBA scoreboard'
        self.left=40
        self.top=60
        self.width = 640
        self.height = 480
        self.initUI()
    

    def initUI(self) :
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)  
       
        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        
        
        self.textbox = QLineEdit(self) 
        self.textbox.move(120,0)
        self.textbox.resize(120,40)


        button1 = QPushButton('info',self)
        button1.setToolTip('see results')
        button1.clicked.connect(self.on_click2)
        button1.move(250,0)

        button2 = QPushButton('save',self)
        button2.setToolTip('save results')
        button2.clicked.connect(self.on_click3)
        button2.move(350,0)
        self.show()
    
    def createTable(self):
        self.tableWidget = QTableWidget()
    
    @pyqtSlot()
    
    def on_click2(self):
        
        textValue = self.textbox.text()
        msg = QMessageBox()
        msg.setText(textValue)
        msg.setStandardButtons(QMessageBox.Ok)
       
        url = 'https://sports.yahoo.com/nba/scoreboard/?confId=&schedState=2&dateRange='
        url2=url+textValue
        
        condition = Condition()
        if condition.internet_on(url2)==True:
            
            page = condition.requestPage(url2)
            page = condition.requestPage(url2)
            soup = bs(page.content,'html.parser')
            
            ##scraping live matchups
            sources = [item for item in soup.find_all('a',{"class":'gamecard-in_progress'})]
            if len(sources)>0:
                live = LiveMatchup()
                dataFromLive = live.ScrapeLive(soup)
                result = Results()
                result.viewData(dataFromLive,self.tableWidget)
            
            ##scraping future matchups
            sources = [item for item in soup.find_all('a',{'class':'gamecard-pregame'})]
            if len(sources)>0:
                upcoming = UpcomingSchedule()
                dataFromFuture = upcoming.scrapeFuture(soup)
                result = Results()
                result.viewData(dataFromFuture,self.tableWidget)
            
            ## scraping ended matchups
            sources = [item for item in soup.find_all('a',{'class':'gamecard-final'})]
            if len(sources)>0:
                past = PastMatchup()
                dataFromPast = past.ScrapePast(soup)
                self.dataEnded = list(dataFromPast)
                result = Results()
                result.viewData(dataFromPast,self.tableWidget)
                
            
            self.tableWidget.move(50,0)
        else:
            msg = QMessageBox()
            msg.setText('No network access')
            msg.setStandardButtons(QMessageBox.Ok)
        
        msg.exec_()
    def on_click3(self):
        

        result = Results()
        data = result.seperateData(self.dataEnded)
        result.saveData(data,self.textbox.text())
        
        
       
if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = App()
sys.exit(app.exec_()) 
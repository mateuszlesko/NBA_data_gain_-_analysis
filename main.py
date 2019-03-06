import sys
import requests
from PyQt5.QtWidgets import (
QApplication,QWidget,QMainWindow,QTableWidget,
QTableWidgetItem,QVBoxLayout,QPushButton,
QMessageBox,QAction, QLineEdit)

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from past import PastMatchup
from bs4 import BeautifulSoup as bs

#from main import ScheduleNBA
from past import PastMatchup
from live import LiveMatchup
from future import UpcomingSchedule
from conditions import Condition


class App(QWidget):

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
                dataFromLive = live.ScrapeLive(soup,sources)
                self.tableWidget.setRowCount(len(dataFromLive)/2)
                self.tableWidget.setColumnCount(2)
                
                for x in range(0,len(dataFromLive)):
                    for y in range(0,1):
                        self.tableWidget.setItem(y,x,QTableWidgetItem(dataFromLive[x]))
            
            ##scraping future matchups
            sources = [item for item in soup.find_all('a',{'class':'gamecard-pregame'})]
            if len(sources)>0:
                upcoming = UpcomingSchedule()
                dataFromFuture = upcoming.scrapeFuture(soup,sources)
                self.tableWidget.setRowCount(len(dataFromFuture)/2)
                self.tableWidget.setColumnCount(2)
                
                for x in range(0,len(dataFromFuture)):
                    for y in range(0,1):
                        self.tableWidget.setItem(y,x,QTableWidgetItem(dataFromFuture[x]))
            
            ## scraping ended matchups
            sources = [item for item in soup.find_all('a',{'class':'gamecard-final'})]
            if len(sources)>0:
                past = PastMatchup()
                data = past.ScrapePast(soup,sources)
                print(len(data))
                self.tableWidget.setRowCount(len(data)/2)
                self.tableWidget.setColumnCount(2)
                
                for x in range(0,len(data)):
                    for y in range(0,1):
                        self.tableWidget.setItem(y,x,QTableWidgetItem(data[x]))
            
            

            self.tableWidget.move(50,0)
        else:
            msg = QMessageBox()
            msg.setText('No network access')
            msg.setStandardButtons(QMessageBox.Ok)
        
        msg.exec_()
        
        
        
       
if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())    
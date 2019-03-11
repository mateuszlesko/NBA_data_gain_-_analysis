import json
from PyQt5.QtWidgets import (
QApplication,QWidget,QMainWindow,QTableWidget,
QTableWidgetItem,QVBoxLayout,QPushButton,
QMessageBox,QAction, QLineEdit)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon


class Results():
    def wantSave(self,x):
        save = False
        if x=='Y' or x=='y':
            save = True
        return save

    def viewData(self,arr,tableWidget):
        tableWidget.setRowCount(len(arr)/2)
        tableWidget.setColumnCount(2)
                
        for x in range(0,len(arr)):
            for y in range(0,1):
                tableWidget.setItem(y,x,QTableWidgetItem(arr[x]))

    def seperateData(self,arr):
        teams = []
        scores =[]
        for y in arr:
            separator_index = y.index(':')
            data = y
            teams.append(data[0:separator_index])
            scores.append(data[separator_index:])
        return teams,scores        
          
    def saveData(self, arr,d):
        teams = []
        scores =[]
        for y in arr[0]:
            teams.append(y)    
        for x in arr[1]:
            scores.append(x)
        
        matchups={}
        matchups['matchup']=[]
        for x in range(0,len(teams),1):
            matchups['matchup'].append({
                'name':teams[x],
                'score':scores[x]
            })
        with open('{date}.json'.format(date=d),'w+') as f:
            json.dump(matchups,f)  
        return 'file was created'  

   
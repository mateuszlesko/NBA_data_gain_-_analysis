# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 21:13:53 2019

@author: 4ever
"""

from bs4 import  BeautifulSoup as bs
class UpcomingSchedule():
    
   
    def prognose(self,record1,record2,name1,name2):
        
          seperator_index = record1.index('-')
          #print(seperator_index)
          
          wins1 = int(record1[0:seperator_index])
          loses1 = int(record1[seperator_index+1::])
          count_of_matches1 = wins1+loses1

          winratio1= wins1/count_of_matches1

          wins2 = int(record2[0:seperator_index])
          loses2 = int(record2[seperator_index+1::])
          count_of_matches2 = wins1+loses2

          winratio2= wins2/count_of_matches2

          if(winratio1>winratio2):
              return name1+' would win'
          else:
              return name2+' would win'

    def scrapeFuture(self,soup):

        teams = []
        records = []
        schedule = []
        
        

        last_names = soup.find_all('span',{'data-tst':'last-name'})
        for last in last_names:
            teams.append(last.getText())
        team_record = soup.find_all('div',{'class':'Whs(nw) D(tbc) Va(m) Fw(b) Fz(14px)'})    
        for record in team_record:
            records.append(record.getText())
             
        if(len(teams)>len(records)):
            del teams[len(records):len(teams)]


        x=0
        for team in teams:
            schedule.append(team+":"+records[x]+'\n')
            x=x+1
         
      
        return schedule 
   

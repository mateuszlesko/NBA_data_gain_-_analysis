# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 21:13:53 2019

@author: 4ever
"""

from bs4 import  BeautifulSoup as bs
class UpcomingSchedule():
    def scrapeFuture(self,soup,source):
    #date = input('format(yyyy-mm-dd): ')
    #page = requests.get('https://sports.yahoo.com/nba/scoreboard/?confId=&schedState=2&dateRange='+date)
    #soup = bs(page.content,'html.parser')
    #soup.prettify()
        teams = []
        records = []
        schedule = []
        
        #sources = [type(item) for item in soup.find_all('a',{'class':'gamecard-pregame'})]
        
        
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
            schedule.append(team+":"+records[x])
            x=x+1
                
        return schedule    
       
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:47:16 2019

@author: 4ever
"""

#https://sports.yahoo.com/nba/scoreboard/

from bs4 import  BeautifulSoup as bs



class PastMatchup:

    def ScrapePast(self,soup):
    
        teams = []
        scores = []
        schedule = []
        
       
        last_names = soup.find_all('span',{'data-tst':'last-name'})
        for last in last_names:
                  teams.append(last.getText())
        team_score = soup.find_all('div',{'class':'Whs(nw) D(tbc) Va(m) Fw(b) Fz(27px)'})    
        for score in team_score:
                  scores.append(score.getText())
               
        if(len(teams)>len(scores)):
           difference=len(teams)-len(scores)
           
           del teams[0:difference]
           
        x=0
        for team in teams:
            schedule.append(team+":"+ scores[x])
            x=x+1
              
        return schedule
         

           
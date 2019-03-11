# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 19:30:48 2019

@author: 4ever
"""

from bs4 import  BeautifulSoup as bs



class LiveMatchup:

    def ScrapeLive(self,soup):
    
        teams = []
        scores = []
        schedule = []
        
        sources = [type(item) for item in soup.find_all('a',{'class':'gamecard-in_progress'})]
        count_live = len(sources)+1
        last_names = soup.find_all('span',{'data-tst':'last-name'})
        for last in last_names:
             teams.append(last.getText())
        team_score = soup.find_all('div',{'class':'Whs(nw) D(tbc) Va(m) Fw(b) Fz(27px)'})    
        for score in team_score:
              scores.append(score.getText())
               
        
        del teams[count_live::]
        del scores[count_live::]
            
        
        for x in range(0,count_live):
            schedule.append(teams[x]+":"+ scores[x])
          
               
        return schedule
       
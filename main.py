# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 20:24:02 2019

@author: 4ever
"""
from bs4 import BeautifulSoup as bs
from conditions import Condition
from future import UpcomingSchedule
from past import PastMatchup
from live import LiveMatchup
from Results import Results

class ScheduleNBA():

    def main(self):

        condition = Condition()
        url = "https://sports.yahoo.com/nba/scoreboard/"
        global date

        if condition.internet_on(url)==True:
            url = 'https://sports.yahoo.com/nba/scoreboard/?confId=&schedState=2&dateRange='
            date = input('format(yyyy.mm.dd): ')
            date = date.replace('.','-')
            url2=url+date

            page = condition.requestPage(url2)
           # soup = bs(page.content,'html.parser')
            if page !=0:
                soup = bs(page.content,'html.parser')
                
                sources = [item for item in soup.find_all('a',{'class':'gamecard-in_progress'})]
                
                if len(sources)>0:
                    
                    print('\n')
                    print('Live results of matches')
                    live = LiveMatchup()
                    dataFromLive = live.ScrapeLive(soup,sources)
                    result = Results()
                    #print(dataFromLive)
                    print(result.viewData(dataFromLive))

                
                sources = [item for item in soup.find_all('a',{'class':'gamecard-pregame'})]

                if len(sources)>0:

                    upcoming = UpcomingSchedule()
                    
                    print('Upcoming matches: ',len(sources))
                    dataFromFuture = upcoming.scrapeFuture(soup,sources)

                    

                    result = Results()
                    print(result.viewData(dataFromFuture))

                    

                sources = [item for item in soup.find_all('a',{'class':'gamecard-final'})]

                if len(sources)>0:
                    
                    final = PastMatchup()
                    print('\n')
                    print('Final results of matches')
                    
                    dataFromPast = final.ScrapePast(soup,sources)
                    
                    result = Results()
                    print(result.viewData(dataFromPast))
                    

                    save=input("Do you want to save data? (Y or y)")
                    if result.wantSave(save)==True:
                        
                        dataFromPast =  result.seperateData(dataFromPast)
                        result.saveData(dataFromPast,date)
                    

                
        else:
            return "No connection to net"
        return 0
if __name__ == '__main__':
    sn = ScheduleNBA()
    sn.main()

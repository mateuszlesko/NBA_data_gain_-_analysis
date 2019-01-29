# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 22:47:16 2019

@author: 4ever

metoda na upcoming jesli w live nie ma puktow dla druzyny oznacza, ze mecz dopiero
odbedzie sie
jesli druzyna ma zamiast rekordu pkty mecz odbedzie sie dopiero
"""
import datetime
import requests
from bs4 import BeautifulSoup as bs


class FinishedScoreboard(object):
    def __init__(self,first_name,last_name,score):
        
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        
        #self.win = win
        #self.lose = lose
        
        
class UpcomingSchedule(object):
    def __init__(self,first_name,last_name,record):
        self.first_name = first_name
        self.last_name = last_name
        self.record = record
        


def ScrapeWebsiteWhenFinished(page):
    
    soup = bs(page.content,'html.parser')
    
    list(soup.children)
    
    [type(item) for item in list(soup.children)]
    
    first_names = []
    last_names =  []
    score = []
    links = []
    
    scoreboard = []
   
    
    string = soup.find_all('span',{'data-tst':'first-name'})
    
    for s in string:
        
        val = s.get_text()
        first_names.append(val)
    
    string = soup.find_all('span',{'data-tst':'last-name'})
    
    for s in string:
        val = s.get_text()
        last_names.append(val)
    
    string= soup.find_all('div',{'class':'Whs(nw) D(tbc) Va(m) Fw(b) Fz(27px)'})
    for s in string:
        val = s.get_text()
        score.append(val)

    string = soup.find_all('a',{'C(primary-text) C(primary-text):link C(primary-text):visited Td(n) gamecard-final'})

    for s in string:
        link = 'https://sports.yahoo.com'
        links.append(link+str(s.get('href')))

    
    
    
    index1 = 0
    index2 = 1
    for team1,team2 in zip(first_names[0::2],first_names[1::2]):
        scoreboard.append(FinishedScoreboard(team1,last_names[index1],score[index1]))
        scoreboard.append(FinishedScoreboard(team1,last_names[index2],score[index2]))
        
        print(team1,last_names[index1],score[index1],sep=' ')
        print(team2,last_names[index2],score[index2],sep=' ')
        print("###############################")
        index1 += 2
        index2 += 2
   
    
        
   
    
def ScrapeWebsiteWhenUpcoming(page):
    first_names = []
    last_names =  []
    records = []
  
    
    soup = bs(page.content,'html.parser')
    
    divs = soup.findAll('span',{'data-tst':'last-name'})
    for div in divs:
        last_names.append(div.text)
    
    divs = soup.findAll('span',{'data-tst':'first-name'})
    for div in divs:
        first_names.append(div.text)
    #print(dates)
    
    divs = soup.findAll('div',{'class':'Whs(nw) D(tbc) Va(m) Fw(b) Fz(14px)'})
    for div in divs:
        records.append(div.text)
    
   
     
    index1 = 0
    index2 = 1
    
    for team1,team2 in zip(first_names[0::2],first_names[1::2]):
        
        print(team1,last_names[index1],records[index1],sep=' ')
        print(team2,last_names[index2],records[index2],sep=' ')
        print("###############################")
        index1 += 2
        index2 += 2
     
    print('fn',len(first_names),'ln',len(last_names),'rec',len(records),sep=':')
    return(first_names,last_names,records)
    
def ScrapeWebsiteWhenLive(page):
    score = []
    first_names = []
    last_names =  []
    dates = []
    
    soup = bs(page.content,'html.parser')
    
    info = soup.find_all('div',{'class':'Whs(nw) D(tbc) Va(m) Fw(b) Fz(27px)'})
    for inf in info:
        #print(inf.text)
        score.append(inf.text)
        
    first_n = soup.find_all('span',{'data-tst':'first-name'})
    for fn in first_n:
        first_names.append(fn.text)
    
    last_n = soup.find_all('span',{'data-tst':'last-name'})
    for fn in last_n:
        last_names.append(fn.text)
    
    divs = soup.findAll('div',{'class':'Ta(end) Cl(b) Fw(b) '})
    for div in divs:
        dates.append(div.text)
    
    x1=0
    x2=1
    
    for ln1,ln2 in zip(last_names[0:2],last_names[1:2]):
        print(dates[x1])
        print(ln1,score[x1],sep=':')
        print(ln2,score[x2],sep=':')
        print('###########')
        x1+=1
        x2+=1
        
      
   
    
    
def main():
    # my code here
    d = input("Date format (yyyy-mm-dd): ")
    page = requests.get('https://sports.yahoo.com/nba/scoreboard/?confId=&schedState=2&dateRange='+d)
    soup = bs(page.content,'html.parser')

    list(soup.children)
        
    
    [type(item) for item in list(soup.children)]
    
    #print(soup.title.string)
    #div = soup.body.div.div
    
    #print(div.contents[0])
    
    divs = soup.body.div.div
    
    #print(divs.findAll('h3'))
    h3s = divs.findAll('h3')
    for h3 in h3s:
        if h3.text=='Live':
            print('live')
            ScrapeWebsiteWhenLive(page)
        if h3.text == 'Upcoming':
            print('Upcoming')
            ScrapeWebsiteWhenUpcoming(page)
        if h3.text == 'Finished':
            print('Finished')
            ScrapeWebsiteWhenFinished(page)
        
if __name__ == "__main__":
   main()
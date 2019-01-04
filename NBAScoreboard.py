from bs4 import BeautifulSoup
import requests

class Scoreboard(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    
        

d = input('date format (yyyy-mm-dd): ')

page = requests.get('https://sports.yahoo.com/nba/scoreboard/?confId=&schedState=2&dateRange='+d)
soup = BeautifulSoup(page.content,'html.parser')

list(soup.children)

[type(item) for item in list(soup.children)]

teams = []
score = []
scoreboard = []


string = soup.find_all('span',{'data-tst':'first-name'})

for s in string:
    
 val = s.get_text()
 teams.append(val)

string= soup.find_all('div',{'class':'Whs(nw) D(tbc) Va(m) Fw(b) Fz(27px)'})
#print(string[2])
for s in string:
    val = s.get_text()
    score.append(val)

    
print(len(teams),len(score),sep=',')
for x in range (0,len(teams),1):
  
  scoreboard.append(Scoreboard(teams[x],int(score[x])))

for s1,s2 in zip(scoreboard[0::2],scoreboard[1::2]):
    
      
    print('Away',s1.name,s1.score,sep=':') 
    print('Home',s2.name,s2.score,sep=':') 
    print('Team at Home won: ',s2.score > s1.score)
    print('######################')
    #print(sc.score>scr.score)
    
    
        
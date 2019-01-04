from bs4 import BeautifulSoup
import requests

class Scoreboard(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def HomeWon(s1,s2):
        won = None
        
        if s1>s2:
            won = True
        else:
            won = False
        
        return won
        

d = input('date format (yyyy-mm-dd): ')

page = requests.get('https://sports.yahoo.com/nba/scoreboard/?confId=&schedState=2&dateRange='+d)
soup = BeautifulSoup(page.content,'html.parser')

list(soup.children)

[type(item) for item in list(soup.children)]

teams = []
score = []
scoreInt = [int(i) for i in score]
scoreboard = []


#print(soup.find_all('span',{'data-tst':'first-name'}))

string = soup.find_all('span',{'data-tst':'first-name'})

for s in string:
    
 val = s.get_text()
 teams.append(val)

string= soup.find_all('div',{'class':'Whs(nw) D(tbc) Va(m) Fw(b) Fz(27px)'})
#print(string[2])
for s in string:
    val = s.get_text()
    score.append(val)

#for x in range(0,2):
    #teams.pop(0)
    
print(len(teams),len(score),sep=',')
for x in range (0,len(teams),1):
  #print(teams[x],score[x],sep=':') 
  scoreboard.append(Scoreboard(teams[x],int(score[x])))

for x,y in zip(score[0::2],score[1::2]):
    x1 = int(x)
    y1=int(y)
    if x1>y1:
        print(int(x),'>',int(y))
    else:
        print(int(x),'<',int(y))

print(len(scoreboard))

for s1,s2 in zip(scoreboard[0::2],scoreboard[1::2]):
    
      
    print(s1.name,s1.score,sep=':') 
    print(s2.name,s2.score,sep=':') 
    print('Team at Home won: ',s2.score > s1.score)
    #print(sc.score>scr.score)
    
    
        
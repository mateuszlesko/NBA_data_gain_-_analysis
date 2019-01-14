from bs4 import BeautifulSoup
import datetime
import requests

class Scoreboard(object):
    def __init__(self,name,score,win,lose):
        self.name = name
        self.score = score
        self.win = win
        self.lose = lose
    
        

d = input('date format (yyyy-mm-dd): ')

def getTodaysDate(x):
    x = datetime.datetime.now()
    y = x.year
    m = x.month
    d = x.day
    
    if m <10:
        m = '0'+str(m)
    if d <10:
        d = '0'+str(d)
    string = str(y)+"-"+str(m)+"-"+str(d)
    return string


page = requests.get('https://sports.yahoo.com/nba/scoreboard/?confId=&schedState=2&dateRange='+d)
soup = BeautifulSoup(page.content,'html.parser')
    
list(soup.children)
    
[type(item) for item in list(soup.children)]
    
teams = []
score = []
scoreboard = []
links = []
    
    
string = soup.find_all('span',{'data-tst':'first-name'})
    
for s in string:
        
 val = s.get_text()
 teams.append(val)
    
string= soup.find_all('div',{'class':'Whs(nw) D(tbc) Va(m) Fw(b) Fz(27px)'})
for s in string:
   val = s.get_text()
   score.append(val)

string = soup.find_all('a',{'C(primary-text) C(primary-text):link C(primary-text):visited Td(n) gamecard-final'})

for s in string:
    link = 'https://sports.yahoo.com'
    links.append(link+str(s.get('href')))
        
print(len(teams),len(score),sep=',')


if d == getTodaysDate(datetime.datetime.now()):
    
    '''
    delete match which haven't got score, still to come
    '''
    print('sometimes result can be mixed, check if matches ended in recent day')
    
    #for x in range(0,2):
       # teams.pop(0)
       # score.pop(0)
        

for x in range (0,len(teams),1):
      
   scoreboard.append(Scoreboard(teams[x],int(score[x]),None,None))

index = 0     
for s1,s2 in zip(scoreboard[0::2],scoreboard[1::2]):
       
  if s1.score > s2.score:
     s1.win = True
     s1.lose = False
     s2.win = False
     s2.lose = True
  else:
     s1.win = False
     s1.lose = True
     s2.win = True
     s2.lose = False
            
  print('Away',s1.name,s1.score,sep=':') 
  print('Home',s2.name,s2.score,sep=':') 
  print('details:',links[index])
  if s1.win == True:
     print(s1.name,' won')
  else:
     print(s2.name,' won')
        #print('Team at Home won: ',s2.score > s1.score)
  print('######################')
  index+=1 

#date = str(datetime.datetime.now())
fname = '{date}.txt'.format(date=d)
f = open(fname,'w+')
string = ''
for s1,s2 in zip(scoreboard[0::2],scoreboard[1::2]):
   string ='{team} : {score} \n'.format(team=s1.name,score=s1.score)
   f.write(string)
   string ='{team} : {score} \n'.format(team=s2.name,score=s2.score)
   f.write(string)
   if(s1.score>s2.score):
       string="{team} won \n".format(team=s1.name)
   else:
       string="{team} won \n".format(team=s2.name)
    
   f.write(string)
   f.write("############################### \n")
   #f.wrire('%team : $s \n',s2.name,s2.score)
   #if(s1.score>s2.score):
    #  f.write('%s1 won',s1.name)
  # else:
    #  f.write('%s2 won',s2.name)
        
f.close()
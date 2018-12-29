from bs4 import BeautifulSoup
import requests

page = requests.get('https://sports.yahoo.com/nba/scoreboard/')
soup = BeautifulSoup(page.content,'html.parser')

list(soup.children)

[type(item) for item in list(soup.children)]

teams = []
score = []
scoreboard = {}

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
    

for x in range (0,len(teams),1):
  print(teams[x],score[x],sep=':') 
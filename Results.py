import json

class Results():
    def wantSave(self,x):
        save = False
        if x=='Y' or x=='y':
            save = True
        return save

    def getData(self,arr):
        teams = []
        scores =[]
        for y in arr:
            separator_index = y.index(':')
            data = y
            teams.append(data[0:separator_index])
            scores.append(data[separator_index:])
        return teams,scores        
          
    def saveData(self, arr,d):
        teams = []
        scores =[]
        for y in arr[0]:
            teams.append(y)    
        for x in arr[1]:
            scores.append(x)
        
        matchups={}
        matchups['matchup']=[]
        for x in range(0,len(teams),1):
            matchups['matchup'].append({
                'name':teams[x],
                'score':scores[x]
            })
        with open('{date}.json'.format(date=d),'w+') as f:
            json.dump(matchups,f)  
        return 'file was created'  

   
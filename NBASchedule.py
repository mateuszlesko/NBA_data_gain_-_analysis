# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 20:24:02 2019
@author: 4ever

Update on Sat May 14 13:56 2022
"""

"""
The NBA season calendar is loaded by an external API, that driver doesn't have access to. 
#SOLVE:
ID of the first game of 2021-22 season is : 0022100001
ID of the last game of 2021-22 season is: 0022101177
We can see that substring 002210 is in both IDs
"""
from scrapper.NBADetailsMatchScrapper import NBADetailsMatchScrapper
START_ID = 0
LAST_ID = 5
class NBASchedule():

    def main(self):
        matches_ids = []
        str_id = ""
        for x in range(START_ID+1,LAST_ID+1):
            if x < 10:
                str_id="002210000{}".format(x)
            elif x >= 10 and x < 100:
                str_id = "00221000{}".format(x)
            elif x >= 100 and x < 1000:
                str_id = "0022100{}".format(x)
            else:
                str_id="{}".format(x)
            matches_ids.append(str_id)

        for mi in matches_ids:
            print("https://www.nba.com/game/{}/box-score#box-score".format(mi))
            scrapper = NBADetailsMatchScrapper("https://www.nba.com/game/{}/box-score#box-score".format(mi)).getContentData().closeDriver().cleanData().saveDataToJSON()    
        pass

if __name__ == '__main__':
    sn = NBASchedule()
    sn.main()
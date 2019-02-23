# -*- coding: utf-8 -*-
"""

@author: 4ever
"""
import urllib.request
import requests
class Condition():
    
    def internet_on(self,url):
        try:
            wp = urllib.request.urlopen(url)
            pw = wp.read()
            return True
        except  urllib.error as err:
            return False
    
    def requestPage(self,url):
         page = requests.get(url)
         
         if page.status_code == 200:
         
             return page
         
         return 0
         
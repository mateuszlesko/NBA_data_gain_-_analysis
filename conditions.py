# -*- coding: utf-8 -*-
"""

@author: 4ever
"""
import urllib3
import requests
class Condition():

    def internet_on(self,url):
        try:
            http = urllib3.PoolManager()
            r = http.request('GET',url)
            if r.status == 200:
                return True
        except  urllib3.exceptions.HTTPError as err:
            return False

    def requestPage(self,url):
         page = requests.get(url)

         if page.status_code == 200:

             return page

         return 0

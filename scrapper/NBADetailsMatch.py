import json

from time import sleep
from selenium import webdriver

class NBADetailsMatch(object):
    def __init__(self, link):
        self.link = link
        self.data = ""
        self.driver = webdriver.Edge()

    def getContentData(self):
        self.driver.get(self.link)
        self.driver.find_element_by_css_selector("button#onetrust-reject-all-handler").click()
        sleep(1)
        self.driver.refresh()
        sleep(2)
        self.data = self.driver.find_element_by_css_selector("script#__NEXT_DATA__").get_attribute('innerHTML')
        return self
    
    def cleanData(self):
        clean_data = (json.loads(self.data)["props"]["pageProps"]["game"])
        del clean_data["broadcasters"]
        del clean_data["videoAvailableFlag"]
        del clean_data["ptAvailable"]
        del clean_data["ptXYZAvailable"]
        del clean_data["whStatus"]
        del clean_data["hustleStatus"]
        del clean_data["pbOdds"]
        del clean_data["gameRecap"]
        self.data = json.dumps(clean_data)
        return self
    def saveToJSON(self):
        with open("scrapper/data/{}.json".format(self.link.split("/")[4]),"a") as f:
            f.write(self.data)
        return self

    def closeDriver(self):
        self.driver.quit()
        return self

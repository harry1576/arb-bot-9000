import os
import time 

import selenium 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(35)


def print_dict(d):
  for k, v in d.items():
      print(k, v)


class TAB():

  def __init__(self):

    self.URL = "https://www.tab.co.nz"
    self.sport_ids = {'tennis' : 37, "football": 16}
    self.events = {}

  def setup(self, sport):

    number = self.sport_ids[sport]
    driver.get(f"{self.URL}/sport/{number}/{sport}/matches")
    time.sleep(10)

  
  def get_event_data(self):
    
    events_el = driver.find_elements("xpath", "//*[@class='event-list__item__event-market']")
    
    for event in events_el:
      split_txt = event.text.split("\n")
      if len(split_txt) != 4:
        continue

      home,home_odds,away,away_odds = split_txt
      self.events[f"{home} v {away}"] = (float(home_odds), float(away_odds))

    return self.events
    
  
class UNIBET():

  def __init__(self):

    self.URL = "https://www.unibet.com.au/"
    self.events = {}

  def setup(self, sport):

    driver.get(f"{self.URL}betting/sports/filter/{sport}/all/matches")
    time.sleep(10)

  def get_event_data(self):
    
    events_el = driver.find_elements("xpath", "//*[@class='f9aec _0c119 bd9c6']")
    
    for event in events_el:
      print(event.text.split("/n"))

    return None

    for event in events_el:
      split_txt = event.text.split("\n")
      if len(split_txt) != 4:
        continue

      home,home_odds,away,away_odds = split_txt
      self.events[f"{home} v {away}"] = (float(home_odds), float(away_odds))

    return self.events


def main():

  UNI_EX = UNIBET()
  UNI_EX.setup("football")
  uni_ev = UNI_EX.get_event_data()


  TAB_EX = TAB()
  TAB_EX.setup("football")
  tab_ev = TAB_EX.get_event_data()






  print_dict(tab_ev)


if __name__ == "__main__":
  main()
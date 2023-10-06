import src.types.weeklyOverview as WO

from bs4 import BeautifulSoup
import requests

URL = "https://www.pro-football-reference.com/"
r = requests.get(URL)
webpage = BeautifulSoup(r.content, "lxml")

WO.findWeeklyResults(webpage)




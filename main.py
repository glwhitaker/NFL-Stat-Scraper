from bs4 import BeautifulSoup
import requests

from src.weeklyOverview import findWeeklyResults

URL = "https://www.pro-football-reference.com/"
r = requests.get(URL)
webpage = BeautifulSoup(r.content, "lxml")

findWeeklyResults(webpage)




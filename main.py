import src.types.weeklyOverview as WO

from bs4 import BeautifulSoup
import requests

URL = "https://www.pro-football-reference.com/"
r = requests.get(URL)
webpage = BeautifulSoup(r.content, "lxml")

print("\nWelcome to NFL Scraper!\n")

print("Select an option:")
print("1. Weekly Overview")
print()

input = input("Enter option: ")

if input == "1":
    result = WO.findWeeklyResults(webpage)
    WO.writeOverview(result)
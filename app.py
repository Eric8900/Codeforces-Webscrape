import requests
import json
from bs4 import BeautifulSoup

links = []

def searchLink(url):
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        datatable = soup.find("div", class_="datatable")
        problems = datatable.find("table", class_="problems")
        tr = problems.find_all("tr")[1:]
        for t in tr:
            td = t.find("td")
            a = td.find("a")
            href = a.get("href")
            # print(href)
            links.append(href)

for i in range(1, 96):
    searchLink("https://codeforces.com/problemset/page/" + str(i))

data = json.dumps(links)

with open('links.json', 'w') as f:
    f.write(data)
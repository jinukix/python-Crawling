import csv
import requests
from bs4 import BeautifulSoup


def save_to_file(data):
    file = open("melon.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["rank", "singer", "title", "album"])

    for d in data:
        writer.writerow(list(d.values()))
    return


hdr = {"User-Agent": "Jinuk"}
url = "https://www.melon.com/chart/day/index.htm"


result = requests.get(url, headers=hdr)

soup = BeautifulSoup(result.text, "html.parser")

lst50 = soup.find_all("tr", {"class": "lst50"})
lst100 = soup.find_all("tr", {"class": "lst100"})

lst = lst50 + lst100

data = []
for l in lst:
    rank = l.find("span", {"class": "rank"}).text
    title = l.find("div", {"class": "rank01"}).text.strip()
    singer = l.find("div", {"class": "rank02"}).find("a").text.strip()
    album = l.find("div", {"class": "rank03"}).find("a").text.strip()

    d = {"rank": rank, "title": title, "singer": singer, "album": album}
    data.append(d)

save_to_file(data)

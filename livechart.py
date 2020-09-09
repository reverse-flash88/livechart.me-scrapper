# python 3.8 venv[not activated]
"""[modules]"""

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

"""[dt modules]"""

from datetime import datetime
import pytz
from datetime import timedelta

"""[Url conf]"""

search_url = "https://www.livechart.me/search?q="
term = input("Search :").replace(" ", "+")
final_url = search_url + term

hdr = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
}
req = Request(final_url, headers=hdr)
page = urlopen(req)
search_page = BeautifulSoup(page, features="lxml")
title = search_page.find_all("a", attrs={"data-target": "anime-item.mainTitle"})
link_s = [
    a["href"]
    for a in search_page.find_all(
        "a", attrs={"data-target": "anime-item.mainTitle"}, href=True
    )
    if a.text
]

"""[Url conf]"""

anime_url = "https://www.livechart.me"
anime_href = link_s[0]
anime_final = anime_url + anime_href

"""[Getting the Episode number]"""

req2 = Request(anime_final, headers=hdr)
page2 = urlopen(req2)
main_page = BeautifulSoup(page2, features="html5lib")
episode = main_page.find("div", attrs={"class": "info-bar-cell info-bar-label"})

"""[Getting time from https://livechart.me/]"""

testt = main_page.find(
    "div", attrs={"title": "Click to view time/convert to another time zone"}
)["data-countdown-bar-timestamp"]

"""[Air time]"""

import time
readable = time.ctime(int(testt))
var1 = str(readable).strip()
day = var1[8] + var1[9]
hours = var1[11] + var1[12]
minutes = var1[14] + var1[15]
seconds = var1[17] + var1[18]

"""[Current time]"""

IST = pytz.timezone("Asia/Kolkata")
datetime_ist = datetime.now(IST)
var2 = str(datetime_ist.strftime("%d %H %M %S"))
cur_day = var2[0] + var2[1]
cur_hour = var2[3] + var2[4]
cur_minute = var2[6] + var2[7]
cur_second = var2[9] + var2[10]

"""[Remaining time calculation]"""

air_time = timedelta(
    days=int(day),
    hours=int(hours),
    minutes=int(minutes),
    seconds=int(seconds)
)
current_time = timedelta(
    days=int(cur_day),
    hours=int(cur_hour),
    minutes=int(cur_minute),
    seconds=int(cur_second),
)
print(episode.text, "airs in", air_time - current_time)

#! /usr/bin/env python
# -*- coding: utf-8 -*-


import re
import requests
import requests_cache

from bs4 import BeautifulSoup as BS

urls = {'today': 'http://www.getyourfixtures.com/all/fixtures/today/football',
        'tomorrow': 'http://www.getyourfixtures.com/all/fixtures/tomorrow/football'
        }
time_offset = '+01:00'
time_offset = requests.utils.quote(time_offset)
timezone_url = "http://www.getyourfixtures.com/setTimeZone.php?offset={}".format(
    time_offset)


def get_data(day, cache=True):
    matches = []
    session = requests_cache.CachedSession(
        '/tmp/foo_cache', backend='sqlite', expire_after=7200)
    session.get(timezone_url)
    response = session.get(urls[day])
    soup = BS(response.content, "lxml")
    for div in soup.find_all("div", class_="match"):
        if div.select("div.home") and div.select("div.away"):
            time = div.select("div.time span")[0].get_text().strip()
            competition = div.find(class_="competition").get_text().strip()
            home = div.select("div.home")[0].get_text().strip()
            away = div.select("div.away")[0].get_text().strip()
            stations = div.select("div.stations ul li.country-qa")
            if stations:
                stations = [clean_channel_name(station.text)
                            for station in stations]
            else:
                stations = []
            matches.append(
                {"time": time, "competition": competition, "station": stations, "home": home, "away": away})
    return matches


def clean_channel_name(channel_name):
    stop_words = ['Sports', 'Sport', 'Channel', 'Television', 'Arabia', 'TV']
    for word in stop_words:
        channel_name = re.sub(r'%s\s?' % word, '', channel_name, re.I)
    return channel_name.strip()
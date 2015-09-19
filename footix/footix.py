#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: walid

import argparse

import re
import requests
import requests_cache

from bs4 import BeautifulSoup as bs
from termcolor import colored

TODAY_URL = "http://www.getyourfixtures.com/all/fixtures/today/football"
TOMORROW_URL = "http://www.getyourfixtures.com/all/fixtures/tomorrow/football"
time_offset = '+01:00'
time_offset = requests.utils.quote(time_offset)
timezone_url = "http://www.getyourfixtures.com/setTimeZone.php?offset={}".format(
    time_offset)
requests_cache.install_cache(
    '/tmp/footix_cache', backend='sqlite', expire_after=7200)


def get_data(base_url):
    matches = []
    session = requests_cache.CachedSession()
    session.get(timezone_url)
    response = session.get(base_url)
    soup = bs(response.content, "lxml")
    for div in soup.find_all("div", {"class": "match"}):
        if div.select("div.home") and div.select("div.away"):
            time = div.select("div.time span")[0].get_text().strip()
            home = div.select("div.home")[0].get_text().strip()
            away = div.select("div.away")[0].get_text().strip()
            stations = div.select("div.stations ul li.country-qa")
            if stations:
                stations = [clean_channel_name(station.text)
                            for station in stations]
            else:
                stations = []
            matches.append(
                {"time": time, "station": stations, "home": home, "away": away})
    return matches


def clean_channel_name(channel_name):
    stop_words = ['Sports', 'Sport', 'Channel', 'Television', 'Arabia', 'TV']
    for word in stop_words:
        channel_name = re.sub(r'%s\s?' % word, '', channel_name, re.I)
    return channel_name.strip()


def main():
    parser = argparse.ArgumentParser(usage="-h for full usage")
    parser.add_argument('-w', help='watchable game', action="store_true")
    parser.add_argument(
        '--today', '-t', help='todays games', action="store_true")
    parser.add_argument(
        '--tomorrow', '-to', help='tomorrow games', action="store_true")
    args = parser.parse_args()
    if args.tomorrow:
        data = get_data(TOMORROW_URL)
    elif args.today:
        data = get_data(TODAY_URL)
    else:
        data = get_data(TODAY_URL)
    if args.w:
        data = [x for x in data if x['station']]
    for match in data:
        match_time = colored(match['time'], "red", "on_yellow")
        channels = colored(" ".join(match['station']), "blue", "on_white")
        first_team = colored(match['home'], "green")
        second_team = colored(match['away'], "cyan")
        vs = colored('VS', "white", attrs=['bold', 'blink'])
        print u"{:10} {:40} {:40} {:30} {:40}".format(match_time, channels, first_team, vs, second_team)

main()

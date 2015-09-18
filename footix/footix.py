#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: walid

import argparse

import re
import requests

from bs4 import BeautifulSoup as bs
from termcolor import colored

base_url = "http://www.getyourfixtures.com/all/fixtures/today/football"
offset = '+01:00'
offset = requests.utils.quote(offset)
timezone_url = "http://www.getyourfixtures.com/setTimeZone.php?offset={}".format(
    offset)


def get_data():
    matches = []
    session = requests.Session()
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
    data = get_data()
    parser = argparse.ArgumentParser(usage="-h for full usage")
    parser.add_argument('-w', help='watchable game', action="store_true")
    parser.add_argument('-f', help='only favorite team', action="store_true")
    args = parser.parse_args()
    if args.w:
        data = [x for x in data if x['station']]
    args = parser.parse_args()
    for match in data:
        match_time = colored(match['time'], "red", "on_yellow")
        channels = colored(" ".join(match['station']), "blue", "on_white")
        first_team = colored(match['home'], "green")
        second_team = colored(match['away'], "cyan")
        vs = colored('VS', "white", attrs=['bold', 'blink'])
        print u"{:10} {:40} {:40} {:30} {:40}".format(match_time, channels, first_team, vs, second_team)
main()

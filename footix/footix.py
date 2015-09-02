#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: walid

import requests
from bs4 import BeautifulSoup as bs
from termcolor import colored
import argparse

url="http://www.getyourfixtures.com/all/fixtures/today/football"
timezone_url="http://www.getyourfixtures.com/setTimeZone.php?offset=%2B01%3A00"
def get_data():
    matches=[]
    session=requests.Session()
    session.get(timezone_url)
    response=session.get(url)
    soup=bs(response.content,"lxml")
    for div in soup.find_all("div",{"class":"match"}):
      if div.select("div.home") and div.select("div.away"):
        time=div.select("div.time span")[0].get_text().strip()
        home=div.select("div.home")[0].get_text().strip()
        away=div.select("div.away")[0].get_text().strip()
        stations=div.select("div.stations ul li.country-qa")
        if stations:
            stations=[station.text.strip().replace('BeIN Sport Arabia','BeIN') for station in stations]
        else:
            stations=[]
        matches.append({"time":time,"station":stations,"home":home,"away":away})
    return matches
def main():
    data=get_data()
    parser = argparse.ArgumentParser(usage="-h for full usage")
    parser.add_argument('-v', help='search query',action="store_true")
    args = parser.parse_args()
    if args.view:
        data=[x for x in data if x['station']]
    args = parser.parse_args()
    for match in data:
        match_time = colored(match['time'], "red", "on_yellow")
        channels=colored(" ".join(match['station']), "blue", "on_white")
        first_team = colored(match['home'], "green")
        second_team = colored(match['away'], "cyan")
        vs = colored('VS', "white", attrs=['bold', 'blink'])
        print u"{:10} {} {:40} {:30} {:40}".format(match_time, channels, first_team, vs, second_team)
main()
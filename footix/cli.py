#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

import footix

from termcolor import colored


def main():
    parser = argparse.ArgumentParser(usage="-h for full usage")
    parser.add_argument('-w', help='watchable game', action="store_true")
    parser.add_argument(
        '--today', '-t', help='todays games', action="store_true")
    parser.add_argument(
        '--tomorrow', '-to', help='tomorrow games', action="store_true")
    args = parser.parse_args()
    if args.tomorrow:
        data = footix.get_data('tomorrow')
    elif args.today:
        data = footix.get_data('today')
    else:
        data = footix.get_data('today')
    if args.w:
        data = [x for x in data if x['station']]
    for match in data:
        match_time = colored(match['time'], "red", "on_yellow")
        channels = colored(" ".join(match['station']), "blue", "on_white")
        first_team = colored(match['home'], "green")
        second_team = colored(match['away'], "cyan")
        vs = colored('VS', "white", attrs=['bold', 'blink'])
        print u"{:10} {:40} {:40} {:30} {:40}".format(match_time, channels, first_team, vs, second_team)

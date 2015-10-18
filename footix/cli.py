#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

import footix

from . import __version__
from prettytable import HEADER
from prettytable import PrettyTable
from termcolor import colored


def main():
    parser = argparse.ArgumentParser(usage="-h for full usage")
    parser.add_argument(
        '-V', '--version', action='version', version=__version__)
    parser.add_argument('-w', help='watchable games', action="store_true")
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
    output = PrettyTable(["Time", "Competition", "Channels", "Home", "Away"])
    output.align = "l"
    output.border = True
    output.hrules = HEADER
    output.horizontal_char = "_"
    for match in data:
        match_time = colored(match['time'], "red", "on_yellow")
        competition = colored(match['competition'], "yellow", attrs=['bold'])
        channels = colored(" ".join(match['station']), "blue", "on_white")
        first_team = colored(match['home'], "green")
        second_team = colored(match['away'], "cyan")
        output.add_row(
            [match_time, competition, channels, first_team, second_team])
    output.add_row(["", "", "", "", ""])
    print output

if __name__ == '__main__':
    main()

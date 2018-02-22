#!/usr/bin/env python

import argparse
import helloworld


def parse_command_line():
    " parses args for the helloworld.py funtions"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add short args
    parser.add_argument(
        "-n", "--name",
        help="optional name to say hello to",
        type=str)

    parser.add_argument(
        "-d", "--date",
        help="print today's date",
        action="store_true")

    # parse args
    args = parser.parse_args()
    return args


def main():
    " run helloworld on parsed args"
    args = parse_command_line()
    helloworld.helloworld(
        name=args.name,
        date=args.date)
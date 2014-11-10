#!/usr/bin/env python

"""
Ant colony visualization
"""

import json
import sys

from board import Board

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "You need to specify initial configuration."
        sys.exit(1)

    input_data = None

    with open(sys.argv[1], 'r') as input_data_fd:
        input_data = json.load(input_data_fd)

    gameboard = Board(input_data['width'],
                      input_data['height'],
                      input_data['colony_pos'],
                      input_data['food'])

    if len(sys.argv) > 2:
        file_fd = open(sys.argv[2], 'r')
        sys.stdin = file_fd

    while True:
        data = sys.stdin.readline().rstrip()
        try:
            data_in = json.loads(data)
            if 'exit' in data_in:
                gameboard.exit()
                sys.stdin.close()
                sys.exit(0)
            gameboard.update(data_in)
        except ValueError:
            pass


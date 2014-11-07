#!/usr/bin/env python

import random
import json

if __name__ == "__main__":
    for i in range(0, 10):
        data = {}
        data['board'] = [{"tau_a": random.uniform(0.1, 1), "tau_b": random.uniform(0.1, 1)} for x in range(0, 50*50)]
        data['ants'] = [{"id": x, "position" : [(x+i), (x+i+1)], "carries_food": False} for x in range(0, 25)]
        print json.dumps(data)

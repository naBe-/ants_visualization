import random
import json
data = {}
data['board'] = [{"tau_a": random.uniform(0.1, 1), "tau_b": random.uniform(0.1, 1)} for x in range(0, 50*50)]
data['ants'] = [{"id": x, "position" : [x*10, (x+1)*10], "carries_food": False} for x in range(0, 25)]
with open('data.in', 'w') as fd_out:
    json.dump(data, fd_out)

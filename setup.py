import random
from node import Node
import pickle
import numpy as np

def read_list():
    with open("players.txt") as f:
        lines = [line.rstrip('\n') for line in f]
        random.shuffle(lines)
        return np.array(lines)
    
def process_list(players):
    n = len(players)
    nodes = []
    for i in range(n-1):
        nodes.append(Node(i+1,players[i], players[i+1]))
    nodes.append(Node(n, players[n-1], players[0]))
    with open('alive.txt', 'wb') as handle:
        pickle.dump(nodes, handle, protocol=pickle.HIGHEST_PROTOCOL)

process_list(read_list())
print("Created randomized list!")
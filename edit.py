import numpy as np
import pickle

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def show_list(nodes):
    print(f"{color.DARKCYAN}List of active players:{color.END}")
    for i in nodes:
        print(f"{color.BLUE}({i.number}): {i.person}{color.END} -----> {color.RED}{i.target}{color.END}")
    

with open('alive.txt', 'rb') as handle:
    nodes = pickle.load(handle)
    names = np.array([n.person for n in nodes])
    numbers = np.array([n.number for n in nodes])
    print(*numbers)
    
name = ""
while name != "done":
    n = len(nodes)
    show_list(nodes)
    name = input(f"Name of the player to eliminate (type 'done' if done eliminating): ")
    if (name == "done"):
        break
    elif (type(name) is str and name in names):
        a = np.where(names == name)[0][0]
        target = nodes[a].target
        nodes[a-1].new_target(target)
        names = np.delete(names, a)
        numbers = np.delete(numbers, a)
        nodes = np.delete(nodes, a)
        print(f"{color.BOLD}{name} has been eliminated!{color.END}\n")
    elif (type(int(name)) is int):
        num = int(name)
        if (num in numbers):
            a = np.where(numbers == num)[0][0]
            target = nodes[a].target
            nodes[a-1].new_target(target)
            names = np.delete(names, a)
            numbers = np.delete(numbers, a)
            nodes = np.delete(nodes, a)
            print(f"{color.BOLD}{name} has been eliminated!{color.END}\n")
    else:
        print(f"{color.BOLD}Invalid name!{color.END}\n")

with open('alive.txt', 'wb') as handle:
    handle.close()
with open('alive.txt', 'wb') as handle:
    pickle.dump(nodes, handle, protocol=pickle.HIGHEST_PROTOCOL)
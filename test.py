import numpy as np

# a = np.array([1, 2, 3])
# print(a[0-3])
# print(np.where(a == 1)[0][0])
# print("hello" in a)
# print(((type(1) is int)))
with open("players.txt") as f:
    lines = [line.rstrip('\n') for line in f]
    for line in lines:
        a = line.strip()
        f.write(a)



class Node:
    def __init__(self, number, person, target):
        self.person = person
        self.target = target
        self.number = number

    def new_target(self, target):
        self.target = target
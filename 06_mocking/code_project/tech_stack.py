import random


class TechStack:

    def __init__(self):
        self.techStacks = list()

    def add_tech(self, name):
        if not name in self.techStacks:
            self.techStacks.append(name)
            return self
        return self

    def get_tech(self):
        return random.choice(self.techStacks)

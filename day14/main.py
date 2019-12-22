from collections import defaultdict

# Build directed graph
graph = defaultdict(list)

class Node:
    def __init__(self, name, amount):
        self.amount = int(amount)
        self.name = name

    def __eq__(self, another):
        return hasattr(another, 'name') and self.name == another.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"({self.name}, {self.amount})"

    def __str__(self):
        return f"({self.name}, {self.amount})"


with open('input.txt') as f:
    for line in f:
        line = line.strip().split(' => ')
        left = line[0].split(',')
        right = Node(line[1].split()[1], line[1].split()[0])

        graph[right] = [Node(x.split()[1], x.split()[0]) for x in left]

print(graph)
TOTAL = 0

def print_nodes(node):
    global TOTAL
    find = graph[node]
    print('NODE', node)
    for n in find:
        print('FOUND ', n)
        if n == Node('ORE', 0):
            TOTAL += n.amount
        print_nodes(n)
    print()

print_nodes(Node('FUEL', '1'))
print(TOTAL)

print('More than 33100')

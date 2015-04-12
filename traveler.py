import math
import itertools


class Node:
    name = ""
    lat = None
    lng = None

    def __init__(self, name, lat=None, lng=None):
        self.name = name

        if lat is not None:
            self.lat = float(lat)

        if lng is not None:
            self.lng = float(lng)

    def info(self):
        return "%s (%d,%d)" % (self.name, float(self.lat), float(self.lng))


class Map:
    size = 5
    nodes = []
    distances = []

    def __init__(self, nodes):

        # Get cities count
        self.size = len(nodes)
        self.nodes = nodes

        # Initialize distances with 0 values
        self.distances = [[0 for i in range(self.size)] for i in range(self.size)]
        self.calculate_all()

    def put(self, origin, destination, distance):
        self.distances[origin][destination] = distance

    def get(self, origin, destination):
        return self.distances[origin][destination]

    def index(self, name):
        for origin in range(len(self.nodes)):
            if self.nodes[origin].name == name:
                return origin

    def calculate_all(self):
        for origin in range(len(self.nodes)):
            for destination in range(len(self.nodes)):
                self.put(origin, destination, self.calculate(origin, destination))

    def calculate(self, o, d):

        if o == d:
            return 0

        else:
            origin = self.nodes[o]
            destination = self.nodes[d]
            return math.sqrt(
                pow((origin.lat - destination.lat), 2)
                + pow((origin.lng - destination.lng), 2))

    def permutations(self, org):
        tam = len(self.nodes)
        filteredlist = sorted(self.nodes[0:org] + self.nodes[org + 1:tam], key=self.cmdName)
        return list(itertools.permutations(filteredlist))

    def routes(self, org):
        perms = self.permutations(org)
        return [([pi.name for pi in p], self.sum_distance(org, p)) for p in perms]

    def sum_distance(self, org, perm):

        total = 0
        last = org

        for p in perm:
            total += self.get(last, self.index(p.name))
            last = self.index(p.name)

        return total

    def cmdName(self, node):
        return node.name

    def cmdDistance(self, node):
        (path, distance) = node
        return distance

    def minimum(self, org):
        possibilities = self.routes(org)
        return sorted(possibilities, key=self.cmdDistance)


def start():
    origin = None
    nodes = []

    while True:

        raw = raw_input()
        parsed = raw.split(' ')
        size = len(parsed)

        if len(parsed) < 2:
            origin = Node(raw)
            break

        else:

            coord = parsed[size - 2:size]

            name = ' '.join(parsed[0: size - 2])
            lat = coord[0]
            lng = coord[1]

        nodes.append(Node(name, lat, lng))

    city_map = Map(nodes)
    org = city_map.index(origin.name)

    (path, distance) = city_map.minimum(org)[0]

    for p in path:
        print p

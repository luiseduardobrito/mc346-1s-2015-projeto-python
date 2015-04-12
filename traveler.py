import math

class Node:
    name = ""
    lat = None
    lng = None

    def __init__(self, name, lat=None, lng=None):
        self.name = name
        self.lat = lat
        self.lng = lng


    def info(self):
        print "%s (%d,%d)" % (self.name, self.lat, self.lng)


class Map:
    size = 5
    nodes = []
    distances = []

    def __init__(self, nodes):

        # Get cities count
        self.size = len(nodes)

        # Initialize distances with 0 values
        distances = [[0 for i in range(self.size)] for i in range(self.size)]

    def put(self, origin, destination, distance):
        self.distances[origin][destination] = distance

    def get(self, origin, destination):
        return self.distances[origin][destination]

    def calculate_all(self):
        for origin in self.nodes:
            for destination in self.nodes:
                self.put(self.calculate(origin, destination))

    def calculate(self, origin, destination):
        # TODO: Calculate distance
        self.distances[origin][destination] = math.sqrt(pow((origin.lat - destination.lat), 2) + pow((origin.lng - destination.lng), 2))


def start():


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

    map = Map(nodes)

    # TODO: find minimum

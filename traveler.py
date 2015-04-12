import math


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

    def minimum(self, org):

        origin = None

        for n in self.nodes:
            if n == org:
                origin = n

        return origin.info()


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

    # print Map(nodes).minimum(origin)

    print Map(nodes).distances

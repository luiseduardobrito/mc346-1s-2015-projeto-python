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


def start():
    origin = None
    nodes = []

    while True:

        raw = raw_input()

        if len(raw) < 2:
            origin = Node(input[0])
            break

        else:
            name = raw[0]
            lat = raw[1]
            lng = raw[2]

        nodes.append(Node(name, lat, lng))

    print nodes
    print origin
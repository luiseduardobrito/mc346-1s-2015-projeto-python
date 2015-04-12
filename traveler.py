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
        parsed = raw.split(' ')
        size = len(parsed)

        if len(parsed) < 2:
            origin = Node(raw)
            break

        else:

            coord = parsed[size-2:size]

            name = ' '.join(parsed[0: size - 2])
            lat = coord[0]
            lng = coord[1]

        nodes.append(Node(name, lat, lng))

    print nodes
    print origin
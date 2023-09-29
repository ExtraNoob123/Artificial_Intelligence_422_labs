import heapq

def astar(start, end):
    path = {}
    distance = {}
    a = priorityQueue()
    h = makehuristikdict()
    a.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []
    while (a.isEmpty() == False):
        t = a.pop()
        expandedList.append(t)
        if (t == end):
            break
        for new in romania[t]:
            g_exp = distance[t] + int(new.distance)

            if (new.town not in distance or g_exp < distance[new.town]):
                distance[new.town] = g_exp
                f_exp = g_exp + heuristic(new.town, h)

                a.push(new.town, f_exp)
                path[new.town] = t
    output(start, end, path, distance, expandedList)


class priorityQueue:
    def __init__(self):
        self.towns = []

    def push(self, town, exp):
        heapq.heappush(self.towns, (exp, town))

    def pop(self):
        return heapq.heappop(self.towns)[1]

    def isEmpty(self):
        if (self.towns == []):
            return True
        else:
            return False

    def check(self):
        print(self.towns)


class last_node:
    def __init__(self, town, distance):
        self.town = str(town)
        self.distance = str(distance)


romania = {}


def create():
    file = open("romania.txt", 'r')
    for string in file:
        line = string.split(',')
        t1 = line[0]
        t2 = line[1]
        dist = int(line[2])
        romania.setdefault(t1, []).append(last_node(t2, dist))
        romania.setdefault(t2, []).append(last_node(t1, dist))


def makehuristikdict():
    h = {}
    with open("romania_sld.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h


def heuristic(node, values):
    return values[node]


def output(start, end, path, distance, expandedList):
    destination = []
    i = end
    while (path.get(i) != None):
        destination.append(i)
        i = path[i]
    destination.append(start)
    destination.reverse()
    print(f"Path: {destination}")
    print(f"Total Distance {distance[end]} KM")



src = "Arad"
dst = "Bucharest"
create()
astar(src, dst)


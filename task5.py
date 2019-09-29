LONG_WAY = 10**10

class Graph:
    def __init__(self, arg):
        self.pair = []
        i = 0
        while i < len(arg):
            while len(self.pair) <= arg[i][0] or len(self.pair) <= arg[i][1]:
                self.pair.append([])
            i += 1
        self.length = len(self.pair)
        self.visited = [False]*self.length
        self.level = [-1] * self.length
        
        i = 0
        while i < self.length:
            j = 0
            while j < self.length:
                self.pair[i].append([j, LONG_WAY])
                j += 1
            i += 1

        i = 0
        while i < len(arg):
            self.pair[arg[i][0]][arg[i][1]][1] = arg[i][2]
            self.pair[arg[i][1]][arg[i][0]][1] = arg[i][2]
            i += 1
    def deikstra(self, nodeStart, nodeEnd):
        hit = []
        way_len = []

        for i in range(len(self.pair)):
            hit.append(0)
            way_len.append(LONG_WAY)
        way_len[nodeStart] = 0

        i = 0
        for i in range(len(self.pair)):
            dot = -1
            j = 0
            for j in range(len(self.pair)):
                if not self.visited[j] and (dot == -1 or way_len[j] < way_len[dot]):
                    dot = j
            if way_len[dot] == LONG_WAY:
                break
            self.visited[dot] = True

            j = 0
            for j in range(len(self.pair[dot])):
                t = self.pair[dot][j][0]
                length = self.pair[dot][j][1]
                if way_len[dot] + length < way_len[t]:
                    way_len[t] = way_len[dot] + length
                    hit[t] = dot

        v = nodeEnd
        path = []
        while v != nodeStart:
            path.append(v)
            v = hit[v]
        path.append(nodeStart)
        print(*reversed(path))
a = Graph([[0, 3, 5], [1, 3, 11], [2, 3, 56], [4, 3, 77],[5, 4, 89]])
a.deikstra(1,5)
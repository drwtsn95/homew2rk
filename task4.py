'''matrix-like representation of graph'''
class Graph:
    def __init__ (self, arg):
        self.pair = []
        i = 0
        while i < len(arg):
            while len(self.pair) <= arg[i][0]:
                self.pair.append([])
            while len(self.pair) <= arg[i][1]:
                self.pair.append([])
            self.pair[arg[i][0]].append(arg[i][1])
            self.pair[arg[i][1]].append(arg[i][0])
            i += 1
        self.length = len(self.pair)
        self.visited = [False] * self.length
        self.level = [-1] * self.length

    def dfs(self, val):
        self.visited[val] = True
        print(val)
        for i in self.pair[val]:
            if not self.visited[i]:
                self.dfs(i)

    def bfs(self, val):
        self.level[val] = 0
        queue = [val]
        while queue:
            v = queue.pop(0)
            print(v)
            for i in self.pair[v]:
                if self.level[i] == -1:
                    queue.append(i)
                    self.level[i] = self.level[v] + 1
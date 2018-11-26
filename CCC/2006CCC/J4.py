class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.visited = False

    def add_neighbor(self, to_v, weight=0):
        self.neighbors[to_v] = weight

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_name(self):
        return self.name

    def __str__(self):
        return str(self.name) + " -> " + str([str(v_name) for v_name in self.neighbors])

    def get_neighbors_count(self):
        return len(self.neighbors)

    def set_visited(self, flag):
        self.visited = flag

    def get_visited(self):
        return self.visited


class Graph:
    def __init__(self):
        self.vert_map = {}

    def add_vertex(self, v):
        self.vert_map[v] = Vertex(v)

    def add_edge(self, from_v, to_v):
        if from_v in self.vert_map:
            self.vert_map[from_v].add_neighbor(to_v)
        else:
            v1 = Vertex(from_v)
            v1.add_neighbor(to_v)
            self.vert_map[from_v] = v1

    def get_vertex(self, from_v):
        if from_v in self.vert_map:
            return self.vert_map[from_v]
        else:
            return None

    def get_all_vertices(self):
        return self.vert_map.values()

    def dfs(self):
        tasks = []
        for aVertex in self.get_all_vertices():
            if not aVertex.get_visited():
                self.dfs_visit(aVertex, tasks)

        for v in tasks:
            print v

    def dfs_visit(self, start_vertex, tasks):
        start_vertex.set_visited(True)
        for nv in start_vertex.get_neighbors():
            next_vertex = self.vert_map[nv]
            if not next_vertex.get_visited():
                self.dfs_visit(next_vertex, tasks)

        tasks.append(start_vertex)


g = Graph()

g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_vertex(7)

g.add_edge(1, 7)
g.add_edge(1, 4)
g.add_edge(2, 1)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(6, 2)
g.add_edge(5, 4)

g.dfs()




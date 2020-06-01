class DirectedGraph:
    def __init__(self):
        self.nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, value):
        self.adjacent_list[value] = []
        self.nodes = self.nodes + 1

    def add_edge(self, node1, node2):
        self.adjacent_list[node1].append(node2)

    def get_connected_nodes(self, node):
        return self.adjacent_list[node]

    def print(self):
        for k,v in self.adjacent_list.items():
            print(str(k) + ' -> ' + ', '.join(map(str, v)))
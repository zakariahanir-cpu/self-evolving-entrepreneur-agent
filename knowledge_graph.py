import networkx as nx

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_entity(self, entity):
        self.graph.add_node(entity)

    def add_relationship(self, entity1, entity2, relationship):
        self.graph.add_edge(entity1, entity2, label=relationship)

    def query_graph(self, query):
        # Implement graph query logic here
        pass
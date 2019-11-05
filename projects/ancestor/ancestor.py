# from projects.graph.graph import Graph as GraphType
from graph import Graph

def earliest_ancestor(ancestors, starting_node=None):
    # format ancestors to adjacency list
    family = Graph()

    # add vertices and edges
    for enum in ancestors:
      parent, child = enum
      family.add_vertex(parent)
      family.add_vertex(child)
      family.add_edge(parent, child)
    
    print(family.vertices)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors)
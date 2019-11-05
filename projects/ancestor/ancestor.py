
def earliest_ancestor(ancestors, starting_node=None):
    # format ancestors to adjacency list
    #
    graph = {}
    for val in ancestors:
      if val[0] in graph:
        graph[val[0]].append(val[1])
      else:
        graph[val[0]] = [val[1]]
    print(graph)
    pass


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors)
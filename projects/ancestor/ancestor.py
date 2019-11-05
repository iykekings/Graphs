
def earliest_ancestor(ancestors, starting_node=None):
    # format ancestors to adjacency list
    graph = {}
    for enum in ancestors:
      key, value = enum
      if key in graph:
        graph[key].append(value)
      else:
        graph[key] = [value]
    print(graph)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors)
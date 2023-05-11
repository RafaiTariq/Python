# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def bds(graph, b, startNode):
    visited = []
    queue = []
    return bdsUtil(graph, b, startNode, visited, queue)


def bdsUtil(graph, b, startNode, visited, queue):

    visited.append(startNode)
    queue.append(startNode)

    while queue:
        s = queue.pop(0)
        if len(graph[s]) <= b:
            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        else:
            for neighbour in graph[s]:
                bdsUtil(graph, b, neighbour,visited,queue)

    return " ".join(visited)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

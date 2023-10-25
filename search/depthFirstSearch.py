import null

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)



    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited


if __name__ == '__main__':
    graph = {'0': set(['1', '2']),
             '1': set(['0', '3', '4']),
             '2': set(['0']),
             '3': set(['1']),
             '4': set(['2', '3'])}

    dfs(graph, '0')

    root  = [6,2,8,0,4,7,9,null,null,3,5]

    print('root val:', root.val)




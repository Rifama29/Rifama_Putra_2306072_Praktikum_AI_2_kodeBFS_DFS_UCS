# -*- coding: utf-8 -*-
"""bfs

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1U4LG6u6k2nrFNz-ymMy_v0vyjhPpH1AF
"""

# -*- coding: utf-8 -*-
"""bfs

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dDk0drn0fwu35-fPrvyUOiwNdjWpddoo
"""

# -*- coding: utf-8 -*-
"""bfs

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AfWoMofdiFG1kdx5VThumu4a6nGkvCw2
"""

# BFS algorithm in python

import collections

# BFS algorithm
def bfs(graph, root):

  visited, queue = set(), collections.deque([root])
  visited.add(root)

  while queue:

    #dequeue a vertex from queue
    vertex = queue.popleft()
    print(str(vertex) + " ", end="")

    #if not visited, mark it as visited, and
    #enqueue it
    for neighbour in graph[vertex]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)

if __name__ == "__main__":
  graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
  print("Following is Breath First Traversal:")
  bfs(graph, 0)# -*- coding: utf-8 -*-
"""bfs

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AfWoMofdiFG1kdx5VThumu4a6nGkvCw2
"""

# BFS algorithm in python

import collections

# BFS algorithm
def bfs(graph, root):

  visited, queue = set(), collections.deque([root])
  visited.add(root)

  while queue:

    #dequeue a vertex from queue
    vertex = queue.popleft()
    print(str(vertex) + " ", end="")

    #if not visited, mark it as visited, and
    #enqueue it
    for neighbour in graph[vertex]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)

if __name__ == "__main__":
  graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
  print("Following is Breath First Traversal:")
  bfs(graph, 0)
# np_complete_project
Minimum vertex cover: the minimum number of vertices that includes an endpoint of every edge in the graph  
Decision problem: is there a number of vertices, n, that includes an endpoint of every edge?  
NP - Complete checking: Check every edge to make sure that an endpoint is included.  
# Approximation Pseudocode:
```
for i in len(E):
  comb = iter.combinations(V, i)
  for combinations in comb:
    NP_Check(combinations)

def NP_Check(combinations):
  for E in graph:
    return (if E.v1 in combinations) or (of E.v2 in combinations)
```

import time
# greedy appeoximation

def vertex_cover_approx(edges):
    # Initialize an empty set to store the vertex cover
    cover = set()
    
    # Create a dictionary to keep track of the degree of each vertex
    degrees = {}
    for u, v in edges:
        degrees[u] = degrees.get(u, 0) + 1
        degrees[v] = degrees.get(v, 0) + 1
    
    # Loop until all edges are covered
    while edges:
        # Pick the vertex with the highest degree
        u = max(degrees, key=degrees.get)
        
        # Add the vertex to the vertex cover
        cover.add(u)
        
        # Remove all edges incident on u
        edges = [e for e in edges if u not in e]
        
        # Update the degrees of remaining vertices
        degrees = {}
        for u, v in edges:
            degrees[u] = degrees.get(u, 0) + 1
            degrees[v] = degrees.get(v, 0) + 1
    
    return cover

def main():
    startTime = time.time()
    vertices = set()
    n = int(input())
    edges = [input().split(" ") for _ in range(n)]
    result = vertex_cover_approx(edges)
    if result:
        print (*result, sep = " ")
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))


if __name__ == "__main__":
    main()

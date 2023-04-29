import itertools

def min_vertex_cover(edges):
    # Create a list of all possible vertex combinations
    vertices = set()
    for edge in edges:
        vertices.update(edge)
    combinations = []
    for i in range(1, len(vertices)+1):
        combinations.extend(itertools.combinations(vertices, i))

    # Check each combination to see if it forms a valid vertex cover
    min_cover = vertices
    for c in combinations:
        cover = set(c)
        if check_np(edges, cover) and len(cover) < len(min_cover):
            min_cover = cover

    return min_cover

def check_np(edges, nodes):
    for edge in edges:
        if not (edge[0] in nodes or edge[1] in nodes):
            return False
    return True


def main():
    vertices = set()
    n = int(input())
    edges = [input().split(" ") for _ in range(n)]
    result = min_vertex_cover(edges)
    if result:
        print (*result, sep = " ")

if __name__ == "__main__":
    main()

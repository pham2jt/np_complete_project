import itertools
def brute_force(edges, vertices):
    for i in range(1, len(vertices) + 1):
        comb = itertools.combinations(vertices, i)
        return check_np(edges, list(comb))

def check_np(edges, vertices):
    print('vert', vertices)
    for set_v in vertices:
        print ('set_v', set_v)
        for edge in edges:
            a, b = edge
            print("edge: ", a, b)
            if (a not in set_v) and (b not in set_v):
                break
        return set_v
    return False


def main():
    vertices = set()
    n = int(input())
    edges = [input().split(" ") for _ in range(n)]
    for edge in edges:
        a, b = edge
        vertices.add(a)
        vertices.add(b)
    print("edges", edges)
    print("vertices", vertices)
    results = brute_force(edges, vertices)
    for result in results:
        print(result, ' ')
    

if __name__ == "__main__":
    main()

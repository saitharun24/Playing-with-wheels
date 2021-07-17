from collections import deque
class Graph:
    def __init__(self):
        NUM_VERTICES = 10000
        self.num_vertices = NUM_VERTICES
        self.edges = [[] for i in range(self.num_vertices)]
        self.forbidden_states = set([])
        def __set_data():
            def to_int(a, b, c, d):
                return d + c * 10 + b * 100 + a * 1000
            # to convert the numbers back to the string and assign individual digits to the variables a, b, c and d
            for i in range(self.num_vertices):
                t = i
                t, d = divmod(t, 10)
                t, c = divmod(t, 10)
                a, b = divmod(t, 10)
                # check all the possible states from the current state
                self.edges[i] = [
                    to_int(a, b, c, d-1 if d > 0 else 9),
                    to_int(a, b, c, d+1 if d < 9 else 0),
                    to_int(a, b, c-1 if c > 0 else 9, d),
                    to_int(a, b, c+1 if c < 9 else 0, d),
                    to_int(a, b-1 if b > 0 else 9, c, d),
                    to_int(a, b+1 if b < 9 else 0, c, d),
                    to_int(a-1 if a > 0 else 9, b, c, d),
                    to_int(a+1 if a < 9 else 0, b, c, d),
                ]
        __set_data()
    def set_forbidden_states(self, forbiddens):
        self.forbidden_states = set(forbiddens)
    # used to calulate the minimum possible path from the graph generated
    def min_path(self, s, e):
        if s == e:
            return 0
        distance_from_s = [-1] * self.num_vertices
        def bfs(start, end):
            discovered = [False] * self.num_vertices
            q = deque([start])
            distance_from_s[start] = 0
            discovered[start] = True
            while len(q) > 0:
                v = q.popleft()
                for y in self.edges[v]:
                    if not self.valid_edge(v, y):
                        continue
                    if not discovered[y]:
                        discovered[y] = True
                        distance_from_s[y] = distance_from_s[v] + 1
                        if y == end:
                            return
                        q.append(y)
            return
        bfs(s, e)
        return distance_from_s[e]
    
    # used to check if the edge is a forbidden one, if yes we are not going to procceed in the path else we are going going to take the edge as the new input and recurse through the entire process again
    def valid_edge(self, v_start, v_end):
        if v_end in self.forbidden_states:
            return False
        return True

# function to convert the number string into a number
def to_int(a, b, c, d):
    return d + c * 10 + b * 100 + a * 1000

# main function
num_cases = int(input())
g = Graph()
for c in range(num_cases):
    line = input().strip()
    while line == "":
        line = input().strip()
    s = to_int(*list(map(int, line.split())))
    e = to_int(*list(map(int, input().split())))
    forbiddens = []
    n_forbidden = int(input())
    for i in range(n_forbidden):
        forbiddens.append(to_int(*list(map(int, input().split()))))
    if s in forbiddens or e in forbiddens:
        print(-1)
    else:
        g.set_forbidden_states(forbiddens)
        print(g.min_path(s, e))

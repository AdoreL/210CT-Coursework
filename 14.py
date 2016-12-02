class Vertex():
    """Create vertex point"""
    def __init__(self,node):
        self.node = node
        self.edge = []

class Graph():
    """Create graph"""
    def __init__(self):
        self.adj_list = {} #gets the adjacency list

    def add_node(self,node):
        new_node = Vertex(node) #creates new_node with node value
        adj_list[node] = [new_node] #adds it as a key into the adj_list
        return new_node #returns the node
    
    def add_edge(self,node, edge):
        adj_list[node] = edge #the node is given the edge as a value within the list
        #actually adds the entire node and edges in one go
        return adj_list #returns the entire list

    def BFS(self,Vertex):
        Q = []
        visited = []
        Q.append(Vertex)
        while Q != []:
            u = Q.pop()
            if u not in visited:
                visited.append(u)
            for u in adj_list:
                e = adj_list.get(u)
                Q.append(e)
        return visited

    def DFS(self, Vertex):
        S = []
        visited = []
        S.push(Vertex)
        while S != []:
            u = S.pop()
            if u not in visited:
                visited.append(u)
                for u in adj_list:
                    e = adj_list.get(u)
                    Q.append(e)
        return visited

if __name__ == '__main__':

    g = Graph()
    adj_list = {0:1,
        1:[0,2],
        2:[1,3],
        3:[2,4],
        4:[3,5],
        5:[4,6],
        6:[5,7],
        7:[6,8],
        8:[7,9],
        9:[8,10]
        }
    g.add_node(11)
    g.add_edge(11,[12])
    print(adj_list)
    print(g.BFS(3))
    print(g.DFS(3))



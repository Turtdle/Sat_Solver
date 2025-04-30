import sys

DEBUG = True

class Graph_to_CNF():
    def __init__(self, input_file):
        # read in the data from the file and create a
        # graph representation
        self.graph = {}
        i = 1
        with open(input_file, "r") as f:
            for line in f:
                data = line.split()
                # convert string to numerical value
                for j in range(0, len(data)):
                    data[j] = int(data[j])

                self.graph[i] = data
                i = i + 1
        if DEBUG:
            print("Graph: \n{}\n".format(self.graph))

    def generatecnf(self):
        num_vertices = len(self.graph)
        clauses = []
        
        def var(vertex, color):
            return (vertex - 1) * 3 + color
        
        
        for vertex in range(1, num_vertices + 1):
            clauses.append([var(vertex, 1), var(vertex, 2), var(vertex, 3)])
        
        for vertex in range(1, num_vertices + 1):
            clauses.append([-var(vertex, 1), -var(vertex, 2)])
            clauses.append([-var(vertex, 1), -var(vertex, 3)])
            clauses.append([-var(vertex, 2), -var(vertex, 3)])
        
        processed_edges = set()
        for vertex in range(1, num_vertices + 1):
            for neighbor in self.graph[vertex]:
                edge = (min(vertex, neighbor), max(vertex, neighbor))
                if edge not in processed_edges:
                    processed_edges.add(edge)
                    for color in range(1, 4):
                        clauses.append([-var(vertex, color), -var(neighbor, color)])
        
       
        total_variables = num_vertices * 3
        print(f"p cnf {total_variables} {len(clauses)}")
        for clause in clauses:
            print(" ".join(map(str, clause + [0])))





if __name__=="__main__":
    # check for the number of arguments
    if len(sys.argv) == 1:
        print("Usage: {} [INPUT_FILE]".format(sys.argv[0]))
        exit(0)
    
    graph_to_cnf = Graph_to_CNF(sys.argv[1])
    graph_to_cnf.generatecnf()
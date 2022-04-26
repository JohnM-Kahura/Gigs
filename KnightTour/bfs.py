from pythonds.graphs import Graph,Vertex
# bfs implementation
def knightGraph(bdSize):
    knight_tour_graph = Graph()
    for row in range(bdSize):
       for col in range(bdSize):
           nodeId = position_to_node_id(row,col,bdSize)
           newPositions = generate_legal_moves(row,col,bdSize)
           for e in newPositions:
               nid = position_to_node_id(e[0],e[1],bdSize)
               knight_tour_graph.addEdge(nodeId,nid)
    return knight_tour_graph
# converts a location on the board in terms of a row and a column into a linear vertex number similar to the vertex numbers
def position_to_node_id(row, column, board_size):
    return (row * board_size) + column
# takes the position of the knight on the board and generates each of the eight possible moves
def generate_legal_moves(x,y,bdSize):
    new = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in moveOffsets:
        new_x = x + i[0]
        new_y = y + i[1]
        if legal_coordinates(new_x,bdSize) and \
                        legal_coordinates(new_y,bdSize):
            new.append((new_x,new_y))
    return new

def legal_coordinates(x,bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False

# with dfs
# backtrscking is also used
def knightTour(n,path,u,limit):
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = list(u.getConnections())
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    done = knightTour(n+1, path, nbrList[i], limit)
                i = i + 1
            if not done:  # prepare to backtrack
                path.pop()
                u.setColor('white')
        else:
            done = True
        return done

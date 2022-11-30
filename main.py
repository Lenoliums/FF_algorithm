
import random
import string
import config as c

global G, G_ 

# prevents cycles
# G_ contains all connected vertices
def cycle_check(edge, id, N):
    if(edge in G_): 
        if(id<0 and (edge[0] != N[id]) and not([edge[0], N[id]] in G)): 
            G.append([edge[0], N[id]]) 
            return(N[-1])
        else: 
            if( (N[0] != edge[1]) and not([N[0],edge[1]] in G)): G.append([N[0],edge[1]])
        return False
    full_G = G + G_
    for i in full_G:
        if(i[1]==edge[0] and not ([edge[1], i[0]] in G_) ):
            G_.append([edge[1], i[0]])
    return True

def bandwidth(limit):
    for i in G:
        i.append(random.randint(1, limit))

def graph_creation(n):
    N = list(string.ascii_uppercase)[0:n]
    G.clear()
    G_.clear()
    inNode = N[1:]
    outNode = N[:-1]
    inNode.append(N[-1])
    outNode.append(N[0])
    # controls that at least one edge exits from each vertex. 2 from first (or more)
    for i in N[:-1]:
        while(i in outNode):
            for j in N[1:]:
                if(i!=j and (not ([i,j] in G)) and (not ([j,i] in G)) and (i!=N[0] or j!=N[-1])):
                    if(random.randrange(0, 2)):
                        if(cycle_check([i,j], -1, N)):
                            G.append([i,j])
                            if (j in inNode): inNode.remove(j)
                        if (i in outNode):outNode.remove(i)
  
#   similarly for incoming edges
    for i in N[1:]:
        while(i in inNode):
            for j in N[:-1]:
                if(i!=j and (not ([i,j] in G)) and (not ([j,i] in G)) and (j!=N[0] or i!=N[-1])):
                    if(random.randrange(0, 2)):
                        if(cycle_check([j,i], 1, N)):
                            G.append([j,i])
                        if (i in inNode): inNode.remove(i)
    return(G)


G= []
G_=[]

# generating graphs and writing to a file
file = open(f"input{c.n}.txt", 'w')
try:
    
    for i in range(100): 
        graph_creation(c.n)
        bandwidth(c.limit)
        file.write(str(G))
        file.write('\n')
    
finally:
    file.close()




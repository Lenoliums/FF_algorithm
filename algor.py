import config as con
import random
global u,c,f, all_path

# finds paths (continuations of paths). if the path ends in last adds to the appropriate, continue if not and if its possible
# all_path containes all paths from first to last nodes and min edge val in each path
def path_finder(prev_path, min_c):
    k=prev_path[-1]
    for i in range(con.n):
        if (c[k][i]!=0 and not(i in prev_path)): 
            if(c[k][i]<min_c):
                if(i==con.n-1):
                    all_path.append([[*prev_path, i], c[k][i]])
                    return 0
                path_finder([*prev_path, i], c[k][i])
            else:
                if(i==con.n-1):
                    all_path.append([[*prev_path, i], min_c])
                    return 0
                path_finder([*prev_path, i], min_c)

# starts find correct paths
def path_colect():
    all_path.clear()
    for i in range(con.n):
        if(c[0][i]!=0):
            path_finder([0, i], c[0][i])


def alg_Forda_falkersona(apr):
    apost=0 #апостериорная оценка
    path_colect()
    while(len(all_path) and apost<=apr):  #работает пока существуют пути расширения
        
        num_path = random.randrange(0, len(all_path)) #выбирает рандомное ребро
        path=all_path[num_path][0]
        c_f = all_path[num_path][-1] #min edge val
        for i in range(len(path)-1):
            u_=path[i]
            v_=path[i+1]
            f[u_][v_]+=c_f
            apost+=2
            f[v_][u_]-=c_f
            apost+=2
            c[u_][v_]=u[u_][v_]-f[u_][v_]
            apost+=2
            c[v_][u_]=u[v_][u_]-f[v_][u_]
            apost+=2
        path_colect() #обновляет all_path
    return (apost)

def ucf_iniz(A):
    for i in range(con.n):
        for j in range(con.n):
            u[i][j]=0 #пропускная способность
            c[i][j]=0 #остаточная пропуск. спос.
            f[i][j]=0 #поток
    #заполнение начальных условий пропускных способностей
    for i in A:
        x =con.N.index(i[0])
        y = con.N.index(i[1])
        u[x][y]=i[2]
        c[x][y]=i[2]

def F_val(): #возвращает мощность максимального потока
    f_val=0
    for i in range(con.n):
        f_val+=f[i][con.n-1]
    return f_val

all_path=[]
u = [[0 for j in range(con.n)] for i in range(con.n)]
c = [[0 for j in range(con.n)] for i in range(con.n)]
f = [[0 for j in range(con.n)] for i in range(con.n)]

k=0
result = open(f"res{con.n}.txt", "w")
file = open(f"input{con.n}.txt", "r")
for line in file: #приводим граф в удобный вид
    G_ = line[2: -3].split('], [')
    A = []
    maxf_module=0
    for i in G_:
        t = i.split(', ')
        A.append( ( t[0][1], t[1][1], int(t[2]) ) )

    apr=0 #априорная оценка
    res=''
    r=[] #хранит апостериорные оценки решений графа
    for l in range(1000): #решаем каждый граф 1000 раз 
        maxf_module=0
        ucf_iniz(A)
        for i in u:                         
            maxf_module+=i[con.n-1]             #максимальная из возможных мощность максимального потока для априорной оценки
        apr=maxf_module*len(A)*(con.n)          #len(A)-число ребер, n- вершин
        apost = alg_Forda_falkersona(apr)   
        #проверка решения
        for i in range(con.n):
            for j in range(con.n):
                if(f[i][j]>u[i][j]):
                    print('error')
                    k+=1
                    break 

        r.append(apost)
    res += str(r[0]) + ' ' + str(r[1]) + ' ' + str(sum(r)/1000) + ' ' #два значения для сравнения и вывода, третье - среднее
    result.write(str(apr) + ' ' + res + str(F_val()))
    result.write('\n')
    result.write(str(len(A))+'\n')
print(k)
file.close()
result.close()

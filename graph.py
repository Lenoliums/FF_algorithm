import matplotlib.pyplot as plt
import config as c


file = open(f"res{c.n}.txt", "r")
Data=[]
E=[] #количества ребер
for line in file:
    Data.append(line[:-1].split(' '))
    E.append(int(file.readline()))
Data = [(int(i[0]), int(i[1]), int(i[2]), float(i[3]), int(i[4])) for i in Data]
# Data_apr=[str(i[0])+'>' for i in Data] #априорная оценк
Data_apost_1=[i[1] for i in Data] #значения получившихся оценок
Data_apost_2=[i[2] for i in Data]
Data_apost_3=[i[3] for i in Data] #массив средних значений
Data_f_val = [i[4] for i in Data] #мощности максимальных потоков

#наглядно. варьируемость количества итераций при изменениях пути
x = [i for i in range(len(Data_apost_1))]
fig, ax = plt.subplots()
ax.bar(x, Data_apost_3)
ax.bar(x, Data_apost_1)
ax.bar(x, Data_apost_2)


fig.set_facecolor('floralwhite')
fig.set_figwidth(10)
fig.set_figheight(12)  
plt.title(label='chart of variation in the number of steps for different path choices') 
plt.xlabel('graphs')
plt.ylabel("number of steps for graph solving")
plt.show()

#наглядно. зависимость трудоемкости от значения максимального потока (зависимость от пропускной способности)
fig1, ax1 = plt.subplots()
ax1.scatter(Data_f_val, Data_apost_3)
fig1.set_facecolor('floralwhite')
fig1.set_figwidth(10)
fig1.set_figheight(12)   
plt.xlabel('value of max flow')
plt.ylabel("number of steps for graph solving")
plt.title(label='graph of the dependence of the number of steps on the value of the max flow')
plt.show()

#наглядно. зависимость трудоемкости от количества ребер
fig3, ax3 = plt.subplots()
ax3.scatter(E, Data_apost_3)
fig3.set_facecolor('floralwhite')
fig3.set_figwidth(10)
fig3.set_figheight(12)   
plt.xlabel('number og edge')
plt.ylabel("number of steps for graph solving")
plt.title(label='graph of the dependence of the number of steps on the value of the num of edge')
plt.show()

#зависимость трудоемкости от заданной в начале оценки
Dific=[E[i]*Data_f_val[i] for i in range(len(E))]
fig2, ax2 = plt.subplots()
ax2.scatter(Dific, Data_apost_3)
fig2.set_facecolor('floralwhite')
fig2.set_figwidth(10)
fig2.set_figheight(12)   
plt.ylabel('number of steps for graph solving')
plt.xlabel("|f|*|E|")
plt.title(label='dependence of the number of iterations on the maximum flow, the number of vertices and edges')
plt.show()


#не наглядно. график с осями мощность макс. потока, число ребер, трудоемкость
fig4 = plt.figure()
ax4 = plt.axes(projection='3d')
ax4.scatter(Data_f_val, E, Data_apost_3)

plt.show()
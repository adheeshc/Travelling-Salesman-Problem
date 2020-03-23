import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from itertools import combinations,chain
import datetime

t1=datetime.datetime.now()

def euclid_dist(x1,y1,x2,y2):
	dist=sqrt((x1-x2)**2+(y1-y2)**2)
	return int(dist)	

def plot_graph(nodelist,visited):
	for i,txt in enumerate(nodelist):
		plt.scatter(nodelist[i][0],nodelist[i][1])
		plt.annotate(txt,(nodelist[i][0],nodelist[i][1]))
	for i in range(0,len(visited)):
		plt.plot((nodelist[visited[i][0]][0],nodelist[visited[i][1]][0]),(nodelist[visited[i][0]][1],nodelist[visited[i][1]][1]))
	plt.show()

def edgedict(nodelist):
	weights=[]
	nodes=[]
	for i in range(0,len(nodelist)-1):
		for j in range(i+1,len(nodelist)):
			(x1,y1)=nodelist[i]
			(x2,y2)=nodelist[j]
			nodes.append((i,j))
			weights.append(euclid_dist(x1,y1,x2,y2))
	nodes=np.array(nodes)
	weights=np.array(weights).reshape(-1,1)
	final=np.concatenate((nodes,weights),axis=1)
			#edges[j,i]=edges[i,j]
	return final

def check(nodelist,final):
	visited=[]
	visited_new=[]
	#print(nodelist)
	#print(final)
	final=list(final)
	while len(final)!=0:
		init_w=final[0][2]
		#print(init_w)
		for i in range(0,len(final)):
			if final[i][2]<=init_w:
				init_w=final[i][2]
				init_node=final[i]
				idx=i
	#	print(np.array(final))
		del final[idx]
		#final.pop(idx)
		visited.append(init_node[:2])
	visited=np.array(visited)
	final=np.array(final)
	visited=visited.tolist()
	data_list = visited
	all_triple_pairs = list(combinations(data_list, 3))
	digit_sets = [set(d for pair in trip for d in pair) for trip in all_triple_pairs]
	dup_inds = [i for i, s in enumerate(digit_sets) if len(s)==3]
	duplicates = [all_triple_pairs[i] for i in dup_inds]
	pairs_to_remove = [trip[-1] for trip in duplicates]
	answer = [pair for pair in data_list if pair not in pairs_to_remove]
	#print(answer)
	for p in answer:
	 	print(p)
	return answer

def file_handling():
	file1=open('eil101.tsp','r')

	Name=file1.readline().split()[2]
	Comment=file1.readline().strip().split()[2:]
	Comment=Comment[0]+' '+Comment[1]+' '+Comment[2]
	Type=file1.readline().split()[2]
	Dimension=file1.readline().split()[2]
	Edge_weight_type=file1.readline().split()[2]

	file1.readline()
	nodelist=[]
	N=int(Dimension)
	for i in range(0,N):
		x,y=file1.readline().split()[1:]
		nodelist.append((float(x),float(y)))

	file1.close()
	filename=Name
	return nodelist,filename
 
def mst_length(visited,nodelist):
	dist=[]
	for i in range(0,len(visited)):
		dist.append(euclid_dist(nodelist[visited[i][0]][0],nodelist[visited[i][0]][1],nodelist[visited[i][1]][0],nodelist[visited[i][1]][1]))
	length=sum(dist)
	return length

def main():

	#nodelist,filename=file_handling()
##FOR 10 points
	nodelist=[(8,2),(5,9),(4,3),(2,6),(1,7),(9,2),(5,5),(8,3),(11,8),(6,14)]
##FOR 20 points
	#nodelist=[(8,-4),(5,9),(4,3),(2,6),(1,7),(9,2),(5,5),(8,3),(11,8),(6,14),(6,8),(20,12),(14,0),(30,2),(4,26),(1,1),(-4,-5),(-10,10),(0,15),(4,4)]
##UNCOMMENT FOR 25 points
	#nodelist=[(8,-4),(5,9),(4,3),(2,6),(1,7),(9,2),(5,5),(8,3),(11,8),(6,14),(6,8),(20,12),(14,0),(30,2),(4,26),(1,1),(-4,-5),(-10,10),(0,15),(4,4),(50,5),(4,29),(20,20),(25,20),(-5,-15)]
	print(f'the total number of nodes are {len(nodelist)}')
	final= edgedict(nodelist)	
	visited=check(nodelist,final)
	length=mst_length(visited,nodelist)
	print(f'the mst cost is {length}')
	t2=datetime.datetime.now()
	print(f'The time take is {t2-t1}')
	plot_graph(nodelist,visited)

if __name__=="__main__":
	main()





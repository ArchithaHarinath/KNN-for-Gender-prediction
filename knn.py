import csv
import random
import math
import operator

#Function to calculte cartesian distance between 2 points		
def cartesiandistance(instance1, instance2, length):
	distance=0
	for x in range(length):
		distance+=pow((instance1[x]-instance2[x]), 2)
	return math.sqrt(distance)

#Fuction to decide the majority of the class in the calculated nearest neighbours
def classmajority(neighbours):
	classcount={}
	for x in range(len(neighbours)):
		temp=neighbours[x][-1]
		if temp in classcount:
			classcount[temp]+= 1
		else:
			classcount[temp]= 1
	temp=classcount.items()
	temp.sort(key=operator.itemgetter(1),reverse=True)
	print temp
	return temp

def main():	
	
	#get the filename as input from the user and store the data in a list
	filename=input("Input the filename: ")
	csvfile=open(filename,'rb')
	lines=csv.reader(csvfile)
	dataset=list(lines)
	#print(dataset)
	trainingSet=[]
	for x in range(len(dataset)):
		for y in range(3):
			dataset[x][y]=float(dataset[x][y])
		trainingSet.append(dataset[x])
		
	#get the input data for which the class has to be calculated
	ts=raw_input('Enter test set data: ')
	testset=map(int,ts.split())
	
	#getting the k nearest neighbors value 
	k=input('Enter the K value for which the nearest neighbors have to be calculated: ')
	
	#Calculating the eucledian distance between the data in the file and the data for which the class has to be calculated
	distances=[]
	length=len(testset)-1
	#print(length)
	for x in range(len(trainingSet)):
		dist=cartesiandistance(testset, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	#print(distances)
	distances.sort(key=operator.itemgetter(1))
	#print(distances)
	neighbours=[]
	for x in range(k):
		neighbours.append(distances[x][0])
	#print(neighbours)
	print(" The "+str(k)+" nearest neighbors for the test set "+str(testset)+"are"+ str(neighbours))
	result=[]
	
	#Decide the class for which the input test data belong to
	result=classmajority(neighbours)
	print("The test set "+str(testset)+" belongs to class "+str(result[0][0]))	
	

main()

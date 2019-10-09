import numpy as np
import random
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

#Costos asociados al arco <ij> .\Original Graph.png
graph = np.array([
	(0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0),
    (1, 0, 2, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 2, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 6, 0, 0, 0, 5, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 3, 0, 5, 0, 9, 0, 9, 3, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 1, 2, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 8, 0, 0, 0),
    (0, 0, 0, 0, 7, 9, 0, 0, 0, 6, 0, 4, 8, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 3, 0, 0, 6, 0, 5, 0, 0, 2, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 7, 4, 0, 0, 0, 2, 0, 6, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 2, 0, 1, 0, 8, 5, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 2, 7),
    (2, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 6, 0, 7, 4),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 0, 7, 0, 5),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 7, 0, 4, 5, 0)
    ])

#Gaussian Test .\Gaussian Test.png
testFunction = np.array([ 
    (0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 0 ,0, 0),
    (0, 0, 1, 3, 6, 9, 11, 9, 6, 3, 1, 0, 0),
    (0, 1, 4, 11, 20, 30, 35, 30, 20 ,11 , 4, 1, 0),
    (0, 3, 11, 26, 50, 73, 82, 73, 50, 26, 11, 3, 0),
    (1, 6, 20, 50, 93, 136, 154, 136 ,93, 50, 20, 6, 1),
    (2, 9, 30, 73, 136, 198, 225, 198, 136, 73, 30, 9, 2),
    (2, 11, 34, 82, 154, 255, 255, 255, 136, 93, 50, 20, 6, 1),
    (2, 9, 30, 73, 136, 198, 225, 198, 136, 73, 30, 9, 2),
    (1, 6, 20, 50, 93, 136, 154, 136 ,93, 50, 20, 6, 1),
    (0, 3, 11, 26, 50, 73, 82, 73, 50, 26, 11, 3, 0),
    (0, 1, 4, 11, 20, 30, 35, 30, 20 ,11 , 4, 1, 0),
    (0, 0, 1, 3, 6, 9, 11, 9, 6, 3, 1, 0, 0),
    (0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 0 ,0, 0),
])

class particle(object):

    def __init__(self, maxCoordinate):

        self.position = []
        self.velocity = 0
        self.best = 0
        self.currentValue = 0
        self.maxCoordinate = maxCoordinate
    
    def initialize(self):

        self.position = (random.randint(1, self.maxCoordinate - 2), random.randint(1, self.maxCoordinate - 2))

    def getBest(self):

        

        

class swarm(object):

    def __init__(self, graph):

        self.globalBest = 0
        self.graph = graph

    def optimize(self, popSize, c1, c2, Wmin, Wmax, Vmax, maxIter):

        mySwarm = [particle(self.graph.shape[0]) for x in range(popSize)] #Populate based on popSize
        
        for ptcl in mySwarm:

            ptcl.initialize() #Set each particle in the map considering its size
            #plt.scatter(ptcl.position[0], ptcl.position[1]) #Scatter positions for particles
        
        #plt.show() #Plot particle in their respective positions
        #print(self.graph.shape[0]) #Print max dimension of graph
        
        i = 0   

        while i < maxIter:

            for ptcl in mySwarm:

                #Calculate current value
                ptcl.currentValue = graph(ptcl.position[0], ptcl.position[1])
                ptcl.getBest() #OUT OF 8 Neighbors




def main():

	swarm(testFunction).optimize(10, 2, 2, 0.4, 1, 10, 250)


if __name__ == '__main__':

	main()
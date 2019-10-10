import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


np.set_printoptions(suppress=True)

#Costos asociados al arco <ij> .\Original Graph.png
city = np.array([
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

#DEFINE GRAPH TO TEST: IMPORTANT!
graph = testFunction

matrix = np.zeros((graph.shape[0], graph.shape[0]), dtype=int)
data = None

def Generate():

    global data

    matrix = np.zeros((graph.shape[0], graph.shape[0]), dtype=int)

    for pair in data[0]:

        while(matrix[pair[0]][pair[1]] != 0):

            matrix[pair[0]][pair[1]] = 1
    
    return matrix

def updateAnimations(i):
    global matrix
    global data

    matrix = np.zeros((graph.shape[0], graph.shape[0]), dtype=int)

    #actualizar
    for pair in data[i]:

         while(matrix[pair[0]][pair[1]] != 0):

            matrix[pair[0]][pair[1]] = 1  

    if i == len(data):

        i = 1     


class particle(object):

    def __init__(self, maxCoordinate):

        self.position = [0, 0]
        self.velocity = [1, 1]
        self.best = [0, 0, 0]
        self.currentValue = 0
        self.maxCoordinate = maxCoordinate
    
    def initialize(self):

        self.position = (random.randint(1, self.maxCoordinate - 2), random.randint(1, self.maxCoordinate - 2))

    def getBest(self): #scans immediate neighbors

        self.currentValue = graph[self.position[0]][self.position[1]] #Gets current value

        for x in range (self.position[0] - 1, self.position[0] + 2):
            for y in range (self.position[1] - 1, self.position[1] + 2):

                if graph[x][y] > self.best[2]:

                    self.best = [x, y, graph[x][y]] #[x pos, y pos, value]

    def updateVelocity(self, w, c1, c2, gBest): #Updates velocity for particle according to ecuation in .\velEcuation.PNG

        """
        :type w: int (inertia weight)
		:type c2, c2: float (cognitive and social components)
		:type gBest: int array (global best)
        """

        r1, r2 = random.uniform(0, 1), random.uniform(0, 1)

        self.velocity = [
            int(w*self.velocity[0] + (c1 * r1 * (self.best[0] - self.position[0])) + (c2 * r2 * (gBest[0] - self.position[0]))),
            int(w*self.velocity[1] + (c1 * r1 * (self.best[1] - self.position[1])) + (c2 * r2 * (gBest[1] - self.position[1])))]

    def updatePosition(self): #Updates position for particle according to ecuation in .\posEcuation.PNG

        self.position = [
            self.position[0] + self.velocity[0], 
            self.position[1] + self.velocity[1]]



class swarm(object):

    def __init__(self):

        self.globalBest = [0, 0, 0]   

    def optimize(self, popSize, c1, c2, wMin, wMax, vMax, maxIter):

        """
        :type popSize: int (population size)
		:type c1, c2: int (cognitive and social components)
		:type wMin, wMax: float (inertia weight's boundaries)
        :type vMax: int (max velocity)
        :type maxIter: int (max number of iterations) 
        """

        swarmPositions, swarmStates, animationData = [], [], []

        mySwarm = [particle(graph.shape[0]) for x in range(popSize)] #Initialize Population of popSize particles
        
        for ptcl in mySwarm: 

            ptcl.initialize() #Set each particle in the map considering its size
            #plt.scatter(ptcl.position[0], ptcl.position[1]) #Scatter positions for particles
        
        #plt.show() #Plot particle in their respective positions
        #print(self.graph.shape[0]) #Print max dimension of graph
        
        i = 1   
        w, wDecreaseFactor = wMax, abs(wMax - wMin) / maxIter


        while i < maxIter:

            for ptcl in mySwarm: #For each particle

                ptcl.currentValue = graph[ptcl.position[0]][ptcl.position[1]] #Calculate current value
                ptcl.getBest()

                if ptcl.best[2] >= self.globalBest[2]: #Set new global if a best one is found

                    self.globalBest = [ptcl.best[0], ptcl.best[1], ptcl.best[2]]

                swarmPositions = [ptcl.position[0], ptcl.position[1]]
                swarmStates.append(swarmPositions)

            
            for component in self.globalBest:
                print(component)

            
            w -= wDecreaseFactor #Update intertia weight (decrease w)

            for ptcl in mySwarm: #For each particle

                ptcl.updateVelocity(w, c1, c2, self.globalBest) #Update velocity
                ptcl.updatePosition() #Update position


            animationData.append(swarmStates)
            swarmStates = []
            i += 1

        for component in self.globalBest:
            print(component)

        return animationData


def main():


    swarm().optimize(2, 2, 2, 0.4, 0.9, 10, 15)


    '''
    global data 
    data = swarm().optimize(2, 2, 2, 0.4, 0.9, 10, 15)

    matrix = Generate()
    fig, ax = plt.subplots()
    matrixA = ax.matshow(matrix)
    matrixA.set_cmap('inferno')
    plt.colorbar(matrixA)
    anim = animation.FuncAnimation(fig, updateAnimations, frames = None,  interval = 100, repeat = True)
    plt.show()
    '''

if __name__ == '__main__':

	main()


'''
        for ptcl in mySwarm: 

            plt.scatter(ptcl.position[0], ptcl.position[1]) #Scatter positions for particles
        
        animate = animation.FuncAnimation(fig, )
        plt.show() #Plot particle in their respective positions
'''
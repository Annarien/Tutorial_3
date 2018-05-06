#Problem 2: Let's write a direct-solving N-body solver. First, write a class that contains
#masses and x and y positions for a collection of particles. The class should also contain a dictionary
#that can contain options. Two entries in the dictionary should be the number of particles and G
#(gravitational constant). The class should also contain a method that calculates the potential
#energy of every particle, P (Gm1m2=r12) . (10)

import math
import numpy
import matplotlib
from matplotlib import pyplot as plt

#this represents a single particle
class Particle:
    mass = 0.0 # mass of particle
    xPos = 0.0 # x position of particle
    yPos = 0.0 # y position of particle

    #constructor
    #constructor that initializes the particle with a mass, x position and y position
    def __init__(self, mass, xPos, yPos): 
        self.mass = mass 
        self.xPos = xPos
        self.yPos = yPos

    # returns mass of particle
    def getMass(self):
        return self.mass

    # returns x position of particle
    def getXPosition(self):
        return self.xPos

    # returns y position of particle
    def getYPosition(self):
        return self.yPos


# worker class to help calculate things against particles such as number of patricles,distance, potential energy
# and any other methods needed against collection of particles 
class ParticleHelper:
    
    g = 6.673*(10**-11) # gravitaional constant defined 
    particles = {}      #empty dictionary of particles

    #constructor initializing helper with the particle dictionary
    def __init__(self, particles):
        self.particles = particles

    # function method to get number of particles
    def getNumberOfParticles(self):
        numberOfParticles = len(self.particles)
        return numberOfParticles

    # gets distances (pythagoras)
    def getDistanceBetweenParticles(self, particle1, particle2):
        x1 = particle1.getXPosition()
        y1 = particle1.getYPosition()
        
        x2 = particle2.getXPosition()
        y2 = particle2.getYPosition()

        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    #gets potential energy between 2 particles
    def getPotentialEnergyBetweenTwoParticles(self, particle1, particle2):
        d = self.getDistanceBetweenParticles(particle1, particle2)
        numerator = self.g * particle1.getMass() * particle2.getMass()
        ep = (self.g * particle1.getMass() * particle2.getMass()) / (d ** 2)
        return ep


    # gets total potential energy of all particles as a sum
    def getPotentialEnergyOfParticles(self):
        totalPotentialEnergy = 0.0

        numberOfParticles = self.getNumberOfParticles()
        for i in range(numberOfParticles - 1):  # n-1 loops for potential energy between n particles
            particle1Key = "P" + str(i)         # define key of current element in particles dictionary
            particle2Key = "P" + str(i + 1)     # define key of next element in particles dictionary

            particle1 = self.particles[particle1Key]    # fetching current particle
            particle2 = self.particles[particle2Key]    # fetching next particle

            potentialEnergyBetweenParticles = self.getPotentialEnergyBetweenTwoParticles(particle1, particle2)
            totalPotentialEnergy = totalPotentialEnergy + self.getPotentialEnergyBetweenTwoParticles(particle1, particle2)

        return totalPotentialEnergy

if __name__ == '__main__':
    particle1 = Particle(100, 0, 0)
    particle2 = Particle(200, 1, 1)
    particle3 = Particle(300, 3, -1)
    particles = {"P0" : particle1, "P1" : particle2, "P2" : particle3}

    particleHelper = ParticleHelper(particles)
    potentialEnergyOfAllParticles = particleHelper.getPotentialEnergyOfParticles()

    print("The total potential energy of all the particles is: " + str(potentialEnergyOfAllParticles))
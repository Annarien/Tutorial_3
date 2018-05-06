import math
import numpy
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.animation as animation

class Particle:
    mass = 0.0
    xPos = 0.0
    yPos = 0.0

    def __init__(self, mass, xPos, yPos):
        self.mass = mass
        self.xPos = xPos
        self.yPos = yPos

    def getMass(self):
        return self.mass

    def getXPosition(self):
        return self.xPos

    def setXPosition(self, xPos):
        self.xPos = xPos

    def getYPosition(self):
        return self.yPos

    def setYPosition(self, yPos):
        self.yPos = yPos

class ParticleHelper:
    g = 6.673*(10**-11)
    softeningFactor = 0.03
    timeStep = 0.1
    particles = {}

    def __init__(self, particles, softeningFactor, timeStep):
        self.particles = particles
        self.softeningFactor = softeningFactor
        self.timeStep = timeStep

    def getNumberOfParticles(self):
        numberOfParticles = len(self.particles) 
        return numberOfParticles

    def getDistanceBetweenParticles(self, particle1, particle2):
        x1 = particle1.getXPosition()
        y1 = particle1.getYPosition()
        
        x2 = particle2.getXPosition()
        y2 = particle2.getYPosition()

        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def getPotentialEnergyBetweenTwoParticles(self, particle1, particle2):
        d = self.getDistanceBetweenParticles(particle1, particle2)
        numerator = self.g * particle1.getMass() * particle2.getMass()
        ep = (self.g * particle1.getMass() * particle2.getMass()) / (d ** 2)
        return ep

    def getPotentialEnergyOfParticles(self):
        totalPotentialEnergy = 0.0

        numberOfParticles = self.getNumberOfParticles()
        for i in range(numberOfParticles - 1):
            particle1Key = "P" + str(i)
            particle2Key = "P" + str(i + 1)

            particle1 = self.particles[particle1Key]
            particle2 = self.particles[particle2Key]

            potentialEnergyBetweenParticles = self.getPotentialEnergyBetweenTwoParticles(particle1, particle2)
            totalPotentialEnergy = totalPotentialEnergy + potentialEnergyBetweenParticles

        return totalPotentialEnergy

    def getSoftenedPotentialEnergyBetweenTwoParticles(self, particle1, particle2):
        d = self.getDistanceBetweenParticles(particle1, particle2)
        numerator = self.g * particle1.getMass() * particle2.getMass()
        ep = (self.g * particle1.getMass() * particle2.getMass()) / math.sqrt((numpy.absolute(d) ** 2) + (self.softeningFactor ** 2))
        return ep

    def getSoftenedPotentialEnergyOfParticles(self):
        totalPotentialEnergy = 0.0

        numberOfParticles = self.getNumberOfParticles()
        for i in range(numberOfParticles - 1):
            particle1Key = "P" + str(i)
            particle2Key = "P" + str(i + 1)

            particle1 = self.particles[particle1Key]
            particle2 = self.particles[particle2Key]

            potentialEnergyBetweenParticles = self.getSoftenedPotentialEnergyBetweenTwoParticles(particle1, particle2)
            totalPotentialEnergy = totalPotentialEnergy + potentialEnergyBetweenParticles

        return totalPotentialEnergy

    def UpdateParticlePosition(self):
        numberOfParticles = self.getNumberOfParticles()
        for i in range(numberOfParticles):
            particleKey = "P" + str(i)
            dx = self.particles[particleKey].getXPosition() + self.timeStep
            dy = self.particles[particleKey].getXPosition() + self.timeStep

            self.particles[particleKey].setXPosition(dx)
            self.particles[particleKey].setYPosition(dy)

#_______________________________________________________________________________-

def getNRandomParticles(numberOfParticlesToCreate):
    particles = {}
    for i in range(numberOfParticlesToCreate):
        mass = numpy.random.randn()
        xPos = numpy.random.randn()
        yPos = numpy.random.randn()
        particle = Particle(mass, xPos, yPos)

        particleKey = "P" + str(i)
        particles[particleKey] = particle
        
    return particles

if __name__ == '__main__':
    numberOfParticles = 5000
    numberOfChanges = 5
    particles = getNRandomParticles(numberOfParticles)

    particleHelper = ParticleHelper(particles, 0.03, 0.1)
    potentialEnergyOfAllParticles = particleHelper.getSoftenedPotentialEnergyOfParticles()

    print("The total softened potential energy of all the particles is: " + str(potentialEnergyOfAllParticles))

    particleHelper.UpdateParticlePosition()
    print("Updating the particle positions")

    potentialEnergyOfAllParticles = particleHelper.getSoftenedPotentialEnergyOfParticles()
    print("The updated total softened potential energy of all the particles is: " + str(potentialEnergyOfAllParticles)) 

    print("Animating change in energy")
    xPoints = numpy.zeros(numberOfChanges)
    yPoints = numpy.zeros(numberOfChanges)

    for i in range(numberOfChanges):
        xPoints[i] = i + 1
        yPoints[i] = particleHelper.getSoftenedPotentialEnergyOfParticles()
    
    plt.ion()
    plt.plot(xPoints, yPoints)
    plt.ylabel('Energy')
    plt.xlabel('Iteration')
    plt.show(block=True)
###This code can be executed for any numerical data 'x1'.
###Press F5 to execute

import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

################################################################################
#Input

print '''
            K-Mean clustering for 3D data set
                                                '''

x1 = -2 + np.random.random((100,3))
#x2 = 1 + (np.random.random((50,3)))
#x1[50:100] = x2
while True:
    try:
        k = int(raw_input('Enter the number of groups needed: '))
        break
    except ValueError:
        print 'Please enter the integer value'

################################################################################
#Functions

emp = []
mean = []
meanlist = []
meandis = []

def randompick(x,y,z): #Randomly sampling clusters, x = Sample Data, y = Clusters, z = Output Random Sample List
    for i in range(y):
        z.append(random.sample(x,len(x)/y))
    return z

def meanval(x,y): #Finding mean of the clusters, x = Random Sample List, y = Output Mean List
    for i in range(k):
        m = np.mean(x[i], axis=0)
        y.append(m)
    return y

def distance(x,y): #Distance between 2 points
    dist = np.sqrt(np.sum(np.square(np.subtract(x,y))))
    return dist

def assigngroups(mean,x1): #Nearest groups w.r.t. mean

    dists = []
    shdis = []

    for j in range(len(mean)):
        for i in range(len(x1)):
            dists.append(distance(x1[i],mean[j]))

    for m in range(len(x1)):
        for n in range(k):
            a = dists[m+(len(x1)*n)]
            shdis.append(a)

    set = np.array(shdis)
    setn = set.reshape(len(x1),k)

    for z in range(len(setn)):
        for x,y in enumerate(setn[z]):
            ind = min(setn[z])
            if y == ind:
                groups[x].append(x1[z])
    return groups

def plot(k):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(k):
        if len(groups[i]) != 0:
            ax.scatter(np.stack(groups[i])[:,0],np.stack(groups[i])[:,1],np.stack(groups[i])[:,2])
    ax.set_xlabel('X Co-ordinates')
    ax.set_ylabel('Y Co-ordinates')
    ax.set_zlabel('Z Co-ordinates')
    plt.show()

##############################################################################2#
#Running Code

randompick(x1,k,emp) #Random Sample
meanval(emp,mean) #K no. of means
meanlist.append(mean)
meandis.append(distance(meanlist[len(meanlist)-1][0],meanlist[len(meanlist)-1][1]))
groups = [[] for x in range(k)]
assigngroups(mean,x1) #Assigning K no. of groups
newmean = []
meanval(groups,newmean) #New K no. of means
meanlist.append(newmean)
meandis.append(distance(meanlist[len(meanlist)-1][0],meanlist[len(meanlist)-1][1]))
while np.subtract(meandis[len(meanlist)-1],meandis[len(meanlist)-2]) >= 0.000000001:
    del groups[:]
    groups = [[] for x in range(k)]
    assigngroups(newmean,x1)
    del newmean[:]
    meanval(groups,newmean)
    meanlist.append(newmean)
    meandis.append(distance(meanlist[len(meanlist)-1][0],meanlist[len(meanlist)-1][1]))

plot(k)

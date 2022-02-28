###### Press 'F5' to run the code in ATOM directly.

import re
import math
import numpy as np

#4. Atomic contact map.

distance = []
contact = []

def coor(m):
    coordinates = []

    for i in range(len(m)):
        x = list(m[i])
        for j in range(len(x)):
            x[j] = float(x[j])
        coordinates.append(x)
    return coordinates

def dist(q):
    for i in range(len(a)):
        x = min(q+i+1,len(a)-1)
        diff = np.subtract(a[q],a[x])
        sqd = np.square(diff)
        sumsqd = np.sum(sqd)
        distance.append(np.sqrt(sumsqd))
    return distance

def total(n,r):
    npr = math.factorial(n)/math.factorial(n-r);
    ncr = npr/math.factorial(r)
    return ncr

welcome = '''

         The contact map of the selected PDB

         '''

print welcome

location = raw_input('Please enter valid and complete location of your PDB file: ') #Location for my file: E:/Study/Biocomputing/Assignments/AS03/101m.pdb

with open(location) as pdbfile:
    comp = pdbfile.read()

    atom = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?\d+\s{2}\w+\s{1,3}.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)
    a = coor(atom)
    for j in range(len(a)):
        dist(j)
    for m in range(len(distance)):
        if distance[m] <= 4.5:
            contact.append(distance[m])
        else:
            pass

print 'The number of atom pairs in atomic contact map are', len(contact), 'out of', total(len(a),2)

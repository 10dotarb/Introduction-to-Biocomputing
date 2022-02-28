###### Press 'F5' to run the code in ATOM directly.

import re
import numpy as np

#2. Calculate average distance between 2 consecutive 'CA' atoms.

welcome = '''

         Here, we will calculate the average distance between consecutive CA atoms

         '''

print welcome

location = raw_input('Please enter valid and complete location of your PDB file: ') #Location for my file: E:/Study/Biocomputing/Assignments/AS03/101m.pdb

with open(location) as pdbfile:
    comp = pdbfile.read()

    CA = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?\d+\s{2}CA\s{2}.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)

    coordinates = []

    for i in range(len(CA)):
        x = list(CA[i])
        for j in range(len(x)):
            x[j] = float(x[j])
        coordinates.append(x)

    distances = []

    for m in range(len(coordinates)-1):
        diff = np.subtract(coordinates[m],coordinates[m+1])
        sqd = np.square(diff)
        sumsqd = np.sum(sqd)
        distances.append(np.sqrt(sumsqd))

    avg = np.mean(distances)
    print 'The average distance between 2 CA atoms is', avg, 'angstrom'

###### Press 'F5' to run the code in ATOM directly.

import re
import numpy as np

#1. Calculate distance between any 2 atoms.

welcome = '''

         Here, we will calculate the distance between 2 CA atoms

         '''
def atomlist(m,n):
    x = []
    if m == 'C':
        x = list(C[n])
        for i in range(len(x)):
            x[i] = float(x[i])
    elif m == 'CA':
        x = list(CA[n])
        for i in range(len(x)):
            x[i] = float(x[i])
    elif m == 'O':
        x = list(O[n])
        for i in range(len(x)):
            x[i] = float(x[i])
    elif m == 'N':
        x = list(N[n])
        for i in range(len(x)):
            x[i] = float(x[i])

    print 'The coordinates of', m,':-',n, 'are   :', x
    return x

print welcome

location = raw_input('Please enter valid and complete location of your PDB file: ') #Location for my file: E:/Study/Biocomputing/Assignments/AS03/101m.pdb

with open(location) as pdbfile:
    comp = pdbfile.read()

    CA = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?\d+\s{2}CA\s{2}.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)
    C = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?\d+\s{2}C\s{3}.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)
    N = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?\d+\s{2}N\s{3}.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)
    O = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?\d+\s{2}O\s{3}.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)
    print 'The range of indices is 0 to',min(len(CA)-1,len(N)-1,len(C)-1,len(O)-1)

    while True:
        try:
            name1 = str(raw_input('Please enter name (CA, N, C, O) of 1st atom: '))
            break
        except ValueError:
            print 'Please enter the value from the given options'

    while True:
        try:
            mol1 = int(raw_input('Please enter residue number of 1st atom number: '))
            break
        except ValueError:
            print 'Please enter an integer in given range'

    x = atomlist(name1,mol1)

    while True:
        try:
            name2 = str(raw_input('Please enter name (CA, N, C, O) of 2nd atom: '))
            break
        except ValueError:
            print 'Please enter the value from the given options'

    while True:
        try:
            mol2 = int(raw_input('Please enter residue number of 2nd atom number: '))
            break
        except ValueError:
            print 'Please enter an integer in given range'

    y = atomlist(name2,mol2)

    diff = np.subtract(x,y)
    sqd = np.square(diff)
    sumsqd = np.sum(sqd)

    print 'Euclidean distance between these 2 atoms is ', np.sqrt(sumsqd), 'angstrom'

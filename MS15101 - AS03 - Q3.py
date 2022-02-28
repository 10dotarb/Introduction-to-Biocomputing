###### Press 'F5' to run the code in ATOM directly.

import re
import numpy as np

#3. Calculate phi and psi torsion angles.

def coor(m):
    coordinates = []

    for i in range(len(m)):
        x = list(m[i])
        for j in range(len(x)):
            x[j] = float(x[j])
        coordinates.append(x)
    return coordinates

welcome = '''

         Here, we will calculate phi and psi torsion angles

         '''

print welcome

location = raw_input('Please enter valid and complete location of your PDB file: ') #Location for my file: E:/Study/Biocomputing/Assignments/AS03/101m.pdb

with open(location) as pdbfile:
    comp = pdbfile.read()

    CA = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?\d+\s{2}CA\s{2}.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)
    C = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?\d+\s{2}C\s{3}.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)
    N = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?\d+\s{2}N\s{3}.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)

    a = coor(CA)
    b = coor(C)
    c = coor(N)

    phis = []
    psis = []

    for i in range(len(b)-1):
        AB = np.subtract(c[i+1],b[i])
        BC = np.subtract(a[i+1],c[i+1])
        CD = np.subtract(b[i+1],a[i+1])
        n1 = np.cross(BC,AB)
        n2 = np.cross(CD,BC)
        sqn1 = np.square(n1)
        sqn2 = np.square(n2)
        modn1 = np.sqrt(np.sum(sqn1))
        modn2 = np.sqrt(np.sum(sqn2))
        n1n2 = np.dot(n1,n2)
        x = n1n2/(modn1*modn2)
        phi = np.rad2deg(np.arccos(x))
        phis.append(phi)

    for j in range(len(c)-1):
        AB = np.subtract(a[j],c[j])
        BC = np.subtract(b[j],a[j])
        CD = np.subtract(c[j+1],b[j])
        n1 = np.cross(BC,AB)
        n2 = np.cross(CD,BC)
        sqn1 = np.square(n1)
        sqn2 = np.square(n2)
        modn1 = np.sqrt(np.sum(sqn1))
        modn2 = np.sqrt(np.sum(sqn2))
        n1n2 = np.dot(n1,n2)
        x = n1n2/(modn1*modn2)
        psi = np.rad2deg(np.arccos(x))
        psis.append(psi)

    print 'The list of phi angles is',phis
    print 'The list of psi angles is',psis

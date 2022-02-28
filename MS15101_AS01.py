#The protein tertiary structures are written in a particular format referred to as PDB format. It is formatted in a way that fixed column widths are assigned for a designated purpose.
#The image pdb.jpg shows the relevant entries and its column numbers.
#Each line in PDB format starts with 'ATOM' record, followed by its associated details such as atom type, residue name, residue ID, X,Y and Z coordinate of that atom.
#Each residue in a protein sequence are given 'RESIDUE ID', each residue has various atoms, and coordinate are given for each atom. Given this, perform following calculations using numpy:
#1. Calculate distance between any 2 'CA' atoms.
#2. Calculate angle between N-CA-C, (angle at CA), CA-C-O (angle at C).

###### Press 'F5' to run the code in ATOM directly.

import re
import numpy as np

#1. Calculate distance between any 2 'CA' atoms.

welcome = '''

         Here, we will calculate the distance between 2 CA atoms

         '''
print welcome

location = raw_input('Please enter valid and complete location of your PDB file: ') #Location for my file: E:/Study/Biocomputing/Assignments/AS01/1a00.pdb

with open(location) as pdbfile:
    comp = pdbfile.read()

    CA = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?CA\s.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)
    print 'The indices of CA atoms in the file range from 0 to',len(CA)-1

    while True:
        try:
            mol1 = int(raw_input('Please enter 1st CA atom number: '))
            break
        except ValueError:
            print 'Please enter an integer in given range'
    x = list(CA[mol1])
    for i in range(len(x)):
        x[i] = float(x[i])

    while True:
        try:
            mol2 = int(raw_input('Please enter 2nd CA atom number: '))
            break
        except ValueError:
            print 'Please enter an integer in given range'
    y = list(CA[mol2])
    for j in range(len(y)):
        y[j] = float(y[j])

    diff = np.subtract(x,y)
    sqd = np.square(diff)
    sumsqd = np.sum(sqd)

    print 'Euclidean distance between 2 CA is ', np.sqrt(sumsqd)

#2. Calculate angle between N-CA-C, (angle at CA), CA-C-O (angle at C).

welcome = '''

         Here, we will calculate the angles with CA and C at centre

         '''
print welcome

with open(location) as pdbfile:
    comp = pdbfile.read()

    CA = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?CA\s.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)
    N = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?N\s.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)
    C = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?C\s.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)
    O = re.findall(r'(?=\b^A.{53}\b)^ATOM.+?O\s.+?\d+\s{1,7}([-\d].+?)\s{2,3}([-\d].+?)\s+([-\d].+?)\s\b',comp,re.M)

    print 'The range of indices is',min(len(N), len(CA), len(C))-1,'for calculating angle at CA'
    print 'The range of indices is',min(len(CA), len(C), len(O))-1,'for calculating angle at C'

    while True:
        try:
            nol1 = int(raw_input('Please enter the index for ange at CA: '))
            break
        except ValueError:
            print 'Please enter an integer in given range'
    while True:
        try:
            nol2 = int(raw_input('Please enter the index for ange at C: '))
            break
        except ValueError:
            print 'Please enter an integer in given range'
    a1 = list(N[nol1])
    for j in range(len(a1)):
        a1[j] = float(a1[j])
    a2 = list(CA[nol1])
    for i in range(len(a2)):
        a2[i] = float(a2[i])
    a3 = list(C[nol1])
    for k in range(len(a3)):
        a3[k] = float(a3[k])
    b1 = list(CA[nol2])
    for l in range(len(b1)):
        b1[l] = float(b1[l])
    b2 = list(C[nol2])
    for m in range(len(b2)):
        b2[m] = float(b2[m])
    b3 = list(O[nol2])
    for n in range(len(b3)):
        b3[n] = float(b3[n])

    aNCA = np.subtract(a1,a2)
    aCAC = np.subtract(a2,a3)
    sqNCA = np.square(aNCA)
    sqCAC = np.square(aCAC)
    modNCA = np.sum(sqNCA)
    modCAC = np.sum(sqCAC)
    adot = np.dot(aNCA,aCAC)
    x = adot/(modNCA*modCAC)
    x1 = np.arccos(x)
    x2 = np.rad2deg(x1)

    bCAC = np.subtract(b1,b2)
    bCO = np.subtract(b2,b3)
    sqbCAC = np.square(bCAC)
    sqbCO = np.square(bCO)
    modbCAC = np.sum(sqbCAC)
    modbCO = np.sum(sqbCO)
    bdot = np.dot(bCAC,bCO)
    y = bdot/(modbCAC*modbCO)
    y1 = np.arccos(y)
    y2 = np.rad2deg(y1)

    print 'The angle around CA at index',nol1,'is',x2,'degrees'
    print 'The angle at C at index',nol2,'is',y2,'degrees'

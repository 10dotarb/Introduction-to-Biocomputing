#MS15101 - Q2
import math
import re

def shannon():
    aa = 'ACDEFGHIKLMNPQRSTVWYZ'
    #p =
    entropy = -p*(log(p))

fd = open('E:/Study/Biocomputing/Mid-Sem/MS15101/q2_msa.fasta')
head = fd.readline()
var = fd.readlines()
fd.close()

ids= []
seqs = []
sortid = []

for line in var:
    line = line.strip('\n')
    id = re.findall(r'^(\w+)',line)
    seq = re.findall(r'\w+\s+([\w-].+)',line)

#Can also be done without using regex by:
#for line in var:
    #line = line.strip('\n')
    #id = line[0:10]
    #seq = line[16:]

    ids.append(id)
    seqs.append(seq)

zipcomb = zip(ids, seqs)

for i in range(len(ids)):
    if ids[i] not in sortid:
        sortid.append(ids[i])

for m in range(len(sortid)):
    for j in range(len(zipcomb)):
        for k in range(len(zipcomb[j])):
            if zipcomb[j][0] == sortid[m]:
                sortid[m].append(zipcomb[j][1])
            else:
                pass

for n in range(len(sortid)):
    for l in range (len(sortid[n])):
        sortid[n][l] == str(sortid[n][l])
print sortid

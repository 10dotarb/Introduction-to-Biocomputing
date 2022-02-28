#MS15101 - Q1

import re

string = '''
Fdafaaf
csasfaffd
Mafdfasdp
Bassdaas
Then ajdfhsldakgh dsgj
The adjflhsldghs sfjghsakljgh sdaljhsda glsj gh.
w778ps
223222
44444444444
<a href="http://www.google.com"> Click here to reach google </a>
'''

# a.
var = re.search(r'(\b\w{8,10}\b)[^A-Z]\w+[a-oq-r]\b',string,re.M)
print var.group(0)

#b.
nar = re.search(r'^T.*?\.',string,re.M)
print nar.group(0)

#c.
aar = re.search(r'(^\d)\1{1,}\1',string,re.M)
print aar.group(0)

#d.
bar = re.search(r'^.+?(\d)\1{1,}.*',string,re.M)
print bar.group(0)

#e.
mar = re.search(r'<(\w).+?"(.*?)">\s*(.+?)</\1>',string,re.M)
print mar.group(2,3)

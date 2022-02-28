#MS15101 - Q3

import re

fd = open('/home/eclass/Desktop/MS15101/email.txt')
whole = fd.read()
fd.close()

sender = re.findall(r'From:\s*"(\w+)"',whole,re.M)
semail = re.findall(r'From:\s*"\w+"\s*<(\w+@\w+\..+?)>',whole,re.M)

receiver = re.findall(r'To:\s*"(.+?)"',whole,re.M)
remail = re.findall(r'To:\s*".+?"\s*<(\w+@\w+\..+?)>',whole,re.M)

date = re.findall(r'Date:\s*(.+?\d{1,2}\s*\w+\s*\d{2,4})',whole,re.M)
subject =re.findall(r'Subject:\s*(.*)',whole,re.M)
contact = re.findall(r'phone no:\s*(\d+)',whole,re.M)

print 'Names of the sender:', sender
print 'Emails of the sender:', semail
print 'Names of the receiver:', receiver
print 'Emails of the receiver:', remail
print 'Date when email was sent:', date
print 'Subject of the email:', subject
print 'Contact no of the sender:', contact

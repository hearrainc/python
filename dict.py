#!/usr/bin/python
#coding:utf-8

ab = {'cl':'chenlin0604@126.com'}

# Adding a key/value pair 
ab['Guido'] = 'guido@python.org'

# Deleting a key/value
del ab['Guido']

print '\nThere are %d contacts in the dict\n' % len(ab) 

for name, address in ab.items():
    print 'Contact %s at %s' % (name, address)
    
if 'cl' in ab: # OR ab.has_key('Guido') 
    print "\ncl's address is %s" % ab['cl']
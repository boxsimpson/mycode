#!/usr/bin/env python3
# Illustrated by Lashawn Simpson

## Create a Dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

## display parts of the dictionary
print( switch['hostname'] )
print( switch[ 'ip'] )

## request a 'fake' key
print( switch[ 'lynx'] )


## request a 'fake key with .get() method
print( "First test - .get()" )
switch.get('lynx')


print( "Second test - .get()" )
switch.get('lynx', "The KEY IS ANOTHER CASTLE!")

print( "Third test - .get()" )
switch.get('version')

print( "Fourth test - .keys()" )
switch.keys()

print( "Fifth test - .values()" )
switch.values()

print( "Sixth test - .pop" )
switch.pop('version') # removes this key ( and value) pair
switch.keys() # notice the value of version is gone
switch.values() # notice te value is 1.2

print( "Seventh test - ADD a new value" )
switch['adminlogin'] = 'kar108'
switch.keys()
switch.values()

print( "Eighth test - ADD a new value" )
switch['password'] = 'qwerety'
switch.keys()
switch.values()
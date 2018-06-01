#!/usr/bin/env python3
#Illustrated by Lashawn Simpson
from napalm import get_network_driver
#Function acts as guide to reach running drivers
def shawnsimp(xdrivecar,ysaddi,zplayer1,wcode): 
    driver = get_network_driver(xdrivecar)
    device = driver(ysaddi, zplayer1, wcode)
    device.open()
    return(device.get_config())
os = ['eos', 'junos', 'iosxr', 'nxos', 'nsox_ssh', 'ios'] #Only valid Devices put in list
x = ""
while x not in os:                                        #While loop created for correct drivers input
    x = input("What is the drivers name?")
#Input prompt for ip address
y = input("What is your ip address?")
#input prompt for username
z = input("What is the current username?")
#input prompt for password
w = input("Provide the password...")
# zconfig being set to function
zconfig = shawnsimp(x,y,z,w)
#printing running drivers
print(zconfig["running"])
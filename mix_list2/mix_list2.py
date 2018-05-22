#!/usr/bin/env python3
#Illustrated by Lashawn Simpson

proto = ['ssh', 'http', 'https']
print(proto)
print(proto[1])
proto.append('dns') # this will add 'dns' to our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # common ports
proto.extend(proto2)
print(proto)
proto.append(proto2)
print(proto)

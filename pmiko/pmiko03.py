#!/usr/bin/env python3
import paramiko
t = paramiko.Transport(('10.10.1.2', 22))
t.connect(username="john", password="alta3")
stfp = paramiko.SFTPClient.from_transport(t)
stfp.listdir()
sftp.put("test.txt", "new_test.txt")

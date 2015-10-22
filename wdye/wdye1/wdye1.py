# Imports Needed Libraries to run  Code
import pexpect
import sys
import os

# Creates Variables to be referenced by code
#
# Creates a variable named switch_ip and sets it to 10.0.0.2
switch_ip = "10.92.200.3"
# Creates a variable named switch_un and sets it to pytest
switch_un = "pytest"
# Creates a variable named switch_pw and sets it to pytest
switch_pw = "pytest"
# Creates a variable named enable_pw and sets it to password
enable_pw = "password"

# Creates Variable (child) for the SSH Session and Starts it.
# The SSH Session is created  from the  (switch_un) and (switch_ip) variables
# The %s@%s python code  is referencing  what folows %
# which is (switch_un, switch_ip)
# In a real life SSH connection it would look like this ssh switch_un@switch_ip
# Which would use the variables we created earlier and
# translate to ssh pytest@10.0.0.2
child = pexpect.spawn('ssh %s@%s' % (switch_un, switch_ip))
# Create a logfile of running code and
# drop it to Standard Out/screen unbuffered.
# We do this for debugging and status of script
child.logfile = os.fdopen(sys.stdout.fileno(), 'w', 0)
# Shows that the next prompt we expect from the SSH Session
# (child) is Password:
child.expect('Password:')
# We now send the varible switch_pw
child.sendline(switch_pw)
# Shows that the next prompt we expect from the SSH Session (child) is >
child.expect('>')
# We now send the IOS command terminal length 0
# to prevent potential need for user inputs
child.sendline('terminal length 0')
# Shows that the next prompt we expect from SSH Session (child) is >
child.expect('\>')
# We no send the IOS command enable
child.sendline('enable')
# Shows that the next prompt we expect from SSH Session (child) is Password
child.expect('Password:')
# We now send the variable (enable_pw)
child.sendline(enable_pw)
# Shows that the next prompt we expect  from SSH Session (child) is #
child.expect('#')
# We now send the IOS command conf t
child.sendline('conf t')
# Shows that the next prompt we expect  from SSH Session (child) is (config)#
child.expect('\(config\)#')
# We now send the IOS command end
child.sendline('end')
# Shows that the next prompt we expect from the SSH Session (child) is >
child.expect('#')
# We now send the IOS command  to quit which will terminate
# the SSH session (child) and end the program
child.sendline('quit')

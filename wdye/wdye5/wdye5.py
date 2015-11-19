# Imports Needed Libraries to run  Code
import pexpect
import sys
import os
#
# Creates Variables to be referenced by code
#
switch_un = "pytest"
switch_pw = "pytest"
enable_pw = "password"
vlan = "300"
vlan_name = "TESTVLAN"
switch_port = "GigabitEthernet0/10"
#
#
# Create a logfile
stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
# Create Import for Text file that contains Switch IP's
# Read the list to variable switches
# Create a for loop in which switch is the variable derived
# from a line of swtiches
with open('device_file1.txt') as fname:
    switches = fname.read().splitlines()
for switch in switches:
	#
	# This section shows the setup of the SSH session and
	# authentication through config T
	#
	print switch
	child = pexpect.spawn('ssh %s@%s' % (switch_un, switch))
	#
	# Drop logfile to Standard Out.
	child.logfile = stdout
#
	got_prompt = True
	try:
		child.expect('Password:')
	except pexpect.TIMEOUT:
		got_prompt = False
	if not got_prompt:
		print "%s failed" % (switch)
		continue
#
	child.sendline(switch_pw)
	child.expect('>')
	child.sendline('terminal length 0')
	child.expect('\>')
	child.sendline('enable')
	child.expect('Password:')
	child.sendline(enable_pw)
	child.expect('#')
	child.sendline('conf t')
	#
	# This section starts the configuration SNMP 
	child.expect('\(config\)#')
	child.sendline('no snmp-server community pycom ro')
	child.expect('\(config\)#')
	child.sendline('exit')
	#
	# This section starts the interface configuration
	#
	# Shows that the next prompt we exped from SSH session (child) is (#)
	#child.expect('#')
	
	# This section starts the termination of the session
	#
	#child.sendline('end')
	child.expect('#')
	child.sendline('wr mem')
	child.expect('#')
	child.sendline('quit')
	child.close()
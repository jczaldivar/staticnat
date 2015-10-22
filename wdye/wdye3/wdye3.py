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
with open('device_file.txt') as fname:
    switches = fname.read().splitlines()
for switch in switches:
	#
	# This section shows the setup of the SSH session and
	# authentication through config T
	#
	print switch
	child = pexpect.spawn('ssh %s@%s' % (switch_un, switch))
	# Drop logfile to Standard Out.
	child.logfile = stdout
	child.expect('Password:')
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
	# This section starts the configuration of VLAN 300
	#
	# Shows that the next prompt we expect from SSH Session (child) is (config)#
	child.expect('\(config\)#')
	#  We now send the IOS command VLAN 300
	child.sendline('%s %s' % ('vlan', vlan))
	# Shows that the next prompt we expect from SSH Session
	# (child) is (config-vlan)
	child.expect('\(config-vlan\)#')
	# We now send the IOS command name and send the variable vlan_name
	child.sendline('%s %s' % ('name', vlan_name))
	# Shows that the next prompt we expect from SSH Session (child) is (config)
	child.expect('\(config-vlan\)#')
	# We now send the IOS command exit
	child.sendline('exit')
	#
	# This section starts the interface configuration
	#
	# Shows that the next prompt we exped from SSH session (child) is (#)
	child.expect('#')
	# We now send the IOS command Interface and the variable switch_port
	child.sendline('%s %s' % ('interface', switch_port))
	# Shows that the next prompt we expect from SSH session (child) is (config-if)
	child.expect('\(config-if\)#')
	# We now send the IOS command Switchport Access vlan and the variable vlan
	child.sendline('%s %s %s %s' % ('switchport', 'access', 'vlan', vlan))
	# Shows that the next prompt we expect from SSH session (child) is (config-if)
	child.expect('\(config-if\)#')
	#
	# This section starts the termination of the session
	#
	child.sendline('end')
	child.expect('#')
	child.sendline('wr mem')
	child.expect('#')
	child.sendline('quit')
	child.close()
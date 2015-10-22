# Import required libraries
import os
#
# Open Text file with host list
with open('device_file1.txt') as fname:
# Set Variable Switches to read each line int file we opened	
    switches = fname.read().splitlines()
# Create a for loop named switch that iterates throug the lines in switches  
for switch in switches:
# Run a ping against the switch loop with 1 ping each
	response = os.system("ping -c 1 " + switch)
#
	#and then check the response and print is up or is down
	if response == 0:
	  print switch, 'is up!'
	else:
	  print switch, 'is down!'
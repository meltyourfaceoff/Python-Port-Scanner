
import socket
import sys

#Begin of input section
print ("==========================================================")
print ("=     Welcome to Kyle's wonderful port scanning tool!    =")
print ("=                                                        =")
print ("==========================================================")
print (" ")

inputType = input("Would you like to scan by host name or by IP?")

print (" ")

inputTypeStr = str(inputType)

if inputTypeStr in ['ip', 'IP', 'Ip', 'iP']:
	targetIP = input("Enter IP address you wish to scan:")
	
elif inputTypeStr in ['host', 'Host']:
	target = input("Enter host name you wish to scan:")
	targetIP = socket.gethostbyname(target)

else:
	print (" ")
	print ("*****please enter either host or IP*****")
	print (" ")
#End of Input Section

print (" ")
print ("Standby, we are scanning the assigned target")
print (" ")

#Begin section of actual port scanning code

try:
	for port in range(1,1024):
		mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = mysock.connect_ex((targetIP,port))
		if result == 0:
			print (('Port {}:   Open').format(port))
			mysock.close()
		#if result != 0:
			#print "Port {}:   Closed".format(port)
			#this is mostly for debugging to ensure it works
				
except KeyboardInterrupt:
	print ("Exiting!!")
	sys.exit()
	
	
except socket.gaierror:
	print ("HOSTNAME COULD NOT BE RESOLVED. LATER!")
	sys.exit()
	
except socket.error:
	print ("Could not connect")
	sys.exit()

#End of port scan section

print ("GOODBYE")


import optparse
from socket import *
from threading import *
import loremipsum

screenLock = Semaphore(value = 1)

def conn_scan(tgtHost, tgtPort):
	# Starts the connection
	try:
		connSkt = socket(AF_INET,SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send(loremipsum.generate_sentence(start_with_lorem=False))
		results = connSkt.recv(100)
		screenLock.acquire()
		print('[+]%d/tcp open' % tgtPort)
		print('[+]', str(results))
		connSkt.close()
	except Exception as e:
		screenLock.acquire()
		#print "Error: {0}".format(str(e))
		print('[-]%d/tcp open' % tgtPort)
	finally:
		screenLock.release()
		connSkt.close()

def port_scan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
		return

	try:
		tgtName = gethostbyaddr(tgtIP)
		print('\n[+]Scan Results for: ' + tgtName[0])
	except:
		print('\n[+]Scan Results for: ' + tgtIP)

	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target = conn_scan, args = (tgtHost, int(tgtPort)))
		t.start()

def main():
	parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] seperated by comma')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts == None):
		tgtHost = input(str("Enter your target here: "))
		tgtPorts = input("Enter your target ports here seperated by spaces: ")
		print(parser.usage)

	try:
		port_scan(tgtHost, tgtPorts)
	except Exception as e:
		print(parser.usage)

if __name__ == '__main__':
	main()
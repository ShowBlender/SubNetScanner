import subprocess
import os
subnet = raw_input("Please enter Subnet(Default is 192.168.0. for example):")
while True:
    # Check if the user presses enter for default
    if subnet == '':
        subnet = "192.168.0."
        break

print "Beginning scan of: ", subnet, "x"

with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 256):
                ipList = []
                ipList.append(subnet)

                quad = "{0}".format(n)
                ipList.append(quad)
                s = ''.join(ipList)
                #print s
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", s],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print s, "inactive"
                else:
                        print s, "active"

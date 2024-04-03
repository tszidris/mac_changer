import optparse
import re
import subprocess



def getInputs():

    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="choose your interface")
    parser.add_option("-m","--mac",dest="macAddress",help="give new mac address")

    return parser.parse_args()

def changeMac(sysInterface,sysMacAddress):

    subprocess.call(["ifconfig",sysInterface,"dows"])
    subprocess.call(["ifconfig",sysInterface,"hw","ether",sysMacAddress])
    subprocess.call(["ifconfig",sysInterface,"up"])

def control(interface):

    ifconfig = subprocess.check_output(["ifconfig",interface])
    newMac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if newMac:
        return newMac.group(0)


print("Operation Is Started")

(inputs,arguments) = getInputs()
changeMac(inputs.interface,inputs.macAddress)
newMac = control(str(inputs.interface))

if newMac == inputs.macAddress:
    print("Operation Successful")

else:
    print("Error!")






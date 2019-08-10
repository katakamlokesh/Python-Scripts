# programe for accepting inputs from user and creating container 
import subprocess
image = input ("enter the image name : ")
container = input (" enter the container name : ")
ports = input (" enter the port mapping : ")
detach = input (" Do you want to run in detach mode y/n: ")

if detach == 'y' :
    subprocess.call(" docker run --name %s -p %s %s "%(container,ports,image),shell=True)
elif detach == 'n' : 
     subprocess.call(" docker run --name %s -p %s %s "%(container,ports,image),shell=True)
else :
    print ("invalid option")

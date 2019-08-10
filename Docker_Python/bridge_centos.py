# creating multiple os containers and link with  multiple bridge network
import subprocess
i=1
while i<=5:

    subprocess.call("docker network create --driver bridge bridge0%d"%i,shell=True)
    subprocess.call("docker run --name c%d -it -d --network=bridge0%d centos"%(i,i),shell=True)
    i=i+1

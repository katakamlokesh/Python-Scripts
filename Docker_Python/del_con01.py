# deleting all containers whose name starts with same image name
import subprocess
subprocess.call('docker container ls | grep centos | cut -d" " -f1 > file1',shell=True) 
Containers = open('file1','r').readlines()
i=0
while i < len(Containers):
    cont_id = Containers[i]
    subprocess.call("docker rm -f %s"%cont_id,shell=True)
    i=i+1

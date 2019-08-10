# creating 10 containers at atime
import subprocess
i=1
while i<=10:
    subprocess.call("docker run --name container%d -d nginx"%i,shell=True)
    i=i+1

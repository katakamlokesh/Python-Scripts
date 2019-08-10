# creating tomcat container 
import subprocess
subprocess.call("docker run --name webserver -d -p 6060:8080 tomcat",shell=True)

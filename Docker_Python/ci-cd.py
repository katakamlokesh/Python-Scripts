import subprocess 
subprocess.call("docker run --name devserver -p 5050:8080 -d jenkins",shell=True)
subprocess.call("docker run --name qaserver -p 6060:8080 -d --link devserver:jenkins tomcat ",shell=True)
subprocess.call("docker run --name prodserver -p 7070:8080 -d --link devserver:jenkins tomcat",shell=True)

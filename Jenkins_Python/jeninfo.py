import jenkins

server = jenkins.Jenkins('http://localhost:8080','admin','admin')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' %(user,version) )

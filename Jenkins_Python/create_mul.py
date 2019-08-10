import jenkins
j= jenkins.Jenkins("http://localhost:8080","admin","admin")
i=1
while i <= 3 :
    j.create_job('develop-%d'%i,jenkins.EMPTY_CONFIG_XML)
    i=i+1

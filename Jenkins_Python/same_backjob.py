import jenkins
j = jenkins.Jenkins("http://localhost:8080","admin","admin")
i = 1 
while i <= 3 :
    j = jenkins.Jenkins("http://localhost:8080","admin","admin")
    j.copy_job('develop-%d'%i,'NewDev-%d'%i)
    i=i+1

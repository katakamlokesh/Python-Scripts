import jenkins
i=1
while i <= 3 :
    j= jenkins.Jenkins("http://localhost:8080","admin","admin")
    j.delete_job('develop-%d'%i)
    i=i+1

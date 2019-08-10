import jenkins
j= jenkins.Jenkins("http://localhost:8080","admin","admin")
i=1
while i <= 3 :
    j.build_job('develop-%d'%i)
    i=i+1

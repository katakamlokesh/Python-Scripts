import jenkins
j= jenkins.Jenkins("http://localhost:8080","admin","admin")
print (j.get_jobs( ))

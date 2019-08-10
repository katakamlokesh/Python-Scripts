import jenkins
j= jenkins.Jenkins("http://localhost:8080","admin","admin")
j.delete_job('myjob')

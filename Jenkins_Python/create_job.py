import jenkins
j= jenkins.Jenkins("http://localhost:8080","admin","admin")
j.create_job('myjob',jenkins.EMPTY_CONFIG_XML)

import jenkins
j= jenkins.Jenkins("http://localhost:8080","admin","admin")
job = raw_input("enter the job name:")
j.create_job('%s'%job,jenkins.EMPTY_CONFIG_XML)
j.build_job('%s'%job)
print('%s'%job)

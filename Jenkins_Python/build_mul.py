import jenkins
j = jenkins.Jenkins("http://localhost:8080","admin","admin")
items = ["Development","NewDev-1","Testing"]
i=0
while i < len(items):
    j.build_job('%s'%items[i])
    i=i+1

import jenkins
j = jenkins.Jenkins('http://localhost:8080','admin','admin')
j.build_job('Dev-02')

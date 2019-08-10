# deleting all stopped and running containers and images
import subprocess
subprocess.call("docker rm -f $(docker ps -aq)",shell=True)
subprocess.call("docker system prune -a ",shell=True)

import paramiko


def execute_ssh_command(host,username,passwd,cmd):
    ssh_client = None
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("Please wait,connecting the remote server")
        ssh_client.connect(hostname=host,username=username,password=passwd)
        print("Please wait executing command on remote server")

        stdin,stdout,stderr=ssh_client.exec_command(cmd, bufsize=-1, timeout=None, get_pty=False)
        print("Succesfully executed command on remote server")
        stdoutput=stdout.readlines()
        stderror=stderr.readlines()
        print("the output is : ")
        print(stdoutput)
        print("the error is : ")
        print(stderror)
        return(stdout,stderr)
    except:
        print("ssh is not connecting")
    finally:
        if ssh_client is not None:
            #close client connection
            ssh_client.close()

host = "172.31.87.197"
username = "ubuntu"
passwd = "ubuntu"
cmd = "sudo apt-get update"

ssh = execute_ssh_command(host,username,passwd,cmd)



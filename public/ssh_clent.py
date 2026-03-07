# -*- coding: utf-8 -*-
import os
import stat
import traceback

import paramiko

from public.logger import log


class SSH(object):

    def __init__(self, ip, timeout=30, *args, **kwargs):
        self.ip = ip
        self.port = kwargs.get("port", 8320)
        self.username = kwargs.get("username", "clog")
        self.password = kwargs.get("passwd", "Aqcp@Mc666_hzmcdba")
        print(f"ip:{self.ip}:port:{self.port}")
        print(f"username:{self.username}:password:{self.password}")
        self.ssh = paramiko.SSHClient()
        self.connect()

    def set_console(self, pwd):
        self.chan = self.ssh.invoke_shell()
        self.chan.send('su - console \n')  # 发送su 命令
        buff = ''
        while not (buff.endswith('Password: ') or buff.endswith('密码：')):
            resp = self.chan.recv(9999).decode()
            buff += resp
        print(buff)
        self.chan.send(f'{pwd}\n')  # 发送console 密码
        buff = ''
        while not buff.endswith('Enter your choice:'):
            resp = self.chan.recv(9999).decode()
            buff += resp
            print(resp)

    def set_capaa_after_root(self, pwd):
        self.chan.send('su - capaa \n')  # 发送su 命令
        buff = ''
        while not buff.endswith('[capaa@MCDCAP ~]$'):
            resp = self.chan.recv(9999).decode()
            buff += resp
            print(resp)

    def set_console_after_root(self, pwd):
        self.chan.send('su - console \n')  # 发送su 命令
        buff = ''
        while not buff.endswith('Enter your choice:'):
            resp = self.chan.recv(9999).decode()
            buff += resp
            print(resp)

    def set_root(self, root_password):
        self.chan = self.ssh.invoke_shell()
        self.chan.send('su - root \n')  # 发送su 命令
        buff = ''
        while not (buff.endswith('Password: ') or buff.endswith('密码：')):
            resp = self.chan.recv(9999).decode()
            print(resp)
            buff += resp
        self.chan.send('{}\n'.format(root_password))  # 发送root密码
        buff = ''
        while not buff.endswith('# '):
            resp = self.chan.recv(9999).decode()
            print(resp)
            buff += resp
        print("切换root 成功！！！")

    def exec_cmd_chan(self, cmd, stop, stop2="占位"):
        if cmd.endswith(".gpg"):
            self.chan.send("{}\r".format(cmd))
        else:
            self.chan.send("{}\n".format(cmd))
        buff = ''
        while not (stop in buff or stop2 in buff):
            resp = self.chan.recv(9999).decode()
            resp = resp.strip()
            buff += resp
            print(resp)
        return buff

    def chanel_exe_cmd(self, cmd, t=0.5):
        self.chan = self.ssh.invoke_shell()
        self.chan.send(cmd)
        self.chan.send("\n")
        time.sleep(t)
        resp = self.chan.recv(9999).decode("utf8")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("Exec sshCmd: %s" % (cmd))
        print("--------------------")
        print("Show Result: %s" % (resp))
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # print(resp)
        return resp

    def connect(self):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.ip, port=self.port,
                         username=self.username, password=self.password)

    def __del__(self):
        self.ssh.close()  # 断开ssh连接

    def execute_cmd(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        try:
            res, err = stdout.readlines(), stderr.readlines()
            result = res if res else err
            return [resu for resu in result]
        except Exception as e:
            print(e)
            res, err = stdout.read(), stderr.read()
            result = res if res else err
            return result

    def put_local_file_to_server(self, host=None, port=None, username=None,
                                 password=None, configfile=None,
                                 remotefile=None):
        transport = paramiko.Transport((host, port))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(configfile, remotefile)
        # 将remove_path 下载到本地 local_path
        # sftp.get('remove_path', 'local_path')
        transport.close()


if __name__ == '__main__':
    ss = SSH()
    log.info(ss.execute_cmd("ls -a ./"))

    # 切换root
    ss.set_root("HzMc#@!0571")

    # root 执行命令
    log.info(ss.exec_cmd_chan("whoami", "[root@MCDCAP ~]#"))

    # 原来用户执行命令 clog
    log.info(ss.execute_cmd("whoami"))

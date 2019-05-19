#!/usr/bin/env python3

import os
import json
import subprocess as subp

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def sftp():
	sftp_conf_path = os.getcwd() + '/conf/sftp.conf'
	
	sftp.server_ip = input(G + '[+]' + C + ' SFTP Server IP : ' + W)
	
	print(G + '[+]' + C + ' Reading SFTP Credentials from ' + W + sftp_conf_path)
	
	with open(sftp_conf_path) as sftp_conf:
		reader = sftp_conf.read()
		reader = reader.split(':')
		sftp.sftp_user = reader[0].strip()
		sftp.sftp_pass = reader[1].strip()

	print(G + '[+]' + C + ' Starting SFTP Server...' + W)
	distro = subp.Popen(['uname', '-r'], stdout = subp.PIPE)
	distro = distro.communicate()[0].decode()
	if 'ARCH' in distro:
		subp.call(['systemctl', 'start', 'sshd.service'])
	else:
		subp.call(['systemctl', 'start', 'ssh.service'])
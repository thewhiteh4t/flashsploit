#!/usr/bin/env python3

import os
import json
from modules.sftp import sftp

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def exfil(win):
	print('\n', end='')
	exfil_scripts = []
	for (dirpath, dirname, filenames) in os.walk('scripts/windows/exfil'):
		exfil_scripts.extend(filenames)
	for item in exfil_scripts:
		print(G + '[{}] '.format(exfil_scripts.index(item)) + C + item)
	
	while True:
		exfil_choice = input(G + '\nfs[windows/exfil] > ' + W)
				
		if exfil_choice == 'clear':
			os.system('clear')
		elif exfil_choice == 'back':
			return win()
		elif exfil_choice == 'help':
			return exfil(win)
		elif exfil_choice == '':
			pass
		elif exfil_choice == 'exit' or exfil_choice == 'quit':
			quit()
		elif int(exfil_choice) <= len(exfil_scripts) - 1:
			with open('conf/exfil_scripts.json', 'r') as json_file:
				options = json.load(json_file)
			try:
				chosen = exfil_scripts[int(exfil_choice)]
			
				for k,v in options.items():
					if k in chosen:
						sftp_state = v['sftp']
						msf_state = v['msf']
						desc = v['desc']
						print('\n', end = '')
						print(G + '[+]' + C + ' Script : ' + W + chosen + '\n')
						print(G + '[+]' + C + ' Info : ' + W + desc + '\n')
						if sftp_state == 1:
							sftp()
						else:
							pass
						if msf_state == 1:
							msf()
						else:
							pass
						script_path = '/scripts/windows/exfil/' + chosen
						exfil_output(script_path, chosen)
			except ValueError:
				pass
		else:
			print('\n' + R + '[-]' + C + ' Invalid Input...' + W)
			pass

def exfil_output(script_path, chosen):
	base_path = os.getcwd() + script_path

	with open(base_path, 'r') as file :
		filedata = file.read()

	filedata = filedata.replace('USERNAME', sftp.sftp_user)
	filedata = filedata.replace('PASSWORD', sftp.sftp_pass)
	filedata = filedata.replace('IPADDR', sftp.server_ip)

	with open('output/{}'.format(chosen), 'w') as file:
		file.write(filedata)

	outfile_path = os.getcwd() + '/output/{}'.format(chosen)
	
	print(G + '[+]' + C + ' Script Generated : ' + W + outfile_path)
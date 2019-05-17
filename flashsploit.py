#!/usr/bin/env python3

import os
import subprocess as subp
from modules.misc import misc
from modules.exfil import exfil
from modules.reverse_shell import rshell

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

version = '1.0.0'

def banner():
	os.system('clear')
	banner = r'''
    ______           __               __      _ __ 
   / __/ /___ ______/ /_  _________  / /___  (_) /_
  / /_/ / __ `/ ___/ __ \/ ___/ __ \/ / __ \/ / __/
 / __/ / /_/ (__  ) / / (__  ) /_/ / / /_/ / / /_  
/_/ /_/\__,_/____/_/ /_/____/ .___/_/\____/_/\__/  
                           /_/                     
'''
	print(G + banner + W)
	print(G + '[+]' + C + ' Created By : ' + W + 'thewhiteh4t')
	print(G + '[+]' + C + ' Version    : ' + W + version)

def main():
	print('\n' + G + '[+]' + C + ' Choose Target : ' + W + '\n')
	print(G + '[1]' + C + ' Windows' + W)
	while True:
		choice = input(G + '\nfs > ' + W)

		if choice == '1':
			win()
		elif choice == 'exit' or choice == 'quit':
			subp.call(['systemctl', 'stop', 'ssh.service'])
			subp.call(['pkill', 'php'])
			exit()
		else:
			print('\n' + R + '[-]' + C + ' Invalid Input...' + W)
			pass

def win():
	print('\n', end='')
	print(G + '[1]' + C + ' exfil' + W)
	print(G + '[2]' + C + ' reverse_shell' + W)
	print(G + '[3]' + C + ' misc' + W)
	
	while True:
		win_choice = input(G + '\nfs[windows] > ' + W)
		
		if win_choice == '1':
			exfil(win)
		elif win_choice == '2':
			rshell(win)
		elif win_choice == '3':
			misc(win)
		elif win_choice == 'clear':
			os.system('clear')
		elif win_choice == 'back':
			return main()
		elif win_choice == 'help':
			return win()
		elif win_choice == '':
			pass
		elif win_choice == 'exit' or win_choice == 'quit':
			subp.call(['systemctl', 'stop', 'ssh.service'])
			subp.call(['pkill', 'php'])
			exit()
		else:
			print('\n' + R + '[-]' + C + ' Invalid Input...' + W)
			pass

try:
	banner()
	main()
except KeyboardInterrupt:
	print(R + '[-]' + C + ' Keyboard Interrupt.' + W)
	subp.call(['systemctl', 'stop', 'ssh.service'])
	subp.call(['pkill', 'php'])

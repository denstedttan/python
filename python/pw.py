#! python3
# pw.py -A "secure" password locker.

""" this program is for compiling complex passwords 
 so that the user doesn't have to remember them
"""

PASSWORDS = {'email': 'F78shsh7388sdha7678gjhGJF567', 'blog':
			'SD78X87876df', 'luggage': '72653'}
	
import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()
	
account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print('There is no account named ' + account)

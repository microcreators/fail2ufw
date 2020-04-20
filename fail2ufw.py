#!/usr/bin/python3

import subprocess
import sys


# block ranges in the firewall
def block (what):
	cmd2 = 'sudo ufw insert 1 deny from ' + what + ' to any'
	print('Blocking: ' + what)
	p2 = subprocess.Popen(cmd2, shell=True)
	p2.wait()
	print('---')

# read command line args
if (len(sys.argv) != 3):
	print('Usage: fail2ufw.py <fail2ban jail name> <number of failed attempts>')
	sys.exit(0)
else:
	jail = str(sys.argv[1])
	badNumber = int(sys.argv[2])

# execute the check
cmd = 'sudo fail2ban-client status ' + jail + ' | grep Banned | cut -d ":" -f 2 | tr " " "\n" | tr -d "[:blank:]" | cut -d "." -f 1,2 | sort | uniq -c | sort -r -n | tr -s " "'

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
ips = p.stdout.readlines()
for line in ips:
	line = line.strip()
	ingrd = line.split()
	count = int(ingrd[0])
	range = str(ingrd[1])
	if (count >=  badNumber):
		block(range[2:-1] + '.0.0/16')
		sys.stdout.flush()

import subprocess

with open('Twitter_accounts.txt', 'r') as f:
	for line in f.readlines():
		subprocess.call('python twitter_get_user_timeline.py %s' % (line), shell=True)


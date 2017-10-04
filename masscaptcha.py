import requests
import random
import subprocess
import sys

def random_line(filename):
    with open(filename) as f:
        lines = [x.rstrip() for x in f.readlines()]
        return random.choice(lines)

with open("users.txt") as usersfile:
	users = [x.rstrip().split(" ") for x in usersfile.readlines()]

captcha = sys.argv[1]

for username, password, wifi_user, wifi_pass in users:

	subprocess.call(["sudo bash ./wifi.sh " + wifi_user + " " + wifi_pass + " &>/dev/null"], shell=True)

	session = requests.Session()
	session.trust_env = False
	
	credentials = {'ctl00$MainContent$Email':username, 'ctl00$MainContent$Password': password, 'ctl00$MainContent$captcha' : captcha}
	headers = {'User-Agent': random_line("useragents.txt")}
	
	#simulate normal behavior (first request the login page)
	session.get('https://catalog.inf.elte.hu/Account/Login')
	
	response = session.post('https://catalog.inf.elte.hu/Account/Login', data=credentials, headers=headers)

	if "logged in" in response.text:
		print "Successfully logged in " + str(username)





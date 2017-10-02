import requests
import random
import subprocess
import sys

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return line

with open("users.txt") as usersfile:
	users = [x.rstrip().split(" ") for x in usersfile.readlines()]

captcha = sys.argv[1]

for user in users:

	username = user[0]
	password = user[1]
	wifi_user = user[2]
	wifi_pass = user[3]

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





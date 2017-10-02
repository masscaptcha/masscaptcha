# masscaptcha
Log in a list of users from different mac+ip+user agent combinations

# Requirements

* Ubuntu/Debian
* `%sudo ALL=(ALL) NOPASSWD: ALL` if getting any permission errors (you shouldn't)

# Installation
`sudo bash install.sh`

# Usage

Enter credentials to `users.txt` in the following format `user pass wifi_user wifi_pass`

`sudo python masscaptcha.py ABCDEFG` (substitute the right captcha ofc)

import sys
import os
import subprocess

username = sys.argv[1]
password = sys.argv[2]
pub_key  = sys.argv[3]
pub_key = int(pub_key)
de_user  = []
de_pass  = []
user     = ""
passwd   = ""

print('Encrypted username = ' + username)
print('Encrypted password = ' + password)
print('RSA public key value = ' + str(pub_key))
print('RSA decryption has been started.....')
print('')

for p in range(1, pub_key):
	for i in range(0, len(username)):
		de_user.append(str((int(username[i])**p)%pub_key))
	for i in range(0, len(password)):
                de_pass.append(str((int(password[i])**p)%pub_key))
	user = ''.join(str(e) for e in de_user)
	passwd = ''.join(str(e) for e in de_pass)
	print('For decryption key = ' + str(p))
	print('username:' + user)
	print('password:' + passwd)
	print('')
	de_user = []
	de_pass = []
	command = 'curl -d "username=' + user + '&password=' + passwd + '" -X POST localhost:80/index.php > response; cat response | grep FLAG; rm response'
	print(command)
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print('')
	if "FLAG" in out:
		print('The FLAG has been found!!!')
		print('Decryption key is ' + str(p))
		break

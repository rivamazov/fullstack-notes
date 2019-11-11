10.10.10.75

Apache httpd 2.4.18 ((Ubuntu)

gobuster dir -u http://10.10.10.75 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster-2.3-medium.txt

http://10.10.10.75/nibbleblog/content/private/plugins/my_image/image.php

can be modified with a reverse shell

author="Diego Najar
<user username="admin">

admin
nibbles


user flag
b02ff32bb332deba49eeaed21152c8d8
root flag
b6d745c0dfb6457c55591efc898ef88c

[+] We can sudo without supplying a password!
Matching Defaults entries for nibbler on Nibbles:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User nibbler may run the following commands on Nibbles:
    (root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh

just make file execute /bin/sh


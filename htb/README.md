# HTB boxes
- [x] Lame
- [x] Beep
- [ ] Bastard
- [ ] Grandpa/Granny
- [ ] Mirai
- [ ] Solidstate
- [ ] Jeeves
- [ ] Tally (Much harder than anything on OSCP, but you've gotta get used to windows)
- [ ] Bashed
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

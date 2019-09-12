# Snort and UFW

### Snort Syntax

`[action] [proto] [srcIP] [srcPort] -> [destIP] [destPort] [(Options)]`

To check if snort is even working:

`alert tcp any any <> any any (msg:"snort";sid:9000)`

Let's say you want to catch all DNS requests originating from any internal IP address when the DNS server is at **192.168.1.4**

`alert udp 192.168.8.1/24 any -> 192.168.8.4 53 (msg:"DNSrequest detected!"; sid:1;)`

Now lets say that the Active Directory server on **192.168.8.64** is compromised and being scanned with `nmap -sT`

`alert tcp any 192.168.8.64 -> 192.168.8.4 22 (msg:”SSH activity detected!"; sid:2;)`

### UFW syntax

Here is an interesting firewall warning.
```
Aug 27 16:52:43.385439 unknown kernel: [UFW BLOCK] IN= OUT=eth0SRC=10.0.2.15 DST=1.1.1.1 LEN=95 TOS=0x00 PREC=0x00 TTL=64 ID=17221 DFPROTO=UDP SPT=46330 DPT=53 LEN=75
```
UFW command to whitelist this packet and allow DNS requests.

`ufw allow out on eth0 from 10.0.2.15 to 1.1.1.1 proto udp port 53`

And another
```
Aug 27 16:55:43.964640 unknown kernel: [UFW BLOCK] IN= OUT=eth0 SRC=10.0.2.15DST=172.217.9.228 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=1756 DF PROTO=TCPSPT=46764 DPT=443 WINDOW=29200 RES=0x00 SYN URGP=0
```
UFW command to allow ALL outbound HTTPS requests.

`ufw allow out on eth0 from 10.0.2.15 to any proto tcp port 443`



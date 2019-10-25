# Cyber

These are assorted notes from Fullstack curriculum. I have a much more organized and larger repo but it has PWK stuff in it so I can't make it public.

There are assorted scripts in the scripts folder. Otherwise it's really just markdown notes at the moment.

# Notes 

## Parsing Network Logs

### Print lines with the most common IP in them

To find all of the IP addresses in a file quickly use

`grep -Po "(\d+\.\d+\.\d+\.\d+)" <file>`

`-P` use Perl syntax ( for `\d` to function as decimal number)

`-o` Print only the matched (non-empty) parts of a matching line, with  each  such  part  on  a  separate output line.

Then to find the most common occurance in this case:

`grep -Po "(\d+\.\d+\.\d+\.\d+)" iptablesyslog | sort | uniq -c | sort -nr | head`

Here `sort` puts the redundant IPs in order allowing `uniq -c` to count the unique ones. This is not in order so another pipe to `sort -nr` for number and reverse respectively piped to `head` to see the first 10 lines.

```
   8629 11.11.79.67
   8201 11.11.79.110
   8117 11.11.79.105
   8041 11.11.79.100
   7980 11.11.79.80
   7915 11.11.79.85
   7810 11.11.79.87
   7632 11.11.79.69
   7623 11.11.79.90
   7494 11.11.79.120
```

Good times.

Then print all of the lines that this IP address occurs on:

 `grep 11.11.79.67 iptablesyslog`

## Log Reading
```
Aug  5 15:12:48 debian kernel: [ 2816.454036] [UFW AUDIT] IN=enp0s8 OUT= MAC=48:2e:7e:38:f4:51:88:77:11:e5:a4:28:08:00 SRC=192.168.56.3 DST=192.168.56.6 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=63825 DF PROTO=TCP SPT=48824 DPT=80 WINDOW=29200 RES=0x00 SYN URGP=0
Aug  5 15:12:49 debian kernel: [ 2818.245909] [UFW AUDIT] IN= OUT=enp0s8 SRC=192.168.56.6 DST=192.168.56.2 LEN=328 TOS=0x00 PREC=0x00 TTL=64 ID=55611 DF PROTO=UDP SPT=68 DPT=67 LEN=308
Aug  5 15:12:49 debian kernel: [ 2818.245918] [UFW BLOCK] IN= OUT=enp0s8 SRC=192.168.56.6 DST=192.168.56.2 LEN=328 TOS=0x00 PREC=0x00 TTL=64 ID=55611 DF PROTO=UDP SPT=68 DPT=67 LEN=308
Aug  5 15:13:08 debian kernel: [ 2836.585918] [UFW AUDIT] IN= OUT=enp0s8 SRC=192.168.56.6 DST=192.168.56.2 LEN=328 TOS=0x00 PREC=0x00 TTL=64 ID=55976 DF PROTO=UDP SPT=68 DPT=67 LEN=308
Aug  5 15:13:08 debian kernel: [ 2836.585926] [UFW BLOCK] IN= OUT=enp0s8 SRC=192.168.56.6 DST=192.168.56.2 LEN=328 TOS=0x00 PREC=0x00 TTL=64 ID=55976 DF PROTO=UDP SPT=68 DPT=67 LEN=308
Aug  5 15:13:10 debian kernel: [ 2838.795866] [UFW AUDIT] IN=enp0s8 OUT= MAC=48:2e:7e:38:f4:51:88:77:11:e5:a4:28:08:00 SRC=192.168.56.3 DST=192.168.56.6 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=26332 DF PROTO=TCP SPT=48852 DPT=80 WINDOW=29200 RES=0x00 SYN URGP=0
Aug  5 15:13:10 debian kernel: [ 2838.886422] [UFW AUDIT] IN=enp0s8 OUT= MAC=48:2e:7e:38:f4:51:88:77:11:e5:a4:28:08:00 SRC=192.168.56.3 DST=192.168.56.6 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=60755 DF PROTO=TCP SPT=48854 DPT=80 WINDOW=29200 RES=0x00 SYN URGP=0
Aug  5 15:13:10 debian kernel: [ 2838.887038] [UFW AUDIT] IN=enp0s8 OUT= MAC=48:2e:7e:38:f4:51:88:77:11:e5:a4:28:08:00 SRC=192.168.56.3 DST=192.168.56.6 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=32790 DF PROTO=TCP SPT=48856 DPT=80 WINDOW=29200 RES=0x00 SYN URGP=0
```

- OS and network device
  - OS is linux ufw on enp0s8 and host IP is 192.168.56.6

- What is each line saying
  1. creator of log .6 recieves tcp data on port 80 from .3 implying a webserver on .6.
  2. .6 sends UDP data on source port 67 to dest port 68 on .2 which implies DHCP client to server request.
  3. ufw says it does not have a rule for this packet so blocks the packet
     - ufw is block all by default. 
  4. .6 tries again
  5. Is blocked again
  6. .3 continues to talk to .6 on port 80.
- Is this normal or malicious?
  - normal

```
Aug  5 16:27:23 debian kernel: [ 3535.868836] [UFW AUDIT] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=36914 DF PROTO=TCP SPT=45734 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:27:23 debian kernel: [ 3535.868842] [UFW BLOCK] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=36914 DF PROTO=TCP SPT=45734 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:27:31 debian kernel: [ 3544.237326] [UFW AUDIT] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=55203 DF PROTO=TCP SPT=45736 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:27:31 debian kernel: [ 3544.237332] [UFW BLOCK] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=55203 DF PROTO=TCP SPT=45736 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:27:57 debian kernel: [ 3570.390818] [UFW AUDIT] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=45455 DF PROTO=TCP SPT=45742 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:27:57 debian kernel: [ 3570.390826] [UFW BLOCK] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=45455 DF PROTO=TCP SPT=45742 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:28:12 debian kernel: [ 3584.699296] [UFW AUDIT] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=742 DF PROTO=TCP SPT=45744 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
Aug  5 16:28:12 debian kernel: [ 3584.699304] [UFW BLOCK] IN= OUT=enp0s3 SRC=10.0.2.15 DST=104.193.19.59 LEN=60 TOS=0x00 PREC=0x00 TTL=64 ID=742 DF PROTO=TCP SPT=45744 DPT=1337 WINDOW=29200 RES=0x00 SYN URGP=0 
```

1. OS and network device that generated
   - 10.0.2.15 is generating ufw logs
2. What does the log say
   - 10.0.2.15 is repeatedly attempting to connect to 104.193.19.59 on port 1337
   - each attempt it blocked because there is a ufw rule for outbound 1337 tcp connections.
3. Normal or malicious
   - clearly malicious

```
2019-08-05 16:42:33 ALLOW UDP 192.168.56.7 224.0.0.251 5353 5353 0 - - - - - - - SEND
2019-08-05 16:42:33 ALLOW UDP 192.168.56.7 192.168.56.255 137 137 0 - - - - - - - SEND
2019-08-05 16:42:39 ALLOW ICMP 192.168.56.7 192.168.56.2 - - 0 - - - - 8 0 - SEND
2019-08-05 16:42:40 ALLOW ICMP 192.168.56.7 192.168.56.2 - - 0 - - - - 8 0 - SEND
2019-08-05 16:42:41 ALLOW ICMP 192.168.56.7 192.168.56.2 - - 0 - - - - 8 0 - SEND
2019-08-05 16:42:42 ALLOW ICMP 192.168.56.7 192.168.56.2 - - 0 - - - - 8 0 - SEND
2019-08-05 16:42:47 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:48 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:49 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:50 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:51 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:42:52 DROP ICMP 192.168.56.3 192.168.56.7 - - 84 - - - - 8 0 - RECEIVE
2019-08-05 16:43:01 ALLOW ICMP ::1 ff02::16 - - 0 - - - - 143 0 - SEND
2019-08-05 16:43:01 ALLOW 2 127.0.0.1 224.0.0.22 - - 0 - - - - - - - SEND
2019-08-05 16:43:01 ALLOW UDP 127.0.0.1 239.255.255.250 63778 1900 0 - - - - - - - SEND
2019-08-05 16:43:01 ALLOW UDP 127.0.0.1 239.255.255.250 63778 1900 0 - - - - - - - RECEIVE
2019-08-05 16:43:16 ALLOW ICMP 192.168.56.7 192.168.56.3 - - 0 - - - - 8 0 - SEND
2019-08-05 16:43:17 ALLOW ICMP 192.168.56.7 192.168.56.3 - - 0 - - - - 8 0 - SEND
2019-08-05 16:43:18 ALLOW ICMP 192.168.56.7 192.168.56.3 - - 0 - - - - 8 0 - SEND
2019-08-05 16:43:19 ALLOW ICMP 192.168.56.7 192.168.56.3 - - 0 - - - - 8 0 - SEND
```
1. OS and network device that generated
   1. Windows firewall
2. What is each log saying
   1. blocking incoming ICMPs which is default behaviour on windows firewall
3. Which logs are normal v malicious
   1. this is normal# Snort and UFW

## Snort Syntax

`[action] [proto] [srcIP] [srcPort] -> [destIP] [destPort] [(Options)]`

To check if snort is even working:

`alert tcp any any <> any any (msg:"snort";sid:9000)`

Let's say you want to catch all DNS requests originating from any internal IP address when the DNS server is at **192.168.1.4**

`alert udp 192.168.8.1/24 any -> 192.168.8.4 53 (msg:"DNSrequest detected!"; sid:1;)`

Now lets say that the Active Directory server on **192.168.8.64** is compromised and being scanned with `nmap -sT`

`alert tcp any 192.168.8.64 -> 192.168.8.4 22 (msg:”SSH activity detected!"; sid:2;)`

## UFW syntax

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




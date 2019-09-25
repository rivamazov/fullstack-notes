# Parsing Network Logs

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




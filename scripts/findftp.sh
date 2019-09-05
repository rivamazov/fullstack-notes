cut -d';' -f3,6 log.txt | grep ';21$' | cut -d';' -f1 | sort | uniq -c | sort -r | head

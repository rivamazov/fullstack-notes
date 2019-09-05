# Splunk

- index=* ERROR date_hour=10 | stats count
- `sudo /opt/splunk/bin/splunk start`
- https://samsclass.info/152/proj/p7bots.htm
- index=botsv1 imreallynotbatman.com | stats count by src_ip
- index=botsv1 imreallynotbatman.com src=40.80.148.42 sourcetype=suricata signature='*' | stats count by signature
- signature field is the message

// TODO look up windows process enumeration


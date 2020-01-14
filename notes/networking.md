# view listening ports with process
ss -tlnup | grep 1234

# with processes

# port forward local->remote
ssh -p 12344 -L 444:0:5900 user@domain

# vnc through a jumpbox
socat -d -d -d -v EXEC:'ssh -A ${JUMPBOX} "ssh -t ${TARGET} -W127.0.0.1:5900"' TCP-LISTEN:1234,bind=127.0.0.1,reuseaddr,fork

# look at the last commands
tail -f terminal.txt

# look for installed packages
dpkg -l | grep vnc

# tunnel port 80 through ssh
ncat -l localhost 8080 --sh-exec "ncat webserver 80"

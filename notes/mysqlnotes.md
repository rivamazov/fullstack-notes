# MySQL

### Installing on ubuntu 19.10

- `sudo apt install mysql-server`
- after install `sudo mysql_secure_installation utility`

### basics

- `show databases;`
- `USE <dbname>;`
- now you can `SHOW TABLES;`
- next `DESCRIBE table` 
- `mysqlcheck fo1`
- `mysqlcheck -r fo1` *-r* for repair.

### backing up a database

- `mysqldump [database] > /tmp/[backupfilename]`
- `mysql [databasename] < /tmp/[backupfilename]`

### copying a database as files

- as root:
- `service stop mysql`
- copy mysql folder to `/var/lib/mysql` ubuntu basedir
- make sure to `chown mysql /var/lib/mysql` or else the service will not start.
- `service start mysql`


### Examples
- `SELECT TicketNumber FROM inventory;` shows all ticketNumbers
- `SELECT TicketNumber FROM inventory WHERE Status = 2;` shows all closed tickets (1 being open tickets)
-	`mysql -e "SELECT TicketNumber, enterTime, exitTime, creationIdLocation, creationIdPosition, creationIdrecordNumber, status FROM Fo1.inventory WHERE Ticketnumber = "897920";"` how to get a specific ticket straight from a shell. 

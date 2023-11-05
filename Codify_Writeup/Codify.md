![](assets/images/banner.png)

<img src="./assets/images/htb.png" style="margin-left: 20px; zoom: 60%;" align=left /> <font size="10">Codify</font>

​ 11<sup>th</sup> November 2023

​ Machine Author(s): kavigihan
<br>
Prepared by: demotedc0der

​

### Difficulty: `Easy`

<br>

# Enumeration

Let's run Nmap to discover any open ports on the remote host (using the proper options):

<img src="./assets/images/capture0.JPG" />

Wappalyzer is a great extension to show all the technologies used on the WebApp.

<img src="./assets/images/capture3.JPG" />

<br>

# Foothold

There's a simple code editor where it executes Node.js code.

<img src="./assets/images/capture1.JPG" />

There technically exists a vulnerability in the exception sanitization of vm2, which can be used to escape the sandbox and run arbitrary code in the host context.

<img src="./assets/images/capture2.JPG" />

<img src="./assets/images/capture01.JPG" />

<br>

# Rev Shell

We successfully got the shell as user svc.

<img src="./assets/images/capture4.JPG" />

<br>

# Lateral Movement

Move to the /var/www/contact directory, and we can find the 'tickets.db' file.

<img src="./assets/images/capture5.JPG" />

Copy this file to the local host and use sqlitebrowser to read the DB.

<img src="./assets/images/capture6.JPG" />

Use John to dehash it.

<img src="./assets/images/capture7.JPG" />

Login as Joshua using SSH, and the user flag can be obtained at /home/joshua.

<img src="./assets/images/capture8.JPG" />

<br>

# Privilege Escalation

<img src="./assets/images/capture9.JPG" />

The conditional statement is the part where things get interesting.
It can be easily manipulated to make it true.

<img src="./assets/images/capture10.JPG" />

<br>

Create 2 SSH sessions, in one execute <b>./pspy32 -f</b> (-f option to see the actions of processes) and in the second one execute the script as sudo <b>sudo /opt/scripts/mysql_backup.sh</b>

<img src="./assets/images/capture11.JPG" />

<img src="./assets/images/capture12.JPG" />

So the tricky thing here is to enter \* (asterisk) so that $DB_PASS matches with it and eventually is true.

<img src="./assets/images/capture13.JPG" />

Check out the pspy's output, and from there, you can see a command is executed, -p specify the password. Use that password to log in as root.

<img src="./assets/images/capture14.JPG" />

<br>

...and voilààà we have a root shell.

<img src="./assets/images/capture15.JPG" />

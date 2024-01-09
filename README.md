# project1

Jan 7 2024

file_system6.py

"file_system6.py" runs on Linux (Ubuntu or Kali) and needs sudo privileges.

to run the program, type:      

sudo python3 file_system6.py

This program is a file explorer for Linux.  It has basic functionality such as viewing and writing files, changing directories as well as querying and downloading from an LDAP directory and more.

This was a project for an Operating Systems class in Fall 2022.  I wrote the program "file_system6.py" myself. The objective of the project was to write a file system program with LDAP functionality, with the ability to download files from an LDAP server. Upload as well as Encryption will be added using LDAPS. Updates coming to logging system as well.

I tested the LDAP functionality with the following site:  

https://www.forumsys.com/2022/05/10/online-ldap-test-server/

address: ldap.forumsys.com

port: 389

username: euclid

password: password

You can also download a VM from the following site to test the program:

https://www.turnkeylinux.org/openldap


sslserver

The program "sslserver" was an another part of the same project where I combined my logging system from "file_system" with my partners' SSL socket.  The sslsocket's client was meant to be combined with "file_system6.py".  My partners wrote the "client" and I assisted with the "sslserver". However, we ran out of time that semester and did not finally combine the programs.  One of the problems we had is that with the "sslserver" and "client", we could only get them to run in Windows; also we had difficulty using LDAP, so a socket was used instead.

Abraham Alayon


# File System with LDAP

A Python program that simulates a file system with LDAP functionality.

## Description

This program allows you to create, modify, and delete files and directories in a virtual file system. You can also navigate through the file system using commands such as cd, ls, pwd, etc. The program also allows you to query and download files from an LDAP server using commands such as ldapsearch, ldapdownload, etc.

## Installation

To install and run this program, you need to have Python 3 installed on your system. You can download Python 3 from [here]. You also need to clone this repository to your local machine using the following command:

```bash
git clone https://github.com/abrahamalayon/project1.git
```

Then, you need to run the program with sudo privileges, as it needs to access the system files and directories. You can do that by executing the file_system6.py file:

```bash
sudo python3 file_system6.py
```

## Usage



Examples of LDAP syntax are below.  For example, the search base may be "dc=example,dc=com" when prompted for search base.  :

- `ldapsearch <base> <filter>`: Searches for entries in the LDAP server that match the given base and filter. The base is the starting point of the search, and the filter is the criteria for selecting entries. For example, `ldapsearch "dc=example,dc=com" "(objectClass=person)"` will search for all entries that are persons in the example.com domain.
- `ldapdownload <base> <filter> <file>`: Downloads a file from the LDAP server that matches the given base and filter, and saves it to the file system with the given name. The base and filter are the same as in the ldapsearch command. For example, `ldapdownload "dc=example,dc=com" "(cn=alice)" alice.txt` will download the file associated with the entry that has the common name alice in the example.com domain, and save it as alice.txt in the file system.

You can test the LDAP functionality with the following site:

https://www.forumsys.com/2022/05/10/online-ldap-test-server/

address: ldap.forumsys.com

port: 389

username: euclid

password: password

You can also download a VM from the following site to test the program:

https://www.turnkeylinux.org/openldap

## License

This project is licensed under the MIT License. See the [LICENSE] file for more details.

## Contributing

This project is open for contributions. If you want to contribute, please follow these steps:

- Fork this repository and clone it to your local machine.
- Create a new branch with a descriptive name
- Make your changes and commit them with a clear message
- Push your branch to your forked repository
- Create a pull request to the original repository
- Wait for feedback and approval

## Credits

This project was created by Abraham Alayon. The file_system6.py program was written by Abraham Alayon. The project was based on the specifications and requirements of the Operating Systems class.

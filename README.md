# Firewall
## Punch a hole into an AWS EC2 security group temporarily
Temporarily allow access to your current IP address into security groups, and automatically closes the hole when quitting. Convenient for SSH-ing into a box from a home or from any off-site location without worrying about leaving SSH open to the world or dealing with VPN.

![](http://i.imgur.com/JcyWU.png)

### Installation
`$ pip install firewall`

### Setup
`$ firewall --configure`

### Usage
```
$ firewall production-web -p 22,8080  # Open up ports 22 and 8080
$ firewall production-web,production-db  # Open up port 22 (default)
```
```
Usage: firewall [SECURITY GROUP][,SECURITY GROUP]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -p PORTS, --ports=PORTS
                        Comma-separated list of ports to open
  -i CONFIG             Path to configuration file
  --configure           Run initial setup
```

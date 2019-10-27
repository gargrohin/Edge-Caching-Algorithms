#!/bin/bash

systemctl stop squid
rm -r /var/spool/squid
apt remove -y squid && apt install squid
systemctl stop squid
ls /var/spool/squid
cat /etc/squid/squid.conf
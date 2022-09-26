#!/bin/bash
set -x

###################
# Clear All Conf.
###################
sudo iptables -F

###################
# Common
###################
# lo
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT

# Extablished
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

###################
# INPUT
###################
sudo iptables -A INPUT -i eth0 -j DROP
#sudo iptables -P INPUT -i eth0 -j DROP

###################
# FORWARD
###################
sudo iptables -A FORWARD -i eth0 -j DROP
#sudo iptables -P FORWARD -i eth0 -j DROP

###################
# OUTPUT (etho)
###################
# Gateway
sudo iptables -A OUTPUT -d 15.26.228.1 -o eth0 -j ACCEPT
# Proxy 
sudo iptables -A OUTPUT -d 15.89.14.62 -o eth0 -j ACCEPT
# DNS
sudo iptables -A OUTPUT -d 15.26.197.15 -o eth0 -j ACCEPT
sudo iptables -A OUTPUT -d 15.64.64.53 -o eth0 -j ACCEPT
# Others
sudo iptables -P OUTPUT -o eth0 -j DROP

###################
# OUTPUT (wlan0)
###################
# apt-get update
sudo iptables -A OUTPUT -d 185.125.190.36 -o wlan0 -j DROP

###################
# List Up
###################
#sudo iptables -L
sudo iptables -L -v

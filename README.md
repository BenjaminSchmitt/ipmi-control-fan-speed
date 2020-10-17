# ipmi-control-fan-speed
Simple tweakable python3 script to change fan speed of your server based on temperature, using IPMI.

# Why ?
Servers are designed to run in rooms where noise is not an issue: they want to be as cold as possible, 
using high air flow and high fan speed. In a homelab, noise can be annoying, even more if you don't have a 
dedicated room for your stuff! Reducing the fan speed of your server can then mitigate your pain.

# Warning: use it at your own risk
Be careful when changing fan speed: temperatures can increase rapidly depending on your workload. Don't forget to monitor 
them.
The default values are working well for my setup (see below), but might not be the best for yours, depending on your 
workload and your hardware.

## Hardware 
I developed this script for my Dell PowerEdge R720 (2* Xeon E5-2650 v2), running Proxmox VE and between 8 and 12 
virtual machines. It is most of the time idle, since the services are only exposed on LAN. 

# Prerequisites
Ipmitool installed: https://github.com/ipmitool/ipmitool (`sudo apt install ipmitool` on debian and ubuntu)

# Base process
Process (can be easily changed):
- if temperature is under 40 celsius degrees (threshold 1), set fan speed at 15%
- if temperature is under 45 celsius degrees (threshold 2), set fan speed at 20%
- else, let the OS manage the fan speed (auto mode)

# Files
- credentials.py is where you have to put the IP of your remote controller, your username and your password
- main.py is an infinite loop, for changing fan speed every 60 seconds
- set-fan-speed.py helps you to set the fan speed you want, between 0% (be careful!) and 100%
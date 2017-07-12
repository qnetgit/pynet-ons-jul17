#!/usr/bin/env python
from __future__ import print_function

net_device = {
    'ip_addr': '169.254.255.1',
    'username': 'admin',
    'password': 'somepass',
    'vendor': 'juniper',
    'model': 'QFX5100-24Q'
}

print()
for k, v in net_device.items():
    print(k, v)

net_device['password'] = 'new_value'
net_device['secret'] = 'some_secret'

device_type = net_device.get('device_type', 'juniper')
print("\nDefault device type: {}\n".format(device_type))
 
try:
    device_type = net_device['device_type']
except KeyError:
    print("Device type not found\n")

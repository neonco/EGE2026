from ipaddress import ip_network

for ip in ip_network('146.180.173.153/255.192.0.0', 0):
    print(ip)

print(146+191+255+254)
# 146.191.255.254
# 846
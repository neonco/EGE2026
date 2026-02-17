from ipaddress import ip_network

for ip in ip_network('190.202.83.62/255.255.252.0', 0):
    print(ip)

print(190+202+83+254)
from ipaddress import ip_network

for ip in ip_network('46.29.170.214/17', 0):
    print(ip)

print(255-29-46)

# 46.29.255.180
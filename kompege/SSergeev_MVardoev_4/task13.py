from ipaddress import ip_network

count = 0
for ip in ip_network('215.124.54.164/255.255.255.240', 0):
    ip = f'{ip:b}'
    if ip.count('0') > 13:
        count += 1
        print(ip, count)



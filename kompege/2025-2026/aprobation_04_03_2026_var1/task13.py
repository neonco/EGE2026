from ipaddress import ip_network

res = 0
for ip in ip_network('172.16.96.0/19', 0):
    b = f'{ip:b}'
    if b.count('1') % 2 == 0:
        res += 1
        print(b, ip)

print(res)
print(2**13//2)
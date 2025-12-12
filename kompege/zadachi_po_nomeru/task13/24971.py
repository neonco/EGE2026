from ipaddress import ip_network

for ip in ip_network('111.222.0.124/255.255.224.0', False):
    # print(ip)
    b = f'{ip:b}'
    if (b.count('0') * b.count('1')) % 2 == 1:
        print(ip)

# 111.222.31.252
print(111+222+31+252)
# 616, но в ответе неправильно, там 619, используется широковещательный адрес 111.222.31.255
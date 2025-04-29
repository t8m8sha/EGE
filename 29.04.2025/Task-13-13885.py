from ipaddress import ip_network

mask = '238.51.1.202'

for A in range(256)[::-1]:
    net = ip_network()
    if all(f'{int(ip):032b}'[:16].count('1') >= f'{int(ip):032b}'[16:].count('1') for ip in net):
        print(A)
        break


from ipaddress import ip_network, ip_address

ip_net = ip_address('238.51.1.202')

for mask in range(16, 24):
    net = ip_network(f'{ip_net}/{mask}', False)

    if all(f'{int(ip):032b}'[:16].count('1') <= f'{int(ip):032b}'[16:].count('1') for ip in net):
        res_mask = str(net.netmask).split('.')
        print(res_mask[2])
        brea
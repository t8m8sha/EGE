from ipaddress import ip_network,ip_address


ip1 = ip_address('157.127.182.76')
ip2 = ip_address('157.127.190.80')

for mask in range(33):
    net1 = ip_network(f'{ip1}/{mask}',False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1.network_address == net2.network_address:
        print(mask)
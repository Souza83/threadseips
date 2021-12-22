import ipaddress  # Importa a biblioteca ipaddress

#########################################################
# Imprime endereço ip
ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print('\n O ip é: ', endereco)
#########################################################
# Imprime endereço ip com a quantidade de ips informado
ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print('\n O endereço final para 257 ips é: ', endereco + 257)
#########################################################
# Imprime endereço ip da mascara de rede informada
ip = '192.168.0.0/24'

rede = ipaddress.ip_network(ip)

print('\n A rede é: ', rede)
#########################################################
# Imprime rede informada, indiferente do ip informado
ip = '192.168.0.100/16'

rede = ipaddress.ip_network(ip, strict=False)

print('\n A rede para o ip 192.168.0.100 é: ', rede)
#########################################################
# Imprime os endereços da rede e mascara informada
ip = '192.168.0.0/24'

rede = ipaddress.ip_network(ip, strict=False)

print('\n Os IPs da rede {} são:'.format(rede))

for ip in rede:
    print('\n {}'.format(ip))
#########################################################
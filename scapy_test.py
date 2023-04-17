# criar venv (opcional, mas recomendado) e instalar o scapy
# sudo apt-get scapy
# para rodar: sudo python3 scapy_test.py

from scapy.all import *

# Define o pacote IP com um cabeçalho TCP
pkt = IP(src="192.168.0.1", dst="8.8.8.8")/TCP(sport=1234, dport=80)

# Envia o pacote
send(pkt)


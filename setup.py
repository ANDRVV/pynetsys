from setuptools import setup
from pip._internal.req import parse_requirements
import os, codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

install_reqs = parse_requirements('requirements.txt', session=False)
dependencies = [str(ir) for ir in install_reqs]

VERSION = "0.0.2"
DESCRIPTION = "pynetsys is a collection of tools and malicious packets."

setup(
    name="pynetsys",
    version=VERSION,
    url="https://github.com/ANDRVV/pynetsys",
    author="Andrea Vaccaro (ANDRVV)",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages= ["pynetsys"],
    license= "BSD 3 License",
    keywords=["python", "socket", "threading", "server", "client", "packet", "packets", "net", "network", "wireless", "dos", "tools", "tool", "traceroute", "arp", "tracert", "arping", "nslookup"],
    install_reqs = dependencies
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"]
    )

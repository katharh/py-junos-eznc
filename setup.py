import os
import sys

sys.path.insert(0,'lib')
from setuptools import setup, find_packages

setup(
    name = "junos-eznc",
    version = "0.0.1",
    author = "Jeremy Schulman",
    author_email = "jschulman@juniper.net",
    description = ( "Junos automation for non-programmers" ),
    license = "BSD-2",
    keywords = "Junos NETCONF networking automation",
    url = "http://www.github.com/jeremyschulman/py-junos-eznc",
    package_dir={'':'lib'},    
    packages=find_packages('lib'),
    install_requires=[
        "netaddr",
        "lxml",
        "jinja2",
        "scp"
    ],
)

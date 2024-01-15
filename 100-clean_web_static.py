#!/usr/bin/python3
"""defines a module that  that deletes out-of-date archives,
    using the function do_clean:"""

from fabric.api import *
import os.path

env.hosts = ['100.26.173.252', '54.160.114.174']
env.user = "ubuntu"
env.key_filename = "my_ssh_private_key"


def do_clean(number=0):
    """Deletes old archives"""
	local("ls -ltr | cut -d' ' -f4")

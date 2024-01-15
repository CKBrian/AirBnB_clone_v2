#!/usr/bin/python3
"""defines a module that  that deletes out-of-date archives,
    using the function do_clean:"""

from fabric.api import *
from fabric.state import *
import os

env.hosts = ['100.26.173.252', '54.160.114.174']
env.user = "ubuntu"
env.key_filename = "my_ssh_private_key"


def do_clean(number=0):
    """Deletes old archives"""
    local('ls -t ~/AirBnB_Clone_V2/versions/').split()
    with cd("/data/web_static/releases"):
        magic = sudo("ls -t .").split()
    paths = "/data/web_static/releases"
    number = int(number)
    if number == 0:
        num = 1
    else:
        num = number
    if len(magic) > 0:
        if len(target) == number or len(target) == 0:
            pass
        else:
            cl = target[num:]
            for i in range(len(cl)):
                local('rm -f ~/AirBnB_Clone_V2/versions/{}'.format(target[-1]))
        rem = magic[num:]
        for j in range(len(rem)):
            sudo('rm -rf {}/{}'.format(paths, rem[-1].strip(".tgz")))

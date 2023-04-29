#!/usr/bin/python3
# Compress before sending
from fabric.api import local
from datetime import datetime


def do_pack():
    """ generates a .tgz archive """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    my_tar = "versions/web_static_{}.tgz".format(date)
    try:
        local("tar -czvf {} web_static".format(my_tar))
        return my_tar
    except:
        return None

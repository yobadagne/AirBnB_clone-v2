#!/usr/bin/python3
# 3. Full deployment
from fabric.api import *
from datetime import datetime
import os
env.hosts = ['54.237.113.148', '54.173.69.37']


def deploy():
    """ creates and distributes an archive """
    try:
        archive_path = do_pack()
    except:
        return False
    return do_deploy(archive_path)


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


def do_deploy(archive_path):
    """ distributes an archive """
    if not os.path.exists(archive_path):
        return False
    try:
        arg = archive_path.split("/")
        folder = arg[0]
        archive = arg[1]
        arch = os.path.splitext(arg[1])
        filename = arch[0]
        extension = arch[1]
        releases = "/data/web_static/releases/"
        current = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}{}/".format(releases, filename))
        run("sudo tar -xzf /tmp/{} -C {}{}/".
            format(archive, releases, filename))
        run("sudo rm /tmp/{}".format(archive))
        run("sudo mv {}{}/web_static/* {}{}/".
            format(releases, filename, releases, filename))
        run("sudo rm -rf {}{}/web_static".format(releases, filename))
        run("sudo rm -rf {}".format(current))
        run("sudo ln -s {}{}/ {}".format(releases, filename, current))
        return True
    except:
        return False

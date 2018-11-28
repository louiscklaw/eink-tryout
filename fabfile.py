#!/usr/bin/env python
# don't generate pyc files
import sys
sys.dont_write_bytecode = True


from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.project import *

WKDIR=['./epd-library-python','~']

def threaded_local(command):
    local(command, capture=True)


def helloworld():
    # p.map(threaded_local,['id'])
    put(WKDIR[0], WKDIR[1])
    with cd('/home/pi/epd-library-python/1.54inch_e-paper_c/raspberrypi/python'):
        run('python main.py')

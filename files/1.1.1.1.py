#!/usr/bin/python
from subprocess import call

def remove_cramfs():
    call(["rmmod", "cramfs"])

if __name__ == "__main__":
    remove_cramfs()

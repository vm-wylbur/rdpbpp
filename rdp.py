#!/usr/bin/env python3
#
# Authors:     PB
# Maintainers: PB
# Copyright:   2017, HRDAG, GPL v2 or later
# ============================================
# rdpbpp/rdp/rdp.py

import argparse
import filelock
from collections import namedtuple


def init_all(tag="rdpbpp"):
    args = get_lock(tag)
    init_lock(args)
    return args


def get_lock(tag="rdpbpp"):
    lock = filelock.FileLock("/tmp/{}.lock".format(tag))
    fname = "/tmp/{}".format(tag)
    Args = namedtuple('Args', ['tag', 'lock', 'fname'])
    return Args(tag, lock, fname)


def init_lock(args):
    with args.lock:
        with open(args.fname, 'wt') as intfile:
            intfile.write("0\n")


def incr_lock(args):
    with args.lock:
        with open(args.fname, 'rt') as intfile:
            rdpint = int(intfile.read().strip())
        rdpint += 1
        with open(args.fname, 'wt') as intfile:
            intfile.write("{}\n".format(rdpint))
    return rdpint


def get_next_line(args, filename):
    with open(filename, 'rt') as datafile:
        lines = datafile.readlines()
    lineno = incr_lock(args) - 1
    try:
        return lines[lineno]
    except IndexError:
        return None


if __name__ == '__main__':
    pass

# end.

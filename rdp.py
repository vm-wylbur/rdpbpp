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


def get_args():
    parser = argparse.ArgumentParser(
        description='Setup locking integer incrementer.')

    parser.add_argument('-t', '--tag', default='rdpbpp', dest='tag',
                        help='the filename in /tmp for the lock and int file')
    parser.add_argument('-s', '--init', dest='init', default=False,
                        action='store_true',
                        help='Init the lock and int files')
    parser.add_argument("-i", "--increment", dest='incr', default=False,
                        action='store_true', help="increment counter file")

    args = parser.parse_args()
    d = vars(args)
    d['lock'] = filelock.FileLock("/tmp/{}.lock".format(args.tag))
    d['fname'] = "/tmp/{}".format(args.tag)
    return args


def init_all(tag="rdpbpp"):
    lock = filelock.FileLock("/tmp/{}.lock".format(tag))
    fname = "/tmp/{}".format(tag)
    Args = namedtuple('Args', ['tag', 'lock', 'fname'])
    args = Args(tag, lock, fname)
    init_lock(args)
    return args


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
    args = get_args()
    if args.init:
        init_lock(args)
    elif args.incr:
        rdpint = incr_lock(args)
        print(rdpint)
    else:
        raise ValueError("must init or increment")

# end.

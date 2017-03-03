#!/usr/bin/env python3

# needs to init lock file
# needs a tag

import argparse
import sys
import filelock

def get_args():
    parser = argparse.ArgumentParser(
        description='Setup locking integer incrementer.')
    parser.add_argument('-t', '--tag', default='pbp', dest='tag',
                        help='the filename in /tmp for the lock and int file')
    parser.add_argument('--init', dest='init', default=False, action='store_true',
                    help='Init the lock and int files')


    args = argparse.parse_args()
    d = vars(args)
    d['lock'] = filelock.FileLock("/tmp/{}.lock".format(args.tag))
    d['file'] = "/tmp/{}".format(args.tag)
    return args


def init_lock(args):
    with args.lock:
        with open(args.file, 'wt') as intfile:
            intfile.write("0\n")


if __name__ == '__main__':
    args = get_args()
    if args.init:
        init_lock(args)

# end.

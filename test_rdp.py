#!/usr/bin/env python3
#
# Authors:     PB
# Maintainers: PB
# Copyright:   2017, HRDAG, GPL v2 or later
# ============================================
# rdpbpp/tests/test_rdp.py

import os
import os.path
import filelock
import rdp

testname = 'bobdog'


def setup_method():
    try:
        os.unlink("/tmp/{}".format(testname))
        os.unlink("/tmp/{}.lock".format(testname))
    except:
        pass


def teardown_module():
    setup_method()


def test_args():
    args = rdp.init_all(tag=testname)
    assert args.tag == testname
    assert args.fname == '/tmp/{}'.format(testname)
    assert os.path.exists(args.fname)
    assert type(args.lock) is filelock.UnixFileLock


def test_get_line():
    args = rdp.init_all(tag=testname)
    line0 = rdp.get_next_line(args, 'testdata.txt').strip()
    assert line0 == "Golden Retriever"
    line1 = rdp.get_next_line(args, 'testdata.txt').strip()
    assert line1 == "Bernese Mountain Dog"


def test_get_line_done():
    args = rdp.init_all(tag=testname)
    last_found = False
    for line in rdp.get_next_line(args, 'testdata.txt'):
        line = line.strip()
        if line == "Giant Pit Bull":
            last_found = True
        elif last_found:
            assert line is None


# done.:

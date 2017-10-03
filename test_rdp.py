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


def setup_module():
    try:
        os.unlink("/tmp/{}".format(testname))
        os.unlink("/tmp/{}.lock".format(testname))
    except:
        pass


def test_args():
    args = rdp.init_all(tag=testname)
    assert args.tag == testname
    assert args.fname == '/tmp/{}'.format(testname)
    assert os.path.exists(args.fname)
    assert type(args.lock) is filelock.UnixFileLock

# done.:

Real Dumb Process-Based Parallelism in python
===========

In a lot of `HRDAG<https://hrdag.org>`'s projects, we want to be able to launch processes that can gradually consume all the elements of a queue. We may want several processes simultaneously consuming elements, without repeating themselves or overlapping. This package makes that possible.

Installation
----------------

This is a poxy hack, and the installation reflects that. Clone the repo someplace temporary (e.g., `~/tmp`), then cd into that directory (e.g., `~/tmp/rdpbpp`). From there, give this command:

    $ pip install -e .

and thereafter you should be able to import rdp. Let me know how it goes.

Usage
----------

Someday I'll write documentation.

Tests
----------

You should install pytest (with pip) and then

     $ pytest test_rdp.py

good luck.

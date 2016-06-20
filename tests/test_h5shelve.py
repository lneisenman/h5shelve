#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_h5shelve
----------------------------------

Tests for `h5shelve` module.
"""

import pytest


import h5shelve as h5s


class Test_open():

    def test_returns_H5shelf(self, tmpdir):
        fn = tmpdir.join('dummy.h5')
        test = h5s.open(fn.strpath)
        assert isinstance(test, h5s.h5shelve.H5shelf)


class TestH5shelve(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass

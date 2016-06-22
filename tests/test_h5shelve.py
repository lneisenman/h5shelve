#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_h5shelve
----------------------------------

Tests for `h5shelve` module.
"""

import h5py
import numpy as np
import pytest


import h5shelve as h5s


class Test_open():

    def test_returns_H5shelf(self, tmpdir):
        fn = tmpdir.join('dummy.h5')
        test = h5s.open(fn.strpath)
        assert isinstance(test, h5s.h5shelve.H5shelf)

    def test_context_manager(self, tmpdir):
        fn = tmpdir.join('dummy.h5')
        with h5s.open(fn.strpath) as test:
            assert len(test) == 0

    def test_read_data_from_hdf5(self, tmpdir):
        fn = tmpdir.join('test_read.h5')
        with h5py.File(fn.strpath, 'w') as db:
            db.create_dataset('array', data=np.linspace(0, 9, 10))
            db.create_dataset('subgroup/group1', data=np.linspace(0, 4, 5))
            db.create_dataset('subgroup/group2', data=3)
            db.create_dataset('sub1/sub2/string', data='string value')

        with h5s.open(fn.strpath) as test:
            assert np.allclose(test['array'], np.linspace(0, 9, 10))
            assert np.allclose(test['subgroup']['group1'],
                               np.linspace(0, 4, 5))
            assert test['subgroup']['group2'] == 3
            assert test['sub1']['sub2']['string'] == 'string value'


class TestH5shelve(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass

# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals, absolute_import,
                        division)

import collections

import h5py


class H5shelf(collections.MutableMapping):
    """ shelf object that emulates shelve behavior using hdf5 files """

    def __init__(self, fn, mode='a', *args, **kwargs):
        self.filename = fn
        self.mode = mode
        self.file = h5py.File(fn)
        self.dict = dict()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.file.close()

    def __iter__(self):
        for k in self.dict.keys():
            yield k

    def __len__(self):
        return len(self.dict)

    def __contains__(self, key):
        return key in self.dict

    def get(self, key, default=None):
        if key in self.dict:
            return self.dict[key]

        return default

    def __getitem__(self, key):
        return self.dict[key]

    def __setitem__(self, key, value):
        self.dict[key] = value

    def __delitem__(self, key):
        del self.dict[key]


def open(fn, *args, **kwargs):
    return H5shelf(fn, *args, **kwargs)

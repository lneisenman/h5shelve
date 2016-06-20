# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals, absolute_import,
                        division)

import h5py


class H5shelf():
    """ shelf object that emulates shelve behavior using hdf5 files """

    def __init__(self, fn, mode='w', *args, **kwargs):
        self.filename = fn
        self.mode = mode
        self.file = h5py.File(fn)


def open(fn, *args, **kwargs):
    return H5shelf(fn, *args, **kwargs)

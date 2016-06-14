# -*- coding: utf-8 -*-

from __future__ import (print_function, unicode_literals, absolute_import,
                        division)


class H5shelf():
    """ shelf object that emulates shelve behavior using hdf5 files """

    def __init__(self, fn, mode):
        self.filename = fn
        self.mode = mode


def open(fn, mode='r'):
    return H5shelf(fn, mode)

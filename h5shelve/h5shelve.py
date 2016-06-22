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
        self.dict = dict()
        if 'w' in mode:
            return

        self.read_data_from_hdf5()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.write_data_to_hdf5()

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

    def read_data_from_hdf5(self):
        with h5py.File(self.filename) as db:
            self.dict = self._extract_data(db)

    def _extract_data(self, db):
        result = dict()
        for key in db:
            if isinstance(db[key], h5py._hl.dataset.Dataset):
                result[key] = db[key][...]
            else:
                result[key] = self._extract_data(db[key])

        return result

    def write_data_to_hdf5(self):
        pass


def open(fn, *args, **kwargs):
    return H5shelf(fn, *args, **kwargs)

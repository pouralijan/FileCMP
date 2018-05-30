#!/bin/usr/env python3
__author__ = "Hassan Pouralijan"
__copyright__ = "Copyright 2018, The FileCMD Project"
__credits__ = ["Hassan Pouralijan"]
__license__ = "GPL3"
__version__ = "0.1.0"
__maintainer__ = "Hassan Pouralijan"
__email__ = "pouralijan@gmail.com"
__status__ = "Production"

import os
import hashlib


class File(object):

    def __init__(self, path: str) -> None:
        self.path = path

    def __hash__(self) -> int:
        with open(self.path, 'rb') as _file:
            md5_hash = hashlib.md5()
            while True:
                data = _file.read()
                if not data:
                    break
                md5_hash.update(data)
            return int(md5_hash.hexdigest(), 16) % (10 ** 16)

    def __len__(self) -> int:
        return os.path.getsize(self.path)

    def __dir__(self) -> list:
        return [os.path.dirname(self.path)]

    def __str__(self) -> str:
        return os.path.basename(self.path)

    def get_dict(self):
        return {"path": dir(self)[0], "hash": hash(self), "size": len(self), "name": str(self)}


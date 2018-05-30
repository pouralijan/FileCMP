#!/usr/bin/env python3
__author__ = "Hassan Pouralijan"
__copyright__ = "Copyright 2018, The FileCMD Project"
__credits__ = ["Hassan Pouralijan"]
__license__ = "GPL3"
__version__ = "0.1.0"
__maintainer__ = "Hassan Pouralijan"
__email__ = "pouralijan@gmail.com"
__status__ = "Production"

import os
from File import File
import datetime
from collections import defaultdict
import tqdm


def scan_dir(dir_):
    db = defaultdict()
    c = 0
    cc = 0
    for r, d, f in os.walk(dir_):
        c += len(f)
    pbar = tqdm.tqdm(total=c)
    now = datetime.datetime.now()
    d = 0
    for root, dirs, files in os.walk(dir_):
        for file in files:
            cc += 1
            pbar.update(1)
            file_path = os.path.join(root, file)
            file_ = File(file_path)
            file_dict = file_.get_dict()
            print(dir(file_))
            if hash(file_) in db:
                os.remove(os.path.join(dir(file_)[0], str(file_)))
                d += 1
            else:
                db[hash(file_)] = file_dict
    print("\nTime: {}".format(datetime.datetime.now() - now))
    print(d)


def main():
    print("Hi !!! This is Pheonix")
    scan_dir("/mnt/Workstation/log/")
    print("END ")


if __name__ == "__main__":
    main()

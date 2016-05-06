#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: omi
# @Date:   2014-08-24 21:51:57
# @Last Modified by:   omi
# @Last Modified time: 2014-08-25 18:01:59


import logging
import const
import os

FILE_NAME = os.path.join(const.Constant.conf_dir, 'musicbox.log')
if os.path.isdir(const.Constant.conf_dir) is False:
    os.mkdir(const.Constant.conf_dir)


with open(FILE_NAME, 'a+') as f:
    f.write('#' * 80)
    f.write('\n')


def getLogger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    # File output handler
    fh = logging.FileHandler(FILE_NAME)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(name)s:%(lineno)s: %(message)s'))   # NOQA
    log.addHandler(fh)

    return log

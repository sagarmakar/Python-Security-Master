# Python Security Project (PySec) and its related class files.
#
# PySec is a set of tools for secure application development under Linux
#
# Copyright 2014 PySec development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# -*- coding: ascii -*-
""""""
import os
import stat
import resource

MIN_INODES = 64
MIN_FDS = 64


def ino_check(dev, min_ino=MIN_INODES):
    return os.fstatvfs(dev).f_ffree >= int(min_ino)


def size_check(size):
    return size <= resource.getrlimit(resource.RLIMIT_FSIZE)[0]


def space_check(dev, size):
    stdev = os.fstatvfs(dev)
    return size < stdev.f_bfree * stdev.f_bsize


def mode_check(mode):
    return 0 <= mode <= 0777
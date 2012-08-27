#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from cx_Freeze import setup, Executable
import os



includefiles = []
includes = []
excludes = []
packages = []


setup(
    name = "photocoord",
    version = "1.0",
    description = "photocoord",
    options = {'build_exe': {'excludes':excludes, 'packages':packages, 'include_files':includefiles, 'build_exe':'../build/photocoord_win'}},
    executables = [Executable("photocoord.py", base = 'Console', targetName="photocoord.exe")])


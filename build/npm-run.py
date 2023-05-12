#!/usr/bin/env python3
from __future__ import print_function
import os
import subprocess
import sys

SOURCE_ROOT = os.path.dirname(os.path.dirname(__file__))
cmd = "npm"
if sys.platform == "win32":
    cmd += ".cmd"
args = [cmd, "run",
    "--prefix",
    SOURCE_ROOT
    ] + sys.argv[1:]
try:
    subprocess.check_output(args, stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    error_msg = f"NPM script '{sys.argv[2]}' failed with code '{e.returncode}':\n"
    print(error_msg + e.output.decode('utf8'))
    sys.exit(e.returncode)

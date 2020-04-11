#!/usr/bin/python3
"""Usage: lnmaker.py dir_with_bins dir_with_symlinks"""

from subprocess import Popen, PIPE, STDOUT
from typing import List

import os
import sys


def run_cmd(cmd: str) -> List[str]:
    val = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
    out, _ = val.communicate()
    return out.decode().rstrip('\n').split('\n')


if __name__ == '__main__':
    for d, _, files in os.walk(sys.argv[1]):
        for f in files:
            path_to_bin = os.path.join(d, f)
            path_to_ln = os.path.join(sys.argv[2], f)
            if os.access(path_to_bin, os.X_OK):
                run_cmd(f'ln -s {path_to_bin} {path_to_ln}')
        break

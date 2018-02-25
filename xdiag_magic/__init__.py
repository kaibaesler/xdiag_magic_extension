#!/usr/bin/env python
"""An Jupyter magic for {block,seq,act,nw}diag"""
__version__ = '0.0.1'

from .magic import Xdiag

def load_ipython_extension(ipython):
    ipython.register_magics(Xdiag)

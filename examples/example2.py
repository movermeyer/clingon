# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
sys.path.insert(0, '..')
from clingon import clingon
clingon.DEBUG = True

# the decorator has parameters
# each option of the decorated function
# will have its default short alias overridden by the decorator
# shortcuts (you can define more than one for each parameter)

# also, a second decorator allows to define variables that can be
# used to generate the help text from your docstring.


def version():
    return '1.2.3'

@clingon.clize(first_option='1', second_option=('2', 's', 'so'))
@clingon.set_variables(VERSION=version, message="you can dynamically customize help message !")
def my_func(p1, p2,
            first_option='default_value',
            second_option=5,
            third_option=[4, 3],
            last_option=False):
    """Help docstring. v{VERSION}
       {message}
    """
    if last_option:
        raise RuntimeError("Test of DEBUG")
    return '%s %s %s %s %s %s' % (p1, p2, first_option, second_option, third_option, last_option)

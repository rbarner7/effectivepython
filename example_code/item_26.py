#!/usr/bin/env PYTHONHASHSEED=1234 python3

# Copyright 2014-2019 Brett Slatkin, Pearson Education Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Reproduce book environment
import random

random.seed(1234)

import logging
from pprint import pprint
from sys import stdout as STDOUT

# Write all output to a temporary directory
import atexit
import gc
import io
import os
import tempfile

TEST_DIR = tempfile.TemporaryDirectory()
atexit.register(TEST_DIR.cleanup)

# Make sure Windows processes exit cleanly
OLD_CWD = os.getcwd()
atexit.register(lambda: os.chdir(OLD_CWD))
os.chdir(TEST_DIR.name)


def close_open_files():
    everything = gc.get_objects()
    for obj in everything:
        if isinstance(obj, io.IOBase):
            obj.close()


atexit.register(close_open_files)


# Example 1
def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result

    return wrapper


# Example 2
@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


# Example 3
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


fibonacci = trace(fibonacci)  # trace returns the wrapper defined within its body
# wrapper gets assigned to the fibonacci name in the containing module because of the decorator
# this is problematic because it undermines tools that do introspection, such as debuggers


# Example 4
fibonacci(4)

# Example 5
print(fibonacci)

# >>>
# <function trace.<locals>.wrapper at 0x108955dc0>

# Example 6: Unexpected behavior
help(fibonacci) # should return fibonacci's docstring ("Return the n-th Fibonacci number") but doesn't

# >>>
# Help on function wrapper in module __main__: # runs help on wrapper instead of fibonacci
# # because fibonacci is decorated bytrace
#
# wrapper(*args, **kwargs)

# Example 7
try:
    import pickle

    pickle.dumps(fibonacci)
except:
    logging.exception('Expected')
else:
    assert False

# Example 8: Correct approach yielding expected behavior
from functools import wraps


def trace(func):
    @wraps(func) 
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result

    return wrapper


@trace # fibonacci is decorated
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


# Example 9
help(fibonacci)
# >>>
# Help on function fibonacci in module __main__:
# fibonacci(n)
#       Return the n-th Fibonacci number


# Example 10
print(pickle.dumps(fibonacci))  # pickle is an object serializer
# >>>
# b'\x80\x04\x95\x1a\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\
# ➥x94\x8c\tfibonacci\x94\x93\x94.
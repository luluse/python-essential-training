#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys

def main():
    v = sys.version_info
    p = sys.platform
    print('Python version {}.{}.{}'.format(*v))
    print(p)

if __name__ == '__main__': main()

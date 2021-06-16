#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('lines.txt')
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()


# open functions:
#r read mode -> default mode
#w write mode -> empties the files and start at the beginning
#a append mode -> if file has some content, continues at the bottom of the file

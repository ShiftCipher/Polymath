#!/usr/bin/env python

def env(name):
    envFile = open(".env", "w+")
        for line in envFile:
           line = line.split("=")
           print line[0]
    file.close()

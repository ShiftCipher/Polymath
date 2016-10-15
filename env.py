#!/usr/bin/env python

def env(name):
    file = open(".env", "w+")
        for line in file:
           line = line.split("=")
           try:
               if line[0] == name:
                   return line[1]
           except Exception as e:
               raise
    file.close()

#!/usr/bin/env python

import os

class env(object):

    """docstring for ENV."""

    def __init__(self, name):
        self.arg = name

    def env(self):
        if os.path.isfile(".env"):
            env = open(".env", "r")
            data = env.readlines()
            for line in data:
                line = line.split("=")
                try:
                    if line[0] == self.name:
                        return str(line[1].replace("\n", ""))
                except Exception as e:
                    raise
            file.close()
        else:
            print("ENV File Not Found")

    def __call__(self):
        return self.env()

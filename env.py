#!/usr/bin/env python

import os

def env(name):
    if os.path.isfile(".env"):
        env = open(".env", "r")
        data = env.readlines()
        for line in data:
            line = line.split("=")
            try:
                if line[0] == name:
                    return str(line[1].replace("\n", ""))
            except Exception as e:
                raise
        env.close()
    else:
        print("ENV File Not Found")

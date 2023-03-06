#!/usr/bin/python3
import sys
text = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
def write_to_stderr():
    sys.stderr.write(text)
    sys.exit(1)
write_to_stderr()

import glob
import sys

CARLA_LIB = './lib/carla-0.9.6-py3.5-linux-x86_64.egg'


def load_lib(path):
    try:
        lib_file = glob.glob(path)[0]
        sys.path.append(lib_file)
    except IndexError as e:
        raise Exception(f"Can't import {path} library!. {e}")

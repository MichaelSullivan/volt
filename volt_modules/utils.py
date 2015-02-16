__author__ = 'msullivan'

import os
import sys
import json
import contextlib
import subprocess

dot_dir = '~/.volt' #get_config['dot_dir']
volt_config_filename = 'config.json'

def get_path_to_volt():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def get_dot_dir():
    expanded_dot_dir = os.path.expanduser(dot_dir)
    if not os.path.exists(expanded_dot_dir):
        os.makedirs(expanded_dot_dir)
    return expanded_dot_dir

def get_path_to_volt_config():
    return os.path.join(get_dot_dir(), volt_config_filename)

def get_value_from_config_file(*keys):
    cfg = get_path_to_volt_config()
    if os.path.isfile(cfg):
        with open(cfg) as data_file:
            data = json.load(data_file)
            for key in keys:
                data = data[key]
            return data

@contextlib.contextmanager
def chdir(path):
    old_dir = os.getcwd()
    if old_dir != path:
        print('switching working directory to {dir}'.format(dir=path))
    try:
        os.chdir(path)
        yield old_dir != path
    finally:
        os.chdir(old_dir)
    if old_dir != path:
        print('switching working directory (back) to {dir}'.format(dir=old_dir))

def check_call_wrapper(*popenargs, **kwargs):
    print(' '.join(*popenargs))
    return subprocess.check_call(*popenargs, **kwargs)

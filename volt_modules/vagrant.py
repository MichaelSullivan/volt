__author__ = 'msullivan'

import utils
import os
import subprocess

def get_os_environ():
    new_environ = os.environ.copy()

    new_environ['VOLT_SSH_USERNAME'] = (utils.get_value_from_config_file("ssh","username"))
    new_environ['VOLT_SSH_PRIVATE_KEY_PATH'] = (utils.get_value_from_config_file("ssh","private_key_path"))

    new_environ['VOLT_NETWORK_IP'] = (utils.get_value_from_config_file("network","ip"))
    
    new_environ['VOLT_VIRTUALBOX_BOX'] = (utils.get_value_from_config_file("virtualbox","box"))
    
    new_environ['VOLT_AWS_ACCESS_KEY'] = (utils.get_value_from_config_file("aws","access_key"))
    new_environ['VOLT_AWS_SECRET_KEY'] = (utils.get_value_from_config_file("aws","secret_key"))
    new_environ['VOLT_AWS_SUBNET_ID'] = (utils.get_value_from_config_file("aws","subnet_id"))
    new_environ['VOLT_AWS_SECURITY_GROUPS'] = (utils.get_value_from_config_file("aws","security_groups"))
    new_environ['VOLT_AWS_AMI'] = (utils.get_value_from_config_file("aws","ami"))
    new_environ['VOLT_AWS_KEYPAIR_NAME'] = (utils.get_value_from_config_file("aws","keypair_name"))
    new_environ['VOLT_AWS_INSTANCE_NAME'] = (utils.get_value_from_config_file("aws","instance_name"))
    new_environ['VOLT_AWS_INSTANCE_TYPE'] = (utils.get_value_from_config_file("aws","instance_type"))

    return new_environ

def run_cmd(provider, vagrant_args):
    assert provider in ['virtualbox','aws']
    dir = utils.get_path_to_volt()
    with utils.chdir(dir):
        utils.check_call_wrapper(
            ['vagrant', 
             '--provider={0}'.format(provider)
            ] + vagrant_args,
            env=get_os_environ()
        )

def status(provider):
    run_cmd(provider, ['status'])
    if provider == 'aws':
        run_cmd(provider, 'awsinfo','-p')
    if provider == 'virtualbox':
        print 'TODO'
    
def up(provider):
    run_cmd(provider, ['up'])
    
def destroy(provider):
    run_cmd(provider, ['destroy', '-f'])
    
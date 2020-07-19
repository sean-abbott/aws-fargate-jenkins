#!/usr/bin/env python3
import boto3
import os

PARAM_SECURE_TYPE = 'SecureString'

def get_parameter_list(ssm_client):
    try:
        return ssm_client.get_parameters_by_path(Path=os.getenv('JENKINS_PARAMETER_PATH'), Recursive=True)['Parameters']
    except:
        raise

def decode_value(ssm_client, param):
    #import pdb; pdb.set_trace()
    if param['Type'] == PARAM_SECURE_TYPE:
        print('Getting decoded value for {}'.format(param['Name']))
        return ssm_client.get_parameter(Name=param['Name'], WithDecryption=True)['Parameter']['Value']

    return param['Value']


def write_param_files(ssm_client):
    param_list = get_parameter_list(ssm_client)
    secrets_dir = os.getenv('SECRETS')
    for param in param_list:
        param_base_levels = len(os.getenv('JENKINS_PARAMETER_PATH').rstrip('/').split('/'))
        param_levels = param_base_levels - len(param['Name'].split('/'))
        param_name = '/'.join(param['Name'].split('/')[param_levels:])
        param_value = decode_value(ssm_client, param)

        param_dirname = '/'.join(param_name.split('/')[:-1])
        os.makedirs(os.path.join(secrets_dir, param_dirname), exist_ok=True)

        final_path = os.path.join(secrets_dir, param_name)
        with open(os.path.join(secrets_dir, param_name), 'w') as f:
            print('Writing secret to {}'.format(final_path))
            f.write(param_value)

def main():
    ssm_client = boto3.client('ssm')
    write_param_files(ssm_client)

if __name__ == '__main__':
    main()

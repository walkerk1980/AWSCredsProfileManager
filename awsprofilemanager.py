#!/usr/bin/env python

import sys
import os
import argparse
import configparser

parser = argparse.ArgumentParser()

OUTPUT_CHOICES=['json','text','table']

# You can pull region list from AWS CLI if it needs to be updated
# aws ec2 describe-regions --query Regions[].RegionName --output text
# This is not updated via python as we cannot assume creds already exist
REGIONS = 'ap-south-1 ap-northeast-2 ap-southeast-1 ap-southeast-2 ap-northeast-1 ca-central-1 \
eu-central-1 eu-west-1 eu-west-2 eu-west-3 sa-east-1 us-east-1 us-east-2 us-west-1 us-west-2'
REGION_CHOICES = REGIONS.split()

CREDSOURCE_CHOICES = ['Environment', 'Ec2InstanceMetadata', 'EcsContainer']

# removed from duration-seconds so argparse doesn't annoyingly
# print the entire range of numbers from 900-43200
# DURATION_CHOICES=range(900,43200,900)

parser.add_argument('-p', '--profile', nargs='?', const='NO', default='default', help='The name of the profile to create or overwrite')
parser.add_argument('-r', '--region', nargs='?', const='NO', choices=REGION_CHOICES, help='the region to set for the profile')
parser.add_argument('-a', '--access-key-id', nargs='?', const='NO', help='AccessKeyID to set in the profile')
parser.add_argument('-s', '--secret-access-key', nargs='?', const='NO', help='The SecretAccessKey to set for the profile')
parser.add_argument('-t', '--session-token', nargs='?', const='NO', help='The SessionToken to set for the profile')
parser.add_argument('-o', '--output', nargs='?', const='NO', choices=OUTPUT_CHOICES, help='Default output style')
parser.add_argument('-R', '--role-arn', nargs='?', const='NO', help='The ARN of the Role to set for the profile to assume')
parser.add_argument('-S', '--role-session-name', nargs='?', const='NO', help='The Role Session Name to set for the profile to use')
parser.add_argument('-P', '--source-profile', nargs='?', const='NO', help='The name of the source profile to set')
parser.add_argument('-c', '--credential-source', nargs='?', const='NO', choices=CREDSOURCE_CHOICES, help='The credential provider to use to get credentials for the initial assume-role call')
parser.add_argument('-e', '--external-id', nargs='?', const='NO', help='A unique identifier that is used by third parties to assume a role')
parser.add_argument('-m', '--mfa-serial', nargs='?', const='NO', help='The identification number of the MFA device to use when assuming a role')
parser.add_argument('-f', '--config-file-path', nargs='?', const='NO', default=os.path.expanduser('~/.aws/config'), help='Path to he file to create the profile in, defaults to ~/.aws/config')
parser.add_argument('-d', '--duration-seconds', nargs='?', const='NO', type=int, help='The duration, in seconds (900..max_session_duration) of the role session. Default=3600')
args = parser.parse_args()

if len(sys.argv) < 2:
    parser.print_help(sys.stderr)
    exit()

new_profile = args.profile
filename = args.config_file_path

open(filename, 'a').close()
config = configparser.RawConfigParser()
config.read(filename)

if not config.has_section(new_profile):
    config.add_section(new_profile)

def set_config_option(profile, name, value):
    if name not in ['profile', 'config_file_path']:
        if name in ['access_key_id','secret_access_key','session_token']:
            key = 'aws_' + name
        else:
            key = name
        config.set(profile, key, value )

for arg in vars(args):
    if getattr(args, arg):
        set_config_option(new_profile, arg, getattr(args, arg))

with open(filename, 'w+') as awsconfig:
    config.write(awsconfig)

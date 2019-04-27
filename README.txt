# AWSCredsProfileManager
CLI tool for managing the .aws/config or .aws/credentials files

examples:

awsprofilemanager.py -r us-west-2 -a AKID0123456789012 -s 'YourSecretAccessKey/klngs/a49nunf98494n' 

awsprofilemanager.py -p saml -r us-east-1 -a AKID0123456789012 -s 'YourSecretAccessKey/klngs/a49nunf98494n' -t 'YourSessionToken/d932u98unf43/a93uh'


usage: awsprofilemanager.py [-h] [-p [PROFILE]]
                            [-r [{ap-south-1,ap-northeast-2,ap-southeast-1,ap-southeast-2,ap-northeast-1,ca-central-1,eu-central-1,eu-west-1,eu-west-2,eu-west-3,sa-east-1,us-east-1,us-east-2,us-west-1,us-west-2}]]
                            [-a [ACCESS_KEY_ID]] [-s [SECRET_ACCESS_KEY]]
                            [-t [SESSION_TOKEN]] [-o [{json,text,table}]]
                            [-R [ROLE_ARN]] [-S [ROLE_SESSION_NAME]]
                            [-P [SOURCE_PROFILE]]
                            [-c [{Environment,Ec2InstanceMetadata,EcsContainer}]]
                            [-e [EXTERNAL_ID]] [-m [MFA_SERIAL]]
                            [-f [CONFIG_FILE_PATH]] [-d [DURATION_SECONDS]]

optional arguments:
  -h, --help            show this help message and exit
  -p [PROFILE], --profile [PROFILE]
                        The name of the profile to create or overwrite
  -r [{ap-south-1,ap-northeast-2,ap-southeast-1,ap-southeast-2,ap-northeast-1,ca-central-1,eu-central-1,eu-west-1,eu-west-2,eu-west-3,sa-east-1,us-east-1,us-east-2,us-west-1,us-west-2}], --region [{ap-south-1,ap-northeast-2,ap-southeast-1,ap-southeast-2,ap-northeast-1,ca-central-1,eu-central-1,eu-west-1,eu-west-2,eu-west-3,sa-east-1,us-east-1,us-east-2,us-west-1,us-west-2}]
                        the region to set for the profile
  -a [ACCESS_KEY_ID], --access-key-id [ACCESS_KEY_ID]
                        AccessKeyID to set in the profile
  -s [SECRET_ACCESS_KEY], --secret-access-key [SECRET_ACCESS_KEY]
                        The SecretAccessKey to set for the profile
  -t [SESSION_TOKEN], --session-token [SESSION_TOKEN]
                        The SessionToken to set for the profile
  -o [{json,text,table}], --output [{json,text,table}]
                        Default output style
  -R [ROLE_ARN], --role-arn [ROLE_ARN]
                        The ARN of the Role to set for the profile to assume
  -S [ROLE_SESSION_NAME], --role-session-name [ROLE_SESSION_NAME]
                        The Role Session Name to set for the profile to use
  -P [SOURCE_PROFILE], --source-profile [SOURCE_PROFILE]
                        The name of the source profile to set
  -c [{Environment,Ec2InstanceMetadata,EcsContainer}], --credential-source [{Environment,Ec2InstanceMetadata,EcsContainer}]
                        The credential provider to use to get credentials for
                        the initial assume-role call
  -e [EXTERNAL_ID], --external-id [EXTERNAL_ID]
                        A unique identifier that is used by third parties to
                        assume a role
  -m [MFA_SERIAL], --mfa-serial [MFA_SERIAL]
                        The identification number of the MFA device to use
                        when assuming a role
  -f [CONFIG_FILE_PATH], --config-file-path [CONFIG_FILE_PATH]
                        Path to he file to create the profile in, defaults to
                        ~/.aws/config
  -d [DURATION_SECONDS], --duration-seconds [DURATION_SECONDS]
                        The duration, in seconds (900..max_session_duration)
                        of the role session. Default=3600

# AWSCredsProfileManager
CLI tool for managing the .aws/config or .aws/credentials files

examples:

awsprofilemanager.py -r us-west-2 -a AKID0123456789012 -s 'YourSecretAccessKey/klngs/a49nunf98494n' 

awsprofilemanager.py -p saml -r us-east-1 -a AKID0123456789012 -s 'YourSecretAccessKey/klngs/a49nunf98494n' -t 'YourSessionToken/d932u98unf43/a93uh'


For full usage and arguments please see: https://github.com/walkerk1980/AWSCredsProfileManager/blob/master/README.txt

For more info on AWS config and credentials files please see the AWS Documentation. [1][2]


[1] Named Profiles - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html

[2] AWS Config/Credential File Format - https://docs.aws.amazon.com/cli/latest/topic/config-vars.html


'-p', '--profile', nargs='?', const='NO', default='default', help='The name of the profile to create or overwrite'
'-r', '--region', nargs='?', const='NO', choices=REGION_CHOICES, help='the region to set for the profile'
'-a', '--access-key-id', nargs='?', const='NO', help='AccessKeyID to set in the profile'
'-s', '--secret-access-key', nargs='?', const='NO', help='The SecretAccessKey to set for the profile'
'-t', '--session-token', nargs='?', const='NO', help='The SessionToken to set for the profile'
'-o', '--output', nargs='?', const='NO', choices=OUTPUT_CHOICES, help='Default output style'
'-R', '--role-arn', nargs='?', const='NO', help='The ARN of the Role to set for the profile to assume'
'-S', '--role-session-name', nargs='?', const='NO', help='The Role Session Name to set for the profile to use'
'-P', '--source-profile', nargs='?', const='NO', help='The name of the source profile to set'
'-c', '--credential-source', nargs='?', const='NO', choices=CREDSOURCE_CHOICES, help='The credential provider to use to get credentials for the initial assume-role call'
'-e', '--external-id', nargs='?', const='NO', help='A unique identifier that is used by third parties to assume a role'
'-m', '--mfa-serial', nargs='?', const='NO', help='The identification number of the MFA device to use when assuming a role'
'-f', '--config-file-path', nargs='?', const='NO', default=os.path.expanduser('~/.aws/config'), help='Path to he file to create the profile in, defaults to ~/.aws/config'
'-d', '--duration-seconds', nargs='?', const='NO', type=int, help='The duration, in seconds (900..max_session_duration) of the role session. Default=3600'

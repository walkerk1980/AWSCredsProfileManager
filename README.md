# AWSCredsProfileManager
CLI tool for managing the .aws/config or .aws/credentials files

examples:

awsprofilemanager.py -r us-west-2 -a AKID0123456789012 -s 'YourSecretAccessKey/klngs/a49nunf98494n' 

awsprofilemanager.py -p saml -r us-east-1 -a AKID0123456789012 -s 'YourSecretAccessKey/klngs/a49nunf98494n' -t 'YourSessionToken/d932u98unf43/a93uh'


For usage and arguments please see: https://github.com/walkerk1980/AWSCredsProfileManager/blob/master/README.txt

For more info on AWS config and credentials files please see the AWS Documentation. [1][2]


[1] Named Profiles - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html

[2] AWS Config/Credential File Format - https://docs.aws.amazon.com/cli/latest/topic/config-vars.html

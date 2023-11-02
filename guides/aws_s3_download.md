# Downloading content from S# using the AWS CLI

1. Install the AWS CLI, using [up to date instructions from AWS](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html). Homebrew is no longer officially supported at the time of writing.
2. Add the AWS credentials with permissions to the buckets desired `aws configure`
    - Access Key
    - Secret Key
    - Region\
3. Download recursively from the S3 bucket `aws cp s3 --recursive s3://<my-bucket-name>/<my-folder> <local_directory>`

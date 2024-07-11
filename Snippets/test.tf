provider "aws" {
  region = "us-west-2" 
}

resource "aws_s3_bucket" "example_bucket" {
  bucket = "example-bucket-name" # Set your desired bucket name
  acl    = "private"             # Set access control for the bucket, options are "private", "public-read", "public-read-write", "authenticated-read", "aws-exec-read", "bucket-owner-read", "bucket-owner-full-control"
}

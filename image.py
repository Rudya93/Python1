#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2')
instance = ec2.Instance('i-0f31b29a8752a52d0')
instance.create_image(Name='ORudenko')



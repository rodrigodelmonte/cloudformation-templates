#!/bin/bash
if [ -f "lambda.zip" ]; then rm lambda.zip; fi
zip lambda.zip lambda_function.py
pip install requests -t lib/
cd lib/
zip -r9 ../lambda.zip requests/*
cd ..
aws s3 cp lambda.zip s3://bedroom-app-00/lambda.zip

import boto3

def main():
    print("Col1,Col2,Col3")
    print("Using boto3, Splunk is great, Kobe!")
    s3 = boto3.resource('s3')
    print("Used boto3, Splunk is still awesome, Kobe!")


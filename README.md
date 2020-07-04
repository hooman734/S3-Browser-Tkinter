## About  

### This application is developed by using [Python3][0] - [Tkinter][1] aiming to simply browse buckets, download and upload files into it.
#### *This application works either with real [AWS][2] or mocked [S3][3] using [Localstack][4].*  

### Dependencies
+ `tkinter`
+ `tkinter.ttk`
+ `boto3`
+ `botocore`
+ `PIL`
+ `csv`


### Description

![Idle](https://github.com/hooman734/S3-Browser-Tkinter/blob/master/screenshots/idle.png)

Here the application has read credential keys from provided csv file from AWS. It is ready to Login and browse over the S3 account to show its content.

![Ready to import credential](https://github.com/hooman734/S3-Browser-Tkinter/blob/master/screenshots/read_keys.png)


![Logged in](https://github.com/hooman734/S3-Browser-Tkinter/blob/master/screenshots/imported_logged_in.png)

[0]: https://www.python.org/download/releases/3.0/
[1]: https://docs.python.org/3/library/tkinter.html
[2]: https://aws.amazon.com/
[3]: https://en.wikipedia.org/wiki/S3
[4]: https://localstack.cloud/
[5]:

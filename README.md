## About  

### This application is developed by using [Python3][0] - [Tkinter][1] aiming to simply browse buckets, download and upload files into it.
#### *This application works either with real [AWS][2] or mocked [S3][3] using [Localstack][4].*  

* #### Python 3.7.6
* #### Tkinter 0.3.1


### Dependencies
+ `tkinter`
+ `tkinter.ttk`
+ `boto3`
+ `botocore`
+ `PIL`
+ `csv`


### Description
install all depencencies 
  + `sudo apt-get install python3`
  + `sudo apt-get install python3-pip`
  + `sudo apt-get install python3-tk`
  + `sudo pip3 install boto3`
  + `sudo pip3 install Pillow`
  
and run `~$ python3 App.py`

### Screenshots


![Idle](https://github.com/hooman734/S3-Browser-Tkinter/blob/master/screenshots/idle.png)

###### Initial view of the application.
------------------------

![Ready to import credential](https://github.com/hooman734/S3-Browser-Tkinter/blob/master/screenshots/read_keys.png)

###### Here the application has read credential keys from provided csv file from AWS. It is ready to Login and browse over the S3 account to show its content.
------------------------


![Logged in](https://github.com/hooman734/S3-Browser-Tkinter/blob/master/screenshots/imported_logged_in.png)

###### Here it already accessed into a S3 account, read its content and showing available buckets.
------------------------


![All windows](https://github.com/hooman734/S3-Browser-Tkinter/blob/master/screenshots/all_windows.png)

###### Here the application is going to download a selected file and also to upload any chosen file into the focused bucket.
------------------------

[0]: https://www.python.org/download/releases/3.0/
[1]: https://docs.python.org/3/library/tkinter.html
[2]: https://aws.amazon.com/
[3]: https://en.wikipedia.org/wiki/S3
[4]: https://localstack.cloud/

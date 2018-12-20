# Bitly url shorterer

The script provides interface for the [bit.ly](https://bit.ly/)-service.
It helps you to shorten long urls in command line interface.

### How to install

[bit.ly](https://bit.ly/) wouldn't provide you data, until you get access-token.
It needs to communicate with API Bitly. All you need - is:
 - to register in [bit.ly](https://bit.ly/) using e-mail
 - generate `GENERIC ACCESS TOKEN`, following this [link](https://bitly.com/a/oauth_apps)
 - create file ``.env`` in the script directory
 - add this line ``TOKEN=MY_TOKEN`` to the `.env`-file, where `MY_TOKEN` is token you have generate on the previous step 


Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
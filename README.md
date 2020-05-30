## Web Tinder Bot

#### Intro
This is a repo to test and get knowledge about the selenium framework. It's only for study matter.


This bot serve as an automatically Tinder swap at the web application.
It'll login Tinder using your Facebook credentials and start swapping to all girls or boys that will appears in your timeline.

For each match, the app launch a pop-up and it'll close automatically too.

#### Instruction
We recommend to use a virtualenv:
```
$ sudo apt-get install python3-pip
$ sudo pip3 install virtualenv
$ virtualenv -p python3 venv_py3
$ source venv_py3/bin/activate
```

After create the development environment, it's need install some requirements:
```
$ make install_requirements
```

Besides that steps, it's need add the driver to interface with the chosen browser in your PATH, e.g., place it in /usr/bin or /usr/local/bin.

| Browser | Link |
| --- | --- |
| Chrome | https://sites.google.com/a/chromium.org/chromedriver/downloads |
| Firefox | https://github.com/mozilla/geckodriver/releases |
| Opera | https://webkit.org/blog/6900/webdriver-support-in-safari-10/ |

Now, this bot only run at the Firefox browser.

To load the app, it's only need to run the following command:
```
$ python tinder.py
```

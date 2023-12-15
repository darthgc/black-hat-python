# Black Hat Python

Source code related to the book Black Hat Python (Second Edition)

Notes:

- Chapter 6 is not present, because the book does not use the new Burp API. It would be best to use Java when extending Burp anyway.
- Chapter 8, the keylogger is not present, because it uses a dead modules that does not work with an up to date version of Python.

## Setup

- `python -m venv venv3`
- `source venv3/bin/activate`

Once done: `deactivate`

Python dependencies:

- `pip install lxml`
- `pip install beautifulsoup4`
- `pip install paramiko`
- `pip install scapy`
- `pip install opencv-python opencv-python-headless`
- `pip install requests`
- `pip install github3.py`
- `pip install pyWinhook`

OS dependencies:

- `sudo apt-get install libopencv-dev python3-opencv python3-numpy python3-scipy`

For Chapter 7, you need to create a GitHub PAT in order to communicate with the C2 and store it in a file named `mytoken.txt`
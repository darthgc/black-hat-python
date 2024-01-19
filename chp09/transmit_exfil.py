import ftplib
import os
import socket
import win32file

def plain_ftp(docpath, server="192.168.1.203"):
    ftp = ftplib.FTP(server)
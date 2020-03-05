#!/usr/bin/env python
import ftplib

FTP_SERVER_URL = 'ftp.kernel.org'
DOWNLOAD_DIR_PATH = '/pub/software/network/tftp'
DOWNLOAD_FILE_NAME = 'tftp-hpa-0.11.tar.gz'

def ftp_file_download(path, username, email):
    ftp_client = ftplib.FTP(path, username, email)
    ftp_client.cwd(DOWNLOAD_DIR_PATH)
    print("File list at %s:" %path)
    files = ftp_client.dir()
    print(files)
    file_handler = open(DOWNLOAD_FILE_NAME, 'wb')
    ftp_client.retrbinary('RETR tftp-hpa-0.11.tar.gz',
    file_handler.write)
    file_handler.close()
    ftp_client.quit()

if __name__ == '__main__':
    ftp_file_download(path=FTP_SERVER_URL, username='anonymous',
    email='nobody@nourl.com')

import os
import shutil
import time
import datetime
import urllib
import logging

logging.basicConfig(format='%(message)s',level=logging.INFO)

class File(object):
    @classmethod
    def GetFileContent(self, file_path, mode='r'):
        fileContent = ""
        f = open(file_path, mode)
        fileContent = f.read()
        f.close()
        return fileContent

class Reporting(object):
    @classmethod
    def TestLog(self, message):
        '''Print info in the Report.html, Console and Jenkins output'''
        label_timestamp = "[" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S] TEST_LOG: ')

        # print in console and Jenkins
        message_console_jenkins = str(label_timestamp) + str(message)
        logging.info(message_console_jenkins)
        
        # print in Report.html
        message_report_html = str(label_timestamp) + str(message) # May need to use RemoveNonASCIIchar function
        print(message_report_html)

class Network(object):
    @classmethod
    def DownloadFile(self, download_url, destination):
        try:
            if os.path.exists(destination):
                os.remove(destination)

            urllib.urlretrieve(download_url, destination)
        except Exception as ex:
            print("Download failed!")
            print("Exception: " + str(ex))

class String(object):
    @classmethod
    def RemoveNonASCIIchar(self, text):
        '''Removes chars>128'''
        if isinstance(text, (int, long)):
            text = str(text)
        return "".join(i for i in text if ord(i) < 128)



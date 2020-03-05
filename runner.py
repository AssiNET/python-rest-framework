import sys
import os
import time
import datetime
import shutil
import argparse
import logging
logging.basicConfig(format='%(message)s',level=logging.INFO)
import tests.lib.rest_lib as rest_lib
import tests.lib.common_lib as common_lib

def RunTestSet(test_set):
    if ".py" in test_set:
        command = 'python ' + test_set
        logging.info("###########################")
        logging.info("######### COMMAND #########")
        logging.info(command)
        logging.info("########### END ###########")
        os.system(command)
    else:
        logging.info("Test set: " + test_set + " is NOT found!")

def CreateResultDir():
    if not DEBUG:
        if not os.path.exists(RESULTS_DIR):
            os.mkdir(RESULTS_DIR)

        timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S_"))
        latest_results_dir_name = timestamp + TEST_SUITE_NAME
        latest_results_dir_path = os.path.join(ROOT_DIR, RESULTS_DIR, latest_results_dir_name)
        os.mkdir(latest_results_dir_path)
        return latest_results_dir_path

def CopyResults(destinations):
    # HTML
    if os.path.exists(REPORT_HTML_FILE):
        shutil.copy(REPORT_HTML_FILE, destinations)

    # XML
    if os.path.exists(REPORT_XML_FILE):
        shutil.copy(REPORT_XML_FILE, destinations)


parser = argparse.ArgumentParser()
parser.add_argument("--set", help="echo the string you use here")
parser.add_argument("--debug", action="store_true", default=False)
args = parser.parse_args()
print args

TEST_SUITE_NAME = args.set
DEBUG = args.debug # default is False

# SET Paths
ROOT_DIR = os.getcwd() 
TOOLS_DIR = os.path.join(ROOT_DIR, 'tools')
RESULTS_DIR = os.path.join(ROOT_DIR, 'results')
CURRENT_TESTS_DIR = os.path.join(ROOT_DIR, 'tests', TEST_SUITE_NAME)
LATEST_RESULTS_DIR = CreateResultDir()

REPORT_HTML_FILE = os.path.join(ROOT_DIR, "Report.html")
REPORT_XML_FILE = os.path.join(ROOT_DIR, "Report.xml")

###########################################################
RunTestSet(CURRENT_TESTS_DIR)
###########################################################

CopyResults(LATEST_RESULTS_DIR)
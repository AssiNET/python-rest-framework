import unittest
import json
from lib import *
import lib.HtmlXmlTestRunner_pkg.HtmlXmlTestRunner as HtmlXmlTestRunner
import lib.rest_lib as restlib
import lib.common_lib as commonlib
import logging

URL_WEATHER_SERVICE = 'http://api.openweathermap.org'

class SmokeTests(unittest.TestCase):

    def setUp(self):
        print("")
        print("##############################################################")
        print("#####", self.id())
        print("##############################################################")

    def test_001_CheckTemperature(self):
        url = URL_WEATHER_SERVICE + '/data/2.5/weather?q=Sofia&appid=52d0bc04ffab9819a4b3900533f16f30&units=metric'
        headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip,deflate',
            'Content-Type': 'application/json'
        }

        response, content = restlib.POST(url, headers, body='')
        assert (response.status == 200)

        data = json.loads(content)
        commonlib.Reporting.TestLog(data)

        temp = data["main"]["temp"]
        assert (-30 < temp < 50)

        # Logging into console/terminal
        commonlib.Reporting.TestLog("Response Status: " + str(response.status))
        commonlib.Reporting.TestLog("Temp in Sofia: " + str(temp))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)

    #Use it to add manually test cases - handy when debugging a specific part of the set
	#suite = unittest.TestSuite()
    #suite.addTest(SmokeTests('test_001_CheckTemperature'))
    #suite.addTest(SmokeTests('FREE_SLOT_FOR_THE_NEXT_TEST'))

    outfile = open("Report.html", "w")
    runner = HtmlXmlTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report', description="Some descr")
    runner.run(suite)
    outfile.close()

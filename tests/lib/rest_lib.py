import httplib2 as http
import json
import time
import logging
logging.basicConfig(format='%(message)s',level=logging.INFO)

def PrintStringOrJson(contentType, content):
    # make sure all special chars are removed
    content = ''.join([i if 31 < ord(i) < 127 else ' ' for i in content])
    try:
        jsonContent = json.loads(content)
    except:
        print contentType + ": "
        print str(content)
    else:
        print contentType + "(JSON): "
        print json.dumps(jsonContent, sort_keys=True, indent=4, separators=(',', ': '))

def SendRequest(url, method, headers, body, printContent=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    conn = http.Http(timeout=200, disable_ssl_certificate_validation=True)
    print "##############################################################"
    print "#######################  REQUEST START  ###################### "
    
    request = ('{}\n{}'.format(
        method + ' ' + url + ' HTTP/1.1',
        '\n'.join('{}: {}'.format(k, v) for k, v in headers.items()),
    ))
    print(request)
    if printContent:
        PrintStringOrJson("REQUEST BODY", body)
    #  Follows the format 001_c.txt, 'c' - request file
    print "------SEND REQUEST-------"
    startRequest = time.time()
    response, content = conn.request(url, method, body, headers, redirections=redirects)

    receiveResponse = time.time()
    elapsedTime = receiveResponse - startRequest
    print "##############################################################"
    print "##########################  RESPONSE  ######################## "
    #  Delete 'transfer-encoding' header in the saz file, because the responce is already decoded in the test run
    if 'transfer-encoding' in response:
        del response['transfer-encoding']
    responseFormat = ('{}\n{}'.format(
        'HTTP/1.1 ' + str(response.status) + ' ' + response.reason,
        '\n'.join('{}: {}'.format(k, v) for k, v in response.items()),
    ))
    print "RESPONSE STATUS: " + str(response.status)
    print responseFormat
    content = '\n\n{}'.format(content)
    if printContent:
        PrintStringOrJson("RESPONSE CONTENT", content)
    #  Follows the format 001_s.txt, 's' - response file
    print "ELAPSED TIME: " + str(elapsedTime)
    print "########################  REQUEST END  ###################### "
    print "##############################################################"
    return (response, content)

def POST(url, headers, body, printContent=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'POST', headers, body, printContent, redirects)

def GET(url, headers, printContent=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'GET', headers, "", printContent, redirects)

def HEAD(url, headers, printContent=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'HEAD', headers, "", printContent, redirects)

def PUT(url, headers, body="", printContent=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'PUT', headers, body, printContent, redirects)

def DELETE(url, headers, printContent=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'DELETE', headers, "", printContent, redirects)

def COPY(url, headers, body, printContent=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'COPY', headers, body, printContent, redirects)

def PATCH(url, headers, body, printContent=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'PATCH', headers, body, printContent, redirects)

def MOVE(url, headers, body, printContent=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'MOVE', headers, body, printContent, redirects)

def INIT(url, headers, printContent=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'INIT', headers, "", printContent, redirects)

def ADD(url, headers, body, printContent=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'ADD', headers, body, printContent, redirects)


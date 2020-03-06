import httplib2 as http
import json
import time
import logging
logging.basicConfig(format='%(message)s',level=logging.INFO)

def PrintStringOrJson(content_type, content):
    # make sure all special chars are removed
    content = ''.join([i if 31 < ord(i) < 127 else ' ' for i in content])
    try:
        json_content = json.loads(content)
    except Exception as ex:
        print("Json loads failed")
        print("Exception: " + str(ex))
    else:
        print(content_type + "(JSON): ")
        print(json.dumps(json_content, sort_keys=True, indent=4, separators=(',', ': ')))

def SendRequest(url, method, headers, body, print_content=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    conn = http.Http(timeout=200, disable_ssl_certificate_validation=True)
    print "##############################################################"
    print "#######################  REQUEST START  ###################### "
    
    request = ('{}\n{}'.format(
        method + ' ' + url + ' HTTP/1.1',
        '\n'.join('{}: {}'.format(k, v) for k, v in headers.items()),
    ))
    print(request)
    if print_content:
        PrintStringOrJson("REQUEST BODY", body)
    #  Follows the format 001_c.txt, 'c' - request file
    print("------SEND REQUEST-------")
    start_request = time.time()
    response, content = conn.request(url, method, body, headers, redirections=redirects)

    receive_response = time.time()
    elapsed_time = receive_response - start_request
    print("##############################################################")
    print("##########################  RESPONSE  ######################## ")
    #  Delete 'transfer-encoding' header in the saz file, because the responce is already decoded in the test run
    if 'transfer-encoding' in response:
        del response['transfer-encoding']
    response_format = ('{}\n{}'.format(
        'HTTP/1.1 ' + str(response.status) + ' ' + response.reason,
        '\n'.join('{}: {}'.format(k, v) for k, v in response.items()),
    ))
    print("RESPONSE STATUS: " + str(response.status))
    print(response_format)
    content = '\n\n{}'.format(content)
    if print_content:
        PrintStringOrJson("RESPONSE CONTENT", content)
    #  Follows the format 001_s.txt, 's' - response file
    print("ELAPSED TIME: " + str(elapsed_time))
    print("########################  REQUEST END  ###################### ")
    print("##############################################################")
    return (response, content)

def POST(url, headers, body, print_content=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'POST', headers, body, print_content, redirects)

def GET(url, headers, print_content=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'GET', headers, "", print_content, redirects)

def HEAD(url, headers, print_content=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'HEAD', headers, "", print_content, redirects)

def PUT(url, headers, body="", print_content=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'PUT', headers, body, print_content, redirects)

def DELETE(url, headers, print_content=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'DELETE', headers, "", print_content, redirects)

def COPY(url, headers, body, print_content=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'COPY', headers, body, print_content, redirects)

def PATCH(url, headers, body, print_content=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'PATCH', headers, body, print_content, redirects)

def MOVE(url, headers, body, print_content=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'MOVE', headers, body, print_content, redirects)

def INIT(url, headers, print_content=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'INIT', headers, "", print_content, redirects)

def ADD(url, headers, body, print_content=True, redirects=http.DEFAULT_MAX_REDIRECTS):
    return SendRequest(url, 'ADD', headers, body, print_content, redirects)


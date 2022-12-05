#!/usr/bin/env python
#
# Author: 
# Purpose: 
# version: 

from __future__ import print_function
from builtins import str
import sys, requests, datetime, os, time, logging
import json
import base64
import logging.config
import math
import concurrent.futures
import argparse
#import os.path
from os import path

# setup_http_session sets up global http session variable for HTTP connection sharing
def setup_http_session():
    global httpSession

    httpSession = requests.Session()

# setup_credentials builds HTTP auth string and base64 encodes it to minimize recalculation
def setup_credentials(username, password, URL):
    global token

    authURL = URL + "/auth"
    usrPass = str(username)+':'+str(password)
    usrPassBytes = bytes(usrPass, "utf-8")
    httpCredentials = base64.b64encode(usrPassBytes).decode("utf-8")
    authBody = "username="+ str(username) + "&password=" + str(password) + "&token=true&permissions=true"

    authHeader = {"Content-Type": "application/x-www-form-urlencoded"}
    response=httpSession.post(authURL, headers=authHeader, data=authBody, verify=True)
    token = response.text
    print("Token = {}".format(str(token)))

def setup_logging(default_path='./config/logging.yml',default_level=logging.INFO,env_key='LOG_CFG'):
    """Setup logging configuration"""
    if not os.path.exists("log"):
        os.makedirs("log")
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


# Called to read in ./config.yml

    

# Get call for API queries to return json data and status code
def Get_Call(token,URL):

    headers = {
        'Accept': '*/*',
        'content-type': 'application/json',
        'Authorization': "Bearer %s" % token
    }

    r = httpSession.get(URL, headers=headers, verify=True)
    logger.debug("Repsonse code for GET to {0} - Response Code {1}".format(str(URL),str(r.status_code)))
    logger.debug("API Data for Response \n {}".format(str(r.text[:10000])))
    
 #  image_list_data, image_list_status = Get_Call(token,image_list_pull_URL)

parser = argparse.ArgumentParser()
parser.add_argument("--example", "-i", help="example", action="store_true")


args = parser.parse_args()

if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    URL = "https://gateway.qg2.apps.qualys.com"
    try:
        username = os.environ["QUALYS_API_USERNAME"]
            #password = base64.b64decode(os.environ["QUALYS_API_PASSWORD"])
        password = os.environ["QUALYS_API_PASSWORD"]

        logger.debug('Username: {0} Password: {1} \n'.format(str(username), str(password)))
 
    except Exception as e:
        logger.critical("Exception {0}".format(str(e)))
        sys.exit(1)

    setup_http_session()
    setup_credentials(username, password, URL)
 

    import requests
    from requests.structures import CaseInsensitiveDict

    url = URL + "/auth"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    usrPass = str(username)+':'+str(password)
    usrPassBytes = bytes(usrPass, "utf-8")
    httpCredentials = base64.b64encode(usrPassBytes).decode("utf-8")
    authBody = "username="+ str(username) + "&password=" + str(password) + "&token=true&permissions=true"

    


    resp = requests.post(url, headers=headers, data=authBody)
    print("---------------------")
    # print(resp.status_code)
    print("Response Code \n {}".format(str(resp.status_code)))
    print("Response Content \n {}".format(str(resp.content)))
  
    # resp = requests.get(url, headers=headers)

    # print(resp.status_code)
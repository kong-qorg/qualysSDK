from __future__ import print_function
import time
import QualysAPI
from QualysAPI.rest import ApiException
from pprint import pprint
from QualysAPI.configuration import Configuration
import base64, os
from QualysAPI.models import repositories
# https://gateway.qg2.apps.qualys.com/apidocs/yaml/csapi-swagger-v1.3.yaml



try:
    import requests
    from requests.structures import CaseInsensitiveDict
    URL = "https://gateway.qg2.apps.qualys.com"
    url = URL + "/auth"
    username = "real_username"
    password = "real_password"
    # try:
    #     username = os.environ["QUALYS_API_USERNAME"]
    #         #password = base64.b64decode(os.environ["QUALYS_API_PASSWORD"])
    #     password = os.environ["QUALYS_API_PASSWORD"]
      
    #     #print('Username: {0} Password: {1} \n'.format(str(username), str(password)))
 
    # except Exception as e:
    #     print("Exception {0}".format(str(e)))
     

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    usrPass = str(username)+':'+str(password)
    usrPassBytes = bytes(usrPass, "utf-8")
    httpCredentials = base64.b64encode(usrPassBytes).decode("utf-8")
    authBody = "username="+ str(username) + "&password=" + str(password) + "&token=true&permissions=true"

    


    resp = requests.post(url, headers=headers, data=authBody)

    # print("Response Code \n {}".format(str(resp.status_code)))
    # print("Response Content \n {}".format(str(resp.content)))

    config = QualysAPI.Configuration()
    config.host = 'https://gateway.qg2.apps.qualys.com/csapi/v1.3'
    config.debug = False  
    config.logger_file = './log.txt'
    
  

    header_params = {'Authorization: Bearer': str(resp.content.decode('UTF-8'))}
    Token= str(resp.content.decode('UTF-8'))

    api_client = QualysAPI.ApiClient(config)
    api_client.user_agent = "TstAgent"
    
    api_client.set_default_header("Authorization" ,"Bearer " + Token)
    
    # create an instance of the API class
    api_instance = QualysAPI.RegistryApi(api_client)
  #  api_instance.getr
  
    api_response = api_instance.get_cs_registry_repositories("72cbe7ca-0cdf-4083-8c7d-20f1ed9896f8")
    # Sensor Activation API
    repos = QualysAPI.Registries(api_response)
  
    
    print(" repos.count : {}".format(str( repos.count)))
    print(" repos.data : {}".format(str( repos.data)))


   # pprint(repos)
except ApiException as e:
    print("Exception when calling API: %s\n" % e)

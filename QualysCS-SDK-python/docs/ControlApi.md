# QualysCSAPI.ControlApi

All URIs are relative to *https://gateway.qg2.apps.qualys.com/csapi/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cs_controls_data_using_get**](ControlApi.md#get_cs_controls_data_using_get) | **GET** /controls/{controlId} | Show details of control
[**get_cs_controls_list**](ControlApi.md#get_cs_controls_list) | **GET** /controls | Show list of controls

# **get_cs_controls_data_using_get**
> PcControl get_cs_controls_data_using_get(control_id)

Show details of control

Show details of control

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ControlApi(QualysCSAPI.ApiClient(configuration))
control_id = 'control_id_example' # str | Specify ID of control

try:
    # Show details of control
    api_response = api_instance.get_cs_controls_data_using_get(control_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControlApi->get_cs_controls_data_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_id** | **str**| Specify ID of control | 

### Return type

[**PcControl**](PcControl.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_controls_list**
> PcControls get_cs_controls_list(filter=filter, page_number=page_number, page_size=page_size, sort=sort)

Show list of controls

Show list of controls

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ControlApi(QualysCSAPI.ApiClient(configuration))
filter = '' # str | Filter the containers list by providing a query using Qualys syntax. (optional)
page_number = 1 # int | The page to be returned. (optional) (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (optional) (default to 50)
sort = 'sort_example' # str | Sort the results using a Qualys token. (optional)

try:
    # Show list of controls
    api_response = api_instance.get_cs_controls_list(filter=filter, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControlApi->get_cs_controls_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter the containers list by providing a query using Qualys syntax. | [optional] 
 **page_number** | **int**| The page to be returned. | [optional] [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [optional] [default to 50]
 **sort** | **str**| Sort the results using a Qualys token. | [optional] 

### Return type

[**PcControls**](PcControls.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


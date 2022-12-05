# QualysCSAPI.ActivationApi

All URIs are relative to *https://gateway.qg2.apps.qualys.com/csapi/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sensor_activation_keys**](ActivationApi.md#get_sensor_activation_keys) | **GET** /activationkey | Sensor Activation API

# **get_sensor_activation_keys**
> Activation get_sensor_activation_keys()

Sensor Activation API

Returns customerId, activationId, platformUrl which is required to activate CS sensor.

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ActivationApi(QualysCSAPI.ApiClient(configuration))

try:
    # Sensor Activation API
    api_response = api_instance.get_sensor_activation_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivationApi->get_sensor_activation_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Activation**](Activation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


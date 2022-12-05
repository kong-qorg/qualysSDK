# QualysCSAPI.SensorApi

All URIs are relative to *https://gateway.qg2.apps.qualys.com/csapi/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cs_sensors**](SensorApi.md#delete_cs_sensors) | **DELETE** /sensors | Delete sensors in your account
[**get_cs_sensor_details**](SensorApi.md#get_cs_sensor_details) | **GET** /sensors/{sensorId} | Show details of a sensor
[**get_cs_sensors_list**](SensorApi.md#get_cs_sensors_list) | **GET** /sensors | Show a list of sensors in your account.

# **delete_cs_sensors**
> str delete_cs_sensors(sensor_ids=sensor_ids, filter=filter)

Delete sensors in your account

Provide one or more sensor Ids or filters in the format shown under Example Value

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.SensorApi(QualysCSAPI.ApiClient(configuration))
sensor_ids = ['sensor_ids_example'] # list[str] | delete the sensors from uuid (optional)
filter = 'filter_example' # str | delete the sensors from filter (optional)

try:
    # Delete sensors in your account
    api_response = api_instance.delete_cs_sensors(sensor_ids=sensor_ids, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorApi->delete_cs_sensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_ids** | [**list[str]**](str.md)| delete the sensors from uuid | [optional] 
 **filter** | **str**| delete the sensors from filter | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_sensor_details**
> Sensor get_cs_sensor_details(sensor_id)

Show details of a sensor

Show details of a sensor

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.SensorApi(QualysCSAPI.ApiClient(configuration))
sensor_id = 'sensor_id_example' # str | Specify the sensor ID of a specific sensor in the user???s scope

try:
    # Show details of a sensor
    api_response = api_instance.get_cs_sensor_details(sensor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorApi->get_cs_sensor_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_id** | **str**| Specify the sensor ID of a specific sensor in the user???s scope | 

### Return type

[**Sensor**](Sensor.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_sensors_list**
> Sensors get_cs_sensors_list(filter=filter, page_number=page_number, page_size=page_size, sort=sort)

Show a list of sensors in your account.

Show a list of sensors in your account.

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.SensorApi(QualysCSAPI.ApiClient(configuration))
filter = 'filter_example' # str | Filter the sensors list by providing a query using Qualys syntax. (optional)
page_number = 1 # int | The page to be returned. (optional) (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (optional) (default to 50)
sort = 'sort_example' # str | Sort the results using a Qualys token. (optional)

try:
    # Show a list of sensors in your account.
    api_response = api_instance.get_cs_sensors_list(filter=filter, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorApi->get_cs_sensors_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter the sensors list by providing a query using Qualys syntax. | [optional] 
 **page_number** | **int**| The page to be returned. | [optional] [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [optional] [default to 50]
 **sort** | **str**| Sort the results using a Qualys token. | [optional] 

### Return type

[**Sensors**](Sensors.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


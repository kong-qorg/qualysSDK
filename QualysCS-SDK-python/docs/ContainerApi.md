# QualysCSAPI.ContainerApi

All URIs are relative to *https://gateway.qg2.apps.qualys.com/csapi/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cs_containers**](ContainerApi.md#delete_cs_containers) | **DELETE** /containers | Delete containers in your account
[**get_container_details_using_get**](ContainerApi.md#get_container_details_using_get) | **GET** /containers/{containerSha} | show details of a container
[**get_container_list_with_details**](ContainerApi.md#get_container_list_with_details) | **GET** /containers/list | Containers Bulk API
[**get_container_policy_compliance_details_using_get**](ContainerApi.md#get_container_policy_compliance_details_using_get) | **GET** /containers/{containerSha}/compliance | show policy compliance details of a container
[**get_container_software_using_get**](ContainerApi.md#get_container_software_using_get) | **GET** /containers/{containerSha}/software | Show software installed on a container
[**get_container_vuln_count_using_get**](ContainerApi.md#get_container_vuln_count_using_get) | **GET** /containers/{containerSha}/vuln/count | Show vulnerability count for a container
[**get_container_vuln_using_get**](ContainerApi.md#get_container_vuln_using_get) | **GET** /containers/{containerSha}/vuln | Show vulnerability details for a container
[**get_cs_containers_data_using_get**](ContainerApi.md#get_cs_containers_data_using_get) | **GET** /containers | Show a list of containers in your account

# **delete_cs_containers**
> str delete_cs_containers(container_ids=container_ids, filter=filter)

Delete containers in your account

Provide one or more container Ids or filters in the format shown under Example Value.

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ContainerApi(QualysCSAPI.ApiClient(configuration))
container_ids = ['container_ids_example'] # list[str] | delete the containers from uuid (optional)
filter = 'filter_example' # str | delete the containers from filter (optional)

try:
    # Delete containers in your account
    api_response = api_instance.delete_cs_containers(container_ids=container_ids, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->delete_cs_containers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_ids** | [**list[str]**](str.md)| delete the containers from uuid | [optional] 
 **filter** | **str**| delete the containers from filter | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_details_using_get**
> ContainerDetails get_container_details_using_get(container_sha)

show details of a container

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ContainerApi(QualysCSAPI.ApiClient(configuration))
container_sha = 'container_sha_example' # str | Specify the SHA value of a Container in the user???s scope.

try:
    # show details of a container
    api_response = api_instance.get_container_details_using_get(container_sha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_sha** | **str**| Specify the SHA value of a Container in the user???s scope. | 

### Return type

[**ContainerDetails**](ContainerDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_list_with_details**
> BulkContainerDetailsList get_container_list_with_details(filter=filter, pagination_query=pagination_query, limit=limit)

Containers Bulk API

Returns response with given number of Container records according to filter along with next page filter query.

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ContainerApi(QualysCSAPI.ApiClient(configuration))
filter = '' # str | Filter the containers list by providing a query using Qualys syntax. (optional)
pagination_query = 'pagination_query_example' # str | The next page filter query. (optional)
limit = 50 # int | The number of records per page to be included in the response. (optional) (default to 50)

try:
    # Containers Bulk API
    api_response = api_instance.get_container_list_with_details(filter=filter, pagination_query=pagination_query, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_list_with_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter the containers list by providing a query using Qualys syntax. | [optional] 
 **pagination_query** | **str**| The next page filter query. | [optional] 
 **limit** | **int**| The number of records per page to be included in the response. | [optional] [default to 50]

### Return type

[**BulkContainerDetailsList**](BulkContainerDetailsList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_policy_compliance_details_using_get**
> PolicyComplianceDetails get_container_policy_compliance_details_using_get(container_sha)

show policy compliance details of a container

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ContainerApi(QualysCSAPI.ApiClient(configuration))
container_sha = 'container_sha_example' # str | Specify the SHA value of a Container in the user???s scope.

try:
    # show policy compliance details of a container
    api_response = api_instance.get_container_policy_compliance_details_using_get(container_sha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_policy_compliance_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_sha** | **str**| Specify the SHA value of a Container in the user???s scope. | 

### Return type

[**PolicyComplianceDetails**](PolicyComplianceDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_software_using_get**
> ContainerSoftware get_container_software_using_get(container_sha, filter=filter, sort=sort, is_drift=is_drift)

Show software installed on a container

Show software installed on a container

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ContainerApi(QualysCSAPI.ApiClient(configuration))
container_sha = 'container_sha_example' # str | Specify the SHA value of a Container in the user???s scope.
filter = '' # str | Filter the containers list by providing a query using Qualys syntax. (optional)
sort = 'name:asc' # str | Sort the results using a Qualys token. For example name:asc (optional) (default to name:asc)
is_drift = false # bool |  (optional) (default to false)

try:
    # Show software installed on a container
    api_response = api_instance.get_container_software_using_get(container_sha, filter=filter, sort=sort, is_drift=is_drift)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_software_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_sha** | **str**| Specify the SHA value of a Container in the user???s scope. | 
 **filter** | **str**| Filter the containers list by providing a query using Qualys syntax. | [optional] 
 **sort** | **str**| Sort the results using a Qualys token. For example name:asc | [optional] [default to name:asc]
 **is_drift** | **bool**|  | [optional] [default to false]

### Return type

[**ContainerSoftware**](ContainerSoftware.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_vuln_count_using_get**
> object get_container_vuln_count_using_get(container_sha)

Show vulnerability count for a container

Show vulnerability count for a container

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ContainerApi(QualysCSAPI.ApiClient(configuration))
container_sha = 'container_sha_example' # str | Specify the SHA value of a Container in the user???s scope.

try:
    # Show vulnerability count for a container
    api_response = api_instance.get_container_vuln_count_using_get(container_sha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_vuln_count_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_sha** | **str**| Specify the SHA value of a Container in the user???s scope. | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_vuln_using_get**
> ContainerVuln get_container_vuln_using_get(container_sha, filter=filter, type=type, is_drift=is_drift)

Show vulnerability details for a container

Show vulnerability details for a container

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ContainerApi(QualysCSAPI.ApiClient(configuration))
container_sha = 'container_sha_example' # str | Specify the SHA value of a Container in the user???s scope.
filter = 'filter_example' # str | Filter the container vulnerability details by providing a query using Qualys syntax. (optional)
type = 'ALL' # str |  (optional) (default to ALL)
is_drift = false # bool |  (optional) (default to false)

try:
    # Show vulnerability details for a container
    api_response = api_instance.get_container_vuln_using_get(container_sha, filter=filter, type=type, is_drift=is_drift)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_container_vuln_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_sha** | **str**| Specify the SHA value of a Container in the user???s scope. | 
 **filter** | **str**| Filter the container vulnerability details by providing a query using Qualys syntax. | [optional] 
 **type** | **str**|  | [optional] [default to ALL]
 **is_drift** | **bool**|  | [optional] [default to false]

### Return type

[**ContainerVuln**](ContainerVuln.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_containers_data_using_get**
> Containers get_cs_containers_data_using_get(filter=filter, page_number=page_number, page_size=page_size, sort=sort)

Show a list of containers in your account

Show a list of containers in your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ContainerApi(QualysCSAPI.ApiClient(configuration))
filter = '' # str | Filter the containers list by providing a query using Qualys syntax. (optional)
page_number = 1 # int | The page to be returned. (optional) (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (optional) (default to 50)
sort = 'created:desc' # str | Sort the results using a Qualys token. (optional) (default to created:desc)

try:
    # Show a list of containers in your account
    api_response = api_instance.get_cs_containers_data_using_get(filter=filter, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainerApi->get_cs_containers_data_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter the containers list by providing a query using Qualys syntax. | [optional] 
 **page_number** | **int**| The page to be returned. | [optional] [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [optional] [default to 50]
 **sort** | **str**| Sort the results using a Qualys token. | [optional] [default to created:desc]

### Return type

[**Containers**](Containers.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


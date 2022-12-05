# QualysCSAPI.RegistryApi

All URIs are relative to *https://gateway.qg2.apps.qualys.com/csapi/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_bulk_cs_registry_schedules**](RegistryApi.md#cancel_bulk_cs_registry_schedules) | **POST** /registry/{registryId}/schedule/cancel | Cancel multiple registry schedules in your account.
[**cancel_cs_registry_schedule**](RegistryApi.md#cancel_cs_registry_schedule) | **POST** /registry/{registryId}/schedule/{scheduleId}/cancel | Cancel registry schedule in your account.
[**create_cs_acr_connector**](RegistryApi.md#create_cs_acr_connector) | **POST** /registry/acr/connector | Create new ACR connector
[**create_cs_aws_connector**](RegistryApi.md#create_cs_aws_connector) | **POST** /registry/aws/connector | Create new AWS connector
[**create_cs_gcp_connector**](RegistryApi.md#create_cs_gcp_connector) | **POST** /registry/gcp/connector | Create new GCP connector
[**create_cs_registry**](RegistryApi.md#create_cs_registry) | **POST** /registry | Create a new registry
[**create_cs_registry_schedule**](RegistryApi.md#create_cs_registry_schedule) | **POST** /registry/{registryId}/schedule | Create a new Registry scan schedule
[**delete_bulk_schedules**](RegistryApi.md#delete_bulk_schedules) | **DELETE** /registry/{registryId}/schedule/bulk | Delete bulk registry schedules in your account.
[**delete_cs_registries**](RegistryApi.md#delete_cs_registries) | **DELETE** /registry | Delete multiple registries in your account
[**delete_cs_registry**](RegistryApi.md#delete_cs_registry) | **DELETE** /registry/{registryId} | Delete registry in you account
[**delete_cs_registry_schedule**](RegistryApi.md#delete_cs_registry_schedule) | **DELETE** /registry/{registryId}/schedule/{scheduleId} | Delete registry schedule in your account
[**delete_cs_registry_schedules**](RegistryApi.md#delete_cs_registry_schedules) | **DELETE** /registry/{registryId}/schedule | Delete multiple registry schedules in your account
[**get_cs_acr_connectors_by_aws_account_id_using_get**](RegistryApi.md#get_cs_acr_connectors_by_aws_account_id_using_get) | **GET** /registry/acr/connector/{connectorId} | Show ACR connector details
[**get_cs_acr_connectors_list_using_get**](RegistryApi.md#get_cs_acr_connectors_list_using_get) | **GET** /registry/acr/connectors | Show list of ACR connectors in your account
[**get_cs_aws_account_id_using_get**](RegistryApi.md#get_cs_aws_account_id_using_get) | **GET** /registry/aws-base | Fetch AWS account ID and external ID for your account
[**get_cs_aws_connectors_by_aws_account_id_using_get**](RegistryApi.md#get_cs_aws_connectors_by_aws_account_id_using_get) | **GET** /registry/aws/connectors/{accountId} | Show list of AWS connectors for an AWS account ID
[**get_cs_aws_connectors_list_using_get**](RegistryApi.md#get_cs_aws_connectors_list_using_get) | **GET** /registry/aws/connectors | Show list of AWS connectors in your account
[**get_cs_aws_gov_account_id_using_get**](RegistryApi.md#get_cs_aws_gov_account_id_using_get) | **GET** /registry/aws-gov-base | Fetch AWS Gov account ID and external ID for your account
[**get_cs_gcp_connectors_by_gcp_connector_id_using_get**](RegistryApi.md#get_cs_gcp_connectors_by_gcp_connector_id_using_get) | **GET** /registry/gcp/connector/{connectorId} | Get GCP connector by connectorId
[**get_cs_gcp_connectors_list_using_get**](RegistryApi.md#get_cs_gcp_connectors_list_using_get) | **GET** /registry/gcp/connectors | Show list of GCP connectors in your account
[**get_cs_registries_data_using_get**](RegistryApi.md#get_cs_registries_data_using_get) | **GET** /registry | Show a list of registries in your account
[**get_cs_registry_details**](RegistryApi.md#get_cs_registry_details) | **GET** /registry/{registryId} | Show details of a registry
[**get_cs_registry_repositories**](RegistryApi.md#get_cs_registry_repositories) | **GET** /registry/{registryId}/repository | Show a list of repositories in a registry
[**get_cs_registry_schedules**](RegistryApi.md#get_cs_registry_schedules) | **GET** /registry/{registryId}/schedule | Show a list of schedules created for a registry
[**update_cs_registry**](RegistryApi.md#update_cs_registry) | **PUT** /registry/{registryId} | Update exiting registry in your account
[**update_cs_registry_schedule**](RegistryApi.md#update_cs_registry_schedule) | **PUT** /registry/{registryId}/schedule/{scheduleId} | Update existing registry schedule in your account
[**validate_cs_registry**](RegistryApi.md#validate_cs_registry) | **POST** /registry/validate | Validate information for new registry

# **cancel_bulk_cs_registry_schedules**
> str cancel_bulk_cs_registry_schedules(registry_id, schedule_ids=schedule_ids, filter=filter)

Cancel multiple registry schedules in your account.

Cancel multiple registry schedules in your account.

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
registry_id = 'registry_id_example' # str | Provide the ID/UUID of the registry you want to cancel the schedules for.
schedule_ids = ['schedule_ids_example'] # list[str] | Provide the ID/UUID of the schedules you want to cancel. You can only cancel schedules which are in the state: Created, Queued, Paused, Running, BaselineQueued or BaselineRunning (optional)
filter = 'filter_example' # str | Cancel the schdules from filter (optional)

try:
    # Cancel multiple registry schedules in your account.
    api_response = api_instance.cancel_bulk_cs_registry_schedules(registry_id, schedule_ids=schedule_ids, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->cancel_bulk_cs_registry_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID/UUID of the registry you want to cancel the schedules for. | 
 **schedule_ids** | [**list[str]**](str.md)| Provide the ID/UUID of the schedules you want to cancel. You can only cancel schedules which are in the state: Created, Queued, Paused, Running, BaselineQueued or BaselineRunning | [optional] 
 **filter** | **str**| Cancel the schdules from filter | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_cs_registry_schedule**
> str cancel_cs_registry_schedule(registry_id, schedule_id)

Cancel registry schedule in your account.

Cancel registry schedule in your account.

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
registry_id = 'registry_id_example' # str | Provide the ID/UUID of the registry you want to cancel the schedule for.
schedule_id = 'schedule_id_example' # str | Provide the ID/UUID of the schedule you want to cancel. You can only cancel schedules which are in the state: Created, Queued, Paused, Running, BaselineQueued or BaselineRunning

try:
    # Cancel registry schedule in your account.
    api_response = api_instance.cancel_cs_registry_schedule(registry_id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->cancel_cs_registry_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID/UUID of the registry you want to cancel the schedule for. | 
 **schedule_id** | **str**| Provide the ID/UUID of the schedule you want to cancel. You can only cancel schedules which are in the state: Created, Queued, Paused, Running, BaselineQueued or BaselineRunning | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cs_acr_connector**
> str create_cs_acr_connector(body)

Create new ACR connector

Create new ACR connector

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
body = QualysCSAPI.AcrConnectorRequest() # AcrConnectorRequest | Provide parameter values in the format shown under Example Value.

try:
    # Create new ACR connector
    api_response = api_instance.create_cs_acr_connector(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->create_cs_acr_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AcrConnectorRequest**](AcrConnectorRequest.md)| Provide parameter values in the format shown under Example Value. | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cs_aws_connector**
> str create_cs_aws_connector(body)

Create new AWS connector

Create new AWS connector

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
body = QualysCSAPI.AwsConnectorRequest() # AwsConnectorRequest | Provide parameter values in the format shown under Example Value. Specify accountType either Global or US_Gov.

try:
    # Create new AWS connector
    api_response = api_instance.create_cs_aws_connector(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->create_cs_aws_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AwsConnectorRequest**](AwsConnectorRequest.md)| Provide parameter values in the format shown under Example Value. Specify accountType either Global or US_Gov. | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cs_gcp_connector**
> str create_cs_gcp_connector(service_account_json, name, description=description, connector_id=connector_id)

Create new GCP connector

Create new GCP connector

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
service_account_json = 'service_account_json_example' # str | 
name = 'name_example' # str | Provide the name for the connector
description = 'description_example' # str | Provide the description for the connector (optional)
connector_id = 'connector_id_example' # str | Provide the connector id for the connector (optional)

try:
    # Create new GCP connector
    api_response = api_instance.create_cs_gcp_connector(service_account_json, name, description=description, connector_id=connector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->create_cs_gcp_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_account_json** | **str**|  | 
 **name** | **str**| Provide the name for the connector | 
 **description** | **str**| Provide the description for the connector | [optional] 
 **connector_id** | **str**| Provide the connector id for the connector | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cs_registry**
> str create_cs_registry(body)

Create a new registry

Create a new registry

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
body = QualysCSAPI.RegistryRequest() # RegistryRequest | Provide parameter values in the format shown under Example Value. Parameters accountId, arn, and region are required when the registryType is AWS ECR and you want to create a new AWS connector. Specify accountType either Global or US_Gov. Specify the ARN if you want to use an existing AWS connector, or if you want to create a new connector. All parameters are required other than dockerHubOrgName which is optional.

try:
    # Create a new registry
    api_response = api_instance.create_cs_registry(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->create_cs_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegistryRequest**](RegistryRequest.md)| Provide parameter values in the format shown under Example Value. Parameters accountId, arn, and region are required when the registryType is AWS ECR and you want to create a new AWS connector. Specify accountType either Global or US_Gov. Specify the ARN if you want to use an existing AWS connector, or if you want to create a new connector. All parameters are required other than dockerHubOrgName which is optional. | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cs_registry_schedule**
> str create_cs_registry_schedule(body, registry_id)

Create a new Registry scan schedule

Create a new Registry scan schedule

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
body = QualysCSAPI.ScheduleRequest() # ScheduleRequest | Provide parameter values in the format shown under Example Value. Specify "onDemand": true if you want to scan immediately. Otherwise, Automatic scan will be triggered based on the scan schedule. For OnDemand scan, use "days" to include images created a certain number of days ago (1-7 or 14 for last two weeks). For Automatic scan, use "scheduleIntervalInDays" to specify the scan recurrence in days (1-365). For example, scan every 1 day, every 7 days, every 30 days, etc. Use "schedule" to specify the scan start time in UTC (e.g., 19:30) when scheduleIntervalInDays is set to 1. For JFrog Artifactory Private registry, use pushedDateFilter to filter the images to be scanned based on when each image was pushed into the repository being scanned. Enter "All" to scan all images pushed into the repository regardless of the pushed date or enter a valid integer value greater than 0 to only scan images pushed into the repository a set number of days ago.
registry_id = 'registry_id_example' # str | Provide the ID of the registry for which you want to scan.

try:
    # Create a new Registry scan schedule
    api_response = api_instance.create_cs_registry_schedule(body, registry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->create_cs_registry_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduleRequest**](ScheduleRequest.md)| Provide parameter values in the format shown under Example Value. Specify &quot;onDemand&quot;: true if you want to scan immediately. Otherwise, Automatic scan will be triggered based on the scan schedule. For OnDemand scan, use &quot;days&quot; to include images created a certain number of days ago (1-7 or 14 for last two weeks). For Automatic scan, use &quot;scheduleIntervalInDays&quot; to specify the scan recurrence in days (1-365). For example, scan every 1 day, every 7 days, every 30 days, etc. Use &quot;schedule&quot; to specify the scan start time in UTC (e.g., 19:30) when scheduleIntervalInDays is set to 1. For JFrog Artifactory Private registry, use pushedDateFilter to filter the images to be scanned based on when each image was pushed into the repository being scanned. Enter &quot;All&quot; to scan all images pushed into the repository regardless of the pushed date or enter a valid integer value greater than 0 to only scan images pushed into the repository a set number of days ago. | 
 **registry_id** | **str**| Provide the ID of the registry for which you want to scan. | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bulk_schedules**
> str delete_bulk_schedules(registry_id, schedule_ids=schedule_ids, filter=filter)

Delete bulk registry schedules in your account.

Delete bulk registry schedules in your account. You can only delete the schedules which are in state: Finished, Error, Failed, Canceled. If both scheduleIds and filter are provided, deletion will be performed using scheduleIds.

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
registry_id = 'registry_id_example' # str | Provide the ID/UUID of the registry you want to delete the schedules for.
schedule_ids = ['schedule_ids_example'] # list[str] | Provide the ID/UUID of the schedules you want to delete. (optional)
filter = 'filter_example' # str | Delete the schedules using filter query. All the schedules matching the filter query will be deleted. (optional)

try:
    # Delete bulk registry schedules in your account.
    api_response = api_instance.delete_bulk_schedules(registry_id, schedule_ids=schedule_ids, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->delete_bulk_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID/UUID of the registry you want to delete the schedules for. | 
 **schedule_ids** | [**list[str]**](str.md)| Provide the ID/UUID of the schedules you want to delete. | [optional] 
 **filter** | **str**| Delete the schedules using filter query. All the schedules matching the filter query will be deleted. | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cs_registries**
> str delete_cs_registries(registry_ids=registry_ids)

Delete multiple registries in your account

Delete multiple registries in your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
registry_ids = ['registry_ids_example'] # list[str] | delete the registries from uuid (optional)

try:
    # Delete multiple registries in your account
    api_response = api_instance.delete_cs_registries(registry_ids=registry_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->delete_cs_registries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_ids** | [**list[str]**](str.md)| delete the registries from uuid | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cs_registry**
> str delete_cs_registry(registry_id)

Delete registry in you account

Delete registry in you account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
registry_id = 'registry_id_example' # str | Provide the ID/UUID of the registry you want to delete. Note: You cannot delete a registry whose schedules are in ???Running??? state.

try:
    # Delete registry in you account
    api_response = api_instance.delete_cs_registry(registry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->delete_cs_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID/UUID of the registry you want to delete. Note: You cannot delete a registry whose schedules are in ???Running??? state. | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cs_registry_schedule**
> str delete_cs_registry_schedule(registry_id, schedule_id)

Delete registry schedule in your account

Delete registry schedule in your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
registry_id = 'registry_id_example' # str | Provide the ID of the registry you want to delete.
schedule_id = 'schedule_id_example' # str | Provide the ID/UUID of the schedule you want to delete. Note: You cannot delete a schedule which is in ???Running??? state.

try:
    # Delete registry schedule in your account
    api_response = api_instance.delete_cs_registry_schedule(registry_id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->delete_cs_registry_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID of the registry you want to delete. | 
 **schedule_id** | **str**| Provide the ID/UUID of the schedule you want to delete. Note: You cannot delete a schedule which is in ???Running??? state. | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cs_registry_schedules**
> str delete_cs_registry_schedules(registry_id, schedule_ids=schedule_ids)

Delete multiple registry schedules in your account

Delete multiple registry schedules in your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
registry_id = 'registry_id_example' # str | Provide the ID of the registry for which you want to delete.
schedule_ids = ['schedule_ids_example'] # list[str] | delete the schedules from uuid (optional)

try:
    # Delete multiple registry schedules in your account
    api_response = api_instance.delete_cs_registry_schedules(registry_id, schedule_ids=schedule_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->delete_cs_registry_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID of the registry for which you want to delete. | 
 **schedule_ids** | [**list[str]**](str.md)| delete the schedules from uuid | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_acr_connectors_by_aws_account_id_using_get**
> AcrConnector get_cs_acr_connectors_by_aws_account_id_using_get(connector_id)

Show ACR connector details

Show ACR connector details

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
connector_id = 'connector_id_example' # str | Provide the ACR connector Id to get connector details.

try:
    # Show ACR connector details
    api_response = api_instance.get_cs_acr_connectors_by_aws_account_id_using_get(connector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_cs_acr_connectors_by_aws_account_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| Provide the ACR connector Id to get connector details. | 

### Return type

[**AcrConnector**](AcrConnector.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_acr_connectors_list_using_get**
> list[AcrConnector] get_cs_acr_connectors_list_using_get()

Show list of ACR connectors in your account

Show list of ACR connectors in your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))

try:
    # Show list of ACR connectors in your account
    api_response = api_instance.get_cs_acr_connectors_list_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_cs_acr_connectors_list_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AcrConnector]**](AcrConnector.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_aws_account_id_using_get**
> AwsAccount get_cs_aws_account_id_using_get()

Fetch AWS account ID and external ID for your account

Fetch AWS account ID and external ID for your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))

try:
    # Fetch AWS account ID and external ID for your account
    api_response = api_instance.get_cs_aws_account_id_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_cs_aws_account_id_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AwsAccount**](AwsAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_aws_connectors_by_aws_account_id_using_get**
> list[AwsConnector] get_cs_aws_connectors_by_aws_account_id_using_get(account_id)

Show list of AWS connectors for an AWS account ID

Show list of AWS connectors for an AWS account ID

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
account_id = 'account_id_example' # str | Provide the AWS account Id to get a list of connectors.

try:
    # Show list of AWS connectors for an AWS account ID
    api_response = api_instance.get_cs_aws_connectors_by_aws_account_id_using_get(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_cs_aws_connectors_by_aws_account_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Provide the AWS account Id to get a list of connectors. | 

### Return type

[**list[AwsConnector]**](AwsConnector.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_aws_connectors_list_using_get**
> AwsConnector get_cs_aws_connectors_list_using_get()

Show list of AWS connectors in your account

Show list of AWS connectors in your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))

try:
    # Show list of AWS connectors in your account
    api_response = api_instance.get_cs_aws_connectors_list_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_cs_aws_connectors_list_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AwsConnector**](AwsConnector.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_aws_gov_account_id_using_get**
> AwsAccount get_cs_aws_gov_account_id_using_get()

Fetch AWS Gov account ID and external ID for your account

Fetch AWS Gov account ID and external ID for your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))

try:
    # Fetch AWS Gov account ID and external ID for your account
    api_response = api_instance.get_cs_aws_gov_account_id_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_cs_aws_gov_account_id_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AwsAccount**](AwsAccount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_gcp_connectors_by_gcp_connector_id_using_get**
> GcpConnector get_cs_gcp_connectors_by_gcp_connector_id_using_get(connector_id)

Get GCP connector by connectorId

Get GCP connector by connectorId

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
connector_id = 'connector_id_example' # str | Provide the GCP connector Id to get connector details.

try:
    # Get GCP connector by connectorId
    api_response = api_instance.get_cs_gcp_connectors_by_gcp_connector_id_using_get(connector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_cs_gcp_connectors_by_gcp_connector_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**| Provide the GCP connector Id to get connector details. | 

### Return type

[**GcpConnector**](GcpConnector.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_gcp_connectors_list_using_get**
> list[GcpConnector] get_cs_gcp_connectors_list_using_get()

Show list of GCP connectors in your account

Show list of GCP connectors in your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))

try:
    # Show list of GCP connectors in your account
    api_response = api_instance.get_cs_gcp_connectors_list_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_cs_gcp_connectors_list_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GcpConnector]**](GcpConnector.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_registries_data_using_get**
> Registries get_cs_registries_data_using_get(filter=filter, page_number=page_number, page_size=page_size, sort=sort)

Show a list of registries in your account

Show a list of registries in your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
filter = '' # str | Filter the registries list by providing a query using Qualys syntax. (optional)
page_number = 1 # int | The page to be returned. (optional) (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (optional) (default to 50)
sort = 'sort_example' # str | Sort the results using a Qualys token. (optional)

try:
    # Show a list of registries in your account
    api_response = api_instance.get_cs_registries_data_using_get(filter=filter, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_cs_registries_data_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter the registries list by providing a query using Qualys syntax. | [optional] 
 **page_number** | **int**| The page to be returned. | [optional] [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [optional] [default to 50]
 **sort** | **str**| Sort the results using a Qualys token. | [optional] 

### Return type

[**Registries**](Registries.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_registry_details**
> RegistryDetails get_cs_registry_details(registry_id)

Show details of a registry

Show details of a registry

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
registry_id = 'registry_id_example' # str | Provide the ID/UUID of the registry you want to fetch the details.

try:
    # Show details of a registry
    api_response = api_instance.get_cs_registry_details(registry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_cs_registry_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID/UUID of the registry you want to fetch the details. | 

### Return type

[**RegistryDetails**](RegistryDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_registry_repositories**
> Repositories get_cs_registry_repositories(registry_id, filter=filter, page_number=page_number, page_size=page_size, sort=sort)

Show a list of repositories in a registry

Show a list of repositories in a registry

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
registry_id = 'registry_id_example' # str | Provide the ID of the registry for which you want to list the repositories.
filter = 'filter_example' # str | Filter the repository list by providing a query using Qualys syntax. (optional)
page_number = 1 # int | The page to be returned. (optional) (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (optional) (default to 50)
sort = 'sort_example' # str | Sort the results using a Qualys token. (optional)

try:
    # Show a list of repositories in a registry
    api_response = api_instance.get_cs_registry_repositories(registry_id, filter=filter, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_cs_registry_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID of the registry for which you want to list the repositories. | 
 **filter** | **str**| Filter the repository list by providing a query using Qualys syntax. | [optional] 
 **page_number** | **int**| The page to be returned. | [optional] [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [optional] [default to 50]
 **sort** | **str**| Sort the results using a Qualys token. | [optional] 

### Return type

[**Repositories**](Repositories.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_registry_schedules**
> Schedules get_cs_registry_schedules(registry_id, filter=filter, page_number=page_number, page_size=page_size, sort=sort)

Show a list of schedules created for a registry

Show a list of schedules created for a registry

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
registry_id = 'registry_id_example' # str | Provide the ID of the registry for which you want to list the schedules.
filter = 'filter_example' # str | Filter the schedules list by providing a query using Qualys syntax. (optional)
page_number = 1 # int | The page to be returned. (optional) (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (optional) (default to 50)
sort = 'sort_example' # str | Sort the results using a Qualys token. (optional)

try:
    # Show a list of schedules created for a registry
    api_response = api_instance.get_cs_registry_schedules(registry_id, filter=filter, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->get_cs_registry_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| Provide the ID of the registry for which you want to list the schedules. | 
 **filter** | **str**| Filter the schedules list by providing a query using Qualys syntax. | [optional] 
 **page_number** | **int**| The page to be returned. | [optional] [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [optional] [default to 50]
 **sort** | **str**| Sort the results using a Qualys token. | [optional] 

### Return type

[**Schedules**](Schedules.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cs_registry**
> str update_cs_registry(body, registry_id)

Update exiting registry in your account

Update exiting registry in your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
body = QualysCSAPI.RegistryRequest() # RegistryRequest | Provide parameter values in the format shown under Example Value. Specify accountType either Global or US_Gov. registryType and registryUri are required even though they are not updatable.
registry_id = 'registry_id_example' # str | Provide the ID/UUID of the registry you want to update.

try:
    # Update exiting registry in your account
    api_response = api_instance.update_cs_registry(body, registry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->update_cs_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegistryRequest**](RegistryRequest.md)| Provide parameter values in the format shown under Example Value. Specify accountType either Global or US_Gov. registryType and registryUri are required even though they are not updatable. | 
 **registry_id** | **str**| Provide the ID/UUID of the registry you want to update. | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cs_registry_schedule**
> str update_cs_registry_schedule(body, registry_id, schedule_id)

Update existing registry schedule in your account

Update existing registry schedule in your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
body = QualysCSAPI.ScheduleRequest() # ScheduleRequest | Provide parameter values in the format shown under Example Value. Specify "onDemand": true if you want to scan immediately. Otherwise, Automatic scan will be triggered based on the scan schedule. For OnDemand scan, use "days" to include images created a certain number of days ago (1-7 or 14 for last two weeks). For Automatic scan, use "scheduleIntervalInDays" to specify the scan recurrence in days (1-365). For example, scan every 1 day, every 7 days, every 30 days, etc. Use "schedule" to specify the scan start time in UTC (e.g., 19:30) when scheduleIntervalInDays is set to 1. For JFrog Artifactory Private registry, use pushedDateFilter to filter the images to be scanned based on when each image was pushed into the repository being scanned. Enter "All" to scan all images pushed into the repository regardless of the pushed date or enter a valid integer value greater than 0 to only scan images pushed into the repository a set number of days ago.
registry_id = 'registry_id_example' # str | Provide the ID of the registry you want to update.
schedule_id = 'schedule_id_example' # str | Provide the ID/UUID of the schedule you want to update.

try:
    # Update existing registry schedule in your account
    api_response = api_instance.update_cs_registry_schedule(body, registry_id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->update_cs_registry_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduleRequest**](ScheduleRequest.md)| Provide parameter values in the format shown under Example Value. Specify &quot;onDemand&quot;: true if you want to scan immediately. Otherwise, Automatic scan will be triggered based on the scan schedule. For OnDemand scan, use &quot;days&quot; to include images created a certain number of days ago (1-7 or 14 for last two weeks). For Automatic scan, use &quot;scheduleIntervalInDays&quot; to specify the scan recurrence in days (1-365). For example, scan every 1 day, every 7 days, every 30 days, etc. Use &quot;schedule&quot; to specify the scan start time in UTC (e.g., 19:30) when scheduleIntervalInDays is set to 1. For JFrog Artifactory Private registry, use pushedDateFilter to filter the images to be scanned based on when each image was pushed into the repository being scanned. Enter &quot;All&quot; to scan all images pushed into the repository regardless of the pushed date or enter a valid integer value greater than 0 to only scan images pushed into the repository a set number of days ago. | 
 **registry_id** | **str**| Provide the ID of the registry you want to update. | 
 **schedule_id** | **str**| Provide the ID/UUID of the schedule you want to update. | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_cs_registry**
> bool validate_cs_registry(body)

Validate information for new registry

Validate information for new registry

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.RegistryApi(QualysCSAPI.ApiClient(configuration))
body = QualysCSAPI.RegistryRequest() # RegistryRequest | Validate parameters for a registry you intend to create. Provide parameter values in the format shown under Example Value. Parameters accountId, arn, and region are required when the registryType is AWS ECR and you want to create a new AWS connector. Specify accountType either Global or US_Gov. Specify the ARN if you want to use an existing AWS connector, or if you want to create a new connector. All parameters are required other than dockerHubOrgName which is optional.

try:
    # Validate information for new registry
    api_response = api_instance.validate_cs_registry(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->validate_cs_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegistryRequest**](RegistryRequest.md)| Validate parameters for a registry you intend to create. Provide parameter values in the format shown under Example Value. Parameters accountId, arn, and region are required when the registryType is AWS ECR and you want to create a new AWS connector. Specify accountType either Global or US_Gov. Specify the ARN if you want to use an existing AWS connector, or if you want to create a new connector. All parameters are required other than dockerHubOrgName which is optional. | 

### Return type

**bool**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


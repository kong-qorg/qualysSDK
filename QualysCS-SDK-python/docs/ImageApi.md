# QualysCSAPI.ImageApi

All URIs are relative to *https://gateway.qg2.apps.qualys.com/csapi/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cs_images**](ImageApi.md#delete_cs_images) | **DELETE** /images | Delete images in your account
[**get_cs_images_data_using_get**](ImageApi.md#get_cs_images_data_using_get) | **GET** /images | Show a list of images in your account
[**get_image_association_using_get**](ImageApi.md#get_image_association_using_get) | **GET** /images/{imageSha}/association | show associations of an image
[**get_image_details_using_get**](ImageApi.md#get_image_details_using_get) | **GET** /images/{imageSha} | show details of an image
[**get_image_list_with_details**](ImageApi.md#get_image_list_with_details) | **GET** /images/list | Images Bulk API
[**get_image_policy_compliance_details_using_get**](ImageApi.md#get_image_policy_compliance_details_using_get) | **GET** /images/{imageSha}/compliance | show policy compliance details of an image
[**get_image_registries_using_get**](ImageApi.md#get_image_registries_using_get) | **GET** /images/{imageSha}/associatedRegistries | Get associated registries with Image
[**get_image_software_using_get**](ImageApi.md#get_image_software_using_get) | **GET** /images/{imageSha}/software | Show software installed on an image
[**get_image_vuln_count_using_get**](ImageApi.md#get_image_vuln_count_using_get) | **GET** /images/{imageSha}/vuln/count | Show vulnerability count for an image
[**get_image_vuln_using_get**](ImageApi.md#get_image_vuln_using_get) | **GET** /images/{imageSha}/vuln | Show vulnerability details for an image
[**instrumente_image**](ImageApi.md#instrumente_image) | **POST** /images/{imageSha}/instrument | Instrumenting the image identified by image id

# **delete_cs_images**
> str delete_cs_images(image_ids=image_ids, filter=filter)

Delete images in your account

Provide one or more image Ids or filters in the format shown under Example Value.

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ImageApi(QualysCSAPI.ApiClient(configuration))
image_ids = ['image_ids_example'] # list[str] | delete the images from uuid (optional)
filter = 'filter_example' # str | delete the images from filter (optional)

try:
    # Delete images in your account
    api_response = api_instance.delete_cs_images(image_ids=image_ids, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->delete_cs_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_ids** | [**list[str]**](str.md)| delete the images from uuid | [optional] 
 **filter** | **str**| delete the images from filter | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_images_data_using_get**
> Images get_cs_images_data_using_get(filter=filter, page_number=page_number, page_size=page_size, sort=sort)

Show a list of images in your account

Show a list of images in your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ImageApi(QualysCSAPI.ApiClient(configuration))
filter = '' # str | Filter the images list by providing a query using Qualys syntax. (optional)
page_number = 1 # int | The page to be returned. (optional) (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (optional) (default to 50)
sort = 'created:desc' # str | Sort the results using a Qualys token. (optional) (default to created:desc)

try:
    # Show a list of images in your account
    api_response = api_instance.get_cs_images_data_using_get(filter=filter, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_cs_images_data_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter the images list by providing a query using Qualys syntax. | [optional] 
 **page_number** | **int**| The page to be returned. | [optional] [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [optional] [default to 50]
 **sort** | **str**| Sort the results using a Qualys token. | [optional] [default to created:desc]

### Return type

[**Images**](Images.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_association_using_get**
> ImageAssociation get_image_association_using_get(image_sha, filter=filter, type=type)

show associations of an image

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ImageApi(QualysCSAPI.ApiClient(configuration))
image_sha = 'image_sha_example' # str | Specify the SHA value of an Image in the user???s scope.
filter = 'filter_example' # str |  (optional)
type = 'type_example' # str |  (optional)

try:
    # show associations of an image
    api_response = api_instance.get_image_association_using_get(image_sha, filter=filter, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_association_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_sha** | **str**| Specify the SHA value of an Image in the user???s scope. | 
 **filter** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**ImageAssociation**](ImageAssociation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_details_using_get**
> ImageDetails get_image_details_using_get(image_sha)

show details of an image

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ImageApi(QualysCSAPI.ApiClient(configuration))
image_sha = 'image_sha_example' # str | Specify the SHA value of an Image in the user???s scope.

try:
    # show details of an image
    api_response = api_instance.get_image_details_using_get(image_sha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_sha** | **str**| Specify the SHA value of an Image in the user???s scope. | 

### Return type

[**ImageDetails**](ImageDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_list_with_details**
> BulkImageDetailsList get_image_list_with_details(filter=filter, pagination_query=pagination_query, limit=limit)

Images Bulk API

Returns response with given number of Image records according to filter along with next page filter query.

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ImageApi(QualysCSAPI.ApiClient(configuration))
filter = '' # str | Filter the containers list by providing a query using Qualys syntax. (optional)
pagination_query = 'pagination_query_example' # str | The next page filter query. (optional)
limit = 50 # int | The number of records per page to be included in the response. (optional) (default to 50)

try:
    # Images Bulk API
    api_response = api_instance.get_image_list_with_details(filter=filter, pagination_query=pagination_query, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_list_with_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter the containers list by providing a query using Qualys syntax. | [optional] 
 **pagination_query** | **str**| The next page filter query. | [optional] 
 **limit** | **int**| The number of records per page to be included in the response. | [optional] [default to 50]

### Return type

[**BulkImageDetailsList**](BulkImageDetailsList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_policy_compliance_details_using_get**
> PolicyComplianceDetails get_image_policy_compliance_details_using_get(image_sha)

show policy compliance details of an image

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ImageApi(QualysCSAPI.ApiClient(configuration))
image_sha = 'image_sha_example' # str | Specify the SHA value of an Image in the user???s scope.

try:
    # show policy compliance details of an image
    api_response = api_instance.get_image_policy_compliance_details_using_get(image_sha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_policy_compliance_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_sha** | **str**| Specify the SHA value of an Image in the user???s scope. | 

### Return type

[**PolicyComplianceDetails**](PolicyComplianceDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_registries_using_get**
> ImageRegistries get_image_registries_using_get(image_sha)

Get associated registries with Image

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ImageApi(QualysCSAPI.ApiClient(configuration))
image_sha = 'image_sha_example' # str | Specify the SHA value of an Image in the user???s scope.

try:
    # Get associated registries with Image
    api_response = api_instance.get_image_registries_using_get(image_sha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_registries_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_sha** | **str**| Specify the SHA value of an Image in the user???s scope. | 

### Return type

[**ImageRegistries**](ImageRegistries.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_software_using_get**
> ImageSoftware get_image_software_using_get(image_sha, filter=filter, sort=sort)

Show software installed on an image

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ImageApi(QualysCSAPI.ApiClient(configuration))
image_sha = 'image_sha_example' # str | Specify the SHA value of an Image in the user???s scope.
filter = 'filter_example' # str | Filter the image vulnerability details by providing a query using Qualys syntax. (optional)
sort = 'sort_example' # str | Sort the results using a Qualys token. (optional)

try:
    # Show software installed on an image
    api_response = api_instance.get_image_software_using_get(image_sha, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_software_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_sha** | **str**| Specify the SHA value of an Image in the user???s scope. | 
 **filter** | **str**| Filter the image vulnerability details by providing a query using Qualys syntax. | [optional] 
 **sort** | **str**| Sort the results using a Qualys token. | [optional] 

### Return type

[**ImageSoftware**](ImageSoftware.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_vuln_count_using_get**
> object get_image_vuln_count_using_get(image_sha)

Show vulnerability count for an image

Show vulnerability count for an image

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ImageApi(QualysCSAPI.ApiClient(configuration))
image_sha = 'image_sha_example' # str | Specify the SHA value of an Image in the user???s scope.

try:
    # Show vulnerability count for an image
    api_response = api_instance.get_image_vuln_count_using_get(image_sha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_vuln_count_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_sha** | **str**| Specify the SHA value of an Image in the user???s scope. | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_vuln_using_get**
> ImageVulnerability get_image_vuln_using_get(image_sha, filter=filter, type=type, sort=sort)

Show vulnerability details for an image

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ImageApi(QualysCSAPI.ApiClient(configuration))
image_sha = 'image_sha_example' # str | Specify the SHA value of an Image in the user???s scope.
filter = 'filter_example' # str | Filter the image vulnerability details by providing a query using Qualys syntax. (optional)
type = 'ALL' # str | Specify the type of information to be fetched: Summary, Details, All (optional) (default to ALL)
sort = 'qid:asc' # str | Sort the results using a Qualys token. (optional) (default to qid:asc)

try:
    # Show vulnerability details for an image
    api_response = api_instance.get_image_vuln_using_get(image_sha, filter=filter, type=type, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->get_image_vuln_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_sha** | **str**| Specify the SHA value of an Image in the user???s scope. | 
 **filter** | **str**| Filter the image vulnerability details by providing a query using Qualys syntax. | [optional] 
 **type** | **str**| Specify the type of information to be fetched: Summary, Details, All | [optional] [default to ALL]
 **sort** | **str**| Sort the results using a Qualys token. | [optional] [default to qid:asc]

### Return type

[**ImageVulnerability**](ImageVulnerability.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instrumente_image**
> str instrumente_image(body, image_sha)

Instrumenting the image identified by image id

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ImageApi(QualysCSAPI.ApiClient(configuration))
body = QualysCSAPI.InstrumentRequest() # InstrumentRequest | Provide parameter values in the format shown under Example Value.
image_sha = 'image_sha_example' # str | Specify the SHA value of an Image in the user???s scope.

try:
    # Instrumenting the image identified by image id
    api_response = api_instance.instrumente_image(body, image_sha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->instrumente_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InstrumentRequest**](InstrumentRequest.md)| Provide parameter values in the format shown under Example Value. | 
 **image_sha** | **str**| Specify the SHA value of an Image in the user???s scope. | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


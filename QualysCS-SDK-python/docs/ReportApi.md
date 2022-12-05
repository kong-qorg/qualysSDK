# QualysCSAPI.ReportApi

All URIs are relative to *https://gateway.qg2.apps.qualys.com/csapi/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report_request**](ReportApi.md#create_report_request) | **POST** /reports | Create Report request
[**delete_cs_reports**](ReportApi.md#delete_cs_reports) | **DELETE** /reports | Delete Reports in your account
[**get_cs_report_download**](ReportApi.md#get_cs_report_download) | **GET** /reports/{reportUuid}/download | Show a details of a Report.
[**get_cs_reports_list**](ReportApi.md#get_cs_reports_list) | **GET** /reports | Show a list of reports in your account.

# **create_report_request**
> str create_report_request(body)

Create Report request

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ReportApi(QualysCSAPI.ApiClient(configuration))
body = QualysCSAPI.ReportRequest() # ReportRequest | Provide parameter values in the format shown under Example Value. displayColumns can have following values if your template is <table> <tr> <th>CS_IMAGE_VULNERABILITY</th> <td>repo, imageId, sha, uuid, created, updated,  qid, title, severity, cveids, vendorReference, cvssBase, cvssTemporal, cvss3Base, cvss3Temporal, threat, impact, solution, exploitability, associatedMalwares, category, software, result</td> </tr> <tr> <th>CS_CONTAINER_VULNERABILITY</th> <td> name, containerId, uuid, imageId, created, hostName, hostIp, state, stateChanged, updated,  qid, title, severity, cveids, vendorReference, cvssBase, cvssTemporal, cvss3Base, cvss3Temporal, threat, impact, solution, exploitability, associatedMalwares, category, software, result</td> </tr> </table> <BR>

try:
    # Create Report request
    api_response = api_instance.create_report_request(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->create_report_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportRequest**](ReportRequest.md)| Provide parameter values in the format shown under Example Value. displayColumns can have following values if your template is &lt;table&gt; &lt;tr&gt; &lt;th&gt;CS_IMAGE_VULNERABILITY&lt;/th&gt; &lt;td&gt;repo, imageId, sha, uuid, created, updated,  qid, title, severity, cveids, vendorReference, cvssBase, cvssTemporal, cvss3Base, cvss3Temporal, threat, impact, solution, exploitability, associatedMalwares, category, software, result&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;th&gt;CS_CONTAINER_VULNERABILITY&lt;/th&gt; &lt;td&gt; name, containerId, uuid, imageId, created, hostName, hostIp, state, stateChanged, updated,  qid, title, severity, cveids, vendorReference, cvssBase, cvssTemporal, cvss3Base, cvss3Temporal, threat, impact, solution, exploitability, associatedMalwares, category, software, result&lt;/td&gt; &lt;/tr&gt; &lt;/table&gt; &lt;BR&gt; | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cs_reports**
> ReportsDeleteSucccess delete_cs_reports(report_uuids)

Delete Reports in your account

Delete Reports in your account

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ReportApi(QualysCSAPI.ApiClient(configuration))
report_uuids = ['report_uuids_example'] # list[str] | delete the reports from uuid

try:
    # Delete Reports in your account
    api_response = api_instance.delete_cs_reports(report_uuids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->delete_cs_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_uuids** | [**list[str]**](str.md)| delete the reports from uuid | 

### Return type

[**ReportsDeleteSucccess**](ReportsDeleteSucccess.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_report_download**
> InlineResponse200 get_cs_report_download(report_uuid)

Show a details of a Report.

Show a details of a Report.

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ReportApi(QualysCSAPI.ApiClient(configuration))
report_uuid = 'report_uuid_example' # str | Specify the report UUID of a specific report in the user???s scope

try:
    # Show a details of a Report.
    api_response = api_instance.get_cs_report_download(report_uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->get_cs_report_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_uuid** | **str**| Specify the report UUID of a specific report in the user???s scope | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cs_reports_list**
> Reports get_cs_reports_list(filter=filter, page_number=page_number, page_size=page_size, sort=sort)

Show a list of reports in your account.

Show a list of reports in your account.

### Example
```python
from __future__ import print_function
import time
import QualysCSAPI
from QualysCSAPI.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = QualysCSAPI.ReportApi(QualysCSAPI.ApiClient(configuration))
filter = 'filter_example' # str | Filter the reports list by providing a query using Qualys syntax.Only reportName is supported in filter query. (optional)
page_number = 1 # int | The page to be returned. (optional) (default to 1)
page_size = 50 # int | The number of records per page to be included in the response. (optional) (default to 50)
sort = 'status:desc' # str | Supported values are reportName/ status. (optional) (default to status:desc)

try:
    # Show a list of reports in your account.
    api_response = api_instance.get_cs_reports_list(filter=filter, page_number=page_number, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportApi->get_cs_reports_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter the reports list by providing a query using Qualys syntax.Only reportName is supported in filter query. | [optional] 
 **page_number** | **int**| The page to be returned. | [optional] [default to 1]
 **page_size** | **int**| The number of records per page to be included in the response. | [optional] [default to 50]
 **sort** | **str**| Supported values are reportName/ status. | [optional] [default to status:desc]

### Return type

[**Reports**](Reports.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_messages_get**](DefaultApi.md#api_v2_messages_get) | **GET** /api/v2/messages | 
[**api_v2_search_get**](DefaultApi.md#api_v2_search_get) | **GET** /api/v2/search | 


# **api_v2_messages_get**
> Messages api_v2_messages_get(start=start, limit=limit)



Retrieve a list of messages 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    start = 0.0 # float | Start index (optional) (default to 0.0)
limit = 50.0 # float | Number of messages (optional) (default to 50.0)

    try:
        api_response = api_instance.api_v2_messages_get(start=start, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->api_v2_messages_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **float**| Start index | [optional] [default to 0.0]
 **limit** | **float**| Number of messages | [optional] [default to 50.0]

### Return type

[**Messages**](Messages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_search_get**
> Messages api_v2_search_get(kind, query, start=start, limit=limit)



Search messages 

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    kind = 'kind_example' # str | Kind of search
query = 'query_example' # str | Search parameter
start = 0.0 # float | Start index (optional) (default to 0.0)
limit = 50.0 # float | Number of messages (optional) (default to 50.0)

    try:
        api_response = api_instance.api_v2_search_get(kind, query, start=start, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->api_v2_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kind** | **str**| Kind of search | 
 **query** | **str**| Search parameter | 
 **start** | **float**| Start index | [optional] [default to 0.0]
 **limit** | **float**| Number of messages | [optional] [default to 50.0]

### Return type

[**Messages**](Messages.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


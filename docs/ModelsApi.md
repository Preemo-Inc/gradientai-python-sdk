# gradientai.ModelsApi

All URIs are relative to *https://api.gradient.ai/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_model**](ModelsApi.md#complete_model) | **POST** /models/{id}/completions | Complete model
[**create_model**](ModelsApi.md#create_model) | **POST** /models | Create model
[**delete_model**](ModelsApi.md#delete_model) | **DELETE** /models/{id} | Delete model.
[**get_model**](ModelsApi.md#get_model) | **GET** /models/{id} | Describe model
[**list_models**](ModelsApi.md#list_models) | **GET** /models | List available models
[**train_model**](ModelsApi.md#train_model) | **PUT** /models/{id} | Train model


# **complete_model**
> CompleteModelSuccess complete_model(id, x_gradient_workspace_id, complete_model_body_params)

Complete model

Completes your fine-tuned model with the specified prompt string. The model will generate a completion.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import gradientai
from gradientai.models.complete_model_body_params import CompleteModelBodyParams
from gradientai.models.complete_model_success import CompleteModelSuccess
from gradientai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gradient.ai/api
# See configuration.py for a list of all supported configuration parameters.
configuration = gradientai.Configuration(
    host = "https://api.gradient.ai/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = gradientai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gradientai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gradientai.ModelsApi(api_client)
    id = 'id_example' # str | 
    x_gradient_workspace_id = 'x_gradient_workspace_id_example' # str | 
    complete_model_body_params = gradientai.CompleteModelBodyParams() # CompleteModelBodyParams | 

    try:
        # Complete model
        api_response = api_instance.complete_model(id, x_gradient_workspace_id, complete_model_body_params)
        print("The response of ModelsApi->complete_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->complete_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_gradient_workspace_id** | **str**|  | 
 **complete_model_body_params** | [**CompleteModelBodyParams**](CompleteModelBodyParams.md)|  | 

### Return type

[**CompleteModelSuccess**](CompleteModelSuccess.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**4XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_model**
> CreateModelSuccess create_model(x_gradient_workspace_id, create_model_request_body)

Create model

Creates a new instance of a model based on a specified model from the existing list.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import gradientai
from gradientai.models.create_model_request_body import CreateModelRequestBody
from gradientai.models.create_model_success import CreateModelSuccess
from gradientai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gradient.ai/api
# See configuration.py for a list of all supported configuration parameters.
configuration = gradientai.Configuration(
    host = "https://api.gradient.ai/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = gradientai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gradientai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gradientai.ModelsApi(api_client)
    x_gradient_workspace_id = 'x_gradient_workspace_id_example' # str | 
    create_model_request_body = gradientai.CreateModelRequestBody() # CreateModelRequestBody | 

    try:
        # Create model
        api_response = api_instance.create_model(x_gradient_workspace_id, create_model_request_body)
        print("The response of ModelsApi->create_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->create_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gradient_workspace_id** | **str**|  | 
 **create_model_request_body** | [**CreateModelRequestBody**](CreateModelRequestBody.md)|  | 

### Return type

[**CreateModelSuccess**](CreateModelSuccess.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**4XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model**
> str delete_model(id, x_gradient_workspace_id)

Delete model.

Deletes the fine-tuned model.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import gradientai
from gradientai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gradient.ai/api
# See configuration.py for a list of all supported configuration parameters.
configuration = gradientai.Configuration(
    host = "https://api.gradient.ai/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = gradientai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gradientai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gradientai.ModelsApi(api_client)
    id = 'id_example' # str | 
    x_gradient_workspace_id = 'x_gradient_workspace_id_example' # str | 

    try:
        # Delete model.
        api_response = api_instance.delete_model(id, x_gradient_workspace_id)
        print("The response of ModelsApi->delete_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->delete_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_gradient_workspace_id** | **str**|  | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**4XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> GetModelSuccess get_model(id, x_gradient_workspace_id)

Describe model

Describes the specified model, including the model ID, name, slug and base model ID.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import gradientai
from gradientai.models.get_model_success import GetModelSuccess
from gradientai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gradient.ai/api
# See configuration.py for a list of all supported configuration parameters.
configuration = gradientai.Configuration(
    host = "https://api.gradient.ai/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = gradientai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gradientai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gradientai.ModelsApi(api_client)
    id = 'id_example' # str | 
    x_gradient_workspace_id = 'x_gradient_workspace_id_example' # str | 

    try:
        # Describe model
        api_response = api_instance.get_model(id, x_gradient_workspace_id)
        print("The response of ModelsApi->get_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->get_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_gradient_workspace_id** | **str**|  | 

### Return type

[**GetModelSuccess**](GetModelSuccess.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**4XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_models**
> ListModelsSuccess list_models(x_gradient_workspace_id, only_base=only_base)

List available models

Lists the currently available models in the selected workspace and provides basic information such as the model name, ID and whether it is a base or fine-tuned model.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import gradientai
from gradientai.models.list_models_success import ListModelsSuccess
from gradientai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gradient.ai/api
# See configuration.py for a list of all supported configuration parameters.
configuration = gradientai.Configuration(
    host = "https://api.gradient.ai/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = gradientai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gradientai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gradientai.ModelsApi(api_client)
    x_gradient_workspace_id = 'x_gradient_workspace_id_example' # str | 
    only_base = False # bool |  (optional) (default to False)

    try:
        # List available models
        api_response = api_instance.list_models(x_gradient_workspace_id, only_base=only_base)
        print("The response of ModelsApi->list_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->list_models: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_gradient_workspace_id** | **str**|  | 
 **only_base** | **bool**|  | [optional] [default to False]

### Return type

[**ListModelsSuccess**](ListModelsSuccess.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**4XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **train_model**
> TrainModelSuccess train_model(id, x_gradient_workspace_id, train_model_request_body)

Train model

Fine-tunes the specified model with your data samples.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import gradientai
from gradientai.models.train_model_request_body import TrainModelRequestBody
from gradientai.models.train_model_success import TrainModelSuccess
from gradientai.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gradient.ai/api
# See configuration.py for a list of all supported configuration parameters.
configuration = gradientai.Configuration(
    host = "https://api.gradient.ai/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = gradientai.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gradientai.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gradientai.ModelsApi(api_client)
    id = 'id_example' # str | 
    x_gradient_workspace_id = 'x_gradient_workspace_id_example' # str | 
    train_model_request_body = gradientai.TrainModelRequestBody() # TrainModelRequestBody | 

    try:
        # Train model
        api_response = api_instance.train_model(id, x_gradient_workspace_id, train_model_request_body)
        print("The response of ModelsApi->train_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelsApi->train_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_gradient_workspace_id** | **str**|  | 
 **train_model_request_body** | [**TrainModelRequestBody**](TrainModelRequestBody.md)|  | 

### Return type

[**TrainModelSuccess**](TrainModelSuccess.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**4XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


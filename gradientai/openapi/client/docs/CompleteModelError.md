# CompleteModelError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**payload** | [**CompleteModelErrorOneOf1Payload**](CompleteModelErrorOneOf1Payload.md) |  | 
**type** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.complete_model_error import CompleteModelError

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteModelError from a JSON string
complete_model_error_instance = CompleteModelError.from_json(json)
# print the JSON string representation of the object
print CompleteModelError.to_json()

# convert the object into a dict
complete_model_error_dict = complete_model_error_instance.to_dict()
# create an instance of CompleteModelError from a dict
complete_model_error_form_dict = complete_model_error.from_dict(complete_model_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



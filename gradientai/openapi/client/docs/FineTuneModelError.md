# FineTuneModelError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**payload** | [**CompleteModelErrorOneOf1Payload**](CompleteModelErrorOneOf1Payload.md) |  | 
**type** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.fine_tune_model_error import FineTuneModelError

# TODO update the JSON string below
json = "{}"
# create an instance of FineTuneModelError from a JSON string
fine_tune_model_error_instance = FineTuneModelError.from_json(json)
# print the JSON string representation of the object
print FineTuneModelError.to_json()

# convert the object into a dict
fine_tune_model_error_dict = fine_tune_model_error_instance.to_dict()
# create an instance of FineTuneModelError from a dict
fine_tune_model_error_form_dict = fine_tune_model_error.from_dict(fine_tune_model_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



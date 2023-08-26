# FineTuneModelRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**samples** | [**List[FineTuneModelRequestBodySamplesInner]**](FineTuneModelRequestBodySamplesInner.md) |  | 

## Example

```python
from gradientai.models.fine_tune_model_request_body import FineTuneModelRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of FineTuneModelRequestBody from a JSON string
fine_tune_model_request_body_instance = FineTuneModelRequestBody.from_json(json)
# print the JSON string representation of the object
print FineTuneModelRequestBody.to_json()

# convert the object into a dict
fine_tune_model_request_body_dict = fine_tune_model_request_body_instance.to_dict()
# create an instance of FineTuneModelRequestBody from a dict
fine_tune_model_request_body_form_dict = fine_tune_model_request_body.from_dict(fine_tune_model_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



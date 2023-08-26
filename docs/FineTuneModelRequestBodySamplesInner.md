# FineTuneModelRequestBodySamplesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fine_tuning_parameters** | [**FineTuneModelRequestBodySamplesInnerFineTuningParameters**](FineTuneModelRequestBodySamplesInnerFineTuningParameters.md) |  | [optional] 
**inputs** | **str** |  | 

## Example

```python
from gradientai.models.fine_tune_model_request_body_samples_inner import FineTuneModelRequestBodySamplesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FineTuneModelRequestBodySamplesInner from a JSON string
fine_tune_model_request_body_samples_inner_instance = FineTuneModelRequestBodySamplesInner.from_json(json)
# print the JSON string representation of the object
print FineTuneModelRequestBodySamplesInner.to_json()

# convert the object into a dict
fine_tune_model_request_body_samples_inner_dict = fine_tune_model_request_body_samples_inner_instance.to_dict()
# create an instance of FineTuneModelRequestBodySamplesInner from a dict
fine_tune_model_request_body_samples_inner_form_dict = fine_tune_model_request_body_samples_inner.from_dict(fine_tune_model_request_body_samples_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



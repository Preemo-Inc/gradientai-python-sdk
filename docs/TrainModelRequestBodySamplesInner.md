# TrainModelRequestBodySamplesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fine_tuning_parameters** | [**TrainModelRequestBodySamplesInnerFineTuningParameters**](TrainModelRequestBodySamplesInnerFineTuningParameters.md) |  | [optional] 
**inputs** | **str** |  | 

## Example

```python
from gradientai.models.train_model_request_body_samples_inner import TrainModelRequestBodySamplesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TrainModelRequestBodySamplesInner from a JSON string
train_model_request_body_samples_inner_instance = TrainModelRequestBodySamplesInner.from_json(json)
# print the JSON string representation of the object
print TrainModelRequestBodySamplesInner.to_json()

# convert the object into a dict
train_model_request_body_samples_inner_dict = train_model_request_body_samples_inner_instance.to_dict()
# create an instance of TrainModelRequestBodySamplesInner from a dict
train_model_request_body_samples_inner_form_dict = train_model_request_body_samples_inner.from_dict(train_model_request_body_samples_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



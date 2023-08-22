# TrainModelRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**samples** | [**List[TrainModelRequestBodySamplesInner]**](TrainModelRequestBodySamplesInner.md) |  | 

## Example

```python
from gradientai.models.train_model_request_body import TrainModelRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TrainModelRequestBody from a JSON string
train_model_request_body_instance = TrainModelRequestBody.from_json(json)
# print the JSON string representation of the object
print TrainModelRequestBody.to_json()

# convert the object into a dict
train_model_request_body_dict = train_model_request_body_instance.to_dict()
# create an instance of TrainModelRequestBody from a dict
train_model_request_body_form_dict = train_model_request_body.from_dict(train_model_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateModelRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_hyperparameters** | [**CreateModelRequestBodyInitialHyperparameters**](CreateModelRequestBodyInitialHyperparameters.md) |  | [optional] 
**model** | [**CreateModelRequestBodyModel**](CreateModelRequestBodyModel.md) |  | 

## Example

```python
from gradientai.models.create_model_request_body import CreateModelRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModelRequestBody from a JSON string
create_model_request_body_instance = CreateModelRequestBody.from_json(json)
# print the JSON string representation of the object
print CreateModelRequestBody.to_json()

# convert the object into a dict
create_model_request_body_dict = create_model_request_body_instance.to_dict()
# create an instance of CreateModelRequestBody from a dict
create_model_request_body_form_dict = create_model_request_body.from_dict(create_model_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateModelBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_hyperparameters** | [**CreateModelBodyParamsInitialHyperparameters**](CreateModelBodyParamsInitialHyperparameters.md) |  | [optional] 
**model** | [**CreateModelBodyParamsModel**](CreateModelBodyParamsModel.md) |  | 

## Example

```python
from gradientai.openapi.client.models.create_model_body_params import CreateModelBodyParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModelBodyParams from a JSON string
create_model_body_params_instance = CreateModelBodyParams.from_json(json)
# print the JSON string representation of the object
print CreateModelBodyParams.to_json()

# convert the object into a dict
create_model_body_params_dict = create_model_body_params_instance.to_dict()
# create an instance of CreateModelBodyParams from a dict
create_model_body_params_form_dict = create_model_body_params.from_dict(create_model_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateModelBodyParamsInitialHyperparameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lora_hyperparameters** | [**CreateModelBodyParamsInitialHyperparametersLoraHyperparameters**](CreateModelBodyParamsInitialHyperparametersLoraHyperparameters.md) |  | [optional] 
**training_arguments** | [**CreateModelBodyParamsInitialHyperparametersTrainingArguments**](CreateModelBodyParamsInitialHyperparametersTrainingArguments.md) |  | [optional] 

## Example

```python
from gradientai.openapi.client.models.create_model_body_params_initial_hyperparameters import CreateModelBodyParamsInitialHyperparameters

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModelBodyParamsInitialHyperparameters from a JSON string
create_model_body_params_initial_hyperparameters_instance = CreateModelBodyParamsInitialHyperparameters.from_json(json)
# print the JSON string representation of the object
print CreateModelBodyParamsInitialHyperparameters.to_json()

# convert the object into a dict
create_model_body_params_initial_hyperparameters_dict = create_model_body_params_initial_hyperparameters_instance.to_dict()
# create an instance of CreateModelBodyParamsInitialHyperparameters from a dict
create_model_body_params_initial_hyperparameters_form_dict = create_model_body_params_initial_hyperparameters.from_dict(create_model_body_params_initial_hyperparameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



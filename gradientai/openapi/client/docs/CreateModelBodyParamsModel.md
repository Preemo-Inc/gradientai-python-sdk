# CreateModelBodyParamsModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_model_id** | **str** | The foundational model you are creating a new instance of for fine-tuning. | 
**name** | **str** | What your new fine-tuned model will be called. | 

## Example

```python
from gradientai.openapi.client.models.create_model_body_params_model import CreateModelBodyParamsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModelBodyParamsModel from a JSON string
create_model_body_params_model_instance = CreateModelBodyParamsModel.from_json(json)
# print the JSON string representation of the object
print CreateModelBodyParamsModel.to_json()

# convert the object into a dict
create_model_body_params_model_dict = create_model_body_params_model_instance.to_dict()
# create an instance of CreateModelBodyParamsModel from a dict
create_model_body_params_model_form_dict = create_model_body_params_model.from_dict(create_model_body_params_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateModelRequestBodyModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_model_id** | **str** | The foundational model you are creating a new instance of for fine-tuning. | 
**name** | **str** | What your new fine-tuned model will be called. | 

## Example

```python
from gradientai.models.create_model_request_body_model import CreateModelRequestBodyModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModelRequestBodyModel from a JSON string
create_model_request_body_model_instance = CreateModelRequestBodyModel.from_json(json)
# print the JSON string representation of the object
print CreateModelRequestBodyModel.to_json()

# convert the object into a dict
create_model_request_body_model_dict = create_model_request_body_model_instance.to_dict()
# create an instance of CreateModelRequestBodyModel from a dict
create_model_request_body_model_form_dict = create_model_request_body_model.from_dict(create_model_request_body_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



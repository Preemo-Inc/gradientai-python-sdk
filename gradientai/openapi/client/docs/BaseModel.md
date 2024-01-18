# BaseModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **List[str]** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.base_model import BaseModel


json = "{}"
# create an instance of BaseModel from a JSON string
base_model_instance = BaseModel.from_json(json)
# print the JSON string representation of the object
print BaseModel.to_json()

# convert the object into a dict
base_model_dict = base_model_instance.to_dict()
# create an instance of BaseModel from a dict
base_model_form_dict = base_model.from_dict(base_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



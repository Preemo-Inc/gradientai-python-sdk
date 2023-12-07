# ModelAdapter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_model_id** | **str** |  | 
**id** | **str** |  | 
**latest_update_time** | **datetime** |  | 
**name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.model_adapter import ModelAdapter

# TODO update the JSON string below
json = "{}"
# create an instance of ModelAdapter from a JSON string
model_adapter_instance = ModelAdapter.from_json(json)
# print the JSON string representation of the object
print ModelAdapter.to_json()

# convert the object into a dict
model_adapter_dict = model_adapter_instance.to_dict()
# create an instance of ModelAdapter from a dict
model_adapter_form_dict = model_adapter.from_dict(model_adapter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



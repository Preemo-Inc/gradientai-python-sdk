# GetModelSuccess


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
from gradientai.openapi.client.models.get_model_success import GetModelSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of GetModelSuccess from a JSON string
get_model_success_instance = GetModelSuccess.from_json(json)
# print the JSON string representation of the object
print GetModelSuccess.to_json()

# convert the object into a dict
get_model_success_dict = get_model_success_instance.to_dict()
# create an instance of GetModelSuccess from a dict
get_model_success_form_dict = get_model_success.from_dict(get_model_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



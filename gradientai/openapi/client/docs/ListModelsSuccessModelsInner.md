# ListModelsSuccessModelsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**type** | **str** |  | 
**base_model_id** | **str** |  | 
**latest_update_time** | **datetime** |  | 

## Example

```python
from gradientai.openapi.client.models.list_models_success_models_inner import ListModelsSuccessModelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListModelsSuccessModelsInner from a JSON string
list_models_success_models_inner_instance = ListModelsSuccessModelsInner.from_json(json)
# print the JSON string representation of the object
print ListModelsSuccessModelsInner.to_json()

# convert the object into a dict
list_models_success_models_inner_dict = list_models_success_models_inner_instance.to_dict()
# create an instance of ListModelsSuccessModelsInner from a dict
list_models_success_models_inner_form_dict = list_models_success_models_inner.from_dict(list_models_success_models_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



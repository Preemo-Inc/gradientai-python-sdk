# ListModelsSuccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[ListModelsSuccessModelsInner]**](ListModelsSuccessModelsInner.md) |  | 

## Example

```python
from gradientai.openapi.client.models.list_models_success import ListModelsSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of ListModelsSuccess from a JSON string
list_models_success_instance = ListModelsSuccess.from_json(json)
# print the JSON string representation of the object
print ListModelsSuccess.to_json()

# convert the object into a dict
list_models_success_dict = list_models_success_instance.to_dict()
# create an instance of ListModelsSuccess from a dict
list_models_success_form_dict = list_models_success.from_dict(list_models_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UserModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**slug** | **str** |  | 
**base_model_id** | **str** |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from gradientai.models.user_model import UserModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserModel from a JSON string
user_model_instance = UserModel.from_json(json)
# print the JSON string representation of the object
print UserModel.to_json()

# convert the object into a dict
user_model_dict = user_model_instance.to_dict()
# create an instance of UserModel from a dict
user_model_form_dict = user_model.from_dict(user_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



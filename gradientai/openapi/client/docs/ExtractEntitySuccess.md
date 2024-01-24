# ExtractEntitySuccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**Dict[str, ExtractEntitySuccessEntityValue]**](ExtractEntitySuccessEntityValue.md) |  | 

## Example

```python
from gradientai.openapi.client.models.extract_entity_success import ExtractEntitySuccess


json = "{}"
# create an instance of ExtractEntitySuccess from a JSON string
extract_entity_success_instance = ExtractEntitySuccess.from_json(json)
# print the JSON string representation of the object
print ExtractEntitySuccess.to_json()

# convert the object into a dict
extract_entity_success_dict = extract_entity_success_instance.to_dict()
# create an instance of ExtractEntitySuccess from a dict
extract_entity_success_form_dict = extract_entity_success.from_dict(extract_entity_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



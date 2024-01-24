# ExtractEntityBodyParamsSchemaValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **bool** |  | [optional] [default to False]
**type** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.extract_entity_body_params_schema_value import ExtractEntityBodyParamsSchemaValue


json = "{}"
# create an instance of ExtractEntityBodyParamsSchemaValue from a JSON string
extract_entity_body_params_schema_value_instance = ExtractEntityBodyParamsSchemaValue.from_json(json)
# print the JSON string representation of the object
print ExtractEntityBodyParamsSchemaValue.to_json()

# convert the object into a dict
extract_entity_body_params_schema_value_dict = extract_entity_body_params_schema_value_instance.to_dict()
# create an instance of ExtractEntityBodyParamsSchemaValue from a dict
extract_entity_body_params_schema_value_form_dict = extract_entity_body_params_schema_value.from_dict(extract_entity_body_params_schema_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



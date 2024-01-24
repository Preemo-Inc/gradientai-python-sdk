# ExtractEntityBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | **str** | The document from which to extract data. | 
**var_schema** | [**Dict[str, ExtractEntityBodyParamsSchemaValue]**](ExtractEntityBodyParamsSchemaValue.md) | The expected schema of the entity result. | 

## Example

```python
from gradientai.openapi.client.models.extract_entity_body_params import ExtractEntityBodyParams


json = "{}"
# create an instance of ExtractEntityBodyParams from a JSON string
extract_entity_body_params_instance = ExtractEntityBodyParams.from_json(json)
# print the JSON string representation of the object
print ExtractEntityBodyParams.to_json()

# convert the object into a dict
extract_entity_body_params_dict = extract_entity_body_params_instance.to_dict()
# create an instance of ExtractEntityBodyParams from a dict
extract_entity_body_params_form_dict = extract_entity_body_params.from_dict(extract_entity_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



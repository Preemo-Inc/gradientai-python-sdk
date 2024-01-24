# GenerateAnswerBodyParamsSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | 
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.generate_answer_body_params_source import GenerateAnswerBodyParamsSource


json = "{}"
# create an instance of GenerateAnswerBodyParamsSource from a JSON string
generate_answer_body_params_source_instance = GenerateAnswerBodyParamsSource.from_json(json)
# print the JSON string representation of the object
print GenerateAnswerBodyParamsSource.to_json()

# convert the object into a dict
generate_answer_body_params_source_dict = generate_answer_body_params_source_instance.to_dict()
# create an instance of GenerateAnswerBodyParamsSource from a dict
generate_answer_body_params_source_form_dict = generate_answer_body_params_source.from_dict(generate_answer_body_params_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



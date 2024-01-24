# GenerateAnswerBodyParamsSourceOneOf

The reference RAG that must be used to answer the question.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.generate_answer_body_params_source_one_of import GenerateAnswerBodyParamsSourceOneOf


json = "{}"
# create an instance of GenerateAnswerBodyParamsSourceOneOf from a JSON string
generate_answer_body_params_source_one_of_instance = GenerateAnswerBodyParamsSourceOneOf.from_json(json)
# print the JSON string representation of the object
print GenerateAnswerBodyParamsSourceOneOf.to_json()

# convert the object into a dict
generate_answer_body_params_source_one_of_dict = generate_answer_body_params_source_one_of_instance.to_dict()
# create an instance of GenerateAnswerBodyParamsSourceOneOf from a dict
generate_answer_body_params_source_one_of_form_dict = generate_answer_body_params_source_one_of.from_dict(generate_answer_body_params_source_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



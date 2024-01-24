# GenerateAnswerSuccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** |  | 
**rag_context** | [**GenerateAnswerSuccessRagContext**](GenerateAnswerSuccessRagContext.md) |  | [optional] 

## Example

```python
from gradientai.openapi.client.models.generate_answer_success import GenerateAnswerSuccess


json = "{}"
# create an instance of GenerateAnswerSuccess from a JSON string
generate_answer_success_instance = GenerateAnswerSuccess.from_json(json)
# print the JSON string representation of the object
print GenerateAnswerSuccess.to_json()

# convert the object into a dict
generate_answer_success_dict = generate_answer_success_instance.to_dict()
# create an instance of GenerateAnswerSuccess from a dict
generate_answer_success_form_dict = generate_answer_success.from_dict(generate_answer_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



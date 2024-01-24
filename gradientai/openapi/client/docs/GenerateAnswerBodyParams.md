# GenerateAnswerBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** |  | 
**source** | [**GenerateAnswerBodyParamsSource**](GenerateAnswerBodyParamsSource.md) |  | 

## Example

```python
from gradientai.openapi.client.models.generate_answer_body_params import GenerateAnswerBodyParams


json = "{}"
# create an instance of GenerateAnswerBodyParams from a JSON string
generate_answer_body_params_instance = GenerateAnswerBodyParams.from_json(json)
# print the JSON string representation of the object
print GenerateAnswerBodyParams.to_json()

# convert the object into a dict
generate_answer_body_params_dict = generate_answer_body_params_instance.to_dict()
# create an instance of GenerateAnswerBodyParams from a dict
generate_answer_body_params_form_dict = generate_answer_body_params.from_dict(generate_answer_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GenerateEmbeddingBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | [**List[GenerateEmbeddingBodyParamsInputsInner]**](GenerateEmbeddingBodyParamsInputsInner.md) |  | 

## Example

```python
from gradientai.openapi.client.models.generate_embedding_body_params import GenerateEmbeddingBodyParams

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateEmbeddingBodyParams from a JSON string
generate_embedding_body_params_instance = GenerateEmbeddingBodyParams.from_json(json)
# print the JSON string representation of the object
print GenerateEmbeddingBodyParams.to_json()

# convert the object into a dict
generate_embedding_body_params_dict = generate_embedding_body_params_instance.to_dict()
# create an instance of GenerateEmbeddingBodyParams from a dict
generate_embedding_body_params_form_dict = generate_embedding_body_params.from_dict(generate_embedding_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



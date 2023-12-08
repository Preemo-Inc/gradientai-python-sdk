# GenerateEmbeddingSuccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embeddings** | [**List[GenerateEmbeddingSuccessEmbeddingsInner]**](GenerateEmbeddingSuccessEmbeddingsInner.md) |  | 

## Example

```python
from gradientai.openapi.client.models.generate_embedding_success import GenerateEmbeddingSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateEmbeddingSuccess from a JSON string
generate_embedding_success_instance = GenerateEmbeddingSuccess.from_json(json)
# print the JSON string representation of the object
print GenerateEmbeddingSuccess.to_json()

# convert the object into a dict
generate_embedding_success_dict = generate_embedding_success_instance.to_dict()
# create an instance of GenerateEmbeddingSuccess from a dict
generate_embedding_success_form_dict = generate_embedding_success.from_dict(generate_embedding_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



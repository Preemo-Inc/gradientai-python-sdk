# ListEmbeddingsSuccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embeddings_models** | [**List[ListEmbeddingsSuccessEmbeddingsModelsInner]**](ListEmbeddingsSuccessEmbeddingsModelsInner.md) |  | 

## Example

```python
from gradientai.openapi.client.models.list_embeddings_success import ListEmbeddingsSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of ListEmbeddingsSuccess from a JSON string
list_embeddings_success_instance = ListEmbeddingsSuccess.from_json(json)
# print the JSON string representation of the object
print ListEmbeddingsSuccess.to_json()

# convert the object into a dict
list_embeddings_success_dict = list_embeddings_success_instance.to_dict()
# create an instance of ListEmbeddingsSuccess from a dict
list_embeddings_success_form_dict = list_embeddings_success.from_dict(list_embeddings_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



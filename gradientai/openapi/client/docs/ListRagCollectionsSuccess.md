# ListRagCollectionsSuccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rag_collections** | [**List[ListRagCollectionsSuccessRagCollectionsInner]**](ListRagCollectionsSuccessRagCollectionsInner.md) |  | 

## Example

```python
from gradientai.openapi.client.models.list_rag_collections_success import ListRagCollectionsSuccess


json = "{}"
# create an instance of ListRagCollectionsSuccess from a JSON string
list_rag_collections_success_instance = ListRagCollectionsSuccess.from_json(json)
# print the JSON string representation of the object
print ListRagCollectionsSuccess.to_json()

# convert the object into a dict
list_rag_collections_success_dict = list_rag_collections_success_instance.to_dict()
# create an instance of ListRagCollectionsSuccess from a dict
list_rag_collections_success_form_dict = list_rag_collections_success.from_dict(list_rag_collections_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GetRagCollectionSuccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time** | **datetime** |  | 
**files** | [**List[GetRagCollectionSuccessFilesInner]**](GetRagCollectionSuccessFilesInner.md) |  | 
**latest_update_time** | **datetime** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.get_rag_collection_success import GetRagCollectionSuccess


json = "{}"
# create an instance of GetRagCollectionSuccess from a JSON string
get_rag_collection_success_instance = GetRagCollectionSuccess.from_json(json)
# print the JSON string representation of the object
print GetRagCollectionSuccess.to_json()

# convert the object into a dict
get_rag_collection_success_dict = get_rag_collection_success_instance.to_dict()
# create an instance of GetRagCollectionSuccess from a dict
get_rag_collection_success_form_dict = get_rag_collection_success.from_dict(get_rag_collection_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



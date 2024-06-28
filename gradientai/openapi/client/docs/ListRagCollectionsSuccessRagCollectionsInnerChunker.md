# ListRagCollectionsSuccessRagCollectionsInnerChunker


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunker_type** | **str** |  | 
**context_sentences** | **int** |  | 
**overlap** | **int** |  | 
**size** | **int** |  | 
**sentence_group_length** | **int** |  | 
**similiarity_percent_threshold** | **int** |  | 

## Example

```python
from gradientai.openapi.client.models.list_rag_collections_success_rag_collections_inner_chunker import ListRagCollectionsSuccessRagCollectionsInnerChunker


json = "{}"
# create an instance of ListRagCollectionsSuccessRagCollectionsInnerChunker from a JSON string
list_rag_collections_success_rag_collections_inner_chunker_instance = ListRagCollectionsSuccessRagCollectionsInnerChunker.from_json(json)
# print the JSON string representation of the object
print ListRagCollectionsSuccessRagCollectionsInnerChunker.to_json()

# convert the object into a dict
list_rag_collections_success_rag_collections_inner_chunker_dict = list_rag_collections_success_rag_collections_inner_chunker_instance.to_dict()
# create an instance of ListRagCollectionsSuccessRagCollectionsInnerChunker from a dict
list_rag_collections_success_rag_collections_inner_chunker_form_dict = list_rag_collections_success_rag_collections_inner_chunker.from_dict(list_rag_collections_success_rag_collections_inner_chunker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



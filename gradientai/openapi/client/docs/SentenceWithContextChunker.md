# SentenceWithContextChunker


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunker_type** | **str** |  | 
**context_sentences** | **int** |  | [optional] 
**overlap** | **int** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from gradientai.openapi.client.models.sentence_with_context_chunker import SentenceWithContextChunker


json = "{}"
# create an instance of SentenceWithContextChunker from a JSON string
sentence_with_context_chunker_instance = SentenceWithContextChunker.from_json(json)
# print the JSON string representation of the object
print SentenceWithContextChunker.to_json()

# convert the object into a dict
sentence_with_context_chunker_dict = sentence_with_context_chunker_instance.to_dict()
# create an instance of SentenceWithContextChunker from a dict
sentence_with_context_chunker_form_dict = sentence_with_context_chunker.from_dict(sentence_with_context_chunker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



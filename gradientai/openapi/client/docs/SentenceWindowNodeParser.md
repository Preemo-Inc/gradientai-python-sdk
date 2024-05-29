# SentenceWindowNodeParser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_overlap** | **int** |  | [optional] 
**chunk_size** | **int** |  | [optional] 
**parser_type** | **str** |  | 
**window_size** | **int** |  | [optional] 

## Example

```python
from gradientai.openapi.client.models.sentence_window_node_parser import SentenceWindowNodeParser


json = "{}"
# create an instance of SentenceWindowNodeParser from a JSON string
sentence_window_node_parser_instance = SentenceWindowNodeParser.from_json(json)
# print the JSON string representation of the object
print SentenceWindowNodeParser.to_json()

# convert the object into a dict
sentence_window_node_parser_dict = sentence_window_node_parser_instance.to_dict()
# create an instance of SentenceWindowNodeParser from a dict
sentence_window_node_parser_form_dict = sentence_window_node_parser.from_dict(sentence_window_node_parser_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



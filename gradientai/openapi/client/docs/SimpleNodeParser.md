# SimpleNodeParser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_overlap** | **int** |  | [optional] 
**chunk_size** | **int** |  | [optional] 
**parser_type** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.simple_node_parser import SimpleNodeParser


json = "{}"
# create an instance of SimpleNodeParser from a JSON string
simple_node_parser_instance = SimpleNodeParser.from_json(json)
# print the JSON string representation of the object
print SimpleNodeParser.to_json()

# convert the object into a dict
simple_node_parser_dict = simple_node_parser_instance.to_dict()
# create an instance of SimpleNodeParser from a dict
simple_node_parser_form_dict = simple_node_parser.from_dict(simple_node_parser_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateRagCollectionBodyParamsParser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_overlap** | **int** |  | [optional] 
**chunk_size** | **int** |  | [optional] 
**parser_type** | **str** |  | 
**window_size** | **int** |  | [optional] 

## Example

```python
from gradientai.openapi.client.models.create_rag_collection_body_params_parser import CreateRagCollectionBodyParamsParser


json = "{}"
# create an instance of CreateRagCollectionBodyParamsParser from a JSON string
create_rag_collection_body_params_parser_instance = CreateRagCollectionBodyParamsParser.from_json(json)
# print the JSON string representation of the object
print CreateRagCollectionBodyParamsParser.to_json()

# convert the object into a dict
create_rag_collection_body_params_parser_dict = create_rag_collection_body_params_parser_instance.to_dict()
# create an instance of CreateRagCollectionBodyParamsParser from a dict
create_rag_collection_body_params_parser_form_dict = create_rag_collection_body_params_parser.from_dict(create_rag_collection_body_params_parser_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



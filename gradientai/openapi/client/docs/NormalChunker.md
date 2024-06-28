# NormalChunker


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunker_type** | **str** |  | 
**overlap** | **int** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from gradientai.openapi.client.models.normal_chunker import NormalChunker


json = "{}"
# create an instance of NormalChunker from a JSON string
normal_chunker_instance = NormalChunker.from_json(json)
# print the JSON string representation of the object
print NormalChunker.to_json()

# convert the object into a dict
normal_chunker_dict = normal_chunker_instance.to_dict()
# create an instance of NormalChunker from a dict
normal_chunker_form_dict = normal_chunker.from_dict(normal_chunker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



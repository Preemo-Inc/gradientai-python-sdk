# FileChunker


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunker_type** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.file_chunker import FileChunker


json = "{}"
# create an instance of FileChunker from a JSON string
file_chunker_instance = FileChunker.from_json(json)
# print the JSON string representation of the object
print FileChunker.to_json()

# convert the object into a dict
file_chunker_dict = file_chunker_instance.to_dict()
# create an instance of FileChunker from a dict
file_chunker_form_dict = file_chunker.from_dict(file_chunker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



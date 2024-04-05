# AddFilesToRagCollectionBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[CreateRagCollectionBodyParamsFilesInner]**](CreateRagCollectionBodyParamsFilesInner.md) |  | 

## Example

```python
from gradientai.openapi.client.models.add_files_to_rag_collection_body_params import AddFilesToRagCollectionBodyParams


json = "{}"
# create an instance of AddFilesToRagCollectionBodyParams from a JSON string
add_files_to_rag_collection_body_params_instance = AddFilesToRagCollectionBodyParams.from_json(json)
# print the JSON string representation of the object
print AddFilesToRagCollectionBodyParams.to_json()

# convert the object into a dict
add_files_to_rag_collection_body_params_dict = add_files_to_rag_collection_body_params_instance.to_dict()
# create an instance of AddFilesToRagCollectionBodyParams from a dict
add_files_to_rag_collection_body_params_form_dict = add_files_to_rag_collection_body_params.from_dict(add_files_to_rag_collection_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



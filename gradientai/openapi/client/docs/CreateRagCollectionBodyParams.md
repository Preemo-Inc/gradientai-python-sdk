# CreateRagCollectionBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[CreateRagCollectionBodyParamsFilesInner]**](CreateRagCollectionBodyParamsFilesInner.md) |  | [optional] 
**name** | **str** |  | 
**slug** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.create_rag_collection_body_params import CreateRagCollectionBodyParams


json = "{}"
# create an instance of CreateRagCollectionBodyParams from a JSON string
create_rag_collection_body_params_instance = CreateRagCollectionBodyParams.from_json(json)
# print the JSON string representation of the object
print CreateRagCollectionBodyParams.to_json()

# convert the object into a dict
create_rag_collection_body_params_dict = create_rag_collection_body_params_instance.to_dict()
# create an instance of CreateRagCollectionBodyParams from a dict
create_rag_collection_body_params_form_dict = create_rag_collection_body_params.from_dict(create_rag_collection_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



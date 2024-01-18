# CompleteModelBodyParamsRag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | The ID of the RAG collection to retrieve context from before running completion | 

## Example

```python
from gradientai.openapi.client.models.complete_model_body_params_rag import CompleteModelBodyParamsRag


json = "{}"
# create an instance of CompleteModelBodyParamsRag from a JSON string
complete_model_body_params_rag_instance = CompleteModelBodyParamsRag.from_json(json)
# print the JSON string representation of the object
print CompleteModelBodyParamsRag.to_json()

# convert the object into a dict
complete_model_body_params_rag_dict = complete_model_body_params_rag_instance.to_dict()
# create an instance of CompleteModelBodyParamsRag from a dict
complete_model_body_params_rag_form_dict = complete_model_body_params_rag.from_dict(complete_model_body_params_rag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



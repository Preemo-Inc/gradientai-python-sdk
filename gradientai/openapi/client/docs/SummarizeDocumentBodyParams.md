# SummarizeDocumentBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | **str** | The document to summarize. | 
**examples** | [**List[SummarizeDocumentBodyParamsExamplesInner]**](SummarizeDocumentBodyParamsExamplesInner.md) | Examples of how to summarize documents. | [optional] 
**length** | **str** | Roughly how long the summary should be. | [optional] 

## Example

```python
from gradientai.openapi.client.models.summarize_document_body_params import SummarizeDocumentBodyParams


json = "{}"
# create an instance of SummarizeDocumentBodyParams from a JSON string
summarize_document_body_params_instance = SummarizeDocumentBodyParams.from_json(json)
# print the JSON string representation of the object
print SummarizeDocumentBodyParams.to_json()

# convert the object into a dict
summarize_document_body_params_dict = summarize_document_body_params_instance.to_dict()
# create an instance of SummarizeDocumentBodyParams from a dict
summarize_document_body_params_form_dict = summarize_document_body_params.from_dict(summarize_document_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



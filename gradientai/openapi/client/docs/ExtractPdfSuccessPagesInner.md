# ExtractPdfSuccessPagesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | [**List[ExtractPdfSuccessPagesInnerImagesInner]**](ExtractPdfSuccessPagesInnerImagesInner.md) |  | 
**page_number** | **int** |  | 
**tables** | [**List[ExtractPdfSuccessPagesInnerTablesInner]**](ExtractPdfSuccessPagesInnerTablesInner.md) |  | 
**text** | **str** |  | 
**text_blocks** | [**List[ExtractPdfSuccessPagesInnerTextBlocksInner]**](ExtractPdfSuccessPagesInnerTextBlocksInner.md) |  | 

## Example

```python
from gradientai.openapi.client.models.extract_pdf_success_pages_inner import ExtractPdfSuccessPagesInner


json = "{}"
# create an instance of ExtractPdfSuccessPagesInner from a JSON string
extract_pdf_success_pages_inner_instance = ExtractPdfSuccessPagesInner.from_json(json)
# print the JSON string representation of the object
print ExtractPdfSuccessPagesInner.to_json()

# convert the object into a dict
extract_pdf_success_pages_inner_dict = extract_pdf_success_pages_inner_instance.to_dict()
# create an instance of ExtractPdfSuccessPagesInner from a dict
extract_pdf_success_pages_inner_form_dict = extract_pdf_success_pages_inner.from_dict(extract_pdf_success_pages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



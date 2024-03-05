# ExtractPdfSuccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pages** | [**List[ExtractPdfSuccessPagesInner]**](ExtractPdfSuccessPagesInner.md) |  | 
**text** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.extract_pdf_success import ExtractPdfSuccess


json = "{}"
# create an instance of ExtractPdfSuccess from a JSON string
extract_pdf_success_instance = ExtractPdfSuccess.from_json(json)
# print the JSON string representation of the object
print ExtractPdfSuccess.to_json()

# convert the object into a dict
extract_pdf_success_dict = extract_pdf_success_instance.to_dict()
# create an instance of ExtractPdfSuccess from a dict
extract_pdf_success_form_dict = extract_pdf_success.from_dict(extract_pdf_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



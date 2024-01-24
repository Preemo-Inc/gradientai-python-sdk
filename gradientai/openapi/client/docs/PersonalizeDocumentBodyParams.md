# PersonalizeDocumentBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_description** | **str** | The description of the audience that the document should be personalized for. | 
**document** | **str** | The document that will be personalized. | 

## Example

```python
from gradientai.openapi.client.models.personalize_document_body_params import PersonalizeDocumentBodyParams


json = "{}"
# create an instance of PersonalizeDocumentBodyParams from a JSON string
personalize_document_body_params_instance = PersonalizeDocumentBodyParams.from_json(json)
# print the JSON string representation of the object
print PersonalizeDocumentBodyParams.to_json()

# convert the object into a dict
personalize_document_body_params_dict = personalize_document_body_params_instance.to_dict()
# create an instance of PersonalizeDocumentBodyParams from a dict
personalize_document_body_params_form_dict = personalize_document_body_params.from_dict(personalize_document_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



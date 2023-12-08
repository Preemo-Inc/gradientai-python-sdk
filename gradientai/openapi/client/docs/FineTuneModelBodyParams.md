# FineTuneModelBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**samples** | [**List[FineTuneModelBodyParamsSamplesInner]**](FineTuneModelBodyParamsSamplesInner.md) |  | 

## Example

```python
from gradientai.openapi.client.models.fine_tune_model_body_params import FineTuneModelBodyParams

# TODO update the JSON string below
json = "{}"
# create an instance of FineTuneModelBodyParams from a JSON string
fine_tune_model_body_params_instance = FineTuneModelBodyParams.from_json(json)
# print the JSON string representation of the object
print FineTuneModelBodyParams.to_json()

# convert the object into a dict
fine_tune_model_body_params_dict = fine_tune_model_body_params_instance.to_dict()
# create an instance of FineTuneModelBodyParams from a dict
fine_tune_model_body_params_form_dict = fine_tune_model_body_params.from_dict(fine_tune_model_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



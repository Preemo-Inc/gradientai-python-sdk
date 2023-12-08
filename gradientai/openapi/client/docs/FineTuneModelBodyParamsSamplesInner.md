# FineTuneModelBodyParamsSamplesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fine_tuning_parameters** | [**FineTuneModelBodyParamsSamplesInnerFineTuningParameters**](FineTuneModelBodyParamsSamplesInnerFineTuningParameters.md) |  | [optional] 
**inputs** | [**FineTuneModelBodyParamsSamplesInnerInputs**](FineTuneModelBodyParamsSamplesInnerInputs.md) |  | 

## Example

```python
from gradientai.openapi.client.models.fine_tune_model_body_params_samples_inner import FineTuneModelBodyParamsSamplesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FineTuneModelBodyParamsSamplesInner from a JSON string
fine_tune_model_body_params_samples_inner_instance = FineTuneModelBodyParamsSamplesInner.from_json(json)
# print the JSON string representation of the object
print FineTuneModelBodyParamsSamplesInner.to_json()

# convert the object into a dict
fine_tune_model_body_params_samples_inner_dict = fine_tune_model_body_params_samples_inner_instance.to_dict()
# create an instance of FineTuneModelBodyParamsSamplesInner from a dict
fine_tune_model_body_params_samples_inner_form_dict = fine_tune_model_body_params_samples_inner.from_dict(fine_tune_model_body_params_samples_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



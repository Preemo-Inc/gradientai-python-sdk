# FineTuneModelSuccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_trainable_tokens** | **int** |  | 
**sum_loss** | **float** |  | 

## Example

```python
from gradientai.openapi.client.models.fine_tune_model_success import FineTuneModelSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of FineTuneModelSuccess from a JSON string
fine_tune_model_success_instance = FineTuneModelSuccess.from_json(json)
# print the JSON string representation of the object
print FineTuneModelSuccess.to_json()

# convert the object into a dict
fine_tune_model_success_dict = fine_tune_model_success_instance.to_dict()
# create an instance of FineTuneModelSuccess from a dict
fine_tune_model_success_form_dict = fine_tune_model_success.from_dict(fine_tune_model_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



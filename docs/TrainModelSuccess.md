# TrainModelSuccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_trainable_tokens** | **int** |  | 
**sum_loss** | **float** |  | 

## Example

```python
from gradientai.models.train_model_success import TrainModelSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of TrainModelSuccess from a JSON string
train_model_success_instance = TrainModelSuccess.from_json(json)
# print the JSON string representation of the object
print TrainModelSuccess.to_json()

# convert the object into a dict
train_model_success_dict = train_model_success_instance.to_dict()
# create an instance of TrainModelSuccess from a dict
train_model_success_form_dict = train_model_success.from_dict(train_model_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



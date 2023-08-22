# CompleteModelBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_generated_token_count** | **int** | The maximum number of tokens to generate. | [optional] 
**query** | **str** | The prompt string you are providing the model, to which the model will generate a completion in response. | 
**temperature** | **float** | This parameter adjusts the degree of randomness in generation. Higher temperature results in more diverse generations. | [optional] 
**top_k** | **int** | This parameter ensures that only the top k most likely tokens are considered for generation at each step. | [optional] 
**top_p** | **float** | This parameter ensures that only the most likely tokens, with total probability mass of p, are considered for generation at each step. If topK is also enabled, topP acts after topK. | [optional] 

## Example

```python
from gradientai.models.complete_model_body_params import CompleteModelBodyParams

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteModelBodyParams from a JSON string
complete_model_body_params_instance = CompleteModelBodyParams.from_json(json)
# print the JSON string representation of the object
print CompleteModelBodyParams.to_json()

# convert the object into a dict
complete_model_body_params_dict = complete_model_body_params_instance.to_dict()
# create an instance of CompleteModelBodyParams from a dict
complete_model_body_params_form_dict = complete_model_body_params.from_dict(complete_model_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MeaningBasedChunker


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunker_type** | **str** |  | 
**overlap** | **int** |  | [optional] 
**sentence_group_length** | **int** |  | [optional] 
**similiarity_percent_threshold** | **int** |  | [optional] 
**size** | **int** |  | [optional] 

## Example

```python
from gradientai.openapi.client.models.meaning_based_chunker import MeaningBasedChunker


json = "{}"
# create an instance of MeaningBasedChunker from a JSON string
meaning_based_chunker_instance = MeaningBasedChunker.from_json(json)
# print the JSON string representation of the object
print MeaningBasedChunker.to_json()

# convert the object into a dict
meaning_based_chunker_dict = meaning_based_chunker_instance.to_dict()
# create an instance of MeaningBasedChunker from a dict
meaning_based_chunker_form_dict = meaning_based_chunker.from_dict(meaning_based_chunker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



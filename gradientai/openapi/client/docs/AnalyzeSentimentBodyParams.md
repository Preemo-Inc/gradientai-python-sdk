# AnalyzeSentimentBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | **str** | The document that will be analyzed to determine the sentiment. | 
**examples** | [**List[AnalyzeSentimentBodyParamsExamplesInner]**](AnalyzeSentimentBodyParamsExamplesInner.md) | Example pairs of documents and sentiments. | 

## Example

```python
from gradientai.openapi.client.models.analyze_sentiment_body_params import AnalyzeSentimentBodyParams


json = "{}"
# create an instance of AnalyzeSentimentBodyParams from a JSON string
analyze_sentiment_body_params_instance = AnalyzeSentimentBodyParams.from_json(json)
# print the JSON string representation of the object
print AnalyzeSentimentBodyParams.to_json()

# convert the object into a dict
analyze_sentiment_body_params_dict = analyze_sentiment_body_params_instance.to_dict()
# create an instance of AnalyzeSentimentBodyParams from a dict
analyze_sentiment_body_params_form_dict = analyze_sentiment_body_params.from_dict(analyze_sentiment_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



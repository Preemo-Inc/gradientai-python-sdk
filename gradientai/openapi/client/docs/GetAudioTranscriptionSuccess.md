# GetAudioTranscriptionSuccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**GetAudioTranscriptionSuccessOneOf1Result**](GetAudioTranscriptionSuccessOneOf1Result.md) |  | 
**status** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.get_audio_transcription_success import GetAudioTranscriptionSuccess


json = "{}"
# create an instance of GetAudioTranscriptionSuccess from a JSON string
get_audio_transcription_success_instance = GetAudioTranscriptionSuccess.from_json(json)
# print the JSON string representation of the object
print GetAudioTranscriptionSuccess.to_json()

# convert the object into a dict
get_audio_transcription_success_dict = get_audio_transcription_success_instance.to_dict()
# create an instance of GetAudioTranscriptionSuccess from a dict
get_audio_transcription_success_form_dict = get_audio_transcription_success.from_dict(get_audio_transcription_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



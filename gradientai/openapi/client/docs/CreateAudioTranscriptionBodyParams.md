# CreateAudioTranscriptionBodyParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | 

## Example

```python
from gradientai.openapi.client.models.create_audio_transcription_body_params import CreateAudioTranscriptionBodyParams


json = "{}"
# create an instance of CreateAudioTranscriptionBodyParams from a JSON string
create_audio_transcription_body_params_instance = CreateAudioTranscriptionBodyParams.from_json(json)
# print the JSON string representation of the object
print CreateAudioTranscriptionBodyParams.to_json()

# convert the object into a dict
create_audio_transcription_body_params_dict = create_audio_transcription_body_params_instance.to_dict()
# create an instance of CreateAudioTranscriptionBodyParams from a dict
create_audio_transcription_body_params_form_dict = create_audio_transcription_body_params.from_dict(create_audio_transcription_body_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



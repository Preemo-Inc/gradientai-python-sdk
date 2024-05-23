# coding: utf-8

"""
    Gradient AI API

    Interface for interacting with Gradient AI.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@gradient.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr, validator
from gradientai.openapi.client.models.get_audio_transcription_success_one_of1_result import GetAudioTranscriptionSuccessOneOf1Result

class GetAudioTranscriptionSuccessOneOf1(BaseModel):
    """
    GetAudioTranscriptionSuccessOneOf1
    """
    result: GetAudioTranscriptionSuccessOneOf1Result = Field(...)
    status: StrictStr = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["result", "status"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('succeeded'):
            raise ValueError("must be one of enum values ('succeeded')")
        return value

    class Config:
        """pydantic.v1 configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GetAudioTranscriptionSuccessOneOf1:
        """Create an instance of GetAudioTranscriptionSuccessOneOf1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetAudioTranscriptionSuccessOneOf1:
        """Create an instance of GetAudioTranscriptionSuccessOneOf1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAudioTranscriptionSuccessOneOf1.parse_obj(obj)

        _obj = GetAudioTranscriptionSuccessOneOf1.parse_obj({
            "result": GetAudioTranscriptionSuccessOneOf1Result.from_dict(obj.get("result")) if obj.get("result") is not None else None,
            "status": obj.get("status")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


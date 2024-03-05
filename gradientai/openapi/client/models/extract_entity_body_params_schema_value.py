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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class ExtractEntityBodyParamsSchemaValue(BaseModel):
    """
    ExtractEntityBodyParamsSchemaValue
    """
    required: Optional[StrictBool] = False
    type: StrictStr = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["required", "type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('boolean', 'number', 'string'):
            raise ValueError("must be one of enum values ('boolean', 'number', 'string')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ExtractEntityBodyParamsSchemaValue:
        """Create an instance of ExtractEntityBodyParamsSchemaValue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if required (nullable) is None
        # and __fields_set__ contains the field
        if self.required is None and "required" in self.__fields_set__:
            _dict['required'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExtractEntityBodyParamsSchemaValue:
        """Create an instance of ExtractEntityBodyParamsSchemaValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExtractEntityBodyParamsSchemaValue.parse_obj(obj)

        _obj = ExtractEntityBodyParamsSchemaValue.parse_obj({
            "required": obj.get("required") if obj.get("required") is not None else False,
            "type": obj.get("type")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

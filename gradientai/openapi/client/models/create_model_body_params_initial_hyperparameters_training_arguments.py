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


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, confloat, conint

class CreateModelBodyParamsInitialHyperparametersTrainingArguments(BaseModel):
    """
    CreateModelBodyParamsInitialHyperparametersTrainingArguments
    """
    learning_rate: Optional[Union[confloat(lt=1, gt=0, strict=True), conint(lt=1, gt=0, strict=True)]] = Field(None, alias="learningRate")
    additional_properties: Dict[str, Any] = {}
    __properties = ["learningRate"]

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
    def from_json(cls, json_str: str) -> CreateModelBodyParamsInitialHyperparametersTrainingArguments:
        """Create an instance of CreateModelBodyParamsInitialHyperparametersTrainingArguments from a JSON string"""
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

        # set to None if learning_rate (nullable) is None
        # and __fields_set__ contains the field
        if self.learning_rate is None and "learning_rate" in self.__fields_set__:
            _dict['learningRate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateModelBodyParamsInitialHyperparametersTrainingArguments:
        """Create an instance of CreateModelBodyParamsInitialHyperparametersTrainingArguments from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateModelBodyParamsInitialHyperparametersTrainingArguments.parse_obj(obj)

        _obj = CreateModelBodyParamsInitialHyperparametersTrainingArguments.parse_obj({
            "learning_rate": obj.get("learningRate")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

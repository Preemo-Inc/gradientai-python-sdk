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
from pydantic.v1 import BaseModel, Field
from gradientai.openapi.client.models.fine_tune_model_body_params_samples_inner_fine_tuning_parameters import FineTuneModelBodyParamsSamplesInnerFineTuningParameters
from gradientai.openapi.client.models.fine_tune_model_body_params_samples_inner_inputs import FineTuneModelBodyParamsSamplesInnerInputs

class FineTuneModelBodyParamsSamplesInner(BaseModel):
    """
    FineTuneModelBodyParamsSamplesInner
    """
    fine_tuning_parameters: Optional[FineTuneModelBodyParamsSamplesInnerFineTuningParameters] = Field(None, alias="fineTuningParameters")
    inputs: FineTuneModelBodyParamsSamplesInnerInputs = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["fineTuningParameters", "inputs"]

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
    def from_json(cls, json_str: str) -> FineTuneModelBodyParamsSamplesInner:
        """Create an instance of FineTuneModelBodyParamsSamplesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of fine_tuning_parameters
        if self.fine_tuning_parameters:
            _dict['fineTuningParameters'] = self.fine_tuning_parameters.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of inputs
        if self.inputs:
            _dict['inputs'] = self.inputs.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if fine_tuning_parameters (nullable) is None
        # and __fields_set__ contains the field
        if self.fine_tuning_parameters is None and "fine_tuning_parameters" in self.__fields_set__:
            _dict['fineTuningParameters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FineTuneModelBodyParamsSamplesInner:
        """Create an instance of FineTuneModelBodyParamsSamplesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FineTuneModelBodyParamsSamplesInner.parse_obj(obj)

        _obj = FineTuneModelBodyParamsSamplesInner.parse_obj({
            "fine_tuning_parameters": FineTuneModelBodyParamsSamplesInnerFineTuningParameters.from_dict(obj.get("fineTuningParameters")) if obj.get("fineTuningParameters") is not None else None,
            "inputs": FineTuneModelBodyParamsSamplesInnerInputs.from_dict(obj.get("inputs")) if obj.get("inputs") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


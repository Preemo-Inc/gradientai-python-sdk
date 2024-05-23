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


from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist
from gradientai.openapi.client.models.list_models_success_models_inner import ListModelsSuccessModelsInner

class ListModelsSuccess(BaseModel):
    """
    ListModelsSuccess
    """
    models: conlist(ListModelsSuccessModelsInner) = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["models"]

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
    def from_json(cls, json_str: str) -> ListModelsSuccess:
        """Create an instance of ListModelsSuccess from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of each item in models (list)
        _items = []
        if self.models:
            for _item in self.models:
                if _item:
                    _items.append(_item.to_dict())
            _dict['models'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListModelsSuccess:
        """Create an instance of ListModelsSuccess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListModelsSuccess.parse_obj(obj)

        _obj = ListModelsSuccess.parse_obj({
            "models": [ListModelsSuccessModelsInner.from_dict(_item) for _item in obj.get("models")] if obj.get("models") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


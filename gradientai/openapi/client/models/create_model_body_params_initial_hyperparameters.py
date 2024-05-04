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
from gradientai.openapi.client.models.create_model_body_params_initial_hyperparameters_lora_hyperparameters import CreateModelBodyParamsInitialHyperparametersLoraHyperparameters
from gradientai.openapi.client.models.create_model_body_params_initial_hyperparameters_training_arguments import CreateModelBodyParamsInitialHyperparametersTrainingArguments

class CreateModelBodyParamsInitialHyperparameters(BaseModel):
    """
    CreateModelBodyParamsInitialHyperparameters
    """
    lora_hyperparameters: Optional[CreateModelBodyParamsInitialHyperparametersLoraHyperparameters] = Field(None, alias="loraHyperparameters")
    training_arguments: Optional[CreateModelBodyParamsInitialHyperparametersTrainingArguments] = Field(None, alias="trainingArguments")
    additional_properties: Dict[str, Any] = {}
    __properties = ["loraHyperparameters", "trainingArguments"]

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
    def from_json(cls, json_str: str) -> CreateModelBodyParamsInitialHyperparameters:
        """Create an instance of CreateModelBodyParamsInitialHyperparameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of lora_hyperparameters
        if self.lora_hyperparameters:
            _dict['loraHyperparameters'] = self.lora_hyperparameters.to_dict()
        # override the default output from pydantic.v1 by calling `to_dict()` of training_arguments
        if self.training_arguments:
            _dict['trainingArguments'] = self.training_arguments.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if lora_hyperparameters (nullable) is None
        # and __fields_set__ contains the field
        if self.lora_hyperparameters is None and "lora_hyperparameters" in self.__fields_set__:
            _dict['loraHyperparameters'] = None

        # set to None if training_arguments (nullable) is None
        # and __fields_set__ contains the field
        if self.training_arguments is None and "training_arguments" in self.__fields_set__:
            _dict['trainingArguments'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateModelBodyParamsInitialHyperparameters:
        """Create an instance of CreateModelBodyParamsInitialHyperparameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateModelBodyParamsInitialHyperparameters.parse_obj(obj)

        _obj = CreateModelBodyParamsInitialHyperparameters.parse_obj({
            "lora_hyperparameters": CreateModelBodyParamsInitialHyperparametersLoraHyperparameters.from_dict(obj.get("loraHyperparameters")) if obj.get("loraHyperparameters") is not None else None,
            "training_arguments": CreateModelBodyParamsInitialHyperparametersTrainingArguments.from_dict(obj.get("trainingArguments")) if obj.get("trainingArguments") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


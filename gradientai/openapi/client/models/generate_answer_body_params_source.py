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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator
from gradientai.openapi.client.models.generate_answer_body_params_source_one_of import GenerateAnswerBodyParamsSourceOneOf
from gradientai.openapi.client.models.generate_answer_body_params_source_one_of1 import GenerateAnswerBodyParamsSourceOneOf1
from typing import Any, List
from pydantic.v1 import StrictStr, Field

GENERATEANSWERBODYPARAMSSOURCE_ONE_OF_SCHEMAS = ["GenerateAnswerBodyParamsSourceOneOf", "GenerateAnswerBodyParamsSourceOneOf1"]

class GenerateAnswerBodyParamsSource(BaseModel):
    """
    GenerateAnswerBodyParamsSource
    """
    # data type: GenerateAnswerBodyParamsSourceOneOf
    oneof_schema_1_validator: Optional[GenerateAnswerBodyParamsSourceOneOf] = None
    # data type: GenerateAnswerBodyParamsSourceOneOf1
    oneof_schema_2_validator: Optional[GenerateAnswerBodyParamsSourceOneOf1] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(GENERATEANSWERBODYPARAMSSOURCE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = GenerateAnswerBodyParamsSource.construct()
        error_messages = []
        match = 0
        # validate data type: GenerateAnswerBodyParamsSourceOneOf
        if not isinstance(v, GenerateAnswerBodyParamsSourceOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GenerateAnswerBodyParamsSourceOneOf`")
        else:
            match += 1
        # validate data type: GenerateAnswerBodyParamsSourceOneOf1
        if not isinstance(v, GenerateAnswerBodyParamsSourceOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GenerateAnswerBodyParamsSourceOneOf1`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GenerateAnswerBodyParamsSource with oneOf schemas: GenerateAnswerBodyParamsSourceOneOf, GenerateAnswerBodyParamsSourceOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GenerateAnswerBodyParamsSource with oneOf schemas: GenerateAnswerBodyParamsSourceOneOf, GenerateAnswerBodyParamsSourceOneOf1. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> GenerateAnswerBodyParamsSource:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> GenerateAnswerBodyParamsSource:
        """Returns the object represented by the json string"""
        instance = GenerateAnswerBodyParamsSource.construct()
        error_messages = []
        match = 0

        # deserialize data into GenerateAnswerBodyParamsSourceOneOf
        try:
            instance.actual_instance = GenerateAnswerBodyParamsSourceOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GenerateAnswerBodyParamsSourceOneOf1
        try:
            instance.actual_instance = GenerateAnswerBodyParamsSourceOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GenerateAnswerBodyParamsSource with oneOf schemas: GenerateAnswerBodyParamsSourceOneOf, GenerateAnswerBodyParamsSourceOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GenerateAnswerBodyParamsSource with oneOf schemas: GenerateAnswerBodyParamsSourceOneOf, GenerateAnswerBodyParamsSourceOneOf1. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        elif isinstance(self.actual_instance, list):
            result = []
            for element in self.actual_instance:
                element_to_dict = getattr(element, "to_dict", None)
                result.append(
                    element.to_dict()
                    if callable(element_to_dict)
                    else element
                )

            return result
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


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
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from gradientai.openapi.client.models.complete_model_error_one_of import CompleteModelErrorOneOf
from gradientai.openapi.client.models.complete_model_error_one_of1 import CompleteModelErrorOneOf1
from gradientai.openapi.client.models.complete_model_error_one_of2 import CompleteModelErrorOneOf2
from gradientai.openapi.client.models.complete_model_error_one_of4 import CompleteModelErrorOneOf4
from gradientai.openapi.client.models.complete_model_error_one_of5 import CompleteModelErrorOneOf5
from gradientai.openapi.client.models.fine_tune_model_error_one_of import FineTuneModelErrorOneOf
from typing import Any, List
from pydantic import StrictStr, Field

FINETUNEMODELERROR_ONE_OF_SCHEMAS = ["CompleteModelErrorOneOf", "CompleteModelErrorOneOf1", "CompleteModelErrorOneOf2", "CompleteModelErrorOneOf4", "CompleteModelErrorOneOf5", "FineTuneModelErrorOneOf"]

class FineTuneModelError(BaseModel):
    """
    FineTuneModelError
    """
    # data type: CompleteModelErrorOneOf1
    oneof_schema_1_validator: Optional[CompleteModelErrorOneOf1] = None
    # data type: CompleteModelErrorOneOf
    oneof_schema_2_validator: Optional[CompleteModelErrorOneOf] = None
    # data type: CompleteModelErrorOneOf2
    oneof_schema_3_validator: Optional[CompleteModelErrorOneOf2] = None
    # data type: FineTuneModelErrorOneOf
    oneof_schema_4_validator: Optional[FineTuneModelErrorOneOf] = None
    # data type: CompleteModelErrorOneOf4
    oneof_schema_5_validator: Optional[CompleteModelErrorOneOf4] = None
    # data type: CompleteModelErrorOneOf5
    oneof_schema_6_validator: Optional[CompleteModelErrorOneOf5] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(FINETUNEMODELERROR_ONE_OF_SCHEMAS, const=True)

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
        instance = FineTuneModelError.construct()
        error_messages = []
        match = 0
        # validate data type: CompleteModelErrorOneOf1
        if not isinstance(v, CompleteModelErrorOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CompleteModelErrorOneOf1`")
        else:
            match += 1
        # validate data type: CompleteModelErrorOneOf
        if not isinstance(v, CompleteModelErrorOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CompleteModelErrorOneOf`")
        else:
            match += 1
        # validate data type: CompleteModelErrorOneOf2
        if not isinstance(v, CompleteModelErrorOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CompleteModelErrorOneOf2`")
        else:
            match += 1
        # validate data type: FineTuneModelErrorOneOf
        if not isinstance(v, FineTuneModelErrorOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FineTuneModelErrorOneOf`")
        else:
            match += 1
        # validate data type: CompleteModelErrorOneOf4
        if not isinstance(v, CompleteModelErrorOneOf4):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CompleteModelErrorOneOf4`")
        else:
            match += 1
        # validate data type: CompleteModelErrorOneOf5
        if not isinstance(v, CompleteModelErrorOneOf5):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CompleteModelErrorOneOf5`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in FineTuneModelError with oneOf schemas: CompleteModelErrorOneOf, CompleteModelErrorOneOf1, CompleteModelErrorOneOf2, CompleteModelErrorOneOf4, CompleteModelErrorOneOf5, FineTuneModelErrorOneOf. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in FineTuneModelError with oneOf schemas: CompleteModelErrorOneOf, CompleteModelErrorOneOf1, CompleteModelErrorOneOf2, CompleteModelErrorOneOf4, CompleteModelErrorOneOf5, FineTuneModelErrorOneOf. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> FineTuneModelError:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> FineTuneModelError:
        """Returns the object represented by the json string"""
        instance = FineTuneModelError.construct()
        error_messages = []
        match = 0

        # deserialize data into CompleteModelErrorOneOf1
        try:
            instance.actual_instance = CompleteModelErrorOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CompleteModelErrorOneOf
        try:
            instance.actual_instance = CompleteModelErrorOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CompleteModelErrorOneOf2
        try:
            instance.actual_instance = CompleteModelErrorOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FineTuneModelErrorOneOf
        try:
            instance.actual_instance = FineTuneModelErrorOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CompleteModelErrorOneOf4
        try:
            instance.actual_instance = CompleteModelErrorOneOf4.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CompleteModelErrorOneOf5
        try:
            instance.actual_instance = CompleteModelErrorOneOf5.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into FineTuneModelError with oneOf schemas: CompleteModelErrorOneOf, CompleteModelErrorOneOf1, CompleteModelErrorOneOf2, CompleteModelErrorOneOf4, CompleteModelErrorOneOf5, FineTuneModelErrorOneOf. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into FineTuneModelError with oneOf schemas: CompleteModelErrorOneOf, CompleteModelErrorOneOf1, CompleteModelErrorOneOf2, CompleteModelErrorOneOf4, CompleteModelErrorOneOf5, FineTuneModelErrorOneOf. Details: " + ", ".join(error_messages))
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

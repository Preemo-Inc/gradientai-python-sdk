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
from gradientai.openapi.client.models.base_model import BaseModel
from gradientai.openapi.client.models.model_adapter import ModelAdapter
from typing import Any, List
from pydantic.v1 import StrictStr, Field

LISTMODELSSUCCESSMODELSINNER_ONE_OF_SCHEMAS = ["BaseModel", "ModelAdapter"]

class ListModelsSuccessModelsInner(BaseModel):
    """
    ListModelsSuccessModelsInner
    """
    # data type: BaseModel
    oneof_schema_1_validator: Optional[BaseModel] = None
    # data type: ModelAdapter
    oneof_schema_2_validator: Optional[ModelAdapter] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(LISTMODELSSUCCESSMODELSINNER_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    discriminator_value_class_map = {
    }

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
        instance = ListModelsSuccessModelsInner.construct()
        error_messages = []
        match = 0
        # validate data type: BaseModel
        if not isinstance(v, BaseModel):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BaseModel`")
        else:
            match += 1
        # validate data type: ModelAdapter
        if not isinstance(v, ModelAdapter):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ModelAdapter`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ListModelsSuccessModelsInner with oneOf schemas: BaseModel, ModelAdapter. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ListModelsSuccessModelsInner with oneOf schemas: BaseModel, ModelAdapter. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ListModelsSuccessModelsInner:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ListModelsSuccessModelsInner:
        """Returns the object represented by the json string"""
        instance = ListModelsSuccessModelsInner.construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `type` in the input.")

        # check if data type is `BaseModel`
        if _data_type == "baseModel":
            instance.actual_instance = BaseModel.from_json(json_str)
            return instance

        # check if data type is `ModelAdapter`
        if _data_type == "modelAdapter":
            instance.actual_instance = ModelAdapter.from_json(json_str)
            return instance

        # deserialize data into BaseModel
        try:
            instance.actual_instance = BaseModel.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ModelAdapter
        try:
            instance.actual_instance = ModelAdapter.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ListModelsSuccessModelsInner with oneOf schemas: BaseModel, ModelAdapter. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ListModelsSuccessModelsInner with oneOf schemas: BaseModel, ModelAdapter. Details: " + ", ".join(error_messages))
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


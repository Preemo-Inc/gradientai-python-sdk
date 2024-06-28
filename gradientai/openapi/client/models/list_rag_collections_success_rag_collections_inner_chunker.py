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
from gradientai.openapi.client.models.list_rag_collections_success_rag_collections_inner_chunker_one_of import ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf
from gradientai.openapi.client.models.list_rag_collections_success_rag_collections_inner_chunker_one_of1 import ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf1
from gradientai.openapi.client.models.list_rag_collections_success_rag_collections_inner_chunker_one_of2 import ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf2
from gradientai.openapi.client.models.list_rag_collections_success_rag_collections_inner_chunker_one_of3 import ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf3
from typing import Any, List
from pydantic.v1 import StrictStr, Field

LISTRAGCOLLECTIONSSUCCESSRAGCOLLECTIONSINNERCHUNKER_ONE_OF_SCHEMAS = ["ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf", "ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf1", "ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf2", "ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf3"]

class ListRagCollectionsSuccessRagCollectionsInnerChunker(BaseModel):
    """
    ListRagCollectionsSuccessRagCollectionsInnerChunker
    """
    # data type: ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf
    oneof_schema_1_validator: Optional[ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf] = None
    # data type: ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf1
    oneof_schema_2_validator: Optional[ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf1] = None
    # data type: ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf2
    oneof_schema_3_validator: Optional[ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf2] = None
    # data type: ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf3
    oneof_schema_4_validator: Optional[ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf3] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(LISTRAGCOLLECTIONSSUCCESSRAGCOLLECTIONSINNERCHUNKER_ONE_OF_SCHEMAS, const=True)

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
        instance = ListRagCollectionsSuccessRagCollectionsInnerChunker.construct()
        error_messages = []
        match = 0
        # validate data type: ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf
        if not isinstance(v, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf`")
        else:
            match += 1
        # validate data type: ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf1
        if not isinstance(v, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf1`")
        else:
            match += 1
        # validate data type: ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf2
        if not isinstance(v, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf2`")
        else:
            match += 1
        # validate data type: ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf3
        if not isinstance(v, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf3):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf3`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ListRagCollectionsSuccessRagCollectionsInnerChunker with oneOf schemas: ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf1, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf2, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf3. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ListRagCollectionsSuccessRagCollectionsInnerChunker with oneOf schemas: ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf1, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf2, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf3. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ListRagCollectionsSuccessRagCollectionsInnerChunker:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ListRagCollectionsSuccessRagCollectionsInnerChunker:
        """Returns the object represented by the json string"""
        instance = ListRagCollectionsSuccessRagCollectionsInnerChunker.construct()
        error_messages = []
        match = 0

        # deserialize data into ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf
        try:
            instance.actual_instance = ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf1
        try:
            instance.actual_instance = ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf2
        try:
            instance.actual_instance = ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf3
        try:
            instance.actual_instance = ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf3.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ListRagCollectionsSuccessRagCollectionsInnerChunker with oneOf schemas: ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf1, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf2, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf3. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ListRagCollectionsSuccessRagCollectionsInnerChunker with oneOf schemas: ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf1, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf2, ListRagCollectionsSuccessRagCollectionsInnerChunkerOneOf3. Details: " + ", ".join(error_messages))
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

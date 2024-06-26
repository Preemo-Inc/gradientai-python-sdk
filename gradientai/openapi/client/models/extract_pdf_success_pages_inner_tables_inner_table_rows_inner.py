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
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, validator
from gradientai.openapi.client.models.extract_pdf_success_pages_inner_tables_inner_table_rows_inner_cells_inner import ExtractPdfSuccessPagesInnerTablesInnerTableRowsInnerCellsInner

class ExtractPdfSuccessPagesInnerTablesInnerTableRowsInner(BaseModel):
    """
    ExtractPdfSuccessPagesInnerTablesInnerTableRowsInner
    """
    cells: conlist(ExtractPdfSuccessPagesInnerTablesInnerTableRowsInnerCellsInner) = Field(...)
    type: StrictStr = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["cells", "type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('table_data_row', 'table_header'):
            raise ValueError("must be one of enum values ('table_data_row', 'table_header')")
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
    def from_json(cls, json_str: str) -> ExtractPdfSuccessPagesInnerTablesInnerTableRowsInner:
        """Create an instance of ExtractPdfSuccessPagesInnerTablesInnerTableRowsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic.v1 by calling `to_dict()` of each item in cells (list)
        _items = []
        if self.cells:
            for _item in self.cells:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cells'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExtractPdfSuccessPagesInnerTablesInnerTableRowsInner:
        """Create an instance of ExtractPdfSuccessPagesInnerTablesInnerTableRowsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExtractPdfSuccessPagesInnerTablesInnerTableRowsInner.parse_obj(obj)

        _obj = ExtractPdfSuccessPagesInnerTablesInnerTableRowsInner.parse_obj({
            "cells": [ExtractPdfSuccessPagesInnerTablesInnerTableRowsInnerCellsInner.from_dict(_item) for _item in obj.get("cells")] if obj.get("cells") is not None else None,
            "type": obj.get("type")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


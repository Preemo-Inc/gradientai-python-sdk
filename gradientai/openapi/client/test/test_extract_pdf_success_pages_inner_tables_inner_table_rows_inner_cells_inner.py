# coding: utf-8

"""
    Gradient AI API

    Interface for interacting with Gradient AI.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@gradient.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import gradientai.openapi.client
from gradientai.openapi.client.models.extract_pdf_success_pages_inner_tables_inner_table_rows_inner_cells_inner import ExtractPdfSuccessPagesInnerTablesInnerTableRowsInnerCellsInner  # noqa: E501
from gradientai.openapi.client.rest import ApiException

class TestExtractPdfSuccessPagesInnerTablesInnerTableRowsInnerCellsInner(unittest.TestCase):
    """ExtractPdfSuccessPagesInnerTablesInnerTableRowsInnerCellsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtractPdfSuccessPagesInnerTablesInnerTableRowsInnerCellsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtractPdfSuccessPagesInnerTablesInnerTableRowsInnerCellsInner`
        """
        model = gradientai.openapi.client.models.extract_pdf_success_pages_inner_tables_inner_table_rows_inner_cells_inner.ExtractPdfSuccessPagesInnerTablesInnerTableRowsInnerCellsInner()  # noqa: E501
        if include_optional :
            return ExtractPdfSuccessPagesInnerTablesInnerTableRowsInnerCellsInner(
                cell_value = '', 
                col_span = 0, 
                row_span = 0
            )
        else :
            return ExtractPdfSuccessPagesInnerTablesInnerTableRowsInnerCellsInner(
                cell_value = '',
                col_span = 0,
                row_span = 0,
        )
        """

    def testExtractPdfSuccessPagesInnerTablesInnerTableRowsInnerCellsInner(self):
        """Test ExtractPdfSuccessPagesInnerTablesInnerTableRowsInnerCellsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

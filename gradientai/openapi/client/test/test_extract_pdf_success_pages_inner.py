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
from gradientai.openapi.client.models.extract_pdf_success_pages_inner import ExtractPdfSuccessPagesInner  # noqa: E501
from gradientai.openapi.client.rest import ApiException

class TestExtractPdfSuccessPagesInner(unittest.TestCase):
    """ExtractPdfSuccessPagesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtractPdfSuccessPagesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtractPdfSuccessPagesInner`
        """
        model = gradientai.openapi.client.models.extract_pdf_success_pages_inner.ExtractPdfSuccessPagesInner()  # noqa: E501
        if include_optional :
            return ExtractPdfSuccessPagesInner(
                images = [
                    gradientai.openapi.client.models.extract_pdf_success_pages_inner_images_inner.ExtractPdfSuccess_pages_inner_images_inner(
                        data = '', 
                        format = 'base64-png', )
                    ], 
                page_number = 0, 
                tables = [
                    gradientai.openapi.client.models.extract_pdf_success_pages_inner_tables_inner.ExtractPdfSuccess_pages_inner_tables_inner(
                        name = '', 
                        table_rows = [
                            gradientai.openapi.client.models.extract_pdf_success_pages_inner_tables_inner_table_rows_inner.ExtractPdfSuccess_pages_inner_tables_inner_tableRows_inner(
                                cells = [
                                    gradientai.openapi.client.models.extract_pdf_success_pages_inner_tables_inner_table_rows_inner_cells_inner.ExtractPdfSuccess_pages_inner_tables_inner_tableRows_inner_cells_inner(
                                        cell_value = '', 
                                        col_span = 0, 
                                        row_span = 0, )
                                    ], 
                                type = 'table_data_row', )
                            ], )
                    ], 
                text = '', 
                text_blocks = [
                    gradientai.openapi.client.models.extract_pdf_success_pages_inner_text_blocks_inner.ExtractPdfSuccess_pages_inner_textBlocks_inner(
                        kind = 'footer', 
                        texts = [
                            ''
                            ], )
                    ]
            )
        else :
            return ExtractPdfSuccessPagesInner(
                images = [
                    gradientai.openapi.client.models.extract_pdf_success_pages_inner_images_inner.ExtractPdfSuccess_pages_inner_images_inner(
                        data = '', 
                        format = 'base64-png', )
                    ],
                page_number = 0,
                tables = [
                    gradientai.openapi.client.models.extract_pdf_success_pages_inner_tables_inner.ExtractPdfSuccess_pages_inner_tables_inner(
                        name = '', 
                        table_rows = [
                            gradientai.openapi.client.models.extract_pdf_success_pages_inner_tables_inner_table_rows_inner.ExtractPdfSuccess_pages_inner_tables_inner_tableRows_inner(
                                cells = [
                                    gradientai.openapi.client.models.extract_pdf_success_pages_inner_tables_inner_table_rows_inner_cells_inner.ExtractPdfSuccess_pages_inner_tables_inner_tableRows_inner_cells_inner(
                                        cell_value = '', 
                                        col_span = 0, 
                                        row_span = 0, )
                                    ], 
                                type = 'table_data_row', )
                            ], )
                    ],
                text = '',
                text_blocks = [
                    gradientai.openapi.client.models.extract_pdf_success_pages_inner_text_blocks_inner.ExtractPdfSuccess_pages_inner_textBlocks_inner(
                        kind = 'footer', 
                        texts = [
                            ''
                            ], )
                    ],
        )
        """

    def testExtractPdfSuccessPagesInner(self):
        """Test ExtractPdfSuccessPagesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

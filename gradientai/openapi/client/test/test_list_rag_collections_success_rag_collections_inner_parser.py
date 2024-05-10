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
from gradientai.openapi.client.models.list_rag_collections_success_rag_collections_inner_parser import ListRagCollectionsSuccessRagCollectionsInnerParser  # noqa: E501
from gradientai.openapi.client.rest import ApiException

class TestListRagCollectionsSuccessRagCollectionsInnerParser(unittest.TestCase):
    """ListRagCollectionsSuccessRagCollectionsInnerParser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListRagCollectionsSuccessRagCollectionsInnerParser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListRagCollectionsSuccessRagCollectionsInnerParser`
        """
        model = gradientai.openapi.client.models.list_rag_collections_success_rag_collections_inner_parser.ListRagCollectionsSuccessRagCollectionsInnerParser()  # noqa: E501
        if include_optional :
            return ListRagCollectionsSuccessRagCollectionsInnerParser(
                chunk_overlap = 0, 
                chunk_size = 0, 
                parser_type = 'simpleNodeParser'
            )
        else :
            return ListRagCollectionsSuccessRagCollectionsInnerParser(
                chunk_overlap = 0,
                chunk_size = 0,
                parser_type = 'simpleNodeParser',
        )
        """

    def testListRagCollectionsSuccessRagCollectionsInnerParser(self):
        """Test ListRagCollectionsSuccessRagCollectionsInnerParser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

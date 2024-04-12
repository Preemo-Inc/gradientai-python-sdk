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

import gradientai.openapi.client
from gradientai.openapi.client.api.rag_api import RAGApi  # noqa: E501
from gradientai.openapi.client.rest import ApiException


class TestRAGApi(unittest.TestCase):
    """RAGApi unit test stubs"""

    def setUp(self):
        self.api = gradientai.openapi.client.api.rag_api.RAGApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_files_to_rag_collection(self):
        """Test case for add_files_to_rag_collection

        Add files to RAG collection  # noqa: E501
        """
        pass

    def test_create_rag_collection(self):
        """Test case for create_rag_collection

        Create RAG collection  # noqa: E501
        """
        pass

    def test_get_rag_collection(self):
        """Test case for get_rag_collection

        Get RAG collection  # noqa: E501
        """
        pass

    def test_list_rag_collections(self):
        """Test case for list_rag_collections

        List RAG collections  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
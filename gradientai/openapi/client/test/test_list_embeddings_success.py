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
from gradientai.openapi.client.models.list_embeddings_success import ListEmbeddingsSuccess  # noqa: E501
from gradientai.openapi.client.rest import ApiException

class TestListEmbeddingsSuccess(unittest.TestCase):
    """ListEmbeddingsSuccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListEmbeddingsSuccess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListEmbeddingsSuccess`
        """
        model = gradientai.openapi.client.models.list_embeddings_success.ListEmbeddingsSuccess()  # noqa: E501
        if include_optional :
            return ListEmbeddingsSuccess(
                embeddings_models = [
                    gradientai.openapi.client.models.list_embeddings_success_embeddings_models_inner.ListEmbeddingsSuccess_embeddingsModels_inner(
                        slug = 'bge-large', )
                    ]
            )
        else :
            return ListEmbeddingsSuccess(
                embeddings_models = [
                    gradientai.openapi.client.models.list_embeddings_success_embeddings_models_inner.ListEmbeddingsSuccess_embeddingsModels_inner(
                        slug = 'bge-large', )
                    ],
        )
        """

    def testListEmbeddingsSuccess(self):
        """Test ListEmbeddingsSuccess"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

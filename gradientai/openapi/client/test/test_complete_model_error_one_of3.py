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
from gradientai.openapi.client.models.complete_model_error_one_of3 import CompleteModelErrorOneOf3  # noqa: E501
from gradientai.openapi.client.rest import ApiException

class TestCompleteModelErrorOneOf3(unittest.TestCase):
    """CompleteModelErrorOneOf3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CompleteModelErrorOneOf3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompleteModelErrorOneOf3`
        """
        model = gradientai.openapi.client.models.complete_model_error_one_of3.CompleteModelErrorOneOf3()  # noqa: E501
        if include_optional :
            return CompleteModelErrorOneOf3(
                message = '0', 
                type = 'failed'
            )
        else :
            return CompleteModelErrorOneOf3(
                message = '0',
                type = 'failed',
        )
        """

    def testCompleteModelErrorOneOf3(self):
        """Test CompleteModelErrorOneOf3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

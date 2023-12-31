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
from gradientai.openapi.client.models.create_model_body_params_initial_hyperparameters import CreateModelBodyParamsInitialHyperparameters  # noqa: E501
from gradientai.openapi.client.rest import ApiException

class TestCreateModelBodyParamsInitialHyperparameters(unittest.TestCase):
    """CreateModelBodyParamsInitialHyperparameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateModelBodyParamsInitialHyperparameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateModelBodyParamsInitialHyperparameters`
        """
        model = gradientai.openapi.client.models.create_model_body_params_initial_hyperparameters.CreateModelBodyParamsInitialHyperparameters()  # noqa: E501
        if include_optional :
            return CreateModelBodyParamsInitialHyperparameters(
                lora_hyperparameters = gradientai.openapi.client.models.create_model_body_params_initial_hyperparameters_lora_hyperparameters.CreateModelBodyParams_initialHyperparameters_loraHyperparameters(
                    rank = 0, ), 
                training_arguments = gradientai.openapi.client.models.create_model_body_params_initial_hyperparameters_training_arguments.CreateModelBodyParams_initialHyperparameters_trainingArguments(
                    learning_rate = 0, )
            )
        else :
            return CreateModelBodyParamsInitialHyperparameters(
        )
        """

    def testCreateModelBodyParamsInitialHyperparameters(self):
        """Test CreateModelBodyParamsInitialHyperparameters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

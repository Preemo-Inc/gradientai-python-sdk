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
from gradientai.openapi.client.models.create_model_body_params import CreateModelBodyParams  # noqa: E501
from gradientai.openapi.client.rest import ApiException

class TestCreateModelBodyParams(unittest.TestCase):
    """CreateModelBodyParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateModelBodyParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateModelBodyParams`
        """
        model = gradientai.openapi.client.models.create_model_body_params.CreateModelBodyParams()  # noqa: E501
        if include_optional :
            return CreateModelBodyParams(
                initial_hyperparameters = gradientai.openapi.client.models.create_model_body_params_initial_hyperparameters.CreateModelBodyParams_initialHyperparameters(
                    lora_hyperparameters = gradientai.openapi.client.models.create_model_body_params_initial_hyperparameters_lora_hyperparameters.CreateModelBodyParams_initialHyperparameters_loraHyperparameters(
                        rank = 0, ), 
                    training_arguments = gradientai.openapi.client.models.create_model_body_params_initial_hyperparameters_training_arguments.CreateModelBodyParams_initialHyperparameters_trainingArguments(
                        learning_rate = 0, ), ), 
                model = gradientai.openapi.client.models.create_model_body_params_model.CreateModelBodyParams_model(
                    base_model_id = '0', 
                    name = '0', )
            )
        else :
            return CreateModelBodyParams(
                model = gradientai.openapi.client.models.create_model_body_params_model.CreateModelBodyParams_model(
                    base_model_id = '0', 
                    name = '0', ),
        )
        """

    def testCreateModelBodyParams(self):
        """Test CreateModelBodyParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

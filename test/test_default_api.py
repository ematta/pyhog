# coding: utf-8

"""
    MailHog API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.default_api import DefaultApi  # noqa: E501
from openapi_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v2_messages_get(self):
        """Test case for api_v2_messages_get

        """
        pass

    def test_api_v2_search_get(self):
        """Test case for api_v2_search_get

        """
        pass


if __name__ == '__main__':
    unittest.main()

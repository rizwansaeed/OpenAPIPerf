# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import luisd
from luisd.paths.api_persons_id_type_scope_id_type_code_code_properties_4 import post  # noqa: E501
from luisd import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiPersonsIdTypeScopeIdTypeCodeCodeProperties(ApiTestMixin, unittest.TestCase):
    """
    ApiPersonsIdTypeScopeIdTypeCodeCodeProperties unit test stubs
        [EXPERIMENTAL] SetPersonProperties: Set Person Properties  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
















if __name__ == '__main__':
    unittest.main()

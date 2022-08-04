# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import luisd
from luisd.paths.api_systemconfiguration_cutlabels_code import delete  # noqa: E501
from luisd import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiSystemconfigurationCutlabelsCode(ApiTestMixin, unittest.TestCase):
    """
    ApiSystemconfigurationCutlabelsCode unit test stubs
        [EARLY ACCESS] DeleteCutLabelDefinition: Delete a Cut Label  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200








if __name__ == '__main__':
    unittest.main()

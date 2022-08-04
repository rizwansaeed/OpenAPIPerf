# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import luisd
from luisd.paths.api_transactionportfolios_scope_code_cashflows import get  # noqa: E501
from luisd import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiTransactionportfoliosScopeCodeCashflows(ApiTestMixin, unittest.TestCase):
    """
    ApiTransactionportfoliosScopeCodeCashflows unit test stubs
        [BETA] GetPortfolioCashFlows: Get portfolio cash flows  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200








if __name__ == '__main__':
    unittest.main()

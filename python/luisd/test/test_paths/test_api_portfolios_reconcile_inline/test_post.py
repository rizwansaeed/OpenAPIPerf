# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import luisd
from luisd.paths.api_portfolios_reconcile_inline import post  # noqa: E501
from luisd import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiPortfoliosReconcileInline(ApiTestMixin, unittest.TestCase):
    """
    ApiPortfoliosReconcileInline unit test stubs
        [BETA] ReconcileInline: Reconcile valuations performed on one or two sets of inline instruments using one or two configuration recipes.  # noqa: E501
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
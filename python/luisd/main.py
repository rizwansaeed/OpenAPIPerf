import cProfile
import pstats
import unittest
from unittest.mock import patch, MagicMock

from luisd import ApiClient
from luisd.api.transaction_portfolios_api import TransactionPortfoliosApi


class DeserializationTests(unittest.TestCase):
    """
    to generate the client
    java -jar /Users/justinblack/programming/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar generate -i data/lusid.json -o python/luisd -g python-experimental --package-name luisd
    """

    def test_deserialize(self):
        with open("../../data/response.json") as f:
            data = f.read()

        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.reason = "OK"
        mock_response.data = str.encode(data)
        mock_response.getheader.return_value = "application/json"

        with patch.object(ApiClient, "request", return_value=mock_response):
            api = TransactionPortfoliosApi()

            profiler = cProfile.Profile()
            profiler.enable()

            api.get_transactions(path_params=dict(scope='a', code='a'))

            profiler.disable()
            stats = pstats.Stats(profiler).sort_stats(pstats.SortKey.CUMULATIVE)
            stats.print_stats()


if __name__ == '__main__':
    unittest.main()
